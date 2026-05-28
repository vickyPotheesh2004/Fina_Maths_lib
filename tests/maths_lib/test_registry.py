import maths_lib as ml


def test_registry_total_and_uniqueness():
    rows = ml.all_formulas()
    ids = [f[0] for _dk, _title, _m, f in rows]
    assert len(ids) == 1500
    assert len(set(ids)) == len(ids)
    assert set(ids) == set(ml.FORMULA_REGISTRY.keys())
    assert set(ids) == set(ml.FORMULA_METADATA_REGISTRY.keys())


def test_no_overlap_between_modules():
    seen = {}
    for dkey, dval in ml.DOMAINS.items():
        for f in dval["formulas"]:
            fid = f[0]
            assert fid not in seen, f"duplicate formula id {fid} in {dkey} and {seen[fid]}"
            seen[fid] = dkey


def test_count_summary_matches_total():
    summary, total = ml.count_summary()
    assert total == 1500
    assert sum(x[2] for x in summary) == 1500
