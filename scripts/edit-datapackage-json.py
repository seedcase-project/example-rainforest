from pathlib import Path

import seedcase_sprout.core as sp

package_path = Path(__file__).resolve().parent.parent

current_properties = sp.read_properties(
    path=sp.PackagePath(package_path).properties(),
)

updated_properties = sp.PackageProperties(
    description=(
        "Dung beetles relocate vertebrate feces under the soil surface, "
        "and this behavior has many ecological consequences. In tropical forests, "
        "those seeds that are defecated by mammals and subsequently buried "
        "by dung beetles are less likely to suffer predation."
    ),
)

updated_package_properties = sp.update_package_properties(
    current_properties=current_properties,
    update_properties=updated_properties,
)

sp.write_package_properties(
    properties=updated_package_properties,
    path=sp.PackagePath(package_path).properties(),
)
