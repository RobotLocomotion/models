from pathlib import Path
from typing import Iterator
import unittest

from pydrake.planning import RobotDiagramBuilder


class TestDrakeModels(unittest.TestCase):

    @staticmethod
    def inventory() -> Iterator[str]:
        """Generates the list of all files in this repository. The result is
        strings like "franka_description/urdf/hand.urdf".
        """
        with open("inventory.txt", encoding="utf-8") as f:
            for line in f.readlines():
                yield line.strip()

    @staticmethod
    def get_all_models() -> Iterator[str]:
        """Generates the Paths of all model files. The result is
        URLs like "package://drake_models/franka_description/urdf/hand.urdf".
        """
        for path in TestDrakeModels.inventory():
            url = f"package://drake_models/{path}"
            if any([path.endswith(".dmd.yaml"),
                    path.endswith(".sdf"),
                    path.endswith(".urdf")]):
                yield url

    def test_all_models(self):
        """Checks that all model files parse without any errors nor warnings.
        """
        all_models = list(TestDrakeModels.get_all_models())

        # Allow warnings on these models until they are repaired.
        models_with_warnings = [
            # TODO(#19992) for tracking these warnings.
            "package://drake_models/atlas/atlas_convex_hull.urdf",
            "package://drake_models/atlas/atlas_minimal_contact.urdf",
            # We don't have any tracking issue for fixing the allegro models,
            # because we don't use them for anything we care about. If someone
            # wants to fix the warnings, be our guest.
            "package://drake_models/allegro_hand_description/urdf/allegro_hand_description_left.urdf",  # noqa
            "package://drake_models/allegro_hand_description/urdf/allegro_hand_description_right.urdf",  # noqa
            # TODO(jwnimmer-tri) Fix these warnings.
            "package://drake_models/jaco_description/urdf/j2n6s300_col.urdf",
            # We don't have any tracking issue for fixing the PR2 models,
            # because we don't use them for anything we care about. If someone
            # wants to fix the warnings, be our guest.
            "package://drake_models/pr2_description/urdf/pr2_simplified.urdf"
        ]
        self.assertFalse(set(models_with_warnings) - set(all_models))

        # Allow errors on these models until they are repaired.
        models_with_errors = [
            # This file is not designed to be loaded independently from its
            # parent file `homecart.dmd.yaml`; it will always error out.
            "package://drake_models/tri_homecart/homecart_grippers.dmd.yaml",
        ]
        self.assertFalse(set(models_with_errors) - set(all_models))
        self.assertFalse(set(models_with_warnings) & set(models_with_errors))

        # Run all tests.
        for url in all_models:
            with self.subTest(url=url):
                expect_warnings = url in models_with_warnings
                expect_errors = url in models_with_errors
                self._check_model(
                    url=url,
                    expect_warnings=expect_warnings,
                    expect_errors=expect_errors)

    def _check_model(self, *,
                     url: str,
                     expect_warnings: bool,
                     expect_errors: bool):
        """Checks that when parsed, the given url contains warnings and/or
        errors consistent with the expected conditions.
        """
        if expect_errors:
            with self.assertRaises(Exception):
                self._parse(url=url, strict=False)
            return
        if expect_warnings:
            self._parse(url=url, strict=False)
            with self.assertRaises(Exception):
                self._parse(url=url, strict=True)
            return
        self._parse(url=url, strict=True)

    def _parse(self, *, url: str, strict: bool):
        builder = RobotDiagramBuilder()
        parser = builder.parser()
        package_map = parser.package_map()
        for name in package_map.GetPackageNames():
            package_map.Remove(name)
        package_map.AddPackageXml(str(Path("package.xml").absolute()))
        if strict:
            parser.SetStrictParsing()
        parser.AddModels(url=url)

if __name__ == "__main__":
    unittest.main()
