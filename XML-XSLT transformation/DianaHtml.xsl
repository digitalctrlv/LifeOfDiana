<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0">

    <xsl:output method="html" encoding="UTF-8"/>

    <xsl:template match="/">
    <html>
      <head>
        <title>Diana: Her True Story - a sample</title>
        <link rel="stylesheet" href="style.css" type="text/css"/>
      </head>
      <body>
        <div class="page">
          <div class="box">
            <h1 class="title1">
                <span class="FirstLetter"><xsl:value-of select="substring(//tei:head[@type='main'], 1, 1)"/></span>
                <span class="characters"><xsl:value-of select="substring(//tei:head[@type='main'], 2, 6)"/></span>
                <span class="FirstLetter"><xsl:value-of select="substring(//tei:head[@type='main'], 8, 1)"/></span>
                <span class="characters"><xsl:value-of select="substring(//tei:head[@type='main'], 9, 11)"/></span>
                <span class="FirstLetter"><xsl:value-of select="substring(//tei:head[@type='main'], 20, 1)"/></span>
                <span class="characters"><xsl:value-of select="substring(//tei:head[@type='main'], 21, 4)"/></span>
            </h1>
            <h1 class="title2">
                <i><xsl:value-of select="//tei:head[@type='subtitle']"/></i>
            </h1>
            <hr/>
            <p class="note"><i><span class="firstLine"><xsl:value-of select="substring(/tei:TEI/tei:text/tei:front/tei:div[@type='intro']/tei:p[@type='note'], 1, 62)"/></span></i><br/>
            <i><span class="secondLine"><xsl:value-of select="substring(/tei:TEI/tei:text/tei:front/tei:div[@type='intro']/tei:p[@type='note'], 62, 78)"/></span></i><br/>
            <i><span class="thirdLine"><xsl:value-of select="substring(/tei:TEI/tei:text/tei:front/tei:div[@type='intro']/tei:p[@type='note'], 140, 76)"/></span></i><br/>
            <i><span class="fourthLine"><xsl:value-of select="substring(/tei:TEI/tei:text/tei:front/tei:div[@type='intro']/tei:p[@type='note'], 216, 41)"/></span></i></p>
            <h4><xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div/tei:h4"/></h4>
            <p><xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div/tei:p[1]"/></p>
            <p class="text"><xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div/tei:p[2]"/></p>
            <p class="text"><xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div/tei:p[3]"/></p>
            <p class="text"><xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div/tei:p[4]"/></p>
            <p class="text">We had so many changes of nannies. My brother and I, if we didn't like them we used to stick pins in their chair and</p>
          </div>
          <div class="pageNumber">[<xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div/tei:pb/@n"/>]</div>
        </div>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>