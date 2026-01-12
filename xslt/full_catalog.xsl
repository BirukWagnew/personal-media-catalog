<xsl:stylesheet version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<head>
<style>
table {
  border-collapse: collapse;
  width: 100%;
  font-family: Arial, sans-serif;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
th {
  background-color: #f2f2f2;
  font-weight: bold;
}
tr:nth-child(even) {
  background-color: #f9f9f9;
}
h1 {
  color: #333;
  text-align: center;
}
</style>
</head>
<body>
<h1>Full Media Catalog</h1>
<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Title</th>
      <th>Year</th>
      <th>Creator</th>
      <th>Extra Info</th>
    </tr>
  </thead>
  <tbody>
    <xsl:for-each select="catalog/media">
    <tr>
      <td><xsl:value-of select="type"/></td>
      <td><xsl:value-of select="title"/></td>
      <td><xsl:value-of select="year"/></td>
      <td><xsl:value-of select="creator"/></td>
      <td><xsl:value-of select="extra"/></td>
    </tr>
    </xsl:for-each>
  </tbody>
</table>
</body>
</html>
</xsl:template>

</xsl:stylesheet>
