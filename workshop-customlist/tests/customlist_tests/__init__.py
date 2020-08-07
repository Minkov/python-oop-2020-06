import pkgutil

# import tests.customlist_tests.customlist_move_tests

print([__import__(name) for _, name, _ in pkgutil.iter_modules()])

