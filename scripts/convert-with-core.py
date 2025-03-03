from pathlib import Path

import janitor.polars  # noqa: F401
import polars as pl

resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"

df_experiment1 = pl.read_csv(folder_path / "Expe1.csv", infer_schema_length=100_000)

df_experiment1 = df_experiment1.rename(
    {
        "bead_size": "bead_size_mm",
        "burial_depth": "burial_depth_cm",
        "cylinder": "cylinder_id",
        "movedup": "num_beads_moved_up",
        "moveddown": "num_beads_moved_down",
        "nomoved": "num_beads_no_movement",
        "total_beads": "total_num_beads",
        "proportion_movedup": "proportion_beads_moved_up",
        "proportion_moveddown": "proportion_beads_moved_down",
        "proportion_nomoved": "proportion_beads_no_movement",
    }
)
df_experiment1.write_csv(folder_path / "data-experiment1-ready.csv")

df_experiment2 = pl.read_csv(folder_path / "Expe2.csv", infer_schema_length=100_000)

treatment_mapping1 = {
    "masHmasE": "with_feces_cover_after_48h",
    "masHmenE": "with_faces_cover_after_0h",
    "menHmenE": "without_faces_cover_after_0h",
}

df_experiment2 = (
    df_experiment2.with_columns(pl.col("beetle_treatment").replace(treatment_mapping1))
    .rename(
        {
            "site": "site_id",
            "burial_depth": "burial_depth_cm",
            "bottle": "bottle_id",
            "plant_species": "plant_species_name",
            "total_seeds": "total_num_seeds",
            "emerged_seedlings": "num_emerged_seedlings",
            "proportion": "proportion_emerged_seedlings",
        }
    )
    .clean_names()
)

df_experiment2.write_csv(folder_path / "data-experiment2-ready.csv")

df_abundance = pl.read_csv(
    folder_path / "Expe3Abundance.csv", infer_schema_length=100_000
)

treatment_mapping2 = {
    "masHmasE1": "feces_once_beetle_access",
    "masHmenE1": "feces_once_beetle_exclusion",
    "masHmasE4": "feces_four_beetle_access",
    "masHmenE4": "feces_four_beetle_exclusion",
    "menHmenE": "feces_exclusion_beetle_exclusion",
}
df_abundance = df_abundance.with_columns(
    pl.col("beetle_treatment").replace(treatment_mapping2)
)

df_richness = pl.read_csv(
    folder_path / "Expe3Richness.csv", infer_schema_length=100_000
)

df_experiment3_all = pl.concat([df_abundance, df_richness], how="align")  # concat wide

df_experiment3_all = df_experiment3_all.rename(
    {"time_measurement": "time_measurement_weeks", "site": "site_id", "plot": "plot_id"}
)

df_experiment3_all.write_csv(folder_path / "data-experiment3-ready.csv")

df_experiment1.glimpse()
df_experiment2.glimpse()
df_experiment3_all.glimpse()
