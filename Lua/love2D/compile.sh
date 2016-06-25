#!/usr/bin/env sh

project_dir='project'
cd "${project_dir}"
zip -r "../${project_dir}.love" *
