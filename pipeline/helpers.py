"""
helpers.py — Shared utilities for the regression pipeline
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from linearmodels.panel import PanelOLS
from scipy import stats
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_TABLES = _REPO_ROOT / 'Outputs' / 'research_design' / 'tables'
OUT_FIGURES = _REPO_ROOT / 'Outputs' / 'research_design' / 'figures'
OUT_TABLES.mkdir(parents=True, exist_ok=True)
OUT_FIGURES.mkdir(parents=True, exist_ok=True)

# ── Variable blocks ──
# Lag-2 as default throughout: uses 2023 source data for 2025 outcomes,
# maximising the effective regression sample across the full 2013-2025 panel.
# Lag-1 available as robustness (loses 2025; lag-0 loses 2024-2025).
DEMOGRAPHICS = ['log_population_city', 'log_percapita_income_city', 'unemployment_city']
DEMOGRAPHICS_L1 = ['log_population_city', 'log_percapita_income_city', 'unemployment_city']
CONSTITUENCY = ['pres_dem_vote_share']
INFRASTRUCTURE = ['cwns_needs_real', 'pct_deficient', 'epa_npdes_violations']
INFRASTRUCTURE_L1 = ['cwns_needs_real_lag1', 'pct_deficient_lag1']
INFRASTRUCTURE_L2 = ['cwns_needs_real_lag2', 'pct_deficient_lag2']
INFRASTRUCTURE_L3 = ['cwns_needs_real_lag3', 'pct_deficient_lag3']
INFRASTRUCTURE_L4 = ['cwns_needs_real_lag4', 'pct_deficient_lag4']
# Default infrastructure block uses lag-2 for full panel coverage
INFRASTRUCTURE_DEFAULT = ['cwns_needs_real_lag2', 'pct_deficient_lag2']
F3_VARS = ['esg_has_antiesg_law', 'esg_has_underwriter_block', 'esg_has_muni_bond_law',
           'state_dem_trifecta', 'state_rep_trifecta', 'tel_stringency_normalized']

# ── Primary and secondary outcomes ──
# Primary: Y_self_green (city's deliberate choice to issue a green bond)
# Secondary: Y_esg_assurance (credibility investment — costliest choice)
# Contextual: Green_Bond_Issued (Bloomberg-observable, conflates project supply with detection)
PRIMARY_DV = 'Y_self_green'
SECONDARY_DV = 'Y_esg_assurance'
BLOOMBERG_DV = 'Green_Bond_Issued'

# ── Three-level outcome hierarchy ──
# Level 1: Bloomberg-observable (conflates infrastructure with labelling visibility)
LEVEL1_OUTCOMES = ['Green_Bond_Issued', 'Y_water_only', 'Y_has_non_water', 'Y_any_esg_project']
# Level 2: Labelling (city actively chose "green") — PRIMARY
LEVEL2_OUTCOMES = ['Y_self_green', 'incidentally_green']
# Level 3: Credibility (city paid to certify) — SECONDARY
LEVEL3_OUTCOMES = ['Y_esg_assurance', 'Y_esg_framework', 'Y_any_credibility']

# ── Financing channel controls (hold investment/borrowing constant) ──
# Without these, Green_Bond_Issued measures infrastructure investment
# With these, it measures bond financing and branding choice
# Lag-2 default for full 2013-2025 coverage
FINANCING_CONTROLS = ['sewerage_expend_lag2', 'net_borrowing_ratio_lag2',
                      'highways_expend_lag2', 'direct_expenditure_pc_lag2']
FINANCING_CONTROLS_L1 = ['sewerage_expend_lag1', 'net_borrowing_ratio_lag1',
                         'highways_expend_lag1', 'direct_expenditure_pc_lag1']

# ── Family 1: Market and Material Conditions ──
# Infrastructure need
WATER_INFRASTRUCTURE = ['cwns_needs_real_lag2', 'pct_deficient_lag2', 'nri_water_risk_score']
WATER_INFRASTRUCTURE_L1 = ['cwns_needs_real_lag1', 'pct_deficient_lag1', 'nri_water_risk_score']
BRIDGE_INFRASTRUCTURE = ['deficient_bridges', 'deficient_deck_area_sqm']
# Climate risk exposure (cross-sectional, from NRI)
CLIMATE_RISK = ['nri_water_risk_score', 'nri_overall_risk_score']
# Enforcement / compulsion (also used in Family 3)
ENFORCEMENT_BROAD = ['npdes_formal_any_prior3yr', 'npdes_effluent_violations_count']
ENFORCEMENT_LADDER = ['npdes_formal_any_prior3yr', 'case_all_any_prior3yr',
                      'case_afr_any_prior3yr', 'case_jdc_any_prior3yr']
SDWA_VIOLATIONS = ['epa_sdwa_viol_health_based']
# Fiscal condition (lag-2 for full coverage)
FISCAL = ['reserve_ratio_lag2', 'debt_service_burden_lag2', 'operating_balance_lag2',
          'fiscal_stress_index_lag2']
FISCAL_EXTENDED = ['expenditure_rigidity_lag1', 'revenue_hhi_lag1', 'own_source_rev_share',
                   'combined_liability_burden', 'rating_agency_composite']
# Economic structure
ECONOMIC = ['manufacturing_city', 'management_city', 'naturalresources_city',
            'transport_city', 'lfpr_city']
# Demographics
DEMOGRAPHICS_FULL = ['log_population_city', 'log_percapita_income_city', 'unemployment_city',
                     'pop_density_sqmi', 'is_principal_city']
# State demographics (Census ACS)
STATE_DEMOGRAPHICS = ['state_poverty_rate', 'state_median_hh_income', 'state_gini_index',
                      'state_pct_bachelors_plus', 'state_pct_white', 'state_pct_black',
                      'state_pct_hispanic', 'state_homeownership_rate']
STATE_POLICY = ['state_right_to_work', 'state_has_income_tax', 'state_medicaid_expanded']
# Emissions
EMISSIONS = ['production_city']
# Bond market conditions (year-level)
BOND_MARKET = ['muni_aaa_yield', 'us_esg_aum_trillion']
# SRF / federal funding
SRF_CAPACITY = ['total_srf_allotment', 'cwsrf_total_allotment', 'dwsrf_total_allotment',
                'portal_total_lending', 'srf_received_any']

# ── Family 2: Mayoral Agency (interactions with Rep_Mayor) ──
INSTITUTIONAL = ['fog', 'partisan', 'termlimits', 'initiative', 'referendum']

# ── Family 3: State Institutional Environment ──
# Permission
PERMISSION = ['esg_has_muni_bond_law', 'esg_has_law_esg_score_ban_govt',
              'esg_has_underwriter_block', 'signed_utah_antiesg_letter',
              'go_supermajority', 'has_state_bond_commission']
# MSRB RFI revealed preference — test separately and prominently
# 24 states actively opposed ESG disclosure for municipal bonds (March 2022)
# This directly measures whether the state views green bond labelling as politically legitimate
# Key tests: signed_utah_antiesg_letter × Rep_Mayor on Level 2 (labelling) and Level 3 (credibility)
# Prediction: effect strongest on labelling/credibility, not project supply
MSRB_RFI = ['signed_utah_antiesg_letter', 'pro_esg_rfi_response']
# Capacity
CAPACITY = ['state_green_bond_ever_lag1', 'state_green_bond_cum_count_lag1',
            'has_bond_bank', 'total_srf_allotment']
# Compulsion (enforcement ladder)
COMPULSION_TIER1 = ['npdes_formal_any_prior3yr']  # broad pressure
COMPULSION_TIER2 = ['case_all_cum']  # federal cross-programme
COMPULSION_TIER3 = ['case_afr_any_prior3yr']  # administrative orders
COMPULSION_TIER4 = ['case_jdc_any_prior3yr']  # judicial consent decrees

# ── Part 2: Financial architecture ──
# Lag-2 default for full panel coverage
FISCAL_DEFAULT = ['reserve_ratio_lag2', 'debt_service_burden_lag2',
                  'fiscal_stress_index_lag2', 'sewerage_expend_lag2']
FISCAL_L1 = ['reserve_ratio_lag1', 'debt_service_burden_lag1',
             'fiscal_stress_index_lag1', 'sewerage_expend_lag1']

# Bloomberg decomposition column maps
USE_OF_FUNDS = {
    'Sustainable_Water': 'Sustainable_Water',
    'Clean_Transportation': 'Clean_Transportation',
    'Energy_Efficiency': 'Energy_Efficiency',
    'Green_Buildings': 'Green_Buildings',
    'Renewable_Energy': 'Renewable_Energy',
    'Pollution_Control': 'Pollution_Control',
    'Climate_Adaptation': 'Climate_Change_Adaptation',
}

CERTIFICATION = {
    'Self_Green_Yes': 'Self-reported Green__Yes',
    'ESG_Framework_Yes': 'ESG Framework__Yes',
    'ESG_Assurance_Yes': 'ESG Assurance Providers__Yes',
    'ESG_Reporting_Yes': 'ESG Reporting__Yes',
    'Mgmt_Proceeds_Yes': 'Mgmt of Proc__Yes',
    'Proj_Selection_Yes': 'Proj Sel Proc__Yes',
}

FINANCING_TYPE = {
    'New_Money': 'Fin Typ__NEW_MONEY',
    'Refunding': 'Fin Typ__REFUNDING',
}

SECURITY_TYPE = {
    'WTRSWR': 'Industry__WTRSWR',
    'GO': 'Industry__GO',
    'PUBPWR': 'Industry__PUBPWR',
    'PUBTRAN': 'Industry__PUBTRAN',
}


def stars(p):
    if pd.isna(p): return ''
    if p < 0.01: return '***'
    if p < 0.05: return '**'
    if p < 0.10: return '*'
    return ''


def load_panel():
    """Load master panel from pickle, set panel index."""
    pkl = Path(__file__).parent / 'panel.pkl'
    df = pd.read_pickle(pkl)
    return df


def available(varlist, df):
    """Filter variable list to columns that exist and have >500 non-null."""
    return [v for v in varlist if v in df.columns and df[v].notna().sum() > 500]


def run_lpm(data, y_var, x_vars, fe='none'):
    """
    Run LPM regression.
    fe: 'none', 'state+year', 'city+year', 'city+state_year'
    Returns (model, is_panel) tuple.
    """
    avail = [v for v in x_vars if v in data.columns]
    if not avail:
        return None, False

    d = data[['fips7', 'year', y_var] + avail + (['state_id'] if 'state_id' in data.columns else [])].dropna(subset=[y_var] + avail).copy()
    if len(d) < 50 or d[y_var].nunique() < 2:
        return None, False

    y = d[y_var]
    X = d[avail]

    if fe == 'none':
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit(cov_type='cluster', cov_kwds={'groups': d['fips7']})
        return model, False

    elif fe == 'state+year':
        if 'state_id' not in d.columns:
            return None, False
        state_dums = pd.get_dummies(d['state_id'], prefix='st', drop_first=True, dtype=float)
        year_dums = pd.get_dummies(d['year'], prefix='yr', drop_first=True, dtype=float)
        X_full = pd.concat([X.reset_index(drop=True), state_dums.reset_index(drop=True),
                            year_dums.reset_index(drop=True)], axis=1)
        X_full = sm.add_constant(X_full).astype(float)
        model = sm.OLS(y.values, X_full).fit(cov_type='cluster', cov_kwds={'groups': d['fips7'].values})
        # Attach original var names for extraction
        model._x_names = avail
        return model, False

    elif fe == 'city+year':
        d2 = d.set_index(['fips7', 'year'])
        try:
            mod = PanelOLS(d2[y_var], d2[avail], entity_effects=True, time_effects=True, check_rank=False)
            return mod.fit(cov_type='clustered', cluster_entity=True), True
        except Exception:
            return None, True

    elif fe == 'city+state_year':
        if 'state_id' not in d.columns:
            return None, False
        d['state_year'] = d['state_id'].astype(str) + '_' + d['year'].astype(str)
        sy_dums = pd.get_dummies(d['state_year'], prefix='sy', drop_first=True, dtype=float)
        d2 = d.set_index(['fips7', 'year'])
        X_full = pd.concat([d2[avail], sy_dums.set_index(d2.index)], axis=1)
        try:
            mod = PanelOLS(d2[y_var], X_full, entity_effects=True, check_rank=False)
            return mod.fit(cov_type='clustered', cluster_entity=True), True
        except Exception:
            return None, True

    return None, False


def extract_coef(model, var, is_panel=False):
    """Extract (coef, se, pvalue) for a variable from a model."""
    if model is None:
        return np.nan, np.nan, np.nan
    try:
        if is_panel:
            return float(model.params[var]), float(model.std_errors[var]), float(model.pvalues[var])
        else:
            return float(model.params[var]), float(model.bse[var]), float(model.pvalues[var])
    except (KeyError, ValueError):
        return np.nan, np.nan, np.nan


def get_nobs(model, is_panel=False):
    """Get number of observations."""
    if model is None:
        return 0
    return int(model.nobs)


def get_r2(model, is_panel=False):
    """Get R-squared."""
    if model is None:
        return np.nan
    if is_panel:
        return float(model.rsquared)
    return float(model.rsquared)


def wald_test_equality(model, var1, var2, is_panel=False):
    """Conservative Wald test for equality of two coefficients (ignoring covariance)."""
    b1, se1, _ = extract_coef(model, var1, is_panel)
    b2, se2, _ = extract_coef(model, var2, is_panel)
    if np.isnan(b1) or np.isnan(b2):
        return np.nan
    diff = b1 - b2
    se_diff = np.sqrt(se1**2 + se2**2)
    if se_diff == 0:
        return np.nan
    return float(2 * (1 - stats.norm.cdf(abs(diff / se_diff))))


def make_interaction(df, party_var, x_var):
    """Create Dem×X and Rep×X interaction terms."""
    dem_col = f'Dem_x_{x_var}'
    rep_col = f'Rep_x_{x_var}'
    df[dem_col] = (1 - df[party_var]) * df[x_var]
    df[rep_col] = df[party_var] * df[x_var]
    return dem_col, rep_col


def construct_category_dvs(df):
    """Build binary and asinh DVs for Bloomberg decomposition categories."""
    # Use of Funds — aggregate across multi-category columns
    for short, pattern in USE_OF_FUNDS.items():
        amt_cols = [c for c in df.columns if c.startswith('Amt_ESG Project Categories') and pattern in c]
        cnt_cols = [c for c in df.columns if c.startswith('Count_ESG Project Categories') and pattern in c]
        df[f'Y_{short}'] = (df[cnt_cols].sum(axis=1) > 0).astype(int) if cnt_cols else 0
        df[f'asinh_Amt_{short}'] = np.arcsinh(df[amt_cols].sum(axis=1)) if amt_cols else 0

    # Certification, Financing, Security — single column each
    for mapping, prefix in [(CERTIFICATION, ''), (FINANCING_TYPE, ''), (SECURITY_TYPE, '')]:
        for short, col_suffix in mapping.items():
            amt_col = f'Amt_{col_suffix}'
            cnt_col = f'Count_{col_suffix}'
            if amt_col in df.columns:
                df[f'Y_{short}'] = (df[cnt_col] > 0).astype(int) if cnt_col in df.columns else 0
                df[f'asinh_Amt_{short}'] = np.arcsinh(df[amt_col])
            # Handle NEW_MONEY case sensitivity
            if amt_col not in df.columns:
                # Try alternate case
                alt_amt = [c for c in df.columns if c.startswith('Amt_') and col_suffix.lower() in c.lower()]
                alt_cnt = [c for c in df.columns if c.startswith('Count_') and col_suffix.lower() in c.lower()]
                if alt_amt:
                    df[f'Y_{short}'] = (df[alt_cnt].sum(axis=1) > 0).astype(int) if alt_cnt else 0
                    df[f'asinh_Amt_{short}'] = np.arcsinh(df[alt_amt].sum(axis=1))

    return df
