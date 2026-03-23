from django import template

register = template.Library()

MONTHS = {
    "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
    "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
    "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
}

@register.filter
def month_short(date_str):
    """Extracts the short month name from a DD/MM/YYYY string."""
    try:
        month = date_str[3:5]
        return MONTHS.get(month, "")
    except Exception:
        return ""
