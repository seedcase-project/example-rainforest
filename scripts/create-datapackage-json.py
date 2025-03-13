from pathlib import Path

import seedcase_sprout.core as sp

properties = sp.PackageProperties(
    name="dung-beetle-activity",
    title=(
        "Dung beetle activity affects rainforest seed bank dynamics "
        "and seedling establishment"
    ),
    description=(
        "Dung beetles relocate vertebrate feces under the soil surface, "
        "and this behavior has many ecological consequences. In tropical forests, "
        "for example, seeds defecated by mammals that are subsequently buried "
        "by dung beetles are less likely to suffer predation."
    ),
    contributors=[
        sp.ContributorProperties(
            title="Lina Adonay Urrea-Galeano",
            path="https://orcid.org/0000-0001-6217-4215",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Ellen Andresen",
            path="https://orcid.org/0000-0001-8957-4454",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Rosamond Coates",
            path="https://orcid.org/0000-0003-0074-1565",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Francisco Mora Ardila",
            path="https://orcid.org/0000-0003-0390-0189",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Guillermo Ibarra-Manríquez",
            path="https://orcid.org/0000-0002-3739-8660",
            roles=["creator"],
        ),
    ],
    sources=[
        sp.SourceProperties(
            title=(
                "Dung beetle activity affects rainforest seed bank dynamics "
                "and seedling establishment"
            ),
            path="https://zenodo.org/record/4965431",
        )
    ],
    licenses=[
        sp.LicenseProperties(
            name="CCO_1.0",
            path="https://creativecommons.org/publicdomain/zero/1.0/legalcode",
            title="CCO 1.0 UNIVERSAL",
        )
    ],
)

# Create the path to the package
package_path = Path(__file__).resolve().parent.parent
package_path = sp.create_package_properties(properties=properties, path=package_path)
