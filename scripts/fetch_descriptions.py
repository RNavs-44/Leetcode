#!/usr/bin/env python3
"""
Script to fetch LeetCode problem descriptions and update README files.
This script can be run to systematically update all READMEs with problem descriptions.
"""

import json
import os
import re
import urllib.request
import urllib.error
from html import unescape

# Get the script directory and parent directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)

# Load problems info
with open(os.path.join(SCRIPT_DIR, 'problems_info.json'), 'r') as f:
    problems_info = json.load(f)

def format_problem_name(name):
    """Convert CamelCase to Title Case"""
    name = re.sub(r'(?<!^)(?=[A-Z])', ' ', name)
    return name

def get_problem_slug(name):
    """Convert CamelCase to kebab-case for LeetCode URLs"""
    slug = re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()
    slug = slug.replace('i-i', 'ii').replace('i-i-i', 'iii')
    slug = slug.replace('2-d', '2d').replace('a2-d', '2d')
    slug = slug.replace('l-r-u', 'lru')
    return slug

def has_description(readme_path):
    """Check if README already has a description (not just template)"""
    full_path = os.path.join(PARENT_DIR, readme_path) if not os.path.isabs(readme_path) else readme_path
    try:
        with open(full_path, 'r') as f:
            content = f.read()
            if '*Visit the LeetCode link' in content or '*Description will be fetched' in content:
                return False
            if '### Description' in content and len(content.split('### Description')[1].split('###')[0].strip()) > 50:
                return True
    except:
        pass
    return False

def create_readme_template(problem_name, leetcode_num, problem_slug):
    """Create a README template with LeetCode link"""
    return f"""# {problem_name}

## LeetCode Problem {leetcode_num}

**Problem Link:** https://leetcode.com/problems/{problem_slug}/

### Description

*Visit the LeetCode link above to view the full problem description, examples, and constraints.*

### Examples

*See LeetCode website for examples*

### Constraints

*See LeetCode website for constraints*

### Approach

*Your solution approach here*

### Complexity

- Time Complexity: 
- Space Complexity: 
"""

def update_readme_with_description(readme_path, problem_name, leetcode_num, problem_slug, description, examples="", constraints=""):
    """Update README with fetched description"""
    full_path = os.path.join(PARENT_DIR, readme_path) if not os.path.isabs(readme_path) else readme_path
    examples_section = f"\n{examples}\n" if examples else "\n*See LeetCode website for examples*\n"
    constraints_section = f"\n{constraints}\n" if constraints else "\n*See LeetCode website for constraints*\n"
    
    content = f"""# {problem_name}

## LeetCode Problem {leetcode_num}

**Problem Link:** https://leetcode.com/problems/{problem_slug}/

### Description

{description}

### Examples
{examples_section}
### Constraints
{constraints_section}
### Approach

*Your solution approach here*

### Complexity

- Time Complexity: 
- Space Complexity: 
"""
    
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)

def main():
    """Main function to update all READMEs"""
    updated = 0
    skipped = 0
    needs_update = 0
    
    print(f"Processing {len(problems_info)} problems...\n")
    
    for i, problem in enumerate(problems_info, 1):
        problem_name = format_problem_name(problem['name'])
        leetcode_num = problem['leetcode_num']
        readme_path = os.path.join(PARENT_DIR, problem['readme_path'])
        problem_slug = get_problem_slug(problem['name'])
        
        if has_description(problem['readme_path']):
            skipped += 1
            continue
        
        needs_update += 1
        # For now, create template - descriptions should be added via web search
        content = create_readme_template(problem_name, leetcode_num, problem_slug)
        
        os.makedirs(os.path.dirname(readme_path), exist_ok=True)
        with open(readme_path, 'w') as f:
            f.write(content)
        
        if i % 10 == 0:
            print(f"Processed {i}/{len(problems_info)} problems...")
    
    print(f"\n✓ Processed {len(problems_info)} problems")
    print(f"  - {skipped} already have descriptions")
    print(f"  - {needs_update} need descriptions (templates created)")
    print("\nNote: Use web search to fetch descriptions for remaining problems,")
    print("      then update READMEs using the update_readme_with_description function.")

if __name__ == "__main__":
    main()
