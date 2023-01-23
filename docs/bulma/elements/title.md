Title and Subtitle
===

Simple headings provided by Markdown.
---

Simple **headings** to add depth to your page.

<!-- This line would be removed when setext titles will support links in their content-->
Look at [Bulma](https://bulma.io/documentation/elements/title) for more examples.

Note: not every style class could be supported and generated from a Markdown file. This plugin actually doesn't support them, since my time has to be spent on the full support of every Markdown tag before the full support of Bulma.

There are **2 types** of headings. I use the [setext headings](https://spec.commonmark.org/0.30/#setext-heading) notation to give support of them.

| Element | Code | Result | |
| --- | --- | --- | --- |
| <code>Title<br />===</code> | `<h1 class="title is-1" id="title">Title</h1>` | <h1 class="title is-1" id="title">Title</h1> | |
| <code>Subtitle<br />---</code> | `<h2 class="subtitle is-2" id="subtitle">Subtitle</h2>` | <h2 class="subtitle is-2" id="subtitle">Subtitle</h2> | |

The Commonmark spec doesn't support any other type of a setext heading underline chars.

Since the last spec support only a first size title and a second size subtitle for those elements, I don't support nativly in this plugin any other size for each element (for now). You have to inject HTML directly in your md code to use them:

    <h3 class="title is-3">Injected Title</h3>
    <h4 class="subtitle is-4">Injected Subtitle</h4>

---

My implementation doesn't support any other Markdown element in the title and subtitle. You can't put emphasis or set a link on it because the regex I made substitute the md tag for title and subtitle and inject an HTML code in the md page, so the mkdocs successive step of HTML output doesn't process it. I'll plan to fix it in a next release, or any contribution about it is welcome.

## [Sizes](https://bulma.io/documentation/elements/title/#sizes)

I use the [ATX headings](https://spec.commonmark.org/0.30/#atx-heading) notation to give support to different sizes of titles:

There are 6 sizes available:

| Markdown | Bulma eq | Result |
| --- | --- | --- |
| `# Title 1` | `<h1 class="title is-1">Title 1</h1>` | <h1 class="title is-1">Title 1</h1> |
| `## Title 2` | `<h2 class="title is-2">Title 2</h2>` | <h2 class="title is-2">Title 2</h2> |
| `### Title 3` | `<h3 class="title is-3">Title 3</h3>` | <h3 class="title is-3">Title 3</h3> |
| `#### Title 4` | `<h4 class="title is-4">Title 4</h4>` | <h4 class="title is-4">Title 4</h4> |
| `##### Title 5` | `<h5 class="title is-5">Title 5</h5>` | <h5 class="title is-5">Title 5</h5> |
| `###### Title 6` | `<h6 class="title is-6">Title 6</h6>` | <h6 class="title is-6">Title 6</h6> |

## PEPs (Plugin Enhancement Proposals)

For those elements there's a Plugin Enhancement Proposal at [issue #9](https://github.com/Daniele-Tentoni/mkdocs-bulma-classes-plugin/issues/9).
