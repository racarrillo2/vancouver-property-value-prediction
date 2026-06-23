"""
Internationalization helper: language selector + session state management.
"""

import streamlit as st
from translations import t

DEFAULT_LANG = "en"
LANGUAGES = {"en": "🇨🇦 English", "es": "🇪🇸 Español"}


def init_language():
    """Initialize language in session state if not set."""
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LANG


def language_selector():
    """Render the language selector in the sidebar."""
    init_language()
    selected = st.sidebar.selectbox(
        t("language_label", st.session_state.lang),
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x],
        index=list(LANGUAGES.keys()).index(st.session_state.lang),
        key="lang_selector"
    )
    if selected != st.session_state.lang:
        st.session_state.lang = selected
        st.rerun()


def get_lang() -> str:
    """Get current language from session state."""
    init_language()
    return st.session_state.lang


def tr(key: str, **kwargs) -> str:
    """Shortcut: translate using current session language."""
    return t(key, get_lang(), **kwargs)