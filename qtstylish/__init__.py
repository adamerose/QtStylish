# Set version
from pkg_resources import get_distribution
__version__ = get_distribution('pandasgui').version

# Imports
from qtstylish.qtstylish import dark, light, ThemeSwitcher
from qtstylish.demo_widget import DemoWidget

__all__ = ["dark", "light", "ThemeSwitcher", "DemoWidget", "__version__"]
