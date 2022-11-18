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

                <header class="w3-container w3-teal w3-center">
                    <h1>Receptář drinků</h1>
                </header>

                <nav class="w3-bar w3-large w3-border-bottom w3-border-teal">
                    <a class="w3-bar-item w3-button w3-hover-none w3-text-grey w3-hover-text-teal w3-right w3-border-left" href="menu.xml">Zobraz recepty</a>
                    <a class="w3-bar-item w3-button w3-hover-none w3-text-grey w3-hover-text-teal w3-right w3-border-left" href="#">Zašli recept</a>
                </nav>

                <aside class="w3-sidebar w3-bar-block w3-border-right w3-border-teal" style="width:20%">
                    <ul> 
                        <xsl:for-each select="menu/recept">
                            <xsl:sort select="informace/název"/>
                            <li class="w3-bar-item w3-button w3-hover-none w3-text-grey w3-hover-text-teal">
                                <a style="text-decoration: none">
                                    <xsl:attribute name="href">
                                        <xsl:value-of select="concat('#article',position())"/>
                                    </xsl:attribute>
                                    <xsl:value-of select="informace/název" />
                                </a>
                            </li>
                        </xsl:for-each>
                    </ul>
                </aside>

                <main style="margin-left:25%">
                    <section>
                        <ul>
                            <xsl:for-each select="menu/recept">
                                <xsl:sort select="informace/název"/>
                                <li class="w3-ul w3-border w3-margin-bottom">

                                    <article class="w3-card-4 w3-bottombar w3-border-teal w3-padding-16">                                        
                                        <xsl:attribute name="id">
                                                <xsl:value-of select="concat('article',position())"/>
                                        </xsl:attribute>
                                        <header class="w3-container">
                                            <h2 class="w3-container w3-serif w3-text-teal">
                                                <xsl:value-of select="informace/název"/>
                                            </h2>
                                            <xsl:apply-templates select="informace"/>
                                        </header>
                                        <section class="w3-container">
                                            <xsl:apply-templates select="ingredience"/>
                                            <xsl:apply-templates select="postup"/>
                                        </section>
                                        <footer class="w3-container w3-text-grey">Autor: <xsl:value-of select="@autor_článku"/></footer>
                                    </article>

                                </li>
                            </xsl:for-each>
                        </ul>
                    </section>
                </main>

            </body>
        </html>
    </xsl:template>

    <xsl:template match = "informace">
        <table class="w3-table w3-tiny w3-bordered">
            <tr>
                <td>Název:</td>
                <td><xsl:value-of select="název" /></td>
            </tr>
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

    <xsl:template match = "postup">
        <h3 class="w3-opacity w3-large w3-margin-top">Postup:</h3>
        <p>
            <xsl:value-of select="." />
        </p>
    </xsl:template>

    
</xsl:transform>