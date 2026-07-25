from enkeksi import render_markdown

rendered = render_markdown("```sql\nSELECT 42 AS answer;\n```\n")
assert "42" in rendered
