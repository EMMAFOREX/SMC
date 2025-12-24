def confidence_score(d):
    score = 0
    if d.get("order_block"): score += 20
    if d.get("liquidity"): score += 20
    if d.get("fair_value_gap"): score += 20
    if d.get("ob_fvg_alignment"): score += 10
    if d.get("liquidity_sweep"): score += 10
    if d.get("valid_stop_loss"): score += 10
    if d.get("valid_take_profit"): score += 5
    if d.get("h1_trend_match"): score += 3
    if d.get("h4_trend_match"): score += 2
    return score
