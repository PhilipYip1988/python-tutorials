import sys

import seaborn as sns

print(f'type: {type(sys.modules)}')
print(f'len: {len(sys.modules)}')
print(sys.modules)
print(sys.modules.keys())

print(f"'numpy' in sys.modules: {'numpy' in sys.modules}")
print(f"'pandas' in sys.modules: {'pandas' in sys.modules}")
print(f"'matplotlib' in sys.modules: {'matplotlib' in sys.modules}")
print(f"'PIL' in sys.modules: {'PIL' in sys.modules}")
