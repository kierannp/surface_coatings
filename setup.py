from setuptools import setup, find_packages

setup(
    name="surface_coatings",
    version="0.1.0",
    descriptions="Generic method to build coated surfaces",
    author="Co D. Quach",
    author_email="daico007@gmail.com",
    license="MIT",
    packages=find_packages(),
    package_data={
        "": ["monomers/*/*.{pdb,mol2}", "*.mol2", "*.pdb",
             "molecules/one_port/pdbs/*.pdb"]

    },
    package_dir={"surface_coatings": "surface_coatings"},
    include_package_data=True,
    zip_safe=False,
)
