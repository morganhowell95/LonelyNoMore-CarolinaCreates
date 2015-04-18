import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
	     for i in installed_packages])
sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])
print(installed_packages_list)
