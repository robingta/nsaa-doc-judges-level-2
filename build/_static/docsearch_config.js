docsearch({
  container: "#docsearch",
  appId: "#Your Algolia DocSearch app ID",
  apiKey: "#Your Search API key",
  indexName: "#Your index name",
  placeholder: "Search these docs",
  getMissingResultsUrl({ query }) {
    return `https://github.com/kai687/sphinxawesome-theme/issues/new?title=${query}`
  }
});