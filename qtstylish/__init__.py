# Set version
from pkg_resources import get_distribution
__version__ = get_distribution('qtstylish').version

# Imports
from qtstylish.qtstylish import dark, light, ThemeSwitcher
from qtstylish.demo_widget import DemoWidget
from qtstylish.modern_window import ModernWindow

__all__ = ["dark", "light", "ThemeSwitcher",
           "DemoWidget", "ModernWindow", "__version__"]
