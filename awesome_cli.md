# `awesome-cli`

Awesome CLI user manager.

**Usage**:

```console
$ awesome-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `create`: Create a new user with USERNAME.
* `delete`: Delete a user with USERNAME.
* `delete-all`: Delete ALL users in the database.
* `init`: Initialize the users database.

## `awesome-cli create`

Create a new user with USERNAME.

**Usage**:

```console
$ awesome-cli create [OPTIONS] USERNAME
```

**Arguments**:

* `USERNAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `awesome-cli delete`

Delete a user with USERNAME.

If --force is not used, will ask for confirmation.

**Usage**:

```console
$ awesome-cli delete [OPTIONS] USERNAME
```

**Arguments**:

* `USERNAME`: [required]

**Options**:

* `--force / --no-force`: Force deletion without confirmation.  [required]
* `--help`: Show this message and exit.

## `awesome-cli delete-all`

Delete ALL users in the database.

If --force is not used, will ask for confirmation.

**Usage**:

```console
$ awesome-cli delete-all [OPTIONS]
```

**Options**:

* `--force / --no-force`: Force deletion without confirmation.  [required]
* `--help`: Show this message and exit.

## `awesome-cli init`

Initialize the users database.

**Usage**:

```console
$ awesome-cli init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
