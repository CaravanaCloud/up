#!/bin/sh

increment_version() {
  local version=$1
  local major=$(echo $version | cut -d. -f1)
  local minor=$(echo $version | cut -d. -f2)
  local patch=$(echo $version | cut -d. -f3)
  patch=$((patch+1))
  echo "$major.$minor.$patch"
}

for file in */pyproject.toml; do
    cp "$file" "$file.bak.$(date +%s)"
    new_version=$(cat "$file" | grep "^version" | cut -d= -f2 | tr -d ' "')
    new_version=$(increment_version $new_version)
    echo "Bumping $file to $new_version "
    sed -i "s/^version = .*/version = \"$new_version\"/" "$file" 
    sed -i "s/^up-ansible = .*/up-ansible = \"$new_version\"/" "$file"
    sed -i "s/^up-splat = .*/up-splat = \"$new_version\"/" "$file"
    sed -i "s/^up-lib = .*/up-lib = \"$new_version\"/" "$file"
    
done
