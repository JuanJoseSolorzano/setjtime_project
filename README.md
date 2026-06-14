# setjtime

> A Jira time logger tool via terminal. 

`setjtime` allows you to log time to JIRA issues directly from your terminal. It supports adding simple comments so you can provide context for the time logged. This tool uses the REST API of JIRA to interact with your JIRA server, and requires environment variables for configuration.
---

## Features
  
- **Log time to JIRA issues** directly from the terminal
- **Add comments to JIRA issues** for context
- **Environment variable configuration** for JIRA server, username, and password
- **Works as** a global CLI command after installation

---

## Installation

```bash
pip install setjcomment
```

Or install from source:

```bash
git clone https://github.com/JuanJoseSolorzano/setjtime_project.git 
cd setjtime_project
pip install .
```
## Required Environment Variables
- `JIRA_SERVER`: The URL of your JIRA server (e.g., `yourdomain.atlassian.net`).
- `JIRA_USERNAME`: Your JIRA username (usually your email address).
- `JIRA_PASSWORD`: Your JIRA API token or password.
---

## Usage

```bash

positional arguments:
  issue_id              The ID of the JIRA issue (e.g., 6552 for SETV-6552).

optional arguments:
  -h, --help    show this help message and exit

  -t TIME,    --time     TIME    : Time spent (e.g., "2h", "30m").
  -c COMMENT, --comment  COMMENT : Add a short unformatted comment [optional].

```

### Examples

```bash
setjcomment 6552 -s "This is a short comment."
setjcomment 6552 -vs # Opens the template file in VScode for editing.
setjcomment 6552 -np # Opens the template file in Notepad for editing.
```
---

## License

See [LICENSE](LICENSE) for details.

---

## Author

**Juan Jose Solorzano Carrillo** — juanjose.solorzano.c@gmail.com
