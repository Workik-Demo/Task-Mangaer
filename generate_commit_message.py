import os
import git

def generate_commit_message(diff_text):
    if not diff_text.strip():
        return "No changes made."
    return f"Updated code with changes: {len(diff_text.splitlines())} lines affected."

def main(repo_path):
    if not os.path.exists(repo_path):
        print(f"Repository path '{repo_path}' does not exist.")
        return

    # Open the repository
    repo = git.Repo(repo_path)

    # Get the latest commit
    latest_commit = repo.head.commit

    # Get the diff of the latest commit (against the previous commit)
    diffs = latest_commit.diff('HEAD~1')

    # Collect the diff information
    diff_text = ""
    for diff in diffs:
        diff_text += diff.diff  # Removed .decode('utf-8'), as diff.diff is already a string

    # Generate commit message
    commit_message = generate_commit_message(diff_text)

    # Print the generated commit message
    print("Generated Commit Message:")
    print(commit_message)

    repo.git.add(A=True)
    repo.index.commit(commit_message)

    origin = repo.remote(name='origin')
    origin.push()
    print("Changes pushed to the remote repository.")

if __name__ == "__main__":
    repository_path = r'C:\Users\KIIT\OneDrive\Desktop\Workik\Docker\express_task_manager'  # Update this path accordingly
    main(repository_path)