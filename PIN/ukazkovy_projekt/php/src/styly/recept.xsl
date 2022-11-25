<?xml version="1.0" encoding="UTF-8"?>
<xsl:transform version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html"/>
    <xsl:template match="/">
        <html>
            <head>
                <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
                <meta name="viewport" content="width=device-width,initial-scale=1"></meta>
                <title>Drinky</title>
            </head>
            <body>
                <main>
                    <xsl:apply-templates />
                </main>
            </body>
        </html>
    </xsl:template>

    <!-- Výpis informací o drinku do tabulky -->
    <xsl:template match = "informace">
        <header class="w3-container w3-teal w3-center">
            <h1 class="w3-opacity w3-large w3-margin-top">
                <xsl:value-of select="název" />
            </h1>
        </header> 
        <table class="w3-table w3-tiny w3-bordered">
            <tr>
                <td>Doba přípravy:</td>
                <td><xsl:value-of select="doba_přípravy" /> minut</td>
            </tr>
            <tr>
                <xsl:choose>
                    <xsl:when test="země_původu">
                        <td>Země původu:</td><td><xsl:value-of select="země_původu" /></td>
                    </xsl:when>
                    <xsl:otherwise>
                        <td>Země původu:</td><td>Neznámá</td>
                    </xsl:otherwise>
                </xsl:choose>
            </tr>
            <tr>
                <xsl:if test="node()">
                    <td>Obtížnost:</td><td><xsl:value-of select ="name(obtížnost/*[1])"/></td>
                </xsl:if>
            </tr>
        </table>
    </xsl:template>

    <!-- výpis ingrediencí do seznamku -->
    <xsl:template match = "ingredience">
        <h3 class="w3-opacity w3-large w3-margin-top">Ingredience:</h3>
        <ul class="w3-ul w3-card-4" style="width:50%">
            <xsl:for-each select="položka">
                <xsl:choose>
                    <xsl:when test="@typ='základ'">
                        <li class="w3-pale-red">
                            <xsl:value-of select="." />
                            <span class="w3-cursive w3-margin">(<xsl:value-of select="@typ"/>)</span>          
                        </li>
                    </xsl:when>
                    <xsl:when test="@typ='dochucovadlo'">
                        <li class="w3-sand">
                            <xsl:value-of select="." />
                            <span class="w3-cursive w3-margin">(<xsl:value-of select="@typ"/>)</span>          
                        </li>
                    </xsl:when>
                    <xsl:when test="@typ='dekorace'">
                        <li class="w3-pale-blue">
                            <xsl:value-of select="." />
                            <span class="w3-cursive w3-margin">(<xsl:value-of select="@typ"/>)</span>          
                        </li>
                    </xsl:when>
                    <xsl:otherwise>
                        <li>
                            <xsl:value-of select="." />
                        </li>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:for-each>
        </ul>
    </xsl:template>

    <!-- výpis postupu receptu -->
    <xsl:template match = "postup">
        <h3 class="w3-opacity w3-large w3-margin-top">Postup:</h3>
        <p>
            <xsl:value-of select="." />
        </p>
    </xsl:template>

    
</xsl:transform>