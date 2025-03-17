from pathlib import Path

import seedcase_sprout.core as sp

properties = sp.PackageProperties(
    description=(
        "Dung beetles relocate vertebrate feces under the soil surface, "
        "and this behavior has many ecological consequences. In tropical forests, "
        "those seeds that are defecated by mammals and subsequently buried "
        "by dung beetles are less likely to suffer predation."
    ),
)

package_path = Path(__file__).resolve().parent.parent / "datapackage.json"

updated_package_properties = sp.edit_package_properties(
    path=package_path,
    properties=properties,
)

package_path = sp.write_package_properties(
    properties=updated_package_properties, path=package_path
)
