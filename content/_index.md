---
title: 'Home'
date: 2023-10-24
type: landing
design:
  # Default section spacing
  spacing: "1rem"
sections:
  - block: resume-biography
    id: biography
    content:
      # The user's folder name in content/authors/
      username: admin
    design:
      biography:
        style: 'text-align: justify; font-size: 0.8em;'
  - block: resume-experience
    id: experiences
    content:
      # The user's folder name in `content/authors/`
      username: admin
    design:
      # Hugo date format
      date_format: 'January 2006'
      # Education or Experience section first?
      is_education_first: true
  - block: collection
    id: publications
    content:
      title: Publications
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      # spacing:
      #   padding: ['3rem', 0, '6rem', 0]
      view: citation
  # - block: collection
  #   content:
  #     filters:
  #       folders:
  #         - blog
  #   design:
  #     spacing:
  #       padding: ['3rem', 0, '6rem', 0]
---
