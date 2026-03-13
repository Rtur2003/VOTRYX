"""UI text constants for the VOTRYX interface."""

from typing import List, TypedDict


class StringsDict(TypedDict):
    """Typed dictionary for UI strings."""

    header_title: str
    header_subtitle: str
    state_idle: str
    section_status: str
    stat_votes: str
    stat_errors: str
    stat_state: str
    stat_runtime: str
    section_settings: str
    section_general: str
    label_target_url: str
    helper_target_url: str
    label_vote_interval: str
    helper_vote_interval: str
    label_batch_size: str
    helper_batch_size: str
    label_timeout: str
    helper_timeout: str
    label_max_errors: str
    helper_max_errors: str
    label_backoff: str
    helper_backoff: str
    label_backoff_cap: str
    helper_backoff_cap: str
    label_parallel: str
    helper_parallel: str
    toggle_headless: str
    toggle_auto_driver: str
    helper_headless: str
    section_advanced: str
    toggle_random_ua: str
    helper_random_ua: str
    toggle_block_images: str
    helper_block_images: str
    label_user_agents: str
    helper_user_agents: str
    label_vote_selectors: str
    helper_vote_selectors: str
    button_apply: str
    button_defaults: str
    section_log: str
    badge_success: str
    badge_errors: str
    toggle_autoscroll: str
    toggle_errors_only: str
    button_clear_log: str
    section_actions: str
    button_start: str
    button_stop: str
    button_preflight: str
    button_open_logs: str
    button_reset_counters: str
    button_tray: str
    welcome_title: str
    welcome_subtitle: str
    welcome_bullets: List[str]
    welcome_cta: str
    tutorial_title: str
    tutorial_subtitle: str
    tutorial_steps: List[str]
    tutorial_cta: str


STRINGS: StringsDict = {
    "header_title": "VOTRYX Control Panel",
    "header_subtitle": "Automated voting controller",
    "state_idle": "Idle",
    "section_status": "Status",
    "stat_votes": "Votes",
    "stat_errors": "Errors",
    "stat_state": "State",
    "stat_runtime": "Runtime",
    "section_settings": "Settings",
    "section_general": "General",
    "label_target_url": "Target URL",
    "helper_target_url": "Voting page URL",
    "label_vote_interval": "Vote Interval (sec)",
    "helper_vote_interval": "Delay between votes",
    "label_batch_size": "Batch Size",
    "helper_batch_size": "Votes per batch",
    "label_timeout": "Timeout (sec)",
    "helper_timeout": "Vote button wait limit",
    "label_max_errors": "Max Errors",
    "helper_max_errors": "Backoff after consecutive errors",
    "label_backoff": "Backoff (sec)",
    "helper_backoff": "Initial backoff delay",
    "label_backoff_cap": "Backoff Cap",
    "helper_backoff_cap": "Max backoff delay",
    "label_parallel": "Parallel Windows",
    "helper_parallel": "Browser count",
    "toggle_headless": "Run headless",
    "toggle_auto_driver": "Use Selenium Manager",
    "helper_headless": "Headless mode hides Chrome windows. Selenium Manager auto-resolves drivers.",
    "section_advanced": "Advanced",
    "toggle_random_ua": "Randomize user agent",
    "helper_random_ua": "Uses custom list or defaults when enabled.",
    "toggle_block_images": "Block images for faster loads",
    "helper_block_images": "When enabled, image loading is disabled.",
    "label_user_agents": "User-Agent list (one per line)",
    "helper_user_agents": "Leave empty for defaults.",
    "label_vote_selectors": "Vote selectors (CSS or XPath per line)",
    "helper_vote_selectors": "Example: css:a[data-action='vote'] or xpath://button[contains(.,'vote')]",
    "button_apply": "Apply Settings",
    "button_defaults": "Reset Defaults",
    "section_log": "Log",
    "badge_success": "Success",
    "badge_errors": "Errors",
    "toggle_autoscroll": "Autoscroll",
    "toggle_errors_only": "Errors only",
    "button_clear_log": "Clear Log",
    "section_actions": "Actions",
    "button_start": "Start",
    "button_stop": "Stop",
    "button_preflight": "Preflight",
    "button_open_logs": "Open Logs",
    "button_reset_counters": "Reset Counters",
    "button_tray": "Minimize to Tray",
    "welcome_title": "Welcome to VOTRYX",
    "welcome_subtitle": "A focused workspace for automated voting control.",
    "welcome_bullets": [
        "Guided setup for URL, timing, and batch size.",
        "Live status, counters, and log visibility.",
        "Guardrails for errors, backoff, and recovery.",
    ],
    "welcome_cta": "Start Setup",
    "tutorial_title": "Quick Start",
    "tutorial_subtitle": "Three steps to launch a clean voting session.",
    "tutorial_steps": [
        "1) Set Target URL and timing in Settings.",
        "2) Run Preflight to confirm driver and Chrome.",
        "3) Press Start and monitor Status + Log.",
    ],
    "tutorial_cta": "Open Control Panel",
}
