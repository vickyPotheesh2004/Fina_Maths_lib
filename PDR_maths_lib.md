# Product Design Requirements (PDR)
# FinBench `maths_lib` — Deterministic Financial Formula Library

**Document ID:** PDR-MATHSLIB-001  
**Revision:** 1.0  
**Date:** 2026-05-28  
**Parent System:** FinBench Multi-Agent Business Analyst AI (PDR-BAAAI-001)  
**Total Formulas:** 910 (target was 600; delivered 910)  
**Status:** APPROVED FOR BUILD  

---

## 1. Purpose & Rationale

`maths_lib` is the deterministic computation core of FinBench. It exists because large language models are unreliable at multi-step arithmetic and formula recall. Instead of asking Llama 3.1 8B to *remember* how to compute Black-Scholes or Macaulay Duration, the model only needs to *recognize* the formula and call a pre-built, unit-tested Python function that returns an exact answer.

This is the **"banana peel" strategy**: once the formula library is fully built (peeled), every reasoning question becomes easy to consume. The LLM becomes an orchestrator, not a calculator.

**Design goals:**

- **100% deterministic** — same inputs always yield same output (no LLM in the math path).
- **Zero cost** — pure Python + NumPy/SciPy. No paid APIs (satisfies C1).
- **Fully local** — no network calls (satisfies C2).
- **Fast** — every formula executes in under 10 milliseconds.
- **Auditable** — each result carries the formula name, inputs used, and the expression evaluated.
- **Reproducible** — `seed=42` wherever randomness appears, e.g. Monte Carlo (satisfies C5).

## 2. Domain Overview

The library is organized into **12 domains** totaling **910 unique formulas**. Each domain maps to exactly one Python module.

| # | Domain | Module File | Formula Count |
|---|--------|-------------|---------------|
| 1 | Profitability & Margin Ratios | `profitability.py` | 50 |
| 2 | Liquidity, Solvency & Efficiency Ratios | `liquidity_solvency.py` | 50 |
| 3 | Valuation Metrics & Models | `valuation.py` | 60 |
| 4 | Time-Series & Technical Analysis | `technical.py` | 80 |
| 5 | Options Pricing & Derivatives | `options.py` | 45 |
| 6 | Fixed Income & Bonds | `fixed_income.py` | 50 |
| 7 | Risk Management & Portfolio Theory | `risk.py` | 50 |
| 8 | Time Value of Money & Capital Budgeting | `tvm.py` | 45 |
| 9 | Corporate Finance & M&A | `corporate_ma.py` | 50 |
| 10 | Accounting & Depreciation | `accounting.py` | 40 |
| 11 | Statistics & Econometrics | `statistics_econ.py` | 45 |
| 12 | Core Math, Trigonometry, Linear Algebra & Geometry | `math_core.py` | 45 |
| 13 | Growth, Segment, Forensic & Modern Metrics | `growth_segment_forensic.py` | 50 |
| 14 | AI / Machine Learning Metrics & Functions | `ai_ml.py` | 93 |
| 15 | Probability Theory & Distributions | `probability.py` | 55 |
| 16 | Advanced Statistics & Hypothesis Testing | `statistics_advanced.py` | 53 |
| 17 | Business Analyst KPIs, Forecasting & Decision | `business_analyst.py` | 49 |
| | **TOTAL** | | **910** |

## 3. Library Structure (Directory Layout)

```
src/
└── maths_lib/
    ├── __init__.py              # exports FORMULA_REGISTRY + all functions
    ├── registry.py              # name -> function map, metadata, lookup API
    ├── base.py                  # FormulaResult dataclass, @formula decorator,
    │                            #   input validation, safe-divide helpers
    ├── exceptions.py            # MissingInputError, DivisionGuard, DomainError
    │
    ├── profitability.py         # D01 - 50 formulas
    ├── liquidity_solvency.py    # D02 - 50 formulas
    ├── valuation.py             # D03 - 60 formulas
    ├── technical.py             # D04 - 80 formulas
    ├── options.py               # D05 - 45 formulas
    ├── fixed_income.py          # D06 - 50 formulas
    ├── risk.py                  # D07 - 50 formulas
    ├── tvm.py                   # D08 - 45 formulas
    ├── corporate_ma.py          # D09 - 50 formulas
    ├── accounting.py            # D10 - 40 formulas
    ├── statistics_econ.py       # D11 - 45 formulas
    └── math_core.py             # D12 - 45 formulas

tests/
└── maths_lib/
    ├── test_profitability.py    # >=3 cases per formula
    ├── test_liquidity_solvency.py
    ├── test_valuation.py
    ├── test_technical.py
    ├── test_options.py
    ├── test_fixed_income.py
    ├── test_risk.py
    ├── test_tvm.py
    ├── test_corporate_ma.py
    ├── test_accounting.py
    ├── test_statistics_econ.py
    ├── test_math_core.py
    ├── test_registry.py         # registry integrity, unique names
    └── golden/                  # known-answer reference values (JSON)
```

## 4. Core Contracts (`base.py`)

Every formula function follows one signature pattern and returns a `FormulaResult`. This is what makes the library auditable and lets the Composite Resolver (N20) chain formulas together.

```python
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional
import functools

@dataclass
class FormulaResult:
    value:        float                       # the computed answer
    formula_id:   str                         # e.g. 'gross_margin'
    formula_name: str                         # e.g. 'Gross Margin %'
    expression:   str                         # e.g. '(Revenue - COGS) / Revenue * 100'
    inputs_used:  Dict[str, float]            # {'revenue': 383285, 'cogs': 214137}
    unit:         str = ''                    # '%', 'x', '$', 'days', ''
    domain:       str = ''                    # 'D01_profitability'
    valid:        bool = True
    error:        Optional[str] = None

FORMULA_REGISTRY: Dict[str, dict] = {}

def formula(fid, name, expression, domain, unit=''):
    """Decorator: registers a function and attaches metadata."""
    def wrap(fn):
        FORMULA_REGISTRY[fid] = {
            'fn': fn, 'name': name, 'expression': expression,
            'domain': domain, 'unit': unit,
            'inputs': list(fn.__code__.co_varnames[:fn.__code__.co_argcount]),
        }
        @functools.wraps(fn)
        def inner(*a, **k):
            return fn(*a, **k)
        return inner
    return wrap

def safe_div(numerator, denominator):
    """Division guard - returns None instead of raising ZeroDivisionError."""
    if denominator == 0 or denominator is None:
        return None
    return numerator / denominator
```

**Example formula implementation:**

```python
@formula('gross_margin', 'Gross Margin %',
         '(Revenue - COGS) / Revenue * 100', 'D01_profitability', unit='%')
def gross_margin(revenue: float, cogs: float) -> FormulaResult:
    val = safe_div((revenue - cogs), revenue)
    return FormulaResult(
        value=(val * 100) if val is not None else None,
        formula_id='gross_margin', formula_name='Gross Margin %',
        expression='(Revenue - COGS) / Revenue * 100',
        inputs_used={'revenue': revenue, 'cogs': cogs},
        unit='%', domain='D01_profitability',
        valid=(val is not None),
        error=None if val is not None else 'division by zero (revenue=0)',
    )
```

## 5. Complete Formula Catalog

All 910 formulas enumerated by domain. Columns: **#** (sequence), **ID** (function name), **Name**, **Description**, **Formula** (expression), **Inputs**.

### 5.1 Profitability & Margin Ratios  ·  `profitability.py`  ·  50 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 1 | `gross_margin` | Gross Margin % | Profit left after COGS as % of revenue | `(Revenue - COGS) / Revenue * 100` | revenue, cogs |
| 2 | `gross_profit` | Gross Profit | Revenue minus cost of goods sold | `Revenue - COGS` | revenue, cogs |
| 3 | `operating_margin` | Operating Margin % | Operating income as % of revenue | `Operating_Income / Revenue * 100` | operating_income, revenue |
| 4 | `net_margin` | Net Profit Margin % | Net income as % of revenue | `Net_Income / Revenue * 100` | net_income, revenue |
| 5 | `ebitda_margin` | EBITDA Margin % | EBITDA as % of revenue | `EBITDA / Revenue * 100` | ebitda, revenue |
| 6 | `ebit_margin` | EBIT Margin % | EBIT as % of revenue | `EBIT / Revenue * 100` | ebit, revenue |
| 7 | `pretax_margin` | Pretax Margin % | Pretax income as % of revenue | `Pretax_Income / Revenue * 100` | pretax_income, revenue |
| 8 | `contribution_margin` | Contribution Margin | Revenue minus variable costs | `Revenue - Variable_Costs` | revenue, variable_costs |
| 9 | `contribution_margin_ratio` | Contribution Margin Ratio % | Contribution margin as % of revenue | `(Revenue - Variable_Costs) / Revenue * 100` | revenue, variable_costs |
| 10 | `fcf_margin` | Free Cash Flow Margin % | FCF as % of revenue | `FCF / Revenue * 100` | fcf, revenue |
| 11 | `ocf_margin` | Operating Cash Flow Margin % | OCF as % of revenue | `OCF / Revenue * 100` | ocf, revenue |
| 12 | `return_on_equity` | Return on Equity (ROE) % | Net income as % of shareholders equity | `Net_Income / Shareholders_Equity * 100` | net_income, shareholders_equity |
| 13 | `return_on_assets` | Return on Assets (ROA) % | Net income as % of total assets | `Net_Income / Total_Assets * 100` | net_income, total_assets |
| 14 | `return_on_invested_capital` | Return on Invested Capital (ROIC) % | NOPAT as % of invested capital | `NOPAT / Invested_Capital * 100` | nopat, invested_capital |
| 15 | `return_on_capital_employed` | Return on Capital Employed (ROCE) % | EBIT as % of capital employed | `EBIT / Capital_Employed * 100` | ebit, capital_employed |
| 16 | `return_on_sales` | Return on Sales (ROS) % | Operating profit as % of sales | `Operating_Income / Sales * 100` | operating_income, sales |
| 17 | `return_on_tangible_equity` | Return on Tangible Equity % | Net income / tangible equity | `Net_Income / (Equity - Intangibles) * 100` | net_income, equity, intangibles |
| 18 | `return_on_net_assets` | Return on Net Assets (RONA) % | Net income / fixed assets + working capital | `Net_Income / (Fixed_Assets + Working_Capital) * 100` | net_income, fixed_assets, working_capital |
| 19 | `nopat` | Net Operating Profit After Tax | Operating income after tax | `EBIT * (1 - Tax_Rate)` | ebit, tax_rate |
| 20 | `ebitda` | EBITDA | Earnings before interest, tax, depreciation, amortization | `Net_Income + Interest + Taxes + Depreciation + Amortization` | net_income, interest, taxes, depreciation, amortization |
| 21 | `ebit` | EBIT | Earnings before interest and tax | `Net_Income + Interest + Taxes` | net_income, interest, taxes |
| 22 | `effective_tax_rate` | Effective Tax Rate % | Tax expense as % of pretax income | `Tax_Expense / Pretax_Income * 100` | tax_expense, pretax_income |
| 23 | `operating_leverage` | Degree of Operating Leverage | % change EBIT / % change sales | `Pct_Change_EBIT / Pct_Change_Sales` | pct_change_ebit, pct_change_sales |
| 24 | `financial_leverage` | Degree of Financial Leverage | % change EPS / % change EBIT | `Pct_Change_EPS / Pct_Change_EBIT` | pct_change_eps, pct_change_ebit |
| 25 | `combined_leverage` | Degree of Combined Leverage | DOL times DFL | `DOL * DFL` | dol, dfl |
| 26 | `dupont_roe_3step` | DuPont ROE (3-Step) | Net margin x asset turnover x equity multiplier | `Net_Margin * Asset_Turnover * Equity_Multiplier` | net_margin, asset_turnover, equity_multiplier |
| 27 | `dupont_roe_5step` | DuPont ROE (5-Step) | Extended DuPont with tax + interest burden | `Tax_Burden * Interest_Burden * Operating_Margin * Asset_Turnover * Equity_Multiplier` | tax_burden, interest_burden, operating_margin, asset_turnover, equity_multiplier |
| 28 | `tax_burden` | Tax Burden Ratio | Net income / pretax income | `Net_Income / Pretax_Income` | net_income, pretax_income |
| 29 | `interest_burden` | Interest Burden Ratio | Pretax income / EBIT | `Pretax_Income / EBIT` | pretax_income, ebit |
| 30 | `equity_multiplier` | Equity Multiplier | Total assets / equity | `Total_Assets / Shareholders_Equity` | total_assets, shareholders_equity |
| 31 | `operating_ratio` | Operating Ratio % | Operating costs / revenue | `Operating_Costs / Revenue * 100` | operating_costs, revenue |
| 32 | `cost_of_revenue_ratio` | Cost of Revenue Ratio % | COGS / revenue | `COGS / Revenue * 100` | cogs, revenue |
| 33 | `overhead_ratio` | Overhead Ratio % | Operating expenses / (net interest + operating income) | `Operating_Expenses / (Net_Interest + Operating_Income) * 100` | operating_expenses, net_interest, operating_income |
| 34 | `sga_ratio` | SG&A to Revenue % | Selling general admin / revenue | `SGA / Revenue * 100` | sga, revenue |
| 35 | `rnd_ratio` | R&D to Revenue % | Research dev / revenue | `RnD / Revenue * 100` | rnd, revenue |
| 36 | `rnd_intensity` | R&D Intensity % | R&D spend / revenue | `RnD_Expense / Revenue * 100` | rnd_expense, revenue |
| 37 | `net_income_growth` | Net Income Growth % | YoY net income change | `(NI_Current - NI_Prior) / NI_Prior * 100` | ni_current, ni_prior |
| 38 | `revenue_growth` | Revenue Growth % | YoY revenue change | `(Rev_Current - Rev_Prior) / Rev_Prior * 100` | rev_current, rev_prior |
| 39 | `operating_income_growth` | Operating Income Growth % | YoY operating income change | `(OI_Current - OI_Prior) / OI_Prior * 100` | oi_current, oi_prior |
| 40 | `eps_basic` | Basic EPS | Net income / weighted basic shares | `(Net_Income - Pref_Dividends) / Basic_Shares` | net_income, pref_dividends, basic_shares |
| 41 | `eps_diluted` | Diluted EPS | Net income / diluted shares | `(Net_Income - Pref_Dividends) / Diluted_Shares` | net_income, pref_dividends, diluted_shares |
| 42 | `eps_growth` | EPS Growth % | YoY EPS change | `(EPS_Current - EPS_Prior) / EPS_Prior * 100` | eps_current, eps_prior |
| 43 | `cash_return_on_assets` | Cash Return on Assets % | OCF / total assets | `OCF / Total_Assets * 100` | ocf, total_assets |
| 44 | `cash_roe` | Cash Return on Equity % | OCF / equity | `OCF / Shareholders_Equity * 100` | ocf, shareholders_equity |
| 45 | `gross_profit_growth` | Gross Profit Growth % | YoY gross profit change | `(GP_Current - GP_Prior) / GP_Prior * 100` | gp_current, gp_prior |
| 46 | `ebitda_growth` | EBITDA Growth % | YoY EBITDA change | `(EBITDA_Current - EBITDA_Prior) / EBITDA_Prior * 100` | ebitda_current, ebitda_prior |
| 47 | `incremental_margin` | Incremental Margin % | Change in profit / change in revenue | `Delta_Profit / Delta_Revenue * 100` | delta_profit, delta_revenue |
| 48 | `breakeven_point_units` | Breakeven Point (Units) | Fixed costs / contribution per unit | `Fixed_Costs / (Price - Variable_Cost_Per_Unit)` | fixed_costs, price, variable_cost_per_unit |
| 49 | `breakeven_point_revenue` | Breakeven Point (Revenue) | Fixed costs / contribution margin ratio | `Fixed_Costs / Contribution_Margin_Ratio` | fixed_costs, contribution_margin_ratio |
| 50 | `margin_of_safety` | Margin of Safety % | (Sales - breakeven) / sales | `(Sales - Breakeven_Sales) / Sales * 100` | sales, breakeven_sales |

### 5.2 Liquidity, Solvency & Efficiency Ratios  ·  `liquidity_solvency.py`  ·  50 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 51 | `current_ratio` | Current Ratio | Current assets / current liabilities | `Current_Assets / Current_Liabilities` | current_assets, current_liabilities |
| 52 | `quick_ratio` | Quick Ratio (Acid Test) | Liquid assets / current liabilities | `(Current_Assets - Inventory) / Current_Liabilities` | current_assets, inventory, current_liabilities |
| 53 | `cash_ratio` | Cash Ratio | Cash + equivalents / current liabilities | `(Cash + Marketable_Securities) / Current_Liabilities` | cash, marketable_securities, current_liabilities |
| 54 | `operating_cash_flow_ratio` | Operating Cash Flow Ratio | OCF / current liabilities | `OCF / Current_Liabilities` | ocf, current_liabilities |
| 55 | `working_capital` | Working Capital | Current assets minus current liabilities | `Current_Assets - Current_Liabilities` | current_assets, current_liabilities |
| 56 | `working_capital_ratio` | Working Capital Ratio | Same as current ratio | `Current_Assets / Current_Liabilities` | current_assets, current_liabilities |
| 57 | `net_working_capital_to_sales` | NWC to Sales % | Net working capital / sales | `Working_Capital / Sales * 100` | working_capital, sales |
| 58 | `defensive_interval_ratio` | Defensive Interval Ratio (days) | Liquid assets / daily expenses | `Liquid_Assets / Daily_Operating_Expenses` | liquid_assets, daily_operating_expenses |
| 59 | `debt_to_equity` | Debt-to-Equity | Total debt / equity | `Total_Debt / Shareholders_Equity` | total_debt, shareholders_equity |
| 60 | `debt_to_assets` | Debt-to-Assets | Total debt / total assets | `Total_Debt / Total_Assets` | total_debt, total_assets |
| 61 | `debt_to_capital` | Debt-to-Capital | Debt / (debt + equity) | `Total_Debt / (Total_Debt + Shareholders_Equity)` | total_debt, shareholders_equity |
| 62 | `debt_to_ebitda` | Debt-to-EBITDA | Total debt / EBITDA | `Total_Debt / EBITDA` | total_debt, ebitda |
| 63 | `net_debt` | Net Debt | Total debt minus cash | `Total_Debt - Cash` | total_debt, cash |
| 64 | `net_debt_to_ebitda` | Net Debt-to-EBITDA | Net debt / EBITDA | `(Total_Debt - Cash) / EBITDA` | total_debt, cash, ebitda |
| 65 | `equity_ratio` | Equity Ratio | Equity / total assets | `Shareholders_Equity / Total_Assets` | shareholders_equity, total_assets |
| 66 | `financial_leverage_ratio` | Financial Leverage Ratio | Total assets / equity | `Total_Assets / Shareholders_Equity` | total_assets, shareholders_equity |
| 67 | `interest_coverage` | Interest Coverage Ratio | EBIT / interest expense | `EBIT / Interest_Expense` | ebit, interest_expense |
| 68 | `ebitda_coverage` | EBITDA Coverage Ratio | EBITDA / interest expense | `EBITDA / Interest_Expense` | ebitda, interest_expense |
| 69 | `fixed_charge_coverage` | Fixed Charge Coverage | (EBIT + lease) / (interest + lease) | `(EBIT + Lease_Payments) / (Interest_Expense + Lease_Payments)` | ebit, lease_payments, interest_expense |
| 70 | `times_interest_earned` | Times Interest Earned | EBIT / interest expense | `EBIT / Interest_Expense` | ebit, interest_expense |
| 71 | `debt_service_coverage` | Debt Service Coverage Ratio (DSCR) | Net operating income / debt service | `Net_Operating_Income / Total_Debt_Service` | net_operating_income, total_debt_service |
| 72 | `cash_flow_to_debt` | Cash Flow to Debt | OCF / total debt | `OCF / Total_Debt` | ocf, total_debt |
| 73 | `capitalization_ratio` | Capitalization Ratio | LT debt / (LT debt + equity) | `Long_Term_Debt / (Long_Term_Debt + Shareholders_Equity)` | long_term_debt, shareholders_equity |
| 74 | `asset_turnover` | Asset Turnover | Revenue / total assets | `Revenue / Total_Assets` | revenue, total_assets |
| 75 | `fixed_asset_turnover` | Fixed Asset Turnover | Revenue / net PP&E | `Revenue / Net_PPE` | revenue, net_ppe |
| 76 | `inventory_turnover` | Inventory Turnover | COGS / average inventory | `COGS / Average_Inventory` | cogs, average_inventory |
| 77 | `receivables_turnover` | Receivables Turnover | Revenue / average receivables | `Revenue / Average_Receivables` | revenue, average_receivables |
| 78 | `payables_turnover` | Payables Turnover | COGS / average payables | `COGS / Average_Payables` | cogs, average_payables |
| 79 | `working_capital_turnover` | Working Capital Turnover | Revenue / working capital | `Revenue / Working_Capital` | revenue, working_capital |
| 80 | `equity_turnover` | Equity Turnover | Revenue / equity | `Revenue / Shareholders_Equity` | revenue, shareholders_equity |
| 81 | `total_capital_turnover` | Total Capital Turnover | Revenue / total capital | `Revenue / Total_Capital` | revenue, total_capital |
| 82 | `days_sales_outstanding` | Days Sales Outstanding (DSO) | 365 / receivables turnover | `365 / Receivables_Turnover` | receivables_turnover |
| 83 | `days_inventory_outstanding` | Days Inventory Outstanding (DIO) | 365 / inventory turnover | `365 / Inventory_Turnover` | inventory_turnover |
| 84 | `days_payable_outstanding` | Days Payable Outstanding (DPO) | 365 / payables turnover | `365 / Payables_Turnover` | payables_turnover |
| 85 | `cash_conversion_cycle` | Cash Conversion Cycle (days) | DSO + DIO - DPO | `DSO + DIO - DPO` | dso, dio, dpo |
| 86 | `operating_cycle` | Operating Cycle (days) | DSO + DIO | `DSO + DIO` | dso, dio |
| 87 | `dso_direct` | DSO Direct | Receivables / revenue x 365 | `Receivables / Revenue * 365` | receivables, revenue |
| 88 | `dio_direct` | DIO Direct | Inventory / COGS x 365 | `Inventory / COGS * 365` | inventory, cogs |
| 89 | `dpo_direct` | DPO Direct | Payables / COGS x 365 | `Payables / COGS * 365` | payables, cogs |
| 90 | `capital_intensity` | Capital Intensity % | CapEx / revenue | `CapEx / Revenue * 100` | capex, revenue |
| 91 | `capital_intensity_assets` | Capital Intensity (Assets) | Total assets / revenue | `Total_Assets / Revenue` | total_assets, revenue |
| 92 | `fixed_assets_to_equity` | Fixed Assets to Equity | Net PP&E / equity | `Net_PPE / Shareholders_Equity` | net_ppe, shareholders_equity |
| 93 | `long_term_debt_to_equity` | LT Debt to Equity | LT debt / equity | `Long_Term_Debt / Shareholders_Equity` | long_term_debt, shareholders_equity |
| 94 | `short_term_debt_ratio` | Short-Term Debt Ratio | ST debt / total debt | `Short_Term_Debt / Total_Debt` | short_term_debt, total_debt |
| 95 | `current_liabilities_ratio` | Current Liabilities Ratio | Current liabilities / total liabilities | `Current_Liabilities / Total_Liabilities` | current_liabilities, total_liabilities |
| 96 | `solvency_ratio` | Solvency Ratio | (Net income + depreciation) / total liabilities | `(Net_Income + Depreciation) / Total_Liabilities` | net_income, depreciation, total_liabilities |
| 97 | `financial_autonomy_ratio` | Financial Autonomy Ratio | Equity / total liabilities | `Shareholders_Equity / Total_Liabilities` | shareholders_equity, total_liabilities |
| 98 | `net_gearing` | Net Gearing % | Net debt / equity | `(Total_Debt - Cash) / Shareholders_Equity * 100` | total_debt, cash, shareholders_equity |
| 99 | `altman_z_score` | Altman Z-Score | Bankruptcy predictor composite | `1.2*A + 1.4*B + 3.3*C + 0.6*D + 1.0*E` | a, b, c, d, e |
| 100 | `piotroski_f_score` | Piotroski F-Score | 9-point financial strength score | `Sum of 9 binary signals` | signals_list |

### 5.3 Valuation Metrics & Models  ·  `valuation.py`  ·  60 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 101 | `pe_ratio` | Price-to-Earnings (P/E) | Price / EPS | `Price / EPS` | price, eps |
| 102 | `forward_pe` | Forward P/E | Price / forward EPS | `Price / Forward_EPS` | price, forward_eps |
| 103 | `peg_ratio` | PEG Ratio | P/E / earnings growth | `PE_Ratio / Earnings_Growth_Rate` | pe_ratio, earnings_growth_rate |
| 104 | `pb_ratio` | Price-to-Book (P/B) | Price / book value per share | `Price / Book_Value_Per_Share` | price, book_value_per_share |
| 105 | `ps_ratio` | Price-to-Sales (P/S) | Market cap / revenue | `Market_Cap / Revenue` | market_cap, revenue |
| 106 | `pcf_ratio` | Price-to-Cash-Flow | Price / cash flow per share | `Price / Cash_Flow_Per_Share` | price, cash_flow_per_share |
| 107 | `p_fcf_ratio` | Price-to-Free-Cash-Flow | Market cap / FCF | `Market_Cap / FCF` | market_cap, fcf |
| 108 | `ev` | Enterprise Value | Market cap + debt - cash | `Market_Cap + Total_Debt - Cash` | market_cap, total_debt, cash |
| 109 | `ev_ebitda` | EV/EBITDA | Enterprise value / EBITDA | `EV / EBITDA` | ev, ebitda |
| 110 | `ev_ebit` | EV/EBIT | Enterprise value / EBIT | `EV / EBIT` | ev, ebit |
| 111 | `ev_sales` | EV/Sales | Enterprise value / revenue | `EV / Revenue` | ev, revenue |
| 112 | `ev_fcf` | EV/FCF | Enterprise value / FCF | `EV / FCF` | ev, fcf |
| 113 | `dividend_yield` | Dividend Yield % | Annual dividend / price | `Annual_Dividend / Price * 100` | annual_dividend, price |
| 114 | `dividend_payout_ratio` | Dividend Payout Ratio % | Dividends / net income | `Dividends / Net_Income * 100` | dividends, net_income |
| 115 | `retention_ratio` | Retention Ratio % | 1 - payout ratio | `(1 - Payout_Ratio) * 100` | payout_ratio |
| 116 | `book_value_per_share` | Book Value Per Share | Equity / shares outstanding | `Shareholders_Equity / Shares_Outstanding` | shareholders_equity, shares_outstanding |
| 117 | `tangible_book_value` | Tangible Book Value | Equity - intangibles - goodwill | `Shareholders_Equity - Intangibles - Goodwill` | shareholders_equity, intangibles, goodwill |
| 118 | `tangible_book_per_share` | Tangible Book Value Per Share | Tangible BV / shares | `Tangible_Book_Value / Shares_Outstanding` | tangible_book_value, shares_outstanding |
| 119 | `market_cap` | Market Capitalization | Price x shares outstanding | `Price * Shares_Outstanding` | price, shares_outstanding |
| 120 | `earnings_yield` | Earnings Yield % | EPS / price | `EPS / Price * 100` | eps, price |
| 121 | `fcf_yield` | Free Cash Flow Yield % | FCF per share / price | `FCF_Per_Share / Price * 100` | fcf_per_share, price |
| 122 | `dcf_value` | DCF Present Value | Sum of discounted cash flows | `Sum(CF_t / (1+r)^t)` | cash_flows, discount_rate |
| 123 | `dcf_two_stage` | Two-Stage DCF | Explicit forecast + terminal value | `Sum(CF_t/(1+r)^t) + TV/(1+r)^n` | cash_flows, discount_rate, terminal_value |
| 124 | `terminal_value_gordon` | Terminal Value (Gordon) | FCF x (1+g) / (r-g) | `FCF * (1 + g) / (r - g)` | fcf, growth_rate, discount_rate |
| 125 | `terminal_value_exit` | Terminal Value (Exit Multiple) | Final year metric x exit multiple | `Final_EBITDA * Exit_Multiple` | final_ebitda, exit_multiple |
| 126 | `gordon_growth_model` | Gordon Growth Model (DDM) | D1 / (r - g) | `D1 / (Required_Return - Growth_Rate)` | d1, required_return, growth_rate |
| 127 | `ddm_multistage` | Multi-Stage DDM | Variable growth dividend model | `Sum(D_t/(1+r)^t) + TV` | dividends, discount_rate, terminal_value |
| 128 | `fcff` | Free Cash Flow to Firm | EBIT(1-t) + D&A - CapEx - WC change | `EBIT*(1-Tax) + DA - CapEx - Delta_WC` | ebit, tax_rate, da, capex, delta_wc |
| 129 | `fcfe` | Free Cash Flow to Equity | FCFF - interest(1-t) + net borrowing | `FCFF - Interest*(1-Tax) + Net_Borrowing` | fcff, interest, tax_rate, net_borrowing |
| 130 | `fcf_simple` | Free Cash Flow (Simple) | OCF - CapEx | `OCF - CapEx` | ocf, capex |
| 131 | `wacc` | Weighted Average Cost of Capital | Weighted equity + debt cost | `We*Re + Wd*Rd*(1-Tax)` | weight_equity, cost_equity, weight_debt, cost_debt, tax_rate |
| 132 | `cost_of_equity_capm` | Cost of Equity (CAPM) | Rf + beta x (Rm - Rf) | `Rf + Beta * (Rm - Rf)` | risk_free, beta, market_return |
| 133 | `cost_of_equity_ddm` | Cost of Equity (DDM) | D1/P + g | `D1 / Price + Growth_Rate` | d1, price, growth_rate |
| 134 | `cost_of_debt` | Cost of Debt (After-Tax) | Interest rate x (1-tax) | `Interest_Rate * (1 - Tax_Rate)` | interest_rate, tax_rate |
| 135 | `capm` | CAPM Expected Return | Rf + beta x equity premium | `Rf + Beta * (Rm - Rf)` | risk_free, beta, market_return |
| 136 | `fama_french_3` | Fama-French 3-Factor | Rf + market + SMB + HML | `Rf + b1*MKT + b2*SMB + b3*HML` | risk_free, b1, mkt, b2, smb, b3, hml |
| 137 | `fama_french_5` | Fama-French 5-Factor | FF3 + RMW + CMA | `Rf + b1*MKT + b2*SMB + b3*HML + b4*RMW + b5*CMA` | risk_free, betas, factors |
| 138 | `residual_income` | Residual Income | Net income - equity charge | `Net_Income - (Equity * Cost_of_Equity)` | net_income, equity, cost_of_equity |
| 139 | `eva` | Economic Value Added | NOPAT - (capital x WACC) | `NOPAT - (Invested_Capital * WACC)` | nopat, invested_capital, wacc |
| 140 | `mva` | Market Value Added | Market value - invested capital | `Market_Value - Invested_Capital` | market_value, invested_capital |
| 141 | `justified_pe` | Justified P/E | Payout x (1+g) / (r-g) | `Payout * (1+g) / (r-g)` | payout, growth_rate, required_return |
| 142 | `justified_pb` | Justified P/B | (ROE - g) / (r - g) | `(ROE - g) / (r - g)` | roe, growth_rate, required_return |
| 143 | `graham_number` | Graham Number | sqrt(22.5 x EPS x BVPS) | `sqrt(22.5 * EPS * BVPS)` | eps, bvps |
| 144 | `sum_of_parts` | Sum-of-the-Parts Value | Sum of segment values | `Sum(Segment_Value_i)` | segment_values |
| 145 | `net_asset_value` | Net Asset Value (NAV) | Assets - liabilities | `Total_Assets - Total_Liabilities` | total_assets, total_liabilities |
| 146 | `liquidation_value` | Liquidation Value | Asset recovery - liabilities | `Asset_Recovery_Value - Total_Liabilities` | asset_recovery_value, total_liabilities |
| 147 | `replacement_value` | Replacement Value | Cost to rebuild assets | `Replacement_Cost_Assets - Liabilities` | replacement_cost_assets, liabilities |
| 148 | `price_to_tangible_book` | Price-to-Tangible-Book | Price / tangible BVPS | `Price / Tangible_BVPS` | price, tangible_bvps |
| 149 | `ev_to_invested_capital` | EV/Invested Capital | Enterprise value / invested capital | `EV / Invested_Capital` | ev, invested_capital |
| 150 | `dividend_per_share` | Dividend Per Share | Total dividends / shares | `Total_Dividends / Shares_Outstanding` | total_dividends, shares_outstanding |
| 151 | `dividend_coverage` | Dividend Coverage Ratio | EPS / DPS | `EPS / Dividend_Per_Share` | eps, dividend_per_share |
| 152 | `total_shareholder_return` | Total Shareholder Return % | (Price change + dividends) / start price | `(Price_End - Price_Start + Dividends) / Price_Start * 100` | price_end, price_start, dividends |
| 153 | `implied_growth_rate` | Implied Growth Rate | r - D1/P | `Required_Return - D1/Price` | required_return, d1, price |
| 154 | `ev_per_share` | EV Per Share | Enterprise value / shares | `EV / Shares_Outstanding` | ev, shares_outstanding |
| 155 | `price_to_nav` | Price-to-NAV | Price / NAV per share | `Price / NAV_Per_Share` | price, nav_per_share |
| 156 | `cape_ratio` | CAPE (Shiller P/E) | Price / 10yr avg real earnings | `Price / Avg_10yr_Real_EPS` | price, avg_10yr_real_eps |
| 157 | `rule_of_40` | Rule of 40 % | Revenue growth + profit margin | `Revenue_Growth_Pct + Profit_Margin_Pct` | revenue_growth_pct, profit_margin_pct |
| 158 | `magic_formula_yield` | Magic Formula Earnings Yield | EBIT / EV | `EBIT / EV` | ebit, ev |
| 159 | `owners_earnings` | Owner's Earnings (Buffett) | NI + D&A - maintenance CapEx | `Net_Income + DA - Maintenance_CapEx` | net_income, da, maintenance_capex |
| 160 | `intrinsic_value_growth` | Intrinsic Value (Growth) | EPS x (8.5 + 2g) Graham formula | `EPS * (8.5 + 2 * Growth_Rate)` | eps, growth_rate |

### 5.4 Time-Series & Technical Analysis  ·  `technical.py`  ·  80 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 161 | `sma` | Simple Moving Average | Mean of last n prices | `Sum(Prices[-n:]) / n` | prices, period |
| 162 | `ema` | Exponential Moving Average | Weighted MA with decay | `Price*k + EMA_prev*(1-k), k=2/(n+1)` | prices, period |
| 163 | `wma` | Weighted Moving Average | Linearly weighted MA | `Sum(Price_i * Weight_i) / Sum(Weights)` | prices, period |
| 164 | `dema` | Double EMA | 2*EMA - EMA(EMA) | `2*EMA - EMA(EMA)` | prices, period |
| 165 | `tema` | Triple EMA | 3*EMA - 3*EMA2 + EMA3 | `3*EMA1 - 3*EMA2 + EMA3` | prices, period |
| 166 | `hma` | Hull Moving Average | WMA-based low-lag MA | `WMA(2*WMA(n/2) - WMA(n), sqrt(n))` | prices, period |
| 167 | `kama` | Kaufman Adaptive MA | Efficiency-ratio adaptive MA | `KAMA_prev + SC*(Price - KAMA_prev)` | prices, period |
| 168 | `vwma` | Volume-Weighted MA | Price weighted by volume | `Sum(Price*Volume) / Sum(Volume)` | prices, volumes, period |
| 169 | `vwap` | Volume-Weighted Avg Price | Cumulative PV / cumulative V | `Sum(Typical_Price*Volume) / Sum(Volume)` | highs, lows, closes, volumes |
| 170 | `atr` | Average True Range | MA of true range | `MA(True_Range, n)` | highs, lows, closes, period |
| 171 | `true_range` | True Range | Max of HL, HC, LC | `max(H-L, abs(H-Cp), abs(L-Cp))` | high, low, prev_close |
| 172 | `bollinger_upper` | Bollinger Upper Band | SMA + k x std | `SMA + 2*StdDev` | prices, period |
| 173 | `bollinger_lower` | Bollinger Lower Band | SMA - k x std | `SMA - 2*StdDev` | prices, period |
| 174 | `bollinger_width` | Bollinger Band Width | (Upper - Lower) / Middle | `(Upper - Lower) / SMA` | prices, period |
| 175 | `bollinger_percent_b` | Bollinger %B | Position within bands | `(Price - Lower) / (Upper - Lower)` | price, upper, lower |
| 176 | `keltner_upper` | Keltner Upper Channel | EMA + mult x ATR | `EMA + Mult*ATR` | prices, highs, lows, period, multiplier |
| 177 | `keltner_lower` | Keltner Lower Channel | EMA - mult x ATR | `EMA - Mult*ATR` | prices, highs, lows, period, multiplier |
| 178 | `donchian_upper` | Donchian Upper Channel | Highest high over n | `max(Highs[-n:])` | highs, period |
| 179 | `donchian_lower` | Donchian Lower Channel | Lowest low over n | `min(Lows[-n:])` | lows, period |
| 180 | `donchian_middle` | Donchian Middle | Avg of upper and lower | `(Upper + Lower) / 2` | highs, lows, period |
| 181 | `rsi` | Relative Strength Index | Momentum oscillator 0-100 | `100 - 100/(1 + AvgGain/AvgLoss)` | prices, period |
| 182 | `stochastic_k` | Stochastic %K | Position in high-low range | `(Close - LowN) / (HighN - LowN) * 100` | highs, lows, closes, period |
| 183 | `stochastic_d` | Stochastic %D | SMA of %K | `SMA(%K, 3)` | stochastic_k, smoothing |
| 184 | `macd_line` | MACD Line | EMA12 - EMA26 | `EMA(12) - EMA(26)` | prices |
| 185 | `macd_signal` | MACD Signal Line | EMA9 of MACD | `EMA(MACD, 9)` | macd_line |
| 186 | `macd_histogram` | MACD Histogram | MACD - signal | `MACD_Line - Signal_Line` | macd_line, signal_line |
| 187 | `cci` | Commodity Channel Index | Deviation from typical price | `(TP - SMA_TP) / (0.015*MeanDev)` | highs, lows, closes, period |
| 188 | `williams_r` | Williams %R | Inverse stochastic | `(HighN - Close) / (HighN - LowN) * -100` | highs, lows, closes, period |
| 189 | `roc` | Rate of Change % | Price momentum % | `(Price - Price_n) / Price_n * 100` | prices, period |
| 190 | `momentum` | Momentum | Price difference over n | `Price - Price_n` | prices, period |
| 191 | `mfi` | Money Flow Index | Volume-weighted RSI | `100 - 100/(1 + PosFlow/NegFlow)` | highs, lows, closes, volumes, period |
| 192 | `adx` | Average Directional Index | Trend strength 0-100 | `MA(DX, n)` | highs, lows, closes, period |
| 193 | `plus_di` | Plus Directional Indicator | Upward movement strength | `100 * EMA(+DM) / ATR` | highs, lows, closes, period |
| 194 | `minus_di` | Minus Directional Indicator | Downward movement strength | `100 * EMA(-DM) / ATR` | highs, lows, closes, period |
| 195 | `aroon_up` | Aroon Up | Periods since high | `(n - PeriodsSinceHigh) / n * 100` | highs, period |
| 196 | `aroon_down` | Aroon Down | Periods since low | `(n - PeriodsSinceLow) / n * 100` | lows, period |
| 197 | `aroon_oscillator` | Aroon Oscillator | Aroon up - down | `Aroon_Up - Aroon_Down` | highs, lows, period |
| 198 | `parabolic_sar` | Parabolic SAR | Stop and reverse trend | `SAR_prev + AF*(EP - SAR_prev)` | highs, lows, acceleration |
| 199 | `obv` | On-Balance Volume | Cumulative volume flow | `Sum(Volume * Sign(Price_Change))` | closes, volumes |
| 200 | `chaikin_money_flow` | Chaikin Money Flow | Volume-weighted accumulation | `Sum(MFV) / Sum(Volume)` | highs, lows, closes, volumes, period |
| 201 | `accumulation_distribution` | Accumulation/Distribution | Money flow volume cumulative | `Prev_AD + MFV` | highs, lows, closes, volumes |
| 202 | `ichimoku_tenkan` | Ichimoku Tenkan-sen | 9-period midpoint | `(High9 + Low9) / 2` | highs, lows |
| 203 | `ichimoku_kijun` | Ichimoku Kijun-sen | 26-period midpoint | `(High26 + Low26) / 2` | highs, lows |
| 204 | `ichimoku_senkou_a` | Ichimoku Senkou Span A | Avg of Tenkan and Kijun | `(Tenkan + Kijun) / 2` | tenkan, kijun |
| 205 | `ichimoku_senkou_b` | Ichimoku Senkou Span B | 52-period midpoint | `(High52 + Low52) / 2` | highs, lows |
| 206 | `linear_regression_slope` | Linear Regression Slope | Trend slope of prices | `Slope of best-fit line` | prices, period |
| 207 | `standard_deviation` | Rolling Standard Deviation | Volatility measure | `sqrt(Sum((x-mean)^2)/n)` | prices, period |
| 208 | `historical_volatility` | Historical Volatility % | Annualized std of returns | `StdDev(LogReturns) * sqrt(252)` | prices, period |
| 209 | `variance` | Rolling Variance | Squared deviation | `Sum((x-mean)^2) / n` | prices, period |
| 210 | `beta_coefficient` | Beta Coefficient | Stock vs market sensitivity | `Cov(Stock,Market) / Var(Market)` | stock_returns, market_returns |
| 211 | `correlation_coefficient` | Correlation Coefficient | Linear relationship -1 to 1 | `Cov(X,Y) / (StdX * StdY)` | series_x, series_y |
| 212 | `z_score_price` | Price Z-Score | Standardized price distance | `(Price - Mean) / StdDev` | prices, period |
| 213 | `price_oscillator` | Price Oscillator % | (Fast MA - Slow MA) / Slow | `(FastMA - SlowMA) / SlowMA * 100` | prices, fast, slow |
| 214 | `trix` | TRIX | Triple-smoothed ROC | `ROC of Triple_EMA` | prices, period |
| 215 | `ultimate_oscillator` | Ultimate Oscillator | Multi-timeframe momentum | `100 * Weighted_BP_Sum / TR_Sum` | highs, lows, closes |
| 216 | `awesome_oscillator` | Awesome Oscillator | SMA5 - SMA34 of midpoint | `SMA(MP,5) - SMA(MP,34)` | highs, lows |
| 217 | `dpo` | Detrended Price Oscillator | Price minus shifted SMA | `Price - SMA_shifted` | prices, period |
| 218 | `vortex_positive` | Vortex Indicator +VI | Upward trend movement | `Sum(+VM) / Sum(TR)` | highs, lows, closes, period |
| 219 | `vortex_negative` | Vortex Indicator -VI | Downward trend movement | `Sum(-VM) / Sum(TR)` | highs, lows, closes, period |
| 220 | `mass_index` | Mass Index | Range expansion reversal | `Sum(EMA9_HL / EMA9_EMA9_HL)` | highs, lows, period |
| 221 | `force_index` | Force Index | Price change x volume | `(Close - Prev_Close) * Volume` | closes, volumes |
| 222 | `ease_of_movement` | Ease of Movement | Price move per volume | `Distance_Moved / Box_Ratio` | highs, lows, volumes |
| 223 | `klinger_oscillator` | Klinger Oscillator | Volume force trend | `EMA34(VF) - EMA55(VF)` | highs, lows, closes, volumes |
| 224 | `chande_momentum` | Chande Momentum Oscillator | Pure momentum -100 to 100 | `(Su - Sd) / (Su + Sd) * 100` | prices, period |
| 225 | `elder_ray_bull` | Elder Ray Bull Power | High minus EMA | `High - EMA` | highs, prices, period |
| 226 | `elder_ray_bear` | Elder Ray Bear Power | Low minus EMA | `Low - EMA` | lows, prices, period |
| 227 | `choppiness_index` | Choppiness Index | Trend vs range 0-100 | `100*log10(SumATR/Range)/log10(n)` | highs, lows, closes, period |
| 228 | `fisher_transform` | Fisher Transform | Gaussian price normalizer | `0.5*ln((1+x)/(1-x))` | prices, period |
| 229 | `coppock_curve` | Coppock Curve | Long-term momentum | `WMA10(ROC14 + ROC11)` | prices |
| 230 | `kst_oscillator` | Know Sure Thing | Smoothed multi-ROC | `Sum(weighted smoothed ROCs)` | prices |
| 231 | `ppo` | Percentage Price Oscillator | MACD as percentage | `(EMA12 - EMA26) / EMA26 * 100` | prices |
| 232 | `pvo` | Percentage Volume Oscillator | PPO applied to volume | `(EMA12_V - EMA26_V) / EMA26_V * 100` | volumes |
| 233 | `relative_vigor_index` | Relative Vigor Index | Close-open vs range | `SMA(Close-Open) / SMA(High-Low)` | opens, highs, lows, closes |
| 234 | `stochastic_rsi` | Stochastic RSI | Stochastic of RSI | `(RSI - MinRSI) / (MaxRSI - MinRSI)` | prices, period |
| 235 | `supertrend` | SuperTrend | ATR-based trend line | `Based on ATR bands` | highs, lows, closes, period, multiplier |
| 236 | `pivot_point` | Pivot Point | Floor trader pivot | `(High + Low + Close) / 3` | high, low, close |
| 237 | `pivot_resistance_1` | Pivot R1 | First resistance | `2*Pivot - Low` | pivot, low |
| 238 | `pivot_support_1` | Pivot S1 | First support | `2*Pivot - High` | pivot, high |
| 239 | `fibonacci_retracement` | Fibonacci Retracement | Key retracement levels | `High - (High-Low)*Ratio` | high, low, ratio |
| 240 | `chandelier_exit_long` | Chandelier Exit Long | ATR trailing stop | `HighN - ATR*Multiplier` | highs, lows, closes, period, multiplier |

### 5.5 Options Pricing & Derivatives  ·  `options.py`  ·  45 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 241 | `black_scholes_call` | Black-Scholes Call | European call price | `S*N(d1) - K*e^(-rT)*N(d2)` | spot, strike, time, rate, volatility |
| 242 | `black_scholes_put` | Black-Scholes Put | European put price | `K*e^(-rT)*N(-d2) - S*N(-d1)` | spot, strike, time, rate, volatility |
| 243 | `bs_d1` | Black-Scholes d1 | First BS parameter | `(ln(S/K)+(r+sig^2/2)T)/(sig*sqrt(T))` | spot, strike, time, rate, volatility |
| 244 | `bs_d2` | Black-Scholes d2 | Second BS parameter | `d1 - sig*sqrt(T)` | d1, volatility, time |
| 245 | `bsm_call_dividend` | BSM Call with Dividend | Call with continuous dividend | `S*e^(-qT)*N(d1) - K*e^(-rT)*N(d2)` | spot, strike, time, rate, volatility, dividend |
| 246 | `bsm_put_dividend` | BSM Put with Dividend | Put with continuous dividend | `K*e^(-rT)*N(-d2) - S*e^(-qT)*N(-d1)` | spot, strike, time, rate, volatility, dividend |
| 247 | `delta_call` | Delta (Call) | Price sensitivity to spot | `N(d1)` | spot, strike, time, rate, volatility |
| 248 | `delta_put` | Delta (Put) | Put price sensitivity | `N(d1) - 1` | spot, strike, time, rate, volatility |
| 249 | `gamma` | Gamma | Delta sensitivity to spot | `N'(d1) / (S*sig*sqrt(T))` | spot, strike, time, rate, volatility |
| 250 | `vega` | Vega | Price sensitivity to volatility | `S*N'(d1)*sqrt(T)` | spot, strike, time, rate, volatility |
| 251 | `theta_call` | Theta (Call) | Time decay of call | `Time decay formula` | spot, strike, time, rate, volatility |
| 252 | `theta_put` | Theta (Put) | Time decay of put | `Time decay formula` | spot, strike, time, rate, volatility |
| 253 | `rho_call` | Rho (Call) | Sensitivity to rate | `K*T*e^(-rT)*N(d2)` | spot, strike, time, rate, volatility |
| 254 | `rho_put` | Rho (Put) | Put rate sensitivity | `-K*T*e^(-rT)*N(-d2)` | spot, strike, time, rate, volatility |
| 255 | `vanna` | Vanna | Delta-vega cross sensitivity | `d(Delta)/d(vol)` | spot, strike, time, rate, volatility |
| 256 | `charm` | Charm | Delta decay | `d(Delta)/d(time)` | spot, strike, time, rate, volatility |
| 257 | `vomma` | Vomma | Vega convexity | `d(Vega)/d(vol)` | spot, strike, time, rate, volatility |
| 258 | `speed` | Speed | Gamma sensitivity to spot | `d(Gamma)/d(S)` | spot, strike, time, rate, volatility |
| 259 | `binomial_call` | Binomial Call (CRR) | Tree-based call pricing | `Cox-Ross-Rubinstein backward induction` | spot, strike, time, rate, volatility, steps |
| 260 | `binomial_put` | Binomial Put (CRR) | Tree-based put pricing | `CRR backward induction` | spot, strike, time, rate, volatility, steps |
| 261 | `trinomial_option` | Trinomial Option | 3-branch tree pricing | `Trinomial backward induction` | spot, strike, time, rate, volatility, steps |
| 262 | `monte_carlo_option` | Monte Carlo Option | Simulated path pricing | `Mean(discounted payoffs)` | spot, strike, time, rate, volatility, simulations |
| 263 | `implied_volatility` | Implied Volatility | Vol from market price | `Newton-Raphson solve for sigma` | option_price, spot, strike, time, rate |
| 264 | `put_call_parity` | Put-Call Parity | C - P = S - Ke^(-rT) | `Call - Put = Spot - PV(Strike)` | call, put, spot, strike, rate, time |
| 265 | `intrinsic_value_call` | Call Intrinsic Value | max(S - K, 0) | `max(Spot - Strike, 0)` | spot, strike |
| 266 | `intrinsic_value_put` | Put Intrinsic Value | max(K - S, 0) | `max(Strike - Spot, 0)` | spot, strike |
| 267 | `time_value_option` | Option Time Value | Price minus intrinsic | `Option_Price - Intrinsic_Value` | option_price, intrinsic_value |
| 268 | `forward_price` | Forward Price | Spot compounded to expiry | `S*e^(rT)` | spot, rate, time |
| 269 | `futures_price` | Futures Price | Spot with cost of carry | `S*e^((r+storage-yield)T)` | spot, rate, storage, yield, time |
| 270 | `forward_rate_agreement` | FRA Value | Forward rate agreement payoff | `Notional*(Ref - FRA)*Days/360` | notional, ref_rate, fra_rate, days |
| 271 | `swap_fixed_rate` | Swap Fixed Rate | Par swap rate | `(1 - DF_n) / Sum(DF_i)` | discount_factors |
| 272 | `swap_value` | Interest Rate Swap Value | PV fixed minus PV floating | `PV_Fixed - PV_Floating` | pv_fixed, pv_floating |
| 273 | `call_payoff` | Call Payoff at Expiry | Long call terminal value | `max(S - K, 0) - Premium` | spot, strike, premium |
| 274 | `put_payoff` | Put Payoff at Expiry | Long put terminal value | `max(K - S, 0) - Premium` | spot, strike, premium |
| 275 | `straddle_payoff` | Straddle Payoff | Long call + put | `\|S - K\| - Total_Premium` | spot, strike, total_premium |
| 276 | `strangle_payoff` | Strangle Payoff | OTM call + put | `max(S-Kc,0)+max(Kp-S,0)-Prem` | spot, strike_call, strike_put, premium |
| 277 | `covered_call_return` | Covered Call Return | Stock + short call yield | `(Premium + max(K-S,0)) / S` | spot, strike, premium |
| 278 | `collar_value` | Collar Value | Protective put + covered call | `Long put + short call payoff` | spot, put_strike, call_strike, net_premium |
| 279 | `butterfly_payoff` | Butterfly Spread Payoff | 3-strike limited spread | `Combined option payoff` | spot, strikes, premiums |
| 280 | `delta_hedge_shares` | Delta Hedge Shares | Shares to hedge option | `-Delta * Contracts * 100` | delta, contracts |
| 281 | `option_leverage` | Option Leverage (Lambda) | Elasticity to underlying | `Delta * S / Option_Price` | delta, spot, option_price |
| 282 | `breakeven_call` | Call Breakeven | Strike plus premium | `Strike + Premium` | strike, premium |
| 283 | `breakeven_put` | Put Breakeven | Strike minus premium | `Strike - Premium` | strike, premium |
| 284 | `max_pain` | Max Pain Price | Strike with max option loss | `Strike minimizing total payout` | strikes, open_interest |
| 285 | `historical_var_option` | Option Position VaR | Value at risk for option book | `Delta-gamma VaR approximation` | delta, gamma, spot, volatility, confidence |

### 5.6 Fixed Income & Bonds  ·  `fixed_income.py`  ·  50 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 286 | `bond_price` | Bond Price | PV of coupons + face | `Sum(C/(1+y)^t) + F/(1+y)^n` | coupon, face, yield, periods |
| 287 | `bond_price_clean` | Clean Bond Price | Dirty price minus accrued | `Dirty_Price - Accrued_Interest` | dirty_price, accrued_interest |
| 288 | `bond_price_dirty` | Dirty Bond Price | Clean plus accrued | `Clean_Price + Accrued_Interest` | clean_price, accrued_interest |
| 289 | `accrued_interest` | Accrued Interest | Coupon earned since last pay | `Coupon * Days_Since / Days_Period` | coupon, days_since, days_period |
| 290 | `ytm` | Yield to Maturity | IRR of bond cash flows | `Solve y in price equation` | price, coupon, face, periods |
| 291 | `ytc` | Yield to Call | Yield if called early | `Solve y to call date` | price, coupon, call_price, call_periods |
| 292 | `ytw` | Yield to Worst | Min of YTM and YTC | `min(YTM, YTC)` | ytm, ytc |
| 293 | `current_yield` | Current Yield | Annual coupon / price | `Annual_Coupon / Price` | annual_coupon, price |
| 294 | `coupon_rate` | Coupon Rate | Annual coupon / face | `Annual_Coupon / Face_Value` | annual_coupon, face_value |
| 295 | `macaulay_duration` | Macaulay Duration | Weighted avg time to CF | `Sum(t*PV_CF) / Price` | cash_flows, yield, periods |
| 296 | `modified_duration` | Modified Duration | Price sensitivity to yield | `Macaulay / (1 + y/n)` | macaulay_duration, yield, frequency |
| 297 | `effective_duration` | Effective Duration | Duration for embedded options | `(P- - P+) / (2*P0*dy)` | price_down, price_up, price_base, yield_change |
| 298 | `dollar_duration` | Dollar Duration | Price change per yield move | `Modified_Duration * Price * 0.0001` | modified_duration, price |
| 299 | `convexity` | Convexity | Curvature of price-yield | `Sum(t*(t+1)*PV_CF) / (Price*(1+y)^2)` | cash_flows, yield, periods |
| 300 | `effective_convexity` | Effective Convexity | Convexity with options | `(P- + P+ - 2*P0) / (P0*dy^2)` | price_down, price_up, price_base, yield_change |
| 301 | `dv01` | DV01 (PV01) | Dollar value of 1bp | `Modified_Duration * Price * 0.0001` | modified_duration, price |
| 302 | `price_change_duration` | Price Change (Duration) | Approx price move | `-Modified_Duration * Price * dy` | modified_duration, price, yield_change |
| 303 | `price_change_convexity` | Price Change (Dur+Conv) | Second-order price move | `-MD*P*dy + 0.5*Conv*P*dy^2` | modified_duration, convexity, price, yield_change |
| 304 | `spot_rate` | Spot Rate | Zero-coupon yield | `(Face/Price)^(1/n) - 1` | price, face, periods |
| 305 | `forward_rate` | Forward Rate | Implied future rate | `((1+s2)^t2/(1+s1)^t1)^(1/(t2-t1)) - 1` | spot1, spot2, time1, time2 |
| 306 | `par_yield` | Par Yield | Coupon for price = par | `(1 - DF_n) / Sum(DF_i)` | discount_factors |
| 307 | `zero_coupon_price` | Zero-Coupon Bond Price | PV of face value | `Face / (1+y)^n` | face, yield, periods |
| 308 | `discount_factor` | Discount Factor | PV of 1 unit | `1 / (1+r)^t` | rate, time |
| 309 | `bond_equivalent_yield` | Bond Equivalent Yield | Semi-annual to annual | `2 * ((1+y_semi) - 1)` | semi_annual_yield |
| 310 | `effective_annual_yield` | Effective Annual Yield | Compounded annual yield | `(1 + y/n)^n - 1` | yield, frequency |
| 311 | `holding_period_return` | Holding Period Return % | Total bond return | `(End + Coupons - Start) / Start * 100` | start_price, end_price, coupons |
| 312 | `realized_compound_yield` | Realized Compound Yield | Yield with reinvestment | `(Total_FV / Price)^(1/n) - 1` | price, total_fv, periods |
| 313 | `z_spread` | Z-Spread | Constant spread over spot curve | `Spread making PV = price` | price, cash_flows, spot_rates |
| 314 | `oas` | Option-Adjusted Spread | Z-spread minus option cost | `Z_Spread - Option_Cost` | z_spread, option_cost |
| 315 | `nominal_spread` | Nominal Spread | Bond yield minus benchmark | `Bond_YTM - Benchmark_YTM` | bond_ytm, benchmark_ytm |
| 316 | `g_spread` | G-Spread | Spread over govt curve | `Bond_Yield - Interpolated_Govt` | bond_yield, govt_yield |
| 317 | `i_spread` | I-Spread | Spread over swap rate | `Bond_Yield - Swap_Rate` | bond_yield, swap_rate |
| 318 | `asset_swap_spread` | Asset Swap Spread | Spread in asset swap | `Asset swap calculation` | bond_price, coupon, swap_rate |
| 319 | `credit_spread` | Credit Spread | Risky minus risk-free yield | `Corporate_Yield - Treasury_Yield` | corporate_yield, treasury_yield |
| 320 | `yield_curve_slope` | Yield Curve Slope | Long minus short yield | `Long_Yield - Short_Yield` | long_yield, short_yield |
| 321 | `yield_curve_butterfly` | Yield Curve Butterfly | Curvature measure | `2*Mid - Short - Long` | short_yield, mid_yield, long_yield |
| 322 | `key_rate_duration` | Key Rate Duration | Sensitivity to one tenor | `Price sensitivity to key rate` | price_changes, yield_change |
| 323 | `portfolio_duration` | Portfolio Duration | Weighted avg duration | `Sum(Weight_i * Duration_i)` | weights, durations |
| 324 | `portfolio_convexity` | Portfolio Convexity | Weighted avg convexity | `Sum(Weight_i * Convexity_i)` | weights, convexities |
| 325 | `reinvestment_income` | Reinvestment Income | FV of reinvested coupons | `Sum(C*(1+r)^(n-t))` | coupon, rate, periods |
| 326 | `interest_on_interest` | Interest on Interest | Compounding of coupons | `Reinvestment_Income - Total_Coupons` | reinvestment_income, total_coupons |
| 327 | `clean_to_invoice` | Invoice Price | Clean x factor + accrued | `Clean_Price*Factor + Accrued` | clean_price, conversion_factor, accrued |
| 328 | `bond_floor` | Convertible Bond Floor | Straight bond value | `PV of bond cash flows` | coupon, face, yield, periods |
| 329 | `conversion_value` | Conversion Value | Shares x stock price | `Conversion_Ratio * Stock_Price` | conversion_ratio, stock_price |
| 330 | `conversion_premium` | Conversion Premium % | Bond price over conversion value | `(Bond_Price - Conv_Value) / Conv_Value * 100` | bond_price, conversion_value |
| 331 | `tips_principal` | TIPS Adjusted Principal | Inflation-adjusted face | `Face * Index_Ratio` | face, index_ratio |
| 332 | `real_yield` | Real Yield | Nominal minus inflation | `Nominal_Yield - Inflation_Rate` | nominal_yield, inflation_rate |
| 333 | `breakeven_inflation` | Breakeven Inflation Rate | Nominal minus real yield | `Nominal_Yield - Real_Yield` | nominal_yield, real_yield |
| 334 | `rolling_yield` | Rolling Yield (Carry+Roll) | Carry plus rolldown | `Carry + Rolldown` | carry, rolldown |
| 335 | `expected_loss` | Expected Loss (Credit) | PD x LGD x EAD | `PD * LGD * EAD` | pd, lgd, ead |

### 5.7 Risk Management & Portfolio Theory  ·  `risk.py`  ·  50 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 336 | `var_historical` | VaR (Historical) | Loss at percentile | `Percentile(Returns, 1-conf)` | returns, confidence |
| 337 | `var_parametric` | VaR (Parametric) | Normal distribution VaR | `-(mu + z*sigma)*Value` | mean, std, confidence, value |
| 338 | `var_monte_carlo` | VaR (Monte Carlo) | Simulated loss distribution | `Percentile of simulated P&L` | returns, confidence, simulations |
| 339 | `cvar` | Conditional VaR (ES) | Expected loss beyond VaR | `Mean(Losses > VaR)` | returns, confidence |
| 340 | `expected_shortfall` | Expected Shortfall | Average tail loss | `Mean(Returns below VaR)` | returns, confidence |
| 341 | `sharpe_ratio` | Sharpe Ratio | Excess return per risk | `(Return - Rf) / StdDev` | returns, risk_free, std |
| 342 | `sortino_ratio` | Sortino Ratio | Return per downside risk | `(Return - Rf) / Downside_Dev` | returns, risk_free, downside_deviation |
| 343 | `treynor_ratio` | Treynor Ratio | Return per beta | `(Return - Rf) / Beta` | returns, risk_free, beta |
| 344 | `information_ratio` | Information Ratio | Active return per tracking error | `(Return - Benchmark) / Tracking_Error` | returns, benchmark, tracking_error |
| 345 | `jensens_alpha` | Jensen's Alpha | Return above CAPM | `Return - (Rf + Beta*(Rm-Rf))` | returns, risk_free, beta, market_return |
| 346 | `calmar_ratio` | Calmar Ratio | Return per max drawdown | `Annual_Return / Max_Drawdown` | annual_return, max_drawdown |
| 347 | `sterling_ratio` | Sterling Ratio | Return per avg drawdown | `Annual_Return / Avg_Drawdown` | annual_return, avg_drawdown |
| 348 | `max_drawdown` | Maximum Drawdown % | Largest peak-trough drop | `(Trough - Peak) / Peak * 100` | prices |
| 349 | `drawdown_duration` | Drawdown Duration | Time underwater | `Periods from peak to recovery` | prices |
| 350 | `beta` | Beta | Systematic risk vs market | `Cov(Stock,Market) / Var(Market)` | stock_returns, market_returns |
| 351 | `alpha` | Alpha | Excess return vs benchmark | `Return - Benchmark_Return` | returns, benchmark_return |
| 352 | `tracking_error` | Tracking Error | Std of active returns | `StdDev(Portfolio - Benchmark)` | portfolio_returns, benchmark_returns |
| 353 | `downside_deviation` | Downside Deviation | Std of negative returns | `sqrt(Mean(min(0, R-MAR)^2))` | returns, min_acceptable_return |
| 354 | `semi_variance` | Semi-Variance | Variance of downside | `Mean((min(0, R-mean))^2)` | returns |
| 355 | `covariance` | Covariance | Joint variability | `Mean((X-Xbar)(Y-Ybar))` | series_x, series_y |
| 356 | `correlation` | Correlation | Normalized covariance | `Cov(X,Y) / (StdX*StdY)` | series_x, series_y |
| 357 | `portfolio_return` | Portfolio Return | Weighted asset returns | `Sum(Weight_i * Return_i)` | weights, returns |
| 358 | `portfolio_variance` | Portfolio Variance | Markowitz 2-asset variance | `w1^2*v1 + w2^2*v2 + 2*w1*w2*cov` | weights, variances, covariance |
| 359 | `portfolio_std` | Portfolio Std Dev | Root of portfolio variance | `sqrt(Portfolio_Variance)` | portfolio_variance |
| 360 | `portfolio_beta` | Portfolio Beta | Weighted average beta | `Sum(Weight_i * Beta_i)` | weights, betas |
| 361 | `minimum_variance_weight` | Min Variance Weight | Optimal 2-asset weight | `(v2-cov)/(v1+v2-2*cov)` | variance1, variance2, covariance |
| 362 | `efficient_frontier_return` | Efficient Frontier Return | Optimal return for risk | `Quadratic optimization` | returns, covariance_matrix, target_risk |
| 363 | `capital_allocation_line` | Capital Allocation Line | Risk-return tradeoff line | `Rf + Sharpe * Sigma` | risk_free, sharpe, sigma |
| 364 | `capital_market_line` | Capital Market Line | Efficient frontier with Rf | `Rf + ((Rm-Rf)/SigmaM)*Sigma` | risk_free, market_return, market_std, portfolio_std |
| 365 | `security_market_line` | Security Market Line | CAPM expected return line | `Rf + Beta*(Rm - Rf)` | risk_free, beta, market_return |
| 366 | `diversification_ratio` | Diversification Ratio | Weighted vol / portfolio vol | `Sum(w*sigma) / Portfolio_Sigma` | weights, volatilities, portfolio_std |
| 367 | `risk_parity_weight` | Risk Parity Weight | Equal risk contribution | `Inverse vol weighting` | volatilities |
| 368 | `marginal_var` | Marginal VaR | VaR change per position | `d(VaR)/d(weight)` | weights, covariance_matrix, position |
| 369 | `component_var` | Component VaR | Position contribution to VaR | `Marginal_VaR * Position` | marginal_var, position_value |
| 370 | `incremental_var` | Incremental VaR | VaR change adding position | `VaR_with - VaR_without` | var_with, var_without |
| 371 | `ulcer_index` | Ulcer Index | Downside volatility measure | `sqrt(Mean(Drawdown^2))` | prices |
| 372 | `gain_to_pain` | Gain to Pain Ratio | Sum returns / sum losses | `Sum(Returns) / abs(Sum(Losses))` | returns |
| 373 | `omega_ratio` | Omega Ratio | Gains vs losses ratio | `Sum(Gains) / Sum(Losses) above threshold` | returns, threshold |
| 374 | `kappa_ratio` | Kappa Ratio | Higher-moment downside ratio | `(Return - MAR) / LPM^(1/n)` | returns, min_acceptable_return, order |
| 375 | `upside_potential_ratio` | Upside Potential Ratio | Upside vs downside | `Upside / Downside_Deviation` | returns, min_acceptable_return |
| 376 | `value_at_risk_normal` | Parametric VaR (Normal) | Z-score based VaR | `Value * z * sigma * sqrt(t)` | value, confidence, sigma, time |
| 377 | `conditional_drawdown` | Conditional Drawdown at Risk | Expected tail drawdown | `Mean of worst drawdowns` | prices, confidence |
| 378 | `pain_index` | Pain Index | Average drawdown depth | `Mean(Drawdowns)` | prices |
| 379 | `burke_ratio` | Burke Ratio | Return per sqrt sum drawdowns | `Return / sqrt(Sum(DD^2))` | returns, drawdowns |
| 380 | `m2_measure` | M-Squared (M2) | Risk-adjusted vs market | `Rf + Sharpe * Market_Std` | sharpe, market_std, risk_free |
| 381 | `active_premium` | Active Premium | Return over benchmark | `Annual_Return - Benchmark_Return` | annual_return, benchmark_return |
| 382 | `hurst_exponent` | Hurst Exponent | Trend persistence measure | `Rescaled range analysis` | prices |
| 383 | `kelly_criterion` | Kelly Criterion | Optimal bet fraction | `(p*b - q) / b` | win_prob, win_loss_ratio |
| 384 | `risk_of_ruin` | Risk of Ruin | Probability of bankruptcy | `((1-edge)/(1+edge))^units` | edge, capital_units |
| 385 | `expected_value` | Expected Value | Probability-weighted outcome | `Sum(Probability_i * Outcome_i)` | probabilities, outcomes |

### 5.8 Time Value of Money & Capital Budgeting  ·  `tvm.py`  ·  45 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 386 | `present_value` | Present Value | Discounted future value | `FV / (1+r)^n` | future_value, rate, periods |
| 387 | `future_value` | Future Value | Compounded present value | `PV * (1+r)^n` | present_value, rate, periods |
| 388 | `npv` | Net Present Value | Sum of discounted CFs minus cost | `Sum(CF_t/(1+r)^t) - Initial` | cash_flows, rate, initial_investment |
| 389 | `irr` | Internal Rate of Return | Rate where NPV = 0 | `Solve r: NPV = 0` | cash_flows, initial_investment |
| 390 | `mirr` | Modified IRR | IRR with reinvestment rate | `(FV_inflows/PV_outflows)^(1/n) - 1` | cash_flows, finance_rate, reinvest_rate |
| 391 | `xirr` | XIRR (Irregular) | IRR for irregular dates | `Solve for rate with dates` | cash_flows, dates |
| 392 | `pv_annuity` | PV of Annuity | PV of equal payments | `PMT * (1-(1+r)^-n)/r` | payment, rate, periods |
| 393 | `fv_annuity` | FV of Annuity | FV of equal payments | `PMT * ((1+r)^n - 1)/r` | payment, rate, periods |
| 394 | `pv_annuity_due` | PV of Annuity Due | PV with payments at start | `PV_Annuity * (1+r)` | payment, rate, periods |
| 395 | `fv_annuity_due` | FV of Annuity Due | FV with payments at start | `FV_Annuity * (1+r)` | payment, rate, periods |
| 396 | `perpetuity` | Perpetuity Value | Infinite equal payments | `PMT / r` | payment, rate |
| 397 | `growing_perpetuity` | Growing Perpetuity | Infinite growing payments | `PMT / (r - g)` | payment, rate, growth |
| 398 | `growing_annuity_pv` | PV Growing Annuity | PV of growing payments | `PMT/(r-g)*(1-((1+g)/(1+r))^n)` | payment, rate, growth, periods |
| 399 | `annuity_payment` | Annuity Payment (PMT) | Payment for loan/annuity | `PV*r / (1-(1+r)^-n)` | present_value, rate, periods |
| 400 | `loan_payment` | Loan Payment | Amortizing loan payment | `P*r / (1-(1+r)^-n)` | principal, rate, periods |
| 401 | `loan_balance` | Remaining Loan Balance | Outstanding after k payments | `P*(1+r)^k - PMT*((1+r)^k-1)/r` | principal, rate, payment, periods_paid |
| 402 | `amortization_interest` | Amortization Interest Portion | Interest in payment k | `Balance * Rate` | balance, rate |
| 403 | `amortization_principal` | Amortization Principal Portion | Principal in payment k | `Payment - Interest` | payment, interest |
| 404 | `effective_annual_rate` | Effective Annual Rate | Annual compounded rate | `(1 + r/n)^n - 1` | nominal_rate, frequency |
| 405 | `nominal_rate` | Nominal Rate from EAR | APR from effective rate | `n*((1+EAR)^(1/n) - 1)` | ear, frequency |
| 406 | `continuous_compounding` | Continuous Compounding FV | FV with continuous rate | `PV * e^(rt)` | present_value, rate, time |
| 407 | `continuous_pv` | Continuous Compounding PV | PV with continuous rate | `FV * e^(-rt)` | future_value, rate, time |
| 408 | `rule_of_72` | Rule of 72 | Doubling time estimate | `72 / Rate_Percent` | rate_percent |
| 409 | `rule_of_69` | Rule of 69.3 | Continuous doubling time | `69.3 / Rate_Percent` | rate_percent |
| 410 | `payback_period` | Payback Period | Time to recover investment | `Years until cumulative CF = 0` | cash_flows, initial_investment |
| 411 | `discounted_payback` | Discounted Payback Period | Payback with discounting | `Years until discounted cum = 0` | cash_flows, rate, initial_investment |
| 412 | `profitability_index` | Profitability Index | PV inflows / initial cost | `PV_Inflows / Initial_Investment` | pv_inflows, initial_investment |
| 413 | `equivalent_annual_cost` | Equivalent Annual Cost | Annualized project cost | `NPV / Annuity_Factor` | npv, rate, periods |
| 414 | `equivalent_annual_annuity` | Equivalent Annual Annuity | Annualized NPV | `NPV * r / (1-(1+r)^-n)` | npv, rate, periods |
| 415 | `crossover_rate` | Crossover Rate | Rate where two NPVs equal | `IRR of CF differences` | cash_flows_a, cash_flows_b |
| 416 | `real_rate` | Real Rate of Return | Inflation-adjusted rate | `(1+nominal)/(1+inflation) - 1` | nominal_rate, inflation_rate |
| 417 | `fisher_equation` | Fisher Equation | Nominal = real + inflation | `(1+real)*(1+inflation) - 1` | real_rate, inflation_rate |
| 418 | `annuity_factor` | Annuity Factor | PV factor for annuity | `(1-(1+r)^-n) / r` | rate, periods |
| 419 | `future_value_factor` | Future Value Factor | Compounding factor | `(1+r)^n` | rate, periods |
| 420 | `present_value_factor` | Present Value Factor | Discount factor | `1 / (1+r)^n` | rate, periods |
| 421 | `sinking_fund` | Sinking Fund Payment | Payment to reach FV | `FV*r / ((1+r)^n - 1)` | future_value, rate, periods |
| 422 | `capital_recovery_factor` | Capital Recovery Factor | Annuity from present value | `r / (1-(1+r)^-n)` | rate, periods |
| 423 | `deferred_annuity_pv` | Deferred Annuity PV | PV of delayed annuity | `PV_Annuity / (1+r)^defer` | payment, rate, periods, deferral |
| 424 | `net_future_value` | Net Future Value | FV of all cash flows | `Sum(CF_t * (1+r)^(n-t))` | cash_flows, rate |
| 425 | `modified_payback` | Modified Payback | Payback with terminal value | `Adjusted payback period` | cash_flows, terminal_value |
| 426 | `accounting_rate_of_return` | Accounting Rate of Return | Avg profit / avg investment | `Avg_Profit / Avg_Investment * 100` | average_profit, average_investment |
| 427 | `bcr` | Benefit-Cost Ratio | PV benefits / PV costs | `PV_Benefits / PV_Costs` | pv_benefits, pv_costs |
| 428 | `annualized_return` | Annualized Return | Geometric annual return | `(End/Start)^(1/years) - 1` | start_value, end_value, years |
| 429 | `holding_period_yield` | Holding Period Yield % | Total period return | `(End + Income - Start)/Start*100` | start_value, end_value, income |
| 430 | `breakeven_interest_rate` | Breakeven Interest Rate | Rate for indifference | `Rate where NPV = 0` | cash_flows |

### 5.9 Corporate Finance & M&A  ·  `corporate_ma.py`  ·  50 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 431 | `sustainable_growth_rate` | Sustainable Growth Rate | ROE x retention | `ROE * Retention_Ratio` | roe, retention_ratio |
| 432 | `internal_growth_rate` | Internal Growth Rate | Growth without external finance | `(ROA*b)/(1-ROA*b)` | roa, retention_ratio |
| 433 | `plowback_ratio` | Plowback Ratio | Retained earnings fraction | `1 - Dividend_Payout` | dividend_payout |
| 434 | `roic` | Return on Invested Capital | NOPAT / invested capital | `NOPAT / Invested_Capital` | nopat, invested_capital |
| 435 | `invested_capital` | Invested Capital | Debt + equity - cash | `Total_Debt + Equity - Cash` | total_debt, equity, cash |
| 436 | `economic_profit` | Economic Profit | NOPAT minus capital charge | `NOPAT - Invested_Capital*WACC` | nopat, invested_capital, wacc |
| 437 | `hamada_equation` | Hamada Equation | Levered beta from unlevered | `Bu*(1 + (1-T)*D/E)` | unlevered_beta, tax_rate, debt, equity |
| 438 | `unlever_beta` | Unlevered Beta | Asset beta from equity beta | `Be / (1 + (1-T)*D/E)` | levered_beta, tax_rate, debt, equity |
| 439 | `relever_beta` | Relevered Beta | Equity beta from asset beta | `Ba*(1 + (1-T)*D/E)` | asset_beta, tax_rate, debt, equity |
| 440 | `mm_proposition1_no_tax` | M&M Proposition I (No Tax) | Value independent of capital | `VL = VU` | unlevered_value |
| 441 | `mm_proposition1_tax` | M&M Proposition I (Tax) | Value with tax shield | `VU + Tax_Rate*Debt` | unlevered_value, tax_rate, debt |
| 442 | `mm_proposition2` | M&M Proposition II | Cost of equity with leverage | `Ru + (Ru-Rd)*(D/E)*(1-T)` | unlevered_cost, cost_debt, debt, equity, tax_rate |
| 443 | `tax_shield` | Tax Shield Value | PV of interest tax savings | `Tax_Rate * Debt` | tax_rate, debt |
| 444 | `interest_tax_shield_annual` | Annual Interest Tax Shield | Yearly tax savings | `Interest * Tax_Rate` | interest, tax_rate |
| 445 | `degree_total_leverage` | Degree of Total Leverage | Combined operating + financial | `DOL * DFL` | dol, dfl |
| 446 | `free_cash_flow_firm` | FCFF (Detailed) | Cash to all capital providers | `NI + NCC + Int*(1-T) - FCInv - WCInv` | net_income, ncc, interest, tax_rate, fcinv, wcinv |
| 447 | `free_cash_flow_equity` | FCFE (Detailed) | Cash to equity holders | `NI + NCC - FCInv - WCInv + Net_Borrowing` | net_income, ncc, fcinv, wcinv, net_borrowing |
| 448 | `cash_flow_available_debt` | CFADS | Cash available for debt service | `EBITDA - Tax - WC - CapEx` | ebitda, tax, working_capital_change, capex |
| 449 | `accretion_dilution` | Accretion/Dilution % | EPS change from deal | `(ProForma_EPS - Standalone_EPS)/Standalone*100` | proforma_eps, standalone_eps |
| 450 | `exchange_ratio` | Exchange Ratio | Target shares per acquirer share | `Offer_Price / Acquirer_Price` | offer_price, acquirer_price |
| 451 | `acquisition_premium` | Acquisition Premium % | Offer over market price | `(Offer - Market)/Market * 100` | offer_price, market_price |
| 452 | `synergy_value` | Synergy Value | Combined value minus standalone | `V_Combined - (V_A + V_B)` | combined_value, value_a, value_b |
| 453 | `goodwill` | Goodwill | Purchase price over fair value | `Purchase_Price - Fair_Value_Net_Assets` | purchase_price, fair_value_net_assets |
| 454 | `purchase_price_allocation` | Net Identifiable Assets | Fair value of assets minus liabilities | `FV_Assets - FV_Liabilities` | fv_assets, fv_liabilities |
| 455 | `pro_forma_eps` | Pro Forma EPS | Combined EPS post-merger | `Combined_NI / Combined_Shares` | combined_net_income, combined_shares |
| 456 | `breakeven_synergies` | Breakeven Synergies | Synergies to justify premium | `Premium_Paid value` | premium, target_shares |
| 457 | `lbo_equity_return` | LBO Equity Return (MOIC) | Multiple of invested capital | `Exit_Equity / Entry_Equity` | exit_equity, entry_equity |
| 458 | `lbo_irr` | LBO IRR | Annualized LBO return | `(Exit/Entry)^(1/years) - 1` | entry_equity, exit_equity, years |
| 459 | `debt_paydown` | Debt Paydown | Cumulative debt reduction | `Entry_Debt - Exit_Debt` | entry_debt, exit_debt |
| 460 | `entry_multiple` | Entry Multiple | Purchase EV / EBITDA | `Entry_EV / EBITDA` | entry_ev, ebitda |
| 461 | `exit_multiple` | Exit Multiple | Sale EV / EBITDA | `Exit_EV / EBITDA` | exit_ev, ebitda |
| 462 | `sources_uses_balance` | Sources and Uses Balance | Total sources = total uses | `Sum(Sources) - Sum(Uses)` | sources, uses |
| 463 | `net_borrowing` | Net Borrowing | New debt minus repayments | `Debt_Issued - Debt_Repaid` | debt_issued, debt_repaid |
| 464 | `dividend_discount_value` | DDM Value | PV of all dividends | `Sum(D_t/(1+r)^t)` | dividends, rate |
| 465 | `clientele_effect` | After-Tax Dividend | Dividend net of tax | `Dividend * (1 - Tax_Rate)` | dividend, tax_rate |
| 466 | `share_buyback_eps_impact` | Buyback EPS Impact | EPS after share reduction | `NI / (Shares - Bought)` | net_income, shares, shares_bought |
| 467 | `treasury_stock_method` | Treasury Stock Method | Diluted shares from options | `Options - (Options*Strike/Price)` | options, strike, price |
| 468 | `weighted_avg_shares` | Weighted Average Shares | Time-weighted share count | `Sum(Shares_i * Months_i / 12)` | share_periods |
| 469 | `capital_structure_weight_equity` | Equity Weight | Equity / total capital | `Equity / (Equity + Debt)` | equity, debt |
| 470 | `capital_structure_weight_debt` | Debt Weight | Debt / total capital | `Debt / (Equity + Debt)` | equity, debt |
| 471 | `operating_working_capital` | Operating Working Capital | Operating current assets - liabilities | `Op_Current_Assets - Op_Current_Liabilities` | op_current_assets, op_current_liabilities |
| 472 | `invested_capital_turnover` | Invested Capital Turnover | Revenue / invested capital | `Revenue / Invested_Capital` | revenue, invested_capital |
| 473 | `reinvestment_rate` | Reinvestment Rate | Net investment / NOPAT | `(CapEx - Depr + WCInv) / NOPAT` | capex, depreciation, wc_investment, nopat |
| 474 | `expected_growth_fundamentals` | Expected Growth (Fundamentals) | Reinvestment x ROIC | `Reinvestment_Rate * ROIC` | reinvestment_rate, roic |
| 475 | `terminal_growth_implied` | Implied Terminal Growth | Growth from terminal value | `r - FCF/TV` | rate, fcf, terminal_value |
| 476 | `equity_value_from_ev` | Equity Value from EV | EV minus net debt | `EV - Net_Debt` | ev, net_debt |
| 477 | `net_debt_to_equity_value` | Net Debt to Equity Value | Leverage in valuation | `Net_Debt / Equity_Value` | net_debt, equity_value |
| 478 | `dilution_percentage` | Dilution Percentage | New shares as % of total | `New_Shares / (Old + New) * 100` | old_shares, new_shares |
| 479 | `control_premium` | Control Premium % | Premium for control stake | `(Control_Price - Minority)/Minority*100` | control_price, minority_price |
| 480 | `minority_interest_value` | Minority Interest Value | Non-controlling stake value | `Subsidiary_Value * Minority_Pct` | subsidiary_value, minority_pct |

### 5.10 Accounting & Depreciation  ·  `accounting.py`  ·  40 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 481 | `straight_line_depreciation` | Straight-Line Depreciation | Equal annual depreciation | `(Cost - Salvage) / Useful_Life` | cost, salvage, useful_life |
| 482 | `declining_balance` | Declining Balance Depreciation | Accelerated depreciation | `Book_Value * Rate` | book_value, rate |
| 483 | `double_declining_balance` | Double Declining Balance | 2x straight-line rate | `Book_Value * (2/Useful_Life)` | book_value, useful_life |
| 484 | `units_of_production` | Units of Production Depreciation | Depreciation per unit used | `(Cost-Salvage)/Total_Units * Units_Used` | cost, salvage, total_units, units_used |
| 485 | `sum_of_years_digits` | Sum-of-Years-Digits | Accelerated depreciation | `(Cost-Salvage)*RemainingLife/SYD` | cost, salvage, useful_life, current_year |
| 486 | `macrs_depreciation` | MACRS Depreciation | US tax depreciation | `Cost * MACRS_Rate` | cost, macrs_rate |
| 487 | `accumulated_depreciation` | Accumulated Depreciation | Total depreciation to date | `Sum(Annual_Depreciation)` | annual_depreciations |
| 488 | `book_value_asset` | Net Book Value | Cost minus accumulated depr | `Cost - Accumulated_Depreciation` | cost, accumulated_depreciation |
| 489 | `depreciation_rate` | Depreciation Rate % | Annual depreciation / cost | `Annual_Depreciation / Cost * 100` | annual_depreciation, cost |
| 490 | `amortization_intangible` | Intangible Amortization | Straight-line for intangibles | `Cost / Useful_Life` | cost, useful_life |
| 491 | `depletion` | Depletion Expense | Natural resource expense | `(Cost-Salvage)/Total_Units * Extracted` | cost, salvage, total_units, units_extracted |
| 492 | `fifo_cogs` | FIFO COGS | First-in-first-out cost | `Oldest inventory costs` | inventory_layers, units_sold |
| 493 | `lifo_cogs` | LIFO COGS | Last-in-first-out cost | `Newest inventory costs` | inventory_layers, units_sold |
| 494 | `weighted_average_cost` | Weighted Average Cost | Average inventory cost | `Total_Cost / Total_Units` | total_cost, total_units |
| 495 | `lifo_reserve` | LIFO Reserve | FIFO minus LIFO inventory | `FIFO_Inventory - LIFO_Inventory` | fifo_inventory, lifo_inventory |
| 496 | `inventory_write_down` | Inventory Write-Down | Lower of cost or market | `max(0, Cost - Market)` | cost, market_value |
| 497 | `ending_inventory` | Ending Inventory | Beginning + purchases - COGS | `Beginning + Purchases - COGS` | beginning, purchases, cogs |
| 498 | `cogs_calculation` | COGS Calculation | Beginning + purchases - ending | `Beginning + Purchases - Ending` | beginning_inventory, purchases, ending_inventory |
| 499 | `gross_profit_method` | Gross Profit Method | Estimate inventory | `Sales - (Sales*Gross_Margin)` | sales, gross_margin |
| 500 | `bad_debt_percentage_sales` | Bad Debt (% of Sales) | Bad debt from sales | `Credit_Sales * Bad_Debt_Rate` | credit_sales, bad_debt_rate |
| 501 | `bad_debt_aging` | Bad Debt (Aging) | Bad debt from receivables aging | `Sum(Receivable_Bucket * Rate)` | receivable_buckets, rates |
| 502 | `allowance_doubtful_accounts` | Allowance for Doubtful Accounts | Estimated uncollectible | `Receivables * Uncollectible_Rate` | receivables, uncollectible_rate |
| 503 | `net_realizable_value` | Net Realizable Value | Receivables minus allowance | `Receivables - Allowance` | receivables, allowance |
| 504 | `deferred_tax_liability` | Deferred Tax Liability | Future tax on temp differences | `Temp_Difference * Tax_Rate` | temporary_difference, tax_rate |
| 505 | `deferred_tax_asset` | Deferred Tax Asset | Future tax benefit | `Deductible_Difference * Tax_Rate` | deductible_difference, tax_rate |
| 506 | `effective_tax_rate_acct` | Effective Tax Rate | Tax expense / pretax income | `Tax_Expense / Pretax_Income * 100` | tax_expense, pretax_income |
| 507 | `stock_compensation_expense` | Stock Comp Expense | Fair value amortized | `Fair_Value / Vesting_Period` | fair_value, vesting_period |
| 508 | `pension_pbo` | Projected Benefit Obligation | PV of pension obligations | `PV of future benefits` | benefits, discount_rate, periods |
| 509 | `pension_funded_status` | Pension Funded Status | Plan assets minus PBO | `Plan_Assets - PBO` | plan_assets, pbo |
| 510 | `pension_expense` | Net Periodic Pension Cost | Annual pension expense | `Service + Interest - ExpReturn + Amort` | service_cost, interest_cost, expected_return, amortization |
| 511 | `operating_lease_expense` | Operating Lease Expense | Straight-line lease cost | `Total_Lease / Lease_Term` | total_lease_payments, lease_term |
| 512 | `finance_lease_liability` | Finance Lease Liability | PV of lease payments | `PV(Lease_Payments, Rate)` | lease_payments, rate, periods |
| 513 | `right_of_use_asset` | Right-of-Use Asset | Lease liability + costs | `Lease_Liability + Initial_Costs` | lease_liability, initial_costs |
| 514 | `capitalized_interest` | Capitalized Interest | Interest during construction | `Avg_Expenditure * Rate` | average_expenditure, interest_rate |
| 515 | `revenue_recognition_percentage` | Percentage of Completion | Revenue by completion | `Total_Revenue * Pct_Complete` | total_revenue, percent_complete |
| 516 | `deferred_revenue` | Deferred Revenue | Unearned revenue liability | `Cash_Received - Revenue_Earned` | cash_received, revenue_earned |
| 517 | `comprehensive_income` | Comprehensive Income | Net income + OCI | `Net_Income + Other_Comprehensive_Income` | net_income, oci |
| 518 | `retained_earnings_ending` | Ending Retained Earnings | Beginning + NI - dividends | `Beginning_RE + Net_Income - Dividends` | beginning_re, net_income, dividends |
| 519 | `goodwill_impairment` | Goodwill Impairment | Carrying minus fair value | `max(0, Carrying - Fair_Value)` | carrying_value, fair_value |
| 520 | `asset_impairment` | Asset Impairment Loss | Carrying over recoverable | `max(0, Carrying - Recoverable)` | carrying_value, recoverable_amount |

### 5.11 Statistics & Econometrics  ·  `statistics_econ.py`  ·  45 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 521 | `arithmetic_mean` | Arithmetic Mean | Simple average | `Sum(x) / n` | values |
| 522 | `geometric_mean` | Geometric Mean | Compound average | `(Prod(x))^(1/n)` | values |
| 523 | `harmonic_mean` | Harmonic Mean | Reciprocal average | `n / Sum(1/x)` | values |
| 524 | `weighted_mean` | Weighted Mean | Weighted average | `Sum(w*x) / Sum(w)` | values, weights |
| 525 | `median` | Median | Middle value | `Middle of sorted values` | values |
| 526 | `mode` | Mode | Most frequent value | `Most common value` | values |
| 527 | `range_stat` | Range | Max minus min | `Max - Min` | values |
| 528 | `variance_population` | Population Variance | Average squared deviation | `Sum((x-mu)^2) / N` | values |
| 529 | `variance_sample` | Sample Variance | Unbiased variance | `Sum((x-xbar)^2) / (n-1)` | values |
| 530 | `standard_deviation_pop` | Population Std Dev | Root of population variance | `sqrt(Population_Variance)` | values |
| 531 | `standard_deviation_sample` | Sample Std Dev | Root of sample variance | `sqrt(Sample_Variance)` | values |
| 532 | `coefficient_variation` | Coefficient of Variation | Std / mean | `StdDev / Mean` | values |
| 533 | `skewness` | Skewness | Distribution asymmetry | `E[(x-mu)^3] / sigma^3` | values |
| 534 | `kurtosis` | Kurtosis | Tail heaviness | `E[(x-mu)^4] / sigma^4` | values |
| 535 | `excess_kurtosis` | Excess Kurtosis | Kurtosis minus 3 | `Kurtosis - 3` | values |
| 536 | `covariance_stat` | Covariance | Joint variability | `Sum((x-xbar)(y-ybar))/(n-1)` | series_x, series_y |
| 537 | `pearson_correlation` | Pearson Correlation | Linear correlation | `Cov(X,Y)/(SdX*SdY)` | series_x, series_y |
| 538 | `spearman_correlation` | Spearman Correlation | Rank correlation | `1 - 6*Sum(d^2)/(n(n^2-1))` | series_x, series_y |
| 539 | `linear_regression_beta` | Regression Slope (Beta) | OLS slope coefficient | `Cov(X,Y) / Var(X)` | series_x, series_y |
| 540 | `linear_regression_alpha` | Regression Intercept | OLS intercept | `Ybar - Beta*Xbar` | series_x, series_y |
| 541 | `r_squared` | R-Squared | Explained variance fraction | `1 - SSres/SStot` | actual, predicted |
| 542 | `adjusted_r_squared` | Adjusted R-Squared | R2 penalized for predictors | `1 - (1-R2)(n-1)/(n-k-1)` | r_squared, n, predictors |
| 543 | `standard_error` | Standard Error | Std of sampling distribution | `StdDev / sqrt(n)` | values |
| 544 | `standard_error_regression` | Standard Error of Regression | Residual standard error | `sqrt(SSres/(n-2))` | residuals, n |
| 545 | `t_statistic` | T-Statistic | Standardized test stat | `(xbar - mu) / (s/sqrt(n))` | sample_mean, pop_mean, std, n |
| 546 | `z_score` | Z-Score | Standard deviations from mean | `(x - mu) / sigma` | value, mean, std |
| 547 | `confidence_interval` | Confidence Interval | Range for parameter | `mean +/- z*(s/sqrt(n))` | mean, std, n, confidence |
| 548 | `chi_square_stat` | Chi-Square Statistic | Goodness of fit test | `Sum((O-E)^2 / E)` | observed, expected |
| 549 | `f_statistic` | F-Statistic | Variance ratio test | `Var1 / Var2` | variance1, variance2 |
| 550 | `percentile` | Percentile | Value at given percentile | `Interpolated rank value` | values, percentile |
| 551 | `quartile` | Quartile | 25/50/75 split values | `Percentile at 25/50/75` | values, quartile_number |
| 552 | `interquartile_range` | Interquartile Range (IQR) | Q3 minus Q1 | `Q3 - Q1` | values |
| 553 | `autocorrelation` | Autocorrelation | Self-correlation at lag | `Corr(x_t, x_t-k)` | series, lag |
| 554 | `moving_average_forecast` | Moving Average Forecast | Average of last n | `Mean(last n values)` | values, window |
| 555 | `exponential_smoothing` | Exponential Smoothing | Weighted recent forecast | `alpha*x + (1-alpha)*prev` | values, alpha |
| 556 | `holt_linear_trend` | Holt's Linear Trend | Level + trend forecast | `Level + Trend smoothing` | values, alpha, beta |
| 557 | `holt_winters` | Holt-Winters Seasonal | Level + trend + seasonal | `Triple exponential smoothing` | values, alpha, beta, gamma, season_length |
| 558 | `ar1_model` | AR(1) Model | First-order autoregression | `c + phi*x_prev + error` | series, phi, constant |
| 559 | `durbin_watson` | Durbin-Watson Statistic | Autocorrelation test | `Sum((e_t-e_t-1)^2)/Sum(e_t^2)` | residuals |
| 560 | `mean_absolute_error` | Mean Absolute Error | Average absolute error | `Mean(\|actual - predicted\|)` | actual, predicted |
| 561 | `mean_squared_error` | Mean Squared Error | Average squared error | `Mean((actual - predicted)^2)` | actual, predicted |
| 562 | `rmse` | Root Mean Squared Error | Root of MSE | `sqrt(MSE)` | actual, predicted |
| 563 | `mape` | Mean Absolute Percentage Error | Average % error | `Mean(\|actual-pred\|/actual)*100` | actual, predicted |
| 564 | `theil_u` | Theil's U Statistic | Forecast accuracy | `RMSE / (RMSE_actual + RMSE_pred)` | actual, predicted |
| 565 | `garch_volatility` | GARCH(1,1) Volatility | Conditional volatility | `omega + alpha*r^2 + beta*var_prev` | returns, omega, alpha, beta |

### 5.12 Core Math, Trigonometry, Linear Algebra & Geometry  ·  `math_core.py`  ·  45 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 566 | `sine` | Sine | Trig sine function | `sin(theta)` | angle_radians |
| 567 | `cosine` | Cosine | Trig cosine function | `cos(theta)` | angle_radians |
| 568 | `tangent` | Tangent | Trig tangent function | `tan(theta)` | angle_radians |
| 569 | `arcsine` | Arcsine | Inverse sine | `asin(x)` | value |
| 570 | `arccosine` | Arccosine | Inverse cosine | `acos(x)` | value |
| 571 | `arctangent` | Arctangent | Inverse tangent | `atan(x)` | value |
| 572 | `atan2` | Atan2 | Two-argument arctangent | `atan2(y, x)` | y, x |
| 573 | `degrees_to_radians` | Degrees to Radians | Angle conversion | `deg * pi/180` | degrees |
| 574 | `radians_to_degrees` | Radians to Degrees | Angle conversion | `rad * 180/pi` | radians |
| 575 | `pythagorean` | Pythagorean Theorem | Right triangle hypotenuse | `sqrt(a^2 + b^2)` | a, b |
| 576 | `law_of_cosines` | Law of Cosines | Triangle side from angle | `sqrt(a^2+b^2-2ab*cos(C))` | a, b, angle_c |
| 577 | `law_of_sines` | Law of Sines | Triangle side-angle ratio | `a/sin(A) = b/sin(B)` | side_a, angle_a, angle_b |
| 578 | `hypotenuse` | Hypotenuse | Longest right-triangle side | `sqrt(a^2 + b^2)` | a, b |
| 579 | `euclidean_distance` | Euclidean Distance | Straight-line distance | `sqrt(Sum((x-y)^2))` | point_a, point_b |
| 580 | `manhattan_distance` | Manhattan Distance | Taxicab distance | `Sum(\|x-y\|)` | point_a, point_b |
| 581 | `cosine_similarity` | Cosine Similarity | Vector angle similarity | `A.B / (\|A\|*\|B\|)` | vector_a, vector_b |
| 582 | `minkowski_distance` | Minkowski Distance | Generalized distance | `(Sum(\|x-y\|^p))^(1/p)` | point_a, point_b, p |
| 583 | `chebyshev_distance` | Chebyshev Distance | Max coordinate difference | `max(\|x-y\|)` | point_a, point_b |
| 584 | `mahalanobis_distance` | Mahalanobis Distance | Covariance-scaled distance | `sqrt((x-mu)' Cov^-1 (x-mu))` | point, mean, covariance_matrix |
| 585 | `hamming_distance` | Hamming Distance | Differing positions count | `Count(x != y)` | sequence_a, sequence_b |
| 586 | `dot_product` | Dot Product | Vector inner product | `Sum(a_i * b_i)` | vector_a, vector_b |
| 587 | `cross_product_2d` | Cross Product (2D) | Scalar cross product | `a_x*b_y - a_y*b_x` | vector_a, vector_b |
| 588 | `vector_magnitude` | Vector Magnitude | Euclidean norm | `sqrt(Sum(x^2))` | vector |
| 589 | `vector_normalize` | Vector Normalization | Unit vector | `v / \|v\|` | vector |
| 590 | `matrix_multiply` | Matrix Multiplication | Matrix product | `C_ij = Sum(A_ik * B_kj)` | matrix_a, matrix_b |
| 591 | `matrix_transpose` | Matrix Transpose | Flip rows/columns | `A_ij -> A_ji` | matrix |
| 592 | `matrix_determinant` | Matrix Determinant | Scalar from square matrix | `det(A)` | matrix |
| 593 | `matrix_inverse` | Matrix Inverse | Multiplicative inverse | `A^-1` | matrix |
| 594 | `matrix_trace` | Matrix Trace | Sum of diagonal | `Sum(A_ii)` | matrix |
| 595 | `eigenvalues` | Eigenvalues | Characteristic roots | `Solve det(A-lambda*I)=0` | matrix |
| 596 | `cholesky_decomposition` | Cholesky Decomposition | Lower triangular factor | `A = L*L'` | matrix |
| 597 | `logarithm_natural` | Natural Logarithm | Log base e | `ln(x)` | value |
| 598 | `logarithm_base10` | Log Base 10 | Common logarithm | `log10(x)` | value |
| 599 | `logarithm_base` | Log Arbitrary Base | Log base b | `log(x) / log(b)` | value, base |
| 600 | `exponential` | Exponential | e to the power x | `e^x` | value |
| 601 | `power_function` | Power Function | Base to exponent | `base^exponent` | base, exponent |
| 602 | `nth_root` | Nth Root | Root of degree n | `x^(1/n)` | value, n |
| 603 | `factorial` | Factorial | Product 1 to n | `n!` | n |
| 604 | `combination` | Combination (nCr) | Ways to choose r from n | `n! / (r!(n-r)!)` | n, r |
| 605 | `permutation` | Permutation (nPr) | Ordered arrangements | `n! / (n-r)!` | n, r |
| 606 | `absolute_value` | Absolute Value | Magnitude without sign | `\|x\|` | value |
| 607 | `percentage_change` | Percentage Change | Relative change % | `(New - Old)/Old * 100` | old_value, new_value |
| 608 | `percentage_of_total` | Percentage of Total | Part over whole | `Part / Total * 100` | part, total |
| 609 | `compound_growth` | Compound Growth | Multi-period growth | `Initial*(1+r)^n` | initial, rate, periods |
| 610 | `cagr` | CAGR | Compound annual growth rate | `(End/Start)^(1/years) - 1` | start_value, end_value, years |

### 5.13 Growth, Segment, Forensic & Modern Metrics  ·  `growth_segment_forensic.py`  ·  50 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 611 | `yoy_change_absolute` | YoY Change (Absolute) | Dollar change year over year | `Current - Prior` | current, prior |
| 612 | `yoy_change_pct` | YoY Change (%) | Percent change year over year | `(Current - Prior) / Prior * 100` | current, prior |
| 613 | `sequential_growth` | Sequential (QoQ) Growth % | Quarter over quarter change | `(Current_Q - Prior_Q) / Prior_Q * 100` | current_q, prior_q |
| 614 | `ttm` | Trailing Twelve Months | Sum of last four quarters | `Q1 + Q2 + Q3 + Q4` | q1, q2, q3, q4 |
| 615 | `ttm_rolling` | TTM Rolling Update | New TTM = old TTM - oldest Q + newest Q | `Prior_TTM - Dropped_Q + New_Q` | prior_ttm, dropped_q, new_q |
| 616 | `quarter_annualized` | Quarterly Annualized Run-Rate | Quarter times four | `Quarter_Value * 4` | quarter_value |
| 617 | `monthly_annualized` | Monthly Annualized Run-Rate | Month times twelve | `Monthly_Value * 12` | monthly_value |
| 618 | `percentage_point_change` | Percentage Point Change | Difference of two percentages | `Current_Pct - Prior_Pct` | current_pct, prior_pct |
| 619 | `compound_quarterly` | Compound Sub-Annual Growth | Compounded periodic growth | `(1 + periodic_rate)^periods - 1` | periodic_rate, periods |
| 620 | `constant_currency_growth` | Constant Currency Growth % | FX-neutral growth | `(Current_CC - Prior) / Prior * 100` | current_cc, prior |
| 621 | `organic_growth` | Organic Growth % | Growth excluding M&A and FX | `(Reported_Growth - MA_Contribution - FX_Contribution)` | reported_growth, ma_contribution, fx_contribution |
| 622 | `inorganic_growth` | Inorganic Growth % | Growth from acquisitions | `MA_Revenue / Prior_Revenue * 100` | ma_revenue, prior_revenue |
| 623 | `two_year_stack` | Two-Year Stacked Growth % | Sum of consecutive YoY rates | `Growth_Y1 + Growth_Y2` | growth_y1, growth_y2 |
| 624 | `multi_year_cagr` | Multi-Year CAGR | Compound growth over n years | `(End/Start)^(1/years) - 1` | start, end, years |
| 625 | `multi_year_average` | Multi-Year Average | Mean across periods | `Sum(values) / count` | values |
| 626 | `dividend_growth_rate` | Dividend Growth Rate (CAGR) | Compound dividend growth | `(D_end/D_start)^(1/years) - 1` | d_start, d_end, years |
| 627 | `revenue_run_rate` | Revenue Run-Rate | Annualized current revenue | `Current_Period_Revenue * Periods_Per_Year` | current_period_revenue, periods_per_year |
| 628 | `segment_growth` | Segment Revenue Growth % | Per-segment YoY growth | `(Seg_Current - Seg_Prior) / Seg_Prior * 100` | seg_current, seg_prior |
| 629 | `segment_margin` | Segment Operating Margin % | Segment profit over segment revenue | `Segment_Operating_Income / Segment_Revenue * 100` | segment_operating_income, segment_revenue |
| 630 | `segment_revenue_share` | Segment Revenue Share % | Segment as % of total | `Segment_Revenue / Total_Revenue * 100` | segment_revenue, total_revenue |
| 631 | `segment_contribution` | Segment Profit Contribution % | Segment profit / total profit | `Segment_Profit / Total_Profit * 100` | segment_profit, total_profit |
| 632 | `mix_shift` | Revenue Mix Shift (pp) | Change in segment share | `Current_Share_Pct - Prior_Share_Pct` | current_share_pct, prior_share_pct |
| 633 | `geographic_concentration` | Geographic Concentration % | Region revenue / total | `Region_Revenue / Total_Revenue * 100` | region_revenue, total_revenue |
| 634 | `customer_concentration` | Customer Concentration % | Top customer revenue / total | `Top_Customer_Revenue / Total_Revenue * 100` | top_customer_revenue, total_revenue |
| 635 | `herfindahl_index` | Herfindahl Concentration Index | Sum of squared shares | `Sum(Share_i^2)` | shares |
| 636 | `weighted_segment_growth` | Weighted Segment Growth % | Share-weighted segment growth | `Sum(Share_i * Growth_i)` | shares, growths |
| 637 | `beneish_m_score` | Beneish M-Score | Earnings manipulation detector | `-4.84 + weighted 8 indices` | dsri, gmi, aqi, sgi, depi, sgai, lvgi, tata |
| 638 | `sloan_ratio` | Sloan Accrual Ratio % | Accruals / total assets | `(NI - CFO - CFI) / Total_Assets * 100` | net_income, cfo, cfi, total_assets |
| 639 | `accruals_ratio_bs` | Balance Sheet Accruals Ratio | Change in NOA / avg NOA | `(NOA_end - NOA_start) / Avg_NOA` | noa_end, noa_start |
| 640 | `accruals_ratio_cf` | Cash Flow Accruals Ratio | (NI - CFO - CFI)/avg NOA | `(NI - CFO - CFI) / Avg_NOA` | net_income, cfo, cfi, avg_noa |
| 641 | `cash_conversion` | Cash Conversion Ratio | Operating cash flow / net income | `CFO / Net_Income` | cfo, net_income |
| 642 | `fcf_conversion` | FCF Conversion % | FCF / net income | `FCF / Net_Income * 100` | fcf, net_income |
| 643 | `earnings_quality_ratio` | Earnings Quality Ratio | CFO / net income | `CFO / Net_Income` | cfo, net_income |
| 644 | `adjusted_ebitda` | Adjusted EBITDA | EBITDA plus one-time addbacks | `EBITDA + Addbacks` | ebitda, addbacks |
| 645 | `normalized_earnings` | Normalized Earnings | Net income excluding one-timers | `Net_Income - One_Time_Items` | net_income, one_time_items |
| 646 | `days_cash_on_hand` | Days Cash on Hand | Cash / daily operating expense | `Cash / (Operating_Expenses / 365)` | cash, operating_expenses |
| 647 | `net_working_capital_change` | Change in Net Working Capital | Period-over-period NWC change | `NWC_Current - NWC_Prior` | nwc_current, nwc_prior |
| 648 | `capex_to_depreciation` | CapEx to Depreciation | Reinvestment signal | `CapEx / Depreciation` | capex, depreciation |
| 649 | `maintenance_capex_estimate` | Maintenance CapEx (Est.) | Depreciation as maintenance proxy | `Depreciation` | depreciation |
| 650 | `growth_capex` | Growth CapEx | CapEx above maintenance | `CapEx - Maintenance_CapEx` | capex, maintenance_capex |
| 651 | `incremental_roic` | Incremental ROIC % | Change in NOPAT / change in capital | `Delta_NOPAT / Delta_Invested_Capital * 100` | delta_nopat, delta_invested_capital |
| 652 | `cfroi` | Cash Flow Return on Investment % | Gross cash flow / gross investment | `Gross_Cash_Flow / Gross_Investment * 100` | gross_cash_flow, gross_investment |
| 653 | `buyback_yield` | Buyback Yield % | Net buybacks / market cap | `Net_Buybacks / Market_Cap * 100` | net_buybacks, market_cap |
| 654 | `total_payout_ratio` | Total Payout Ratio % | Dividends plus buybacks / NI | `(Dividends + Buybacks) / Net_Income * 100` | dividends, buybacks, net_income |
| 655 | `total_yield` | Total Shareholder Yield % | Dividend yield plus buyback yield | `Dividend_Yield + Buyback_Yield` | dividend_yield, buyback_yield |
| 656 | `effective_interest_rate` | Effective Interest Rate % | Interest expense / avg debt | `Interest_Expense / Average_Debt * 100` | interest_expense, average_debt |
| 657 | `weighted_avg_cost_debt` | Weighted Avg Cost of Debt % | Sum of weighted debt rates | `Sum(Weight_i * Rate_i)` | weights, rates |
| 658 | `arpu` | Average Revenue Per User | Revenue / users | `Revenue / Users` | revenue, users |
| 659 | `net_revenue_retention` | Net Revenue Retention % | Expansion-adjusted retention | `(Start + Expansion - Churn - Contraction) / Start * 100` | starting_revenue, expansion, churn, contraction |
| 660 | `ltv_cac_ratio` | LTV/CAC Ratio | Lifetime value over acquisition cost | `LTV / CAC` | ltv, cac |

### 5.14 AI / Machine Learning Metrics & Functions  ·  `ai_ml.py`  ·  93 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 661 | `mse_loss` | Mean Squared Error Loss | Average squared prediction error | `Mean((y - yhat)^2)` | y_true, y_pred |
| 662 | `mae_loss` | Mean Absolute Error Loss | Average absolute prediction error | `Mean(\|y - yhat\|)` | y_true, y_pred |
| 663 | `rmse_loss` | Root Mean Squared Error Loss | Root of MSE | `sqrt(Mean((y - yhat)^2))` | y_true, y_pred |
| 664 | `huber_loss` | Huber Loss | MSE/MAE hybrid robust to outliers | `0.5*e^2 if \|e\|<=d else d*(\|e\|-0.5d)` | y_true, y_pred, delta |
| 665 | `cross_entropy_loss` | Cross-Entropy Loss | Multi-class log loss | `-Sum(y*log(yhat))` | y_true, y_pred |
| 666 | `binary_cross_entropy` | Binary Cross-Entropy | Two-class log loss | `-Mean(y*log(p)+(1-y)*log(1-p))` | y_true, y_pred |
| 667 | `categorical_cross_entropy` | Categorical Cross-Entropy | One-hot multi-class loss | `-Sum(y_i*log(p_i))` | y_true, y_pred |
| 668 | `hinge_loss` | Hinge Loss | SVM margin loss | `Mean(max(0, 1 - y*yhat))` | y_true, y_pred |
| 669 | `kl_divergence` | KL Divergence | Distribution difference | `Sum(p*log(p/q))` | p_dist, q_dist |
| 670 | `focal_loss` | Focal Loss | Class-imbalance weighted CE | `-alpha*(1-p)^gamma*log(p)` | y_true, y_pred, alpha, gamma |
| 671 | `log_loss` | Log Loss | Logarithmic probability loss | `-Mean(y*log(p)+(1-y)*log(1-p))` | y_true, y_pred |
| 672 | `msle_loss` | Mean Squared Log Error | Log-scaled squared error | `Mean((log(1+y)-log(1+yhat))^2)` | y_true, y_pred |
| 673 | `sigmoid` | Sigmoid | Logistic squashing 0-1 | `1 / (1 + e^-x)` | x |
| 674 | `relu` | ReLU | Rectified linear unit | `max(0, x)` | x |
| 675 | `leaky_relu` | Leaky ReLU | ReLU with small negative slope | `x if x>0 else alpha*x` | x, alpha |
| 676 | `tanh_activation` | Tanh | Hyperbolic tangent -1 to 1 | `(e^x - e^-x)/(e^x + e^-x)` | x |
| 677 | `softmax` | Softmax | Normalized exponential probabilities | `e^xi / Sum(e^xj)` | x_vector |
| 678 | `gelu` | GELU | Gaussian error linear unit | `x * Phi(x)` | x |
| 679 | `elu` | ELU | Exponential linear unit | `x if x>0 else alpha*(e^x - 1)` | x, alpha |
| 680 | `swish` | Swish | Self-gated activation | `x * sigmoid(x)` | x |
| 681 | `softplus` | Softplus | Smooth ReLU | `log(1 + e^x)` | x |
| 682 | `accuracy` | Accuracy | Correct / total predictions | `(TP + TN) / (TP+TN+FP+FN)` | tp, tn, fp, fn |
| 683 | `precision` | Precision | True positives / predicted positives | `TP / (TP + FP)` | tp, fp |
| 684 | `recall` | Recall (Sensitivity) | True positives / actual positives | `TP / (TP + FN)` | tp, fn |
| 685 | `f1_score` | F1 Score | Harmonic mean precision-recall | `2*P*R / (P + R)` | precision, recall |
| 686 | `f_beta_score` | F-Beta Score | Weighted precision-recall mean | `(1+b^2)*P*R / (b^2*P + R)` | precision, recall, beta |
| 687 | `specificity` | Specificity | True negatives / actual negatives | `TN / (TN + FP)` | tn, fp |
| 688 | `roc_auc` | ROC AUC | Area under ROC curve | `Integral of TPR over FPR` | y_true, y_scores |
| 689 | `pr_auc` | PR AUC | Area under precision-recall curve | `Integral of precision over recall` | y_true, y_scores |
| 690 | `matthews_corr` | Matthews Correlation Coefficient | Balanced binary quality | `(TP*TN-FP*FN)/sqrt(...)` | tp, tn, fp, fn |
| 691 | `cohen_kappa` | Cohen's Kappa | Agreement beyond chance | `(po - pe) / (1 - pe)` | observed_agreement, expected_agreement |
| 692 | `balanced_accuracy` | Balanced Accuracy | Mean of recall per class | `(Sensitivity + Specificity) / 2` | sensitivity, specificity |
| 693 | `false_positive_rate` | False Positive Rate | FP / actual negatives | `FP / (FP + TN)` | fp, tn |
| 694 | `false_negative_rate` | False Negative Rate | FN / actual positives | `FN / (FN + TP)` | fn, tp |
| 695 | `r2_score` | R-Squared Score | Variance explained | `1 - SSres/SStot` | y_true, y_pred |
| 696 | `adjusted_r2_ml` | Adjusted R-Squared | R2 penalized for features | `1 - (1-R2)(n-1)/(n-k-1)` | r2, n, k |
| 697 | `explained_variance` | Explained Variance Score | 1 - Var(residual)/Var(y) | `1 - Var(y-yhat)/Var(y)` | y_true, y_pred |
| 698 | `mape_metric` | MAPE | Mean absolute percent error | `Mean(\|y-yhat\|/y)*100` | y_true, y_pred |
| 699 | `smape` | SMAPE | Symmetric MAPE | `Mean(2\|y-yhat\|/(\|y\|+\|yhat\|))*100` | y_true, y_pred |
| 700 | `median_absolute_error` | Median Absolute Error | Median of absolute errors | `Median(\|y - yhat\|)` | y_true, y_pred |
| 701 | `jaccard_similarity` | Jaccard Similarity | Intersection over union | `\|A and B\| / \|A or B\|` | set_a, set_b |
| 702 | `dice_coefficient` | Dice Coefficient | 2x intersection over sum | `2\|A and B\| / (\|A\|+\|B\|)` | set_a, set_b |
| 703 | `canberra_distance` | Canberra Distance | Weighted Manhattan | `Sum(\|x-y\|/(\|x\|+\|y\|))` | vector_a, vector_b |
| 704 | `braycurtis_distance` | Bray-Curtis Distance | Compositional dissimilarity | `Sum(\|x-y\|)/Sum(\|x+y\|)` | vector_a, vector_b |
| 705 | `haversine_distance` | Haversine Distance | Great-circle distance | `2r*asin(sqrt(hav))` | lat1, lon1, lat2, lon2 |
| 706 | `jaro_winkler` | Jaro-Winkler Similarity | String similarity with prefix | `Jaro + prefix*scale*(1-Jaro)` | string_a, string_b |
| 707 | `silhouette_score` | Silhouette Score | Cluster cohesion vs separation | `(b - a) / max(a, b)` | intra_distance, nearest_cluster_distance |
| 708 | `davies_bouldin` | Davies-Bouldin Index | Avg cluster similarity | `Mean(max((si+sj)/dij))` | cluster_scatters, cluster_distances |
| 709 | `calinski_harabasz` | Calinski-Harabasz Index | Between/within variance ratio | `(BGSS/WGSS)*((n-k)/(k-1))` | between_ss, within_ss, n, k |
| 710 | `inertia` | Inertia (WCSS) | Within-cluster sum of squares | `Sum(\|\|x - centroid\|\|^2)` | points, centroids |
| 711 | `dunn_index` | Dunn Index | Min inter / max intra cluster | `Min_Inter_Cluster / Max_Intra_Cluster` | inter_distances, intra_distances |
| 712 | `rand_index` | Rand Index | Clustering agreement | `(a + b) / C(n,2)` | agreements, n |
| 713 | `adjusted_rand_index` | Adjusted Rand Index | Chance-corrected Rand | `(RI - Expected) / (Max - Expected)` | contingency_table |
| 714 | `normalized_mutual_info` | Normalized Mutual Information | Clustering MI normalized | `MI / sqrt(H(U)*H(V))` | labels_true, labels_pred |
| 715 | `entropy` | Shannon Entropy | Information content | `-Sum(p*log2(p))` | probabilities |
| 716 | `conditional_entropy` | Conditional Entropy | Entropy given another variable | `H(Y) - I(X;Y)` | joint_dist, marginal_dist |
| 717 | `mutual_information` | Mutual Information | Shared information | `Sum(p*log(p/(px*py)))` | joint_dist, marginal_x, marginal_y |
| 718 | `information_gain` | Information Gain | Entropy reduction from split | `H(parent) - Weighted_H(children)` | parent_entropy, child_entropies, weights |
| 719 | `gini_impurity` | Gini Impurity | Node impurity for trees | `1 - Sum(p^2)` | class_probabilities |
| 720 | `gain_ratio` | Gain Ratio | Information gain / split info | `Information_Gain / Split_Info` | information_gain, split_info |
| 721 | `gradient_descent_step` | Gradient Descent Step | Parameter update rule | `theta - lr*gradient` | theta, learning_rate, gradient |
| 722 | `momentum_update` | Momentum Update | Velocity-based update | `beta*v + (1-beta)*gradient` | velocity, gradient, beta |
| 723 | `adam_update` | Adam Optimizer Step | Adaptive moment estimation | `theta - lr*mhat/(sqrt(vhat)+eps)` | theta, m_hat, v_hat, learning_rate, epsilon |
| 724 | `rmsprop_update` | RMSProp Update | Root mean square propagation | `theta - lr*g/sqrt(E[g^2]+eps)` | theta, gradient, mean_sq_grad, learning_rate, epsilon |
| 725 | `learning_rate_decay` | Learning Rate Decay | Exponential LR schedule | `lr0 * decay^epoch` | initial_lr, decay_rate, epoch |
| 726 | `l1_regularization` | L1 Regularization (Lasso) | Absolute weight penalty | `lambda * Sum(\|w\|)` | weights, lambda |
| 727 | `l2_regularization` | L2 Regularization (Ridge) | Squared weight penalty | `lambda * Sum(w^2)` | weights, lambda |
| 728 | `elastic_net_penalty` | Elastic Net Penalty | L1 + L2 combined | `lambda*(alpha*L1 + (1-alpha)*L2)` | weights, lambda, alpha |
| 729 | `tf_idf` | TF-IDF | Term frequency inverse doc freq | `TF * log(N / DF)` | term_freq, num_docs, doc_freq |
| 730 | `cosine_sim_vectors` | Cosine Similarity (Vectors) | Vector angle cosine | `A.B / (\|A\|*\|B\|)` | vector_a, vector_b |
| 731 | `levenshtein_distance` | Levenshtein Distance | Edit distance between strings | `Min edits to transform` | string_a, string_b |
| 732 | `bleu_score` | BLEU Score | Translation quality n-gram | `BP * exp(Sum(wn*log(pn)))` | reference, candidate, max_n |
| 733 | `perplexity` | Perplexity | Language model uncertainty | `2^(-Mean(log2(p)))` | probabilities |
| 734 | `bm25_score` | BM25 Score | Probabilistic relevance ranking | `IDF * (tf*(k+1))/(tf + k*(1-b+b*dl/avgdl))` | term_freq, doc_len, avg_doc_len, idf, k, b |
| 735 | `min_max_scaling` | Min-Max Scaling | Scale feature to [0,1] | `(x - min) / (max - min)` | x, min_val, max_val |
| 736 | `standard_scaling` | Standard Scaling (Z) | Zero-mean unit-variance scaling | `(x - mean) / std` | x, mean, std |
| 737 | `robust_scaling` | Robust Scaling | Median/IQR scaling | `(x - median) / IQR` | x, median, iqr |
| 738 | `pca_explained_variance` | PCA Explained Variance Ratio | Eigenvalue share | `Eigenvalue_i / Sum(Eigenvalues)` | eigenvalue, total_eigenvalue_sum |
| 739 | `sigmoid_derivative` | Sigmoid Derivative | Gradient of sigmoid | `sigmoid(x) * (1 - sigmoid(x))` | x |
| 740 | `dropout_inverted` | Inverted Dropout Scale | Scale activations at train time | `x / (1 - drop_rate)` | x, drop_rate |
| 741 | `batch_normalization` | Batch Normalization | Normalize then scale/shift | `gamma * (x - mean)/sqrt(var+eps) + beta` | x, mean, var, gamma, beta, eps |
| 742 | `layer_normalization` | Layer Normalization | Per-sample feature normalization | `gamma * (x - mean)/sqrt(var+eps) + beta` | x, mean, var, gamma, beta, eps |
| 743 | `cosine_annealing` | Cosine Annealing LR | Cosine learning-rate schedule | `lr_min + 0.5*(lr_max-lr_min)*(1+cos(pi*t/T))` | lr_min, lr_max, t, total_steps |
| 744 | `attention_score` | Scaled Dot-Product Attention | Softmax(QK'/sqrt(d))V weight | `softmax(QK^T / sqrt(d_k))` | query_key_dot, d_k |
| 745 | `nadam_update` | NAdam Update Step | Nesterov-accelerated Adam | `theta - lr*mhat/(sqrt(vhat)+eps)` | theta, lr, mhat, vhat, eps |
| 746 | `adagrad_update` | AdaGrad Update Step | Per-parameter adaptive LR | `theta - lr*g/(sqrt(G)+eps)` | theta, lr, gradient, accumulated_sq, eps |
| 747 | `weight_init_xavier` | Xavier Init Variance | Glorot initialization variance | `2 / (fan_in + fan_out)` | fan_in, fan_out |
| 748 | `weight_init_he` | He Init Variance | He initialization variance | `2 / fan_in` | fan_in |
| 749 | `top_k_accuracy` | Top-K Accuracy | Correct if true label in top k | `Correct_in_TopK / Total` | correct_in_topk, total |
| 750 | `ndcg` | NDCG | Normalized discounted cumulative gain | `DCG / IDCG` | dcg, idcg |
| 751 | `map_at_k` | Mean Average Precision @K | Mean of average precisions | `Mean(AP@k per query)` | average_precisions |
| 752 | `hamming_loss` | Hamming Loss | Multi-label misclassification rate | `Wrong_Labels / Total_Labels` | wrong_labels, total_labels |
| 753 | `wasserstein_distance_1d` | Wasserstein Distance (1D) | Earth movers distance | `Sum(\|CDF1 - CDF2\|)` | cdf1, cdf2 |

### 5.15 Probability Theory & Distributions  ·  `probability.py`  ·  55 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 754 | `normal_pdf` | Normal PDF | Gaussian density | `1/(sig*sqrt(2pi))*e^(-(x-mu)^2/(2sig^2))` | x, mean, std |
| 755 | `normal_cdf` | Normal CDF | Cumulative Gaussian | `0.5*(1 + erf((x-mu)/(sig*sqrt(2))))` | x, mean, std |
| 756 | `standard_normal_pdf` | Standard Normal PDF | Z-distribution density | `1/sqrt(2pi)*e^(-z^2/2)` | z |
| 757 | `binomial_pmf` | Binomial PMF | k successes in n trials | `C(n,k)*p^k*(1-p)^(n-k)` | k, n, p |
| 758 | `poisson_pmf` | Poisson PMF | Rare event count | `lambda^k * e^-lambda / k!` | k, lambda |
| 759 | `exponential_pdf` | Exponential PDF | Time between events | `lambda*e^(-lambda*x)` | x, lambda |
| 760 | `uniform_pdf` | Uniform PDF | Equal density over range | `1/(b-a)` | a, b |
| 761 | `bernoulli_pmf` | Bernoulli PMF | Single trial success | `p^k*(1-p)^(1-k)` | k, p |
| 762 | `geometric_pmf` | Geometric PMF | Trials until first success | `(1-p)^(k-1)*p` | k, p |
| 763 | `negative_binomial_pmf` | Negative Binomial PMF | Failures before r successes | `C(k+r-1,k)*p^r*(1-p)^k` | k, r, p |
| 764 | `beta_pdf` | Beta PDF | Bounded continuous density | `x^(a-1)*(1-x)^(b-1)/B(a,b)` | x, alpha, beta |
| 765 | `gamma_pdf` | Gamma PDF | Waiting time density | `x^(a-1)*e^(-x/b)/(b^a*Gamma(a))` | x, shape, scale |
| 766 | `lognormal_pdf` | Log-Normal PDF | Log-Gaussian density | `1/(x*s*sqrt(2pi))*e^(-(ln x-mu)^2/(2s^2))` | x, mu, sigma |
| 767 | `student_t_pdf` | Student's t PDF | Heavy-tail density | `Gamma((v+1)/2)/... t-density` | t, degrees_freedom |
| 768 | `chi2_pdf` | Chi-Square PDF | Sum of squared normals density | `x^(k/2-1)*e^(-x/2)/(2^(k/2)*Gamma(k/2))` | x, degrees_freedom |
| 769 | `f_distribution_pdf` | F-Distribution PDF | Variance ratio density | `F-density formula` | x, df1, df2 |
| 770 | `weibull_pdf` | Weibull PDF | Reliability/failure density | `(k/l)*(x/l)^(k-1)*e^(-(x/l)^k)` | x, shape, scale |
| 771 | `conditional_probability` | Conditional Probability | P(A given B) | `P(A and B) / P(B)` | p_a_and_b, p_b |
| 772 | `bayes_theorem` | Bayes' Theorem | Posterior probability | `P(B\|A)*P(A) / P(B)` | p_b_given_a, p_a, p_b |
| 773 | `joint_probability_independent` | Joint Probability (Independent) | P(A and B) when independent | `P(A) * P(B)` | p_a, p_b |
| 774 | `union_probability` | Union Probability | P(A or B) | `P(A) + P(B) - P(A and B)` | p_a, p_b, p_a_and_b |
| 775 | `complement_probability` | Complement Probability | P(not A) | `1 - P(A)` | p_a |
| 776 | `total_probability` | Total Probability | Marginalize over partition | `Sum(P(A\|Bi)*P(Bi))` | conditionals, priors |
| 777 | `odds_from_probability` | Odds from Probability | Convert probability to odds | `p / (1 - p)` | probability |
| 778 | `probability_from_odds` | Probability from Odds | Convert odds to probability | `odds / (1 + odds)` | odds |
| 779 | `permutations_count` | Permutations Count | Ordered arrangements | `n! / (n-r)!` | n, r |
| 780 | `combinations_count` | Combinations Count | Unordered selections | `n! / (r!(n-r)!)` | n, r |
| 781 | `multinomial_coefficient` | Multinomial Coefficient | Multi-group arrangements | `n! / (n1!*n2!*...*nk!)` | n, group_sizes |
| 782 | `permutations_with_repetition` | Permutations with Repetition | Arrangements with repeats | `n^r` | n, r |
| 783 | `circular_permutations` | Circular Permutations | Round-table arrangements | `(n-1)!` | n |
| 784 | `expected_value_discrete` | Expected Value (Discrete) | Probability-weighted mean | `Sum(x_i * p_i)` | values, probabilities |
| 785 | `variance_discrete` | Variance (Discrete) | Expected squared deviation | `Sum(p*(x-mu)^2)` | values, probabilities |
| 786 | `covariance_random_vars` | Covariance (Random Vars) | Joint expectation deviation | `E[XY] - E[X]E[Y]` | joint_values, probabilities |
| 787 | `correlation_random_vars` | Correlation (Random Vars) | Normalized covariance | `Cov(X,Y)/(sigX*sigY)` | covariance, std_x, std_y |
| 788 | `moment_generating` | Moment (n-th) | n-th raw moment | `E[X^n]` | values, probabilities, n |
| 789 | `variance_sum_independent` | Variance of Sum (Independent) | Sum of variances | `Var(X) + Var(Y)` | var_x, var_y |
| 790 | `markov_steady_state` | Markov Steady State | Stationary distribution | `pi = pi*P` | transition_matrix |
| 791 | `poisson_process_prob` | Poisson Process Probability | Events in interval | `(lambda*t)^k*e^(-lambda*t)/k!` | rate, time, k |
| 792 | `geometric_brownian_motion` | Geometric Brownian Motion | Stock price diffusion | `S0*e^((mu-sig^2/2)t + sig*W)` | s0, mu, sigma, time, wiener |
| 793 | `random_walk_position` | Random Walk Position | Cumulative step position | `Sum(steps)` | steps |
| 794 | `chebyshev_inequality` | Chebyshev Inequality | Bound on tail probability | `1 / k^2` | k |
| 795 | `markov_inequality` | Markov Inequality | Bound P(X>=a) | `Mean / a` | mean, a |
| 796 | `central_limit_theorem` | CLT Sampling Std | Std of sample mean | `sigma / sqrt(n)` | sigma, n |
| 797 | `bayesian_posterior` | Bayesian Posterior | Posterior via Bayes rule | `(Likelihood*Prior) / Evidence` | likelihood, prior, evidence |
| 798 | `law_large_numbers_error` | LLN Convergence Error | Sample mean deviation bound | `sigma / sqrt(n)` | sigma, n |
| 799 | `hypergeometric_pmf` | Hypergeometric PMF | Draws without replacement | `C(K,k)C(N-K,n-k)/C(N,n)` | population, successes, draws, observed |
| 800 | `multinomial_pmf` | Multinomial PMF | Multi-category probability | `n!/Prod(xi!) * Prod(pi^xi)` | n, counts, probabilities |
| 801 | `cauchy_pdf` | Cauchy PDF | Heavy-tailed density | `1/(pi*gamma*(1+((x-x0)/gamma)^2))` | x, location, scale |
| 802 | `pareto_pdf` | Pareto PDF | Power-law density | `alpha*xm^alpha / x^(alpha+1)` | x, scale_min, alpha |
| 803 | `survival_function` | Survival Function | Probability of exceeding t | `1 - CDF(t)` | cdf |
| 804 | `hazard_rate` | Hazard Rate | Instantaneous failure rate | `pdf(t) / Survival(t)` | pdf, survival |
| 805 | `entropy_shannon` | Shannon Entropy | Information content of distribution | `-Sum(p * log2(p))` | probabilities |
| 806 | `cross_entropy_dist` | Cross Entropy (Distributions) | Between true and predicted | `-Sum(p * log(q))` | p_true, q_pred |
| 807 | `conditional_variance` | Conditional Variance | Var of X given Y | `E[X^2\|Y] - E[X\|Y]^2` | e_x2_given_y, e_x_given_y |
| 808 | `expected_shortfall_prob` | Tail Expectation | Expected value beyond threshold | `E[X \| X > threshold]` | tail_values |

### 5.16 Advanced Statistics & Hypothesis Testing  ·  `statistics_advanced.py`  ·  53 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 809 | `t_test_one_sample` | One-Sample t-Test | Mean vs hypothesized value | `(xbar - mu) / (s/sqrt(n))` | sample_mean, pop_mean, std, n |
| 810 | `t_test_two_sample` | Two-Sample t-Test | Compare two means | `(x1-x2)/sqrt(s1^2/n1 + s2^2/n2)` | mean1, mean2, std1, std2, n1, n2 |
| 811 | `paired_t_test` | Paired t-Test | Compare paired observations | `dbar / (sd/sqrt(n))` | mean_diff, std_diff, n |
| 812 | `welch_t_test` | Welch's t-Test | Unequal-variance t-test | `(x1-x2)/sqrt(s1^2/n1 + s2^2/n2)` | mean1, mean2, var1, var2, n1, n2 |
| 813 | `z_test_proportion` | Z-Test for Proportion | Sample proportion test | `(phat - p0)/sqrt(p0(1-p0)/n)` | sample_prop, pop_prop, n |
| 814 | `z_test_mean` | Z-Test for Mean | Known-variance mean test | `(xbar - mu)/(sigma/sqrt(n))` | sample_mean, pop_mean, sigma, n |
| 815 | `anova_f_statistic` | ANOVA F-Statistic | Between vs within variance | `MSB / MSW` | between_group_var, within_group_var |
| 816 | `chi2_independence` | Chi-Square Independence | Test variable association | `Sum((O-E)^2/E)` | observed, expected |
| 817 | `chi2_goodness_of_fit` | Chi-Square Goodness of Fit | Observed vs expected | `Sum((O-E)^2/E)` | observed, expected |
| 818 | `mann_whitney_u` | Mann-Whitney U | Nonparametric rank test | `U = R1 - n1(n1+1)/2` | ranks, n1, n2 |
| 819 | `wilcoxon_signed_rank` | Wilcoxon Signed-Rank | Paired nonparametric test | `Sum of signed ranks` | differences |
| 820 | `kruskal_wallis_h` | Kruskal-Wallis H | Multi-group nonparametric | `12/(N(N+1))*Sum(Ri^2/ni) - 3(N+1)` | rank_sums, group_sizes, n_total |
| 821 | `levene_test` | Levene's Test | Equality of variances | `F-stat on abs deviations` | groups |
| 822 | `f_test_variance` | F-Test for Variances | Ratio of two variances | `s1^2 / s2^2` | variance1, variance2 |
| 823 | `cohens_d` | Cohen's d | Standardized mean difference | `(mean1 - mean2) / pooled_std` | mean1, mean2, pooled_std |
| 824 | `hedges_g` | Hedges' g | Bias-corrected Cohen's d | `Cohens_d * (1 - 3/(4df-1))` | cohens_d, degrees_freedom |
| 825 | `eta_squared` | Eta Squared | ANOVA effect size | `SS_between / SS_total` | ss_between, ss_total |
| 826 | `odds_ratio` | Odds Ratio | Exposure-outcome association | `(a*d) / (b*c)` | a, b, c, d |
| 827 | `relative_risk` | Relative Risk | Risk ratio between groups | `(a/(a+b)) / (c/(c+d))` | a, b, c, d |
| 828 | `confidence_interval_mean` | CI for Mean | Mean confidence bounds | `xbar +/- t*(s/sqrt(n))` | mean, std, n, confidence |
| 829 | `confidence_interval_proportion` | CI for Proportion | Proportion confidence bounds | `phat +/- z*sqrt(phat(1-phat)/n)` | proportion, n, confidence |
| 830 | `margin_of_error` | Margin of Error | Half-width of CI | `z * (std / sqrt(n))` | z_score, std, n |
| 831 | `prediction_interval` | Prediction Interval | Future observation bounds | `yhat +/- t*s*sqrt(1+1/n+...)` | prediction, std_error, n, confidence |
| 832 | `p_value_from_z` | P-Value from Z | Tail probability from z | `2*(1 - Phi(\|z\|))` | z_score |
| 833 | `logistic_regression_prob` | Logistic Regression Probability | Sigmoid of linear combo | `1/(1+e^-(b0+b1*x))` | intercept, coefficient, x |
| 834 | `multiple_regression_predict` | Multiple Regression Prediction | Linear combination of features | `b0 + Sum(bi*xi)` | intercept, coefficients, features |
| 835 | `ridge_penalty_cost` | Ridge Regression Cost | SSE plus L2 penalty | `SSE + lambda*Sum(b^2)` | sse, coefficients, lambda |
| 836 | `vif` | Variance Inflation Factor | Multicollinearity measure | `1 / (1 - R2_i)` | r_squared_i |
| 837 | `partial_correlation` | Partial Correlation | Correlation controlling for Z | `(rxy - rxz*ryz)/sqrt(...)` | rxy, rxz, ryz |
| 838 | `durbin_watson_test` | Durbin-Watson | Residual autocorrelation | `Sum((e_t - e_t-1)^2)/Sum(e_t^2)` | residuals |
| 839 | `standardized_residual` | Standardized Residual | Residual / std error | `residual / std_error` | residual, std_error |
| 840 | `leverage_hat` | Leverage (Hat Value) | Observation influence | `Diagonal of hat matrix` | x_matrix, observation |
| 841 | `cooks_distance` | Cook's Distance | Influence of observation | `(e^2/(p*MSE))*(h/(1-h)^2)` | residual, leverage, p, mse |
| 842 | `sample_size_mean` | Sample Size for Mean | n for desired margin | `(z*sigma/E)^2` | z_score, std, margin_error |
| 843 | `sample_size_proportion` | Sample Size for Proportion | n for proportion estimate | `z^2*p(1-p)/E^2` | z_score, proportion, margin_error |
| 844 | `standard_error_proportion` | Standard Error of Proportion | Proportion sampling error | `sqrt(p(1-p)/n)` | proportion, n |
| 845 | `finite_population_correction` | Finite Population Correction | FPC factor | `sqrt((N-n)/(N-1))` | population, sample |
| 846 | `bootstrap_std_error` | Bootstrap Standard Error | Resampling-based SE | `Std of bootstrap statistics` | bootstrap_estimates |
| 847 | `pooled_variance` | Pooled Variance | Combined sample variance | `((n1-1)s1^2+(n2-1)s2^2)/(n1+n2-2)` | var1, var2, n1, n2 |
| 848 | `spearman_rank` | Spearman Rank Correlation | Monotonic correlation | `1 - 6*Sum(d^2)/(n(n^2-1))` | rank_diffs, n |
| 849 | `kendall_tau_b` | Kendall Tau-b | Ordinal association with ties | `(C - D)/sqrt((C+D+T)(C+D+U))` | concordant, discordant, ties_x, ties_y |
| 850 | `point_biserial` | Point-Biserial Correlation | Binary vs continuous correlation | `(M1-M0)/Std * sqrt(p*q)` | mean1, mean0, std, p, q |
| 851 | `shapiro_wilk_stat` | Shapiro-Wilk Statistic | Normality test W | `(Sum(a_i*x_i))^2 / Sum((x-xbar)^2)` | ordered_values, coefficients |
| 852 | `kolmogorov_smirnov` | Kolmogorov-Smirnov D | Max CDF deviation | `max\|F_empirical - F_theoretical\|` | empirical_cdf, theoretical_cdf |
| 853 | `jarque_bera` | Jarque-Bera Statistic | Normality from skew/kurtosis | `n/6*(S^2 + (K-3)^2/4)` | n, skewness, kurtosis |
| 854 | `bonferroni_correction` | Bonferroni Alpha | Adjusted significance level | `alpha / m` | alpha, num_tests |
| 855 | `benjamini_hochberg` | Benjamini-Hochberg Threshold | FDR adjusted critical value | `(i/m) * alpha` | rank, num_tests, alpha |
| 856 | `tukey_hsd` | Tukey HSD Critical Diff | Honest significant difference | `q * sqrt(MSE/n)` | q_critical, mse, n |
| 857 | `power_analysis` | Statistical Power | 1 minus beta | `1 - Beta` | beta |
| 858 | `kaplan_meier` | Kaplan-Meier Survival | Product-limit survival estimate | `Prod((n_i - d_i)/n_i)` | at_risk, events |
| 859 | `gini_coefficient_stat` | Gini Coefficient | Inequality measure 0-1 | `Sum of Lorenz deviations` | values |
| 860 | `theil_index` | Theil Index | Entropy-based inequality | `Mean((x/xbar)*ln(x/xbar))` | values |
| 861 | `cohens_kappa_stat` | Cohen's Kappa | Inter-rater agreement | `(Po - Pe)/(1 - Pe)` | observed_agreement, expected_agreement |

### 5.17 Business Analyst KPIs, Forecasting & Decision  ·  `business_analyst.py`  ·  49 formulas

| # | ID | Name | Description | Formula | Inputs |
|---|----|------|-------------|---------|--------|
| 862 | `conversion_rate` | Conversion Rate % | Conversions / total visitors | `Conversions / Visitors * 100` | conversions, visitors |
| 863 | `retention_rate` | Retention Rate % | Retained / starting customers | `(End - New) / Start * 100` | start_customers, end_customers, new_customers |
| 864 | `churn_rate` | Churn Rate % | Lost / starting customers | `Lost_Customers / Start_Customers * 100` | lost_customers, start_customers |
| 865 | `customer_lifetime_value` | Customer Lifetime Value | Total value per customer | `ARPU * Gross_Margin / Churn_Rate` | arpu, gross_margin, churn_rate |
| 866 | `cac` | Customer Acquisition Cost | Sales+marketing / new customers | `Total_Sales_Marketing / New_Customers` | sales_marketing_cost, new_customers |
| 867 | `cac_payback_period` | CAC Payback Period (months) | Months to recover CAC | `CAC / (ARPU * Gross_Margin)` | cac, arpu, gross_margin |
| 868 | `net_promoter_score` | Net Promoter Score | Promoters minus detractors % | `(Promoters - Detractors) / Total * 100` | promoters, detractors, total |
| 869 | `market_share` | Market Share % | Company sales / market sales | `Company_Sales / Market_Sales * 100` | company_sales, market_sales |
| 870 | `wallet_share` | Share of Wallet % | Our spend / total customer spend | `Customer_Spend_With_Us / Total_Customer_Spend * 100` | spend_with_us, total_spend |
| 871 | `funnel_conversion` | Funnel Conversion % | Stage-to-stage conversion | `Stage_N / Stage_1 * 100` | stage_n, stage_1 |
| 872 | `active_user_ratio` | Active User Ratio (DAU/MAU) | Stickiness measure | `DAU / MAU` | dau, mau |
| 873 | `engagement_rate` | Engagement Rate % | Engaged / total users | `Engaged_Users / Total_Users * 100` | engaged_users, total_users |
| 874 | `bounce_rate` | Bounce Rate % | Single-page sessions / total | `Single_Page_Sessions / Total_Sessions * 100` | single_page_sessions, total_sessions |
| 875 | `cohort_retention` | Cohort Retention % | Active cohort / original cohort | `Active_In_Period / Original_Cohort * 100` | active_in_period, original_cohort |
| 876 | `linear_forecast` | Linear Forecast | Trend-line projection | `intercept + slope * period` | intercept, slope, period |
| 877 | `seasonal_index` | Seasonal Index | Seasonal adjustment factor | `Period_Average / Overall_Average` | period_average, overall_average |
| 878 | `weighted_moving_forecast` | Weighted Moving Forecast | Weighted recent values | `Sum(weight*value) / Sum(weights)` | values, weights |
| 879 | `forecast_bias` | Forecast Bias | Average forecast error | `Sum(Actual - Forecast) / n` | actuals, forecasts |
| 880 | `tracking_signal` | Tracking Signal | Cumulative bias / MAD | `Cumulative_Error / MAD` | cumulative_error, mad |
| 881 | `mean_absolute_deviation` | Mean Absolute Deviation | Average absolute forecast error | `Mean(\|Actual - Forecast\|)` | actuals, forecasts |
| 882 | `exponential_smoothing_forecast` | Exponential Smoothing Forecast | Weighted recency forecast | `alpha*actual + (1-alpha)*prev_forecast` | actual, prev_forecast, alpha |
| 883 | `expected_monetary_value` | Expected Monetary Value | Probability-weighted payoff | `Sum(Probability * Payoff)` | probabilities, payoffs |
| 884 | `value_of_information` | Expected Value of Information | Value of perfect info | `EV_With_Info - EV_Without_Info` | ev_with_info, ev_without_info |
| 885 | `decision_tree_value` | Decision Tree Node Value | Best expected branch value | `Max(branch EMVs)` | branch_values |
| 886 | `regret_value` | Maximum Regret | Opportunity loss measure | `Max(Best_Payoff - Chosen_Payoff)` | payoff_matrix, chosen |
| 887 | `sensitivity_elasticity` | Sensitivity Elasticity | % output change / % input change | `Pct_Change_Output / Pct_Change_Input` | pct_change_output, pct_change_input |
| 888 | `breakeven_units_ba` | Breakeven Units | Fixed costs / unit margin | `Fixed_Costs / (Price - Variable_Cost)` | fixed_costs, price, variable_cost |
| 889 | `roi_business` | Return on Investment % | Net gain / cost | `(Gain - Cost) / Cost * 100` | gain, cost |
| 890 | `tam_sam_som` | TAM/SAM/SOM | Serviceable obtainable market | `TAM * SAM_Pct * SOM_Pct` | tam, sam_pct, som_pct |
| 891 | `price_elasticity_demand` | Price Elasticity of Demand | % qty change / % price change | `Pct_Change_Qty / Pct_Change_Price` | pct_change_qty, pct_change_price |
| 892 | `cross_price_elasticity` | Cross-Price Elasticity | Demand sensitivity to other price | `Pct_Change_Qty_A / Pct_Change_Price_B` | pct_change_qty_a, pct_change_price_b |
| 893 | `income_elasticity` | Income Elasticity | Demand sensitivity to income | `Pct_Change_Qty / Pct_Change_Income` | pct_change_qty, pct_change_income |
| 894 | `economic_order_quantity` | Economic Order Quantity | Optimal order size | `sqrt(2*D*S / H)` | annual_demand, order_cost, holding_cost |
| 895 | `reorder_point` | Reorder Point | Inventory trigger level | `Daily_Demand * Lead_Time + Safety_Stock` | daily_demand, lead_time, safety_stock |
| 896 | `safety_stock` | Safety Stock | Buffer inventory | `Z * sigma * sqrt(Lead_Time)` | z_service, demand_std, lead_time |
| 897 | `capacity_utilization` | Capacity Utilization % | Actual vs potential output | `Actual_Output / Potential_Output * 100` | actual_output, potential_output |
| 898 | `learning_curve` | Learning Curve Unit Cost | Cost decline with volume | `First_Cost * Units^(log(rate)/log(2))` | first_unit_cost, cumulative_units, learning_rate |
| 899 | `gmv` | Gross Merchandise Value | Total marketplace sales | `Sum(Order_Values)` | order_values |
| 900 | `take_rate` | Take Rate % | Platform revenue / GMV | `Revenue / GMV * 100` | revenue, gmv |
| 901 | `average_order_value` | Average Order Value | Revenue per order | `Total_Revenue / Order_Count` | total_revenue, order_count |
| 902 | `repeat_purchase_rate` | Repeat Purchase Rate % | Returning customers share | `Repeat_Customers / Total_Customers * 100` | repeat_customers, total_customers |
| 903 | `attribution_linear` | Linear Attribution Credit | Equal credit per touchpoint | `Conversion_Value / Touchpoints` | conversion_value, touchpoints |
| 904 | `roi_marketing` | Marketing ROI % | Profit from marketing / spend | `(Revenue - Cost) / Cost * 100` | revenue, cost |
| 905 | `roas` | Return on Ad Spend | Revenue per ad dollar | `Ad_Revenue / Ad_Spend` | ad_revenue, ad_spend |
| 906 | `ltv_cac_payback` | LTV/CAC Payback (months) | Months to recover CAC | `CAC / (ARPU * Gross_Margin)` | cac, arpu, gross_margin |
| 907 | `cash_runway_months` | Cash Runway (months) | Months until cash out | `Cash / Monthly_Burn` | cash, monthly_burn |
| 908 | `weighted_pipeline` | Weighted Sales Pipeline | Probability-weighted deals | `Sum(Deal_Value * Win_Probability)` | deal_values, win_probabilities |
| 909 | `win_rate` | Sales Win Rate % | Won deals / total deals | `Won_Deals / Total_Deals * 100` | won_deals, total_deals |
| 910 | `market_growth_rate` | Market Growth Rate % | YoY market size change | `(Market_Now - Market_Prior)/Market_Prior*100` | market_now, market_prior |

## 6. Testing Strategy

Testing is **mandatory** and gates every formula. No formula is considered "done" until its tests pass.

### 6.1 Test Requirements Per Formula

Each of the 610 formulas must have **at least 3 test cases**:

1. **Known-answer (golden) test** — a textbook/real-filing example where the correct answer is independently known. Example: Apple FY2023 gross margin = 44.13% from the 10-K.
2. **Edge case** — zero denominators, negative values, empty series, single-element series. Must return `valid=False` gracefully, never crash.
3. **Property/invariant test** — a mathematical property that must hold. Example: `gross_margin <= 100`, `current_ratio > 0` for positive inputs, `put_call_parity` residual ≈ 0.

Minimum test count: **910 × 3 = 2730 test cases**.

### 6.2 Test File Pattern

```python
import pytest
from src.maths_lib.profitability import gross_margin

def test_gross_margin_known_answer():
    # Apple FY2023: Revenue 383,285  COGS 214,137
    r = gross_margin(revenue=383285, cogs=214137)
    assert r.valid is True
    assert abs(r.value - 44.13) < 0.01      # tolerance 0.01pp
    assert r.unit == '%'

def test_gross_margin_zero_revenue():
    r = gross_margin(revenue=0, cogs=100)
    assert r.valid is False                  # division guard
    assert r.value is None

def test_gross_margin_invariant():
    r = gross_margin(revenue=1000, cogs=300)
    assert r.value <= 100                    # margin can't exceed 100%
```

### 6.3 Numerical Tolerance Standards

| Formula Type | Tolerance | Reason |
|--------------|-----------|--------|
| Ratios, margins (%) | ±0.01 | Rounding in source filings |
| Currency values ($) | ±0.5 or ±0.01% | Rounding to nearest unit |
| Option prices (Black-Scholes) | ±0.001 | Sensitive to vol/time |
| Monte Carlo / VaR | ±2% (seed=42) | Stochastic, fixed-seed |
| Duration / convexity | ±0.001 | Bond math precision |
| Trig / pure math | ±1e-9 | Floating-point limit |

### 6.4 Golden Reference Set

`tests/maths_lib/golden/` holds JSON files with known-answer inputs and outputs sourced from: real SEC 10-K filings (Apple, NVIDIA, 3M), CFA curriculum examples, and standard textbook problems (Hull for options, Fabozzi for fixed income). These are the regression anchors.

### 6.5 CI Gate

```bash
# Run the full maths_lib test suite
pytest tests/maths_lib/ -v --tb=short

# Coverage requirement: 100% line coverage on maths_lib/
pytest tests/maths_lib/ --cov=src.maths_lib --cov-fail-under=100

# Registry integrity (no duplicate IDs, every fn registered)
pytest tests/maths_lib/test_registry.py -v
```

The build does not advance to the next domain until the current domain's tests are green.

## 7. Registry & Lookup API (`registry.py`)

The registry is how the Composite Resolver (N20) and Formula Router find formulas at runtime.

```python
from src.maths_lib.registry import (
    get_formula, search_by_keyword, list_by_domain, compute
)

# Direct lookup by ID
fn = get_formula('black_scholes_call')
result = fn(spot=100, strike=105, time=0.5, rate=0.03, volatility=0.2)

# Keyword search (for Composite Resolver side-word matching)
matches = search_by_keyword('turnover')
#   -> ['asset_turnover', 'inventory_turnover', 'receivables_turnover', ...]

# Compute by ID with a dict of inputs (used by N20 matrix solver)
result = compute('current_ratio',
                 {'current_assets': 143566, 'current_liabilities': 145308})
#   -> FormulaResult(value=0.988, unit='x', ...)

# List a whole domain
ratio_fns = list_by_domain('D01_profitability')
```

**Registry guarantees:**

- Every formula ID is globally unique (enforced by `test_registry.py`).
- Every registered function has metadata: name, expression, domain, unit, input list.
- `compute(fid, inputs)` validates that all required inputs are present before calling.

## 8. Integration With the FinBench Pipeline

`maths_lib` plugs into two pipeline nodes:

### 8.1 Formula Router (between N06 Sniper and N07 BM25)

When a question contains formula keywords (`ratio`, `margin`, `turnover`, `duration`, `Black-Scholes`, etc.), the Formula Router:

1. Identifies the target formula via `search_by_keyword`.
2. Uses Sniper to extract the required input values from the filing.
3. Calls `compute(fid, inputs)`.
4. Returns a deterministic `FormulaResult` — bypassing the LLM entirely.

### 8.2 Composite Resolver / N20 (the JEE side-word method)

For multi-step questions ("5-in-1" formulas), N20:

1. Harvests side-words to detect which sub-formulas are needed.
2. Builds a dependency graph among `maths_lib` functions.
3. Anchors on the single given value (Sniper-extracted).
4. Topologically sorts and calls sub-formulas in order.
5. Self-verifies via 3 independent computation paths.

Because every `maths_lib` function returns inputs + expression, N20 can emit a full audit trail — a key differentiator for enterprise/audit use.

## 9. Build Plan (Session-by-Session)

One domain per session. Each session: write module -> write tests -> run tests green -> commit -> update CONTEXT.md.

| Session | Domain | Module | Formulas | Cumulative |
|---------|--------|--------|----------|------------|
| 1 | Profitability & Margin Ratios | `profitability.py` | 50 | 50 |
| 2 | Liquidity, Solvency & Efficiency Ratios | `liquidity_solvency.py` | 50 | 100 |
| 3 | Valuation Metrics & Models | `valuation.py` | 60 | 160 |
| 4 | Time-Series & Technical Analysis | `technical.py` | 80 | 240 |
| 5 | Options Pricing & Derivatives | `options.py` | 45 | 285 |
| 6 | Fixed Income & Bonds | `fixed_income.py` | 50 | 335 |
| 7 | Risk Management & Portfolio Theory | `risk.py` | 50 | 385 |
| 8 | Time Value of Money & Capital Budgeting | `tvm.py` | 45 | 430 |
| 9 | Corporate Finance & M&A | `corporate_ma.py` | 50 | 480 |
| 10 | Accounting & Depreciation | `accounting.py` | 40 | 520 |
| 11 | Statistics & Econometrics | `statistics_econ.py` | 45 | 565 |
| 12 | Core Math, Trigonometry, Linear Algebra & Geometry | `math_core.py` | 45 | 610 |
| 13 | Growth, Segment, Forensic & Modern Metrics | `growth_segment_forensic.py` | 50 | 660 |
| 14 | AI / Machine Learning Metrics & Functions | `ai_ml.py` | 93 | 753 |
| 15 | Probability Theory & Distributions | `probability.py` | 55 | 808 |
| 16 | Advanced Statistics & Hypothesis Testing | `statistics_advanced.py` | 53 | 861 |
| 17 | Business Analyst KPIs, Forecasting & Decision | `business_analyst.py` | 49 | 910 |

At your stated pace (~30 formulas/day), the remaining work is roughly **910 total**, and you reported ~150 already done — so about **760 remaining ≈ 15 days** of focused building, including tests.

## 10. Constraints Compliance

| Constraint | How `maths_lib` complies |
|------------|--------------------------|
| C1 Zero Cost | Pure Python/NumPy/SciPy — no paid APIs |
| C2 Local Inference | No network calls; all computation in-process |
| C5 Deterministic Seed | `seed=42` for Monte Carlo, simulations |
| C9 Private Fields | `maths_lib` never reads/writes `_rlef_` fields |
| A-perf | Each formula < 10 ms execution |

## 11. Acceptance Criteria (Definition of Done)

- [ ] All 910 formulas implemented across 12 modules.
- [ ] All 910 formulas registered in `FORMULA_REGISTRY` with unique IDs.
- [ ] ≥ 2730 test cases, all passing.
- [ ] 100% line coverage on `src/maths_lib/`.
- [ ] Golden reference set populated from real filings.
- [ ] Registry integrity test passing (unique IDs, all functions registered).
- [ ] Formula Router integrated and tested on FinanceBench ratio questions.
- [ ] Every `FormulaResult` carries name + expression + inputs (audit trail).
- [ ] No formula exceeds 10 ms execution time.

---

*End of PDR-MATHSLIB-001 Rev 1.0 — 910 formulas specified.*