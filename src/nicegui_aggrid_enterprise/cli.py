"""CLI for building AG Grid Enterprise JavaScript bundles."""

import shutil
import subprocess
import sys
from pathlib import Path


def get_package_dir() -> Path:
    """Get the directory where this package is installed."""
    return Path(__file__).parent


def check_node_installed() -> bool:
    """Check if Node.js and npm are available."""
    try:
        subprocess.run(
            ["node", "--version"],
            capture_output=True,
            check=True,
        )
        subprocess.run(
            ["npm", "--version"],
            capture_output=True,
            check=True,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def build() -> int:
    """Build the AG Grid Enterprise JavaScript bundles.

    Returns:
        0 on success, non-zero on failure.
    """
    package_dir = get_package_dir()

    print("=" * 60)
    print("AG Grid Enterprise Bundle Builder")
    print("=" * 60)
    print()

    # Check for Node.js
    if not check_node_installed():
        print("ERROR: Node.js and npm are required but not found.")
        print()
        print("Please install Node.js from https://nodejs.org/")
        print("or via your package manager:")
        print("  - macOS: brew install node")
        print("  - Ubuntu/Debian: sudo apt install nodejs npm")
        print("  - Windows: winget install OpenJS.NodeJS")
        return 1

    # Check for package.json
    package_json = package_dir / "package.json"
    if not package_json.exists():
        print(f"ERROR: package.json not found at {package_json}")
        print("The package may not have been installed correctly.")
        return 1

    print(f"Building in: {package_dir}")
    print()

    # Run npm install
    print("Step 1/2: Installing npm dependencies...")
    print("-" * 40)
    try:
        result = subprocess.run(
            ["npm", "install"],
            cwd=package_dir,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"ERROR: npm install failed with exit code {e.returncode}")
        return e.returncode

    print()
    print("Step 2/2: Building JavaScript bundles...")
    print("-" * 40)

    # Run npm build
    try:
        result = subprocess.run(
            ["npm", "run", "build"],
            cwd=package_dir,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"ERROR: npm run build failed with exit code {e.returncode}")
        return e.returncode

    print()
    print("=" * 60)
    print("SUCCESS! AG Grid Enterprise bundles built successfully.")
    print("=" * 60)
    print()
    print("Built bundles:")
    print(f"  - {package_dir / 'dist' / 'index.js'}")
    print(f"  - {package_dir / 'dist-enterprise-charts' / 'index.js'}")
    print()
    print("You can now use AgGridEnterprise and AgGridEnterpriseCharts in your NiceGUI app.")

    return 0


def clean() -> int:
    """Remove built bundles and node_modules.

    Returns:
        0 on success, non-zero on failure.
    """
    package_dir = get_package_dir()

    print("Cleaning build artifacts...")

    dirs_to_remove = [
        package_dir / "dist",
        package_dir / "dist-enterprise-charts",
        package_dir / "node_modules",
    ]

    for dir_path in dirs_to_remove:
        if dir_path.exists():
            print(f"  Removing {dir_path}")
            shutil.rmtree(dir_path)

    print("Done.")
    return 0


def main() -> int:
    """Main entry point for the CLI."""
    if len(sys.argv) < 2:
        # Default to build
        return build()

    command = sys.argv[1]

    if command in ("build", "-b"):
        return build()
    elif command in ("clean", "-c"):
        return clean()
    elif command in ("--help", "-h"):
        print("Usage: nicegui-aggrid-enterprise [command]")
        print()
        print("Commands:")
        print("  build   Build the AG Grid Enterprise JavaScript bundles (default)")
        print("  clean   Remove built bundles and node_modules")
        print("  --help  Show this help message")
        return 0
    else:
        print(f"Unknown command: {command}")
        print("Run 'nicegui-aggrid-enterprise --help' for usage.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
