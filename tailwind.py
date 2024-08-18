from fasthtml.common import Script, Style

plugins = "forms,typography,aspect-ratio,container-queries"
tailwind_link = (
    Script(src=f"https://cdn.tailwindcss.com?plugins={plugins}"),
    Style(
        """
@layer utilities {
      .content-auto {
        content-visibility: auto;
      }
    }""",
        type="text/tailwindcss",
    ),
)
