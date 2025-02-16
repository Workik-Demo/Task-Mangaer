import os
import git

def generate_commit_message(diff):
    # Basic heuristic to generate commit messages
    added_lines = sum(1 for line in diff.splitlines() if line.startswith('+') and not line.startswith('+++'))
    removed_lines = sum(1 for line in diff.splitlines() if line.startswith('-') and not line.startswith('---'))
    
    if added_lines > 0 and removed_lines > 0:
        return f"Modified {added_lines} lines and removed {removed_lines} lines."
    elif added_lines > 0:
        return f"Added {added_lines} lines."
    elif removed_lines > 0:
        return f"Removed {removed_lines} lines."
    else:
        return "No changes detected."

def main(repo_path):
    if not os.path.exists(repo_path):
        print(f"Repository path '{repo_path}' does not exist.")
        return

    # Open the repository
    repo = git.Repo(repo_path)

    # Get the latest commit
    latest_commit = repo.head.commit

    # Get the diff of the latest commit
    diff = latest_commit.diff('HEAD~1', create_patch=True).patch

    # Generate commit message
    commit_message = generate_commit_message(diff)

    # Print the generated commit message
    print("Generated Commit Message:")
    print(commit_message)

if __name__ == "__main__":
    # Specify the path to your Git repository
    repository_path = r'C:\Users\KIIT\OneDrive\Desktop\Workik\Docker\express_task_manager'
    main(repository_path)