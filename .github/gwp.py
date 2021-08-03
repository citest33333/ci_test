#!python3
import argparse
import os
import os.path


def main():
    parser = argparse.ArgumentParser(
        description="Github Workflow Preprocessor. This script will explode"
        "all aliases to anchors, then prune the root `anchors` entry",
        epilog="Example: cd into .github and do: `python gwp.py rust.yml`"
    )
    parser.add_argument(
        "WORKFLOW_PATH", help="path to source workflow yaml file")
    args = parser.parse_args()
    github_dir = os.path.dirname(os.path.realpath(__file__))
    outfile = os.path.basename(args.WORKFLOW_PATH)
    os.system(
        "yq e \""
        "explode(.) | "
        "del(.anchors) | "
        ". headComment="
        "\"\"Do_not_edit_directly."
        "_See_readme_section_editing_github_workflows\"\""
        "\""
        f" {args.WORKFLOW_PATH} > {github_dir}\\workflows\\_{outfile}")


if __name__ == '__main__':
    main()
