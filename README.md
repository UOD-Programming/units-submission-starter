# Units Submission Starter

The starter repository containing unit 1. All subsequent units will need to be downloaded from Blackboard and unzipped into this repository in the correct manner.

## Units (36%)


There are a total of 8 units which include Lessons and Exercises.

These are auto-graded, and you will be assessed on your answers to these, but also on your engagement in practicals.

## Practical Engagement (16%)


You will also be assessed on your engagement with the lessons in 8 out of 12 practicals. These are worth 2% each, totalling 16%.

Award the 2% session credit where the student can demonstrate meaningful progress on relevant unit work during the practical. The work does not need to be complete or correct, and the student may be working on any unit.

## Release of Units


Each week, a new unit will be released. You will be asked to maintain your GitHub repository of your work and finally submit your repository as a zip folder.

These should be unzipped and placed in a Github repository in the correct manner.

## Maintaining your GitHub repository


You must maintain one private GitHub repository containing all your unit work. Name the repository using your student number followed by _units_submission.

For example:

``` 100123456_units_submission ```
 
 
### Adding each unit

When a new unit is released:

1. Download the unit ZIP file from Blackboard.
2. Extract the ZIP file.
3. Copy the complete extracted unit folder into your local repository folder.
4. Do not alter the supplied folder structure.
5. Commit the new unit folder and push it to GitHub.
6. Your repository will gradually build up as follows:

```
100123456_units_submission/
├── unit_01/
├── unit_02/
├── unit_03/
└── ...
```

Only edit the .py files inside each unit’s src/lessons and src/exercises folders. All other supplied files and folders must remain unchanged.

Do not place the ZIP file itself in your repository. You must extract it and copy the contents of the unit folder into the correct folder in your repository.

## Required folder structure


Your final submission must be contained within a single parent folder named using your student number, followed by _units_submission.

For example, if your student number is 100123456, your parent folder must be named:

``` 100123456_units_submission```

Your final folder should contain all eight unit folders:

```
100123456_units_submission/
├── unit_01/
├── unit_02/
├── unit_03/
├── unit_04/
├── unit_05/
├── unit_06/
├── unit_07/
└── unit_08/
```

### Structure of each unit

Each unit folder must retain the structure supplied when the unit was released:

```
unit_01/
├── .vscode/
│   └── settings.json
├── src/
│   ├── lessons/
│   │   └── lesson Python files
│   └── exercises/
│       └── exercise Python files
├── tests/
│   └── supplied test files
├── .pytest.ini
└── README.md
```

The same structure should be present in every unit folder.

### Files you are permitted to edit

You should only edit the .py files contained within:

```src/lessons/```

and:

```src/exercises/```

Other than completing these Python files, each unit folder must remain untouched.

You must not:

- Rename, move or delete any supplied files or folders.
- Edit files in the tests folder.
- Edit .gitattributes, .gitignore, .pytest.ini or README.md.
- Edit the .vscode folder or its contents.
- Add your answers to a different location.
- Change the required folder structure.
- Changing the supplied structure or editing other files may prevent the automated tests from running correctly.

### Final checks

Before submitting, check that:

- The parent folder is named using your student number followed by _units_submission.
- Every unit retains its original folder structure.
- You have edited only the .py files in src/lessons and src/exercises.
- The supplied tests and configuration files remain unchanged.
- Your completed work has been committed and pushed to your GitHub repository.
- Your submitted ZIP contains the required parent folder and is not enclosed within unnecessary additional folders.