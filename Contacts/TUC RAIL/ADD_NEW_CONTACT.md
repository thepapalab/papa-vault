# Add a New Contact — Quick Form

Copy this template to create a new contact file:

```
---
name: [First Last]
role: [Job title]
company: TUC RAIL / Infrabel
email: [email@domain]
phone: [+32 X XXX XX XX]
team: [Department]
reports_to: [[Manager Name]]
direct_reports: []
projects: [[ProjectName]]
tags: [keyword1, keyword2]
---

## Role & Responsibility
[Brief description of what they do]

## Projects Involved
- **ProjectName** — [Role and scope]

## Work Style
- [How they prefer to communicate]
- [Decision speed]
- [Documentation needs]

## Notes
- [Relevant history or preferences]

## Last Contact
Date: [YYYY-MM-DD]
Context: [What was discussed]

## See Also
[[Related Contact]] | [[Related Project]]
```

**Steps:**
1. Copy the template above
2. Create a new file: `Contacts/[FirstName].md`
3. Fill in all frontmatter fields
4. Add narrative sections
5. Link to related contacts/projects using `[[WikiLink]]`
6. Update `_Index.md` to include the new person

**Quick Rules:**
- Use full names for filenames (`Contacts/François Lapy.md`)
- Link to people and projects using `[[Name]]` syntax — Obsidian auto-links them
- Keep emails in frontmatter (not plain text in body) for privacy
- Use `tags` field for searchable keywords
- Update "Last Contact" each time you interact

---

## Bulk Add Example

If you want to add missing people quickly (e.g., contractors, external partners), list them here and I can create skeleton files:

```
Name | Role | Company | Email
-----|------|---------|-------
```

Let me know who's missing.
