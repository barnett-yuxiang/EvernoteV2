# Open Issue Action

![test workflow](https://github.com/github-actions-course/open-issue-action/actions/workflows/test.yml/badge.svg?event=push&branch=main)

This action opens a new issue on GitHub with a title, body and a list of assignees.

## Inputs

### `token`

**Required** A GitHub token with issues:write scope.

### `title`

**Required** The title of the issue

### `body`

The body of the issue.

### `assignees`

A list of GitHub usernames to assign to the issue.

## Outputs

### `issue`

The created issue object as a json string.

## Example usage

```yaml
uses: github-actions-course/open-issue-action@v1
  id: issue
  with:
    token: ${{ secrets.GITHUB_TOKEN }}
    title: Test Issue
    body: Test issue body
    assignees: |
      alialaa
```
