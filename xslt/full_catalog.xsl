<xsl:stylesheet version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<body>
<h1>Full Media Catalog</h1>
<ul>
<xsl:for-each select="catalog/media">
<li>
<xsl:value-of select="title"/> - 
<xsl:value-of select="year"/>
</li>
</xsl:for-each>
</ul>
</body>
</html>
</xsl:template>

</xsl:stylesheet>
