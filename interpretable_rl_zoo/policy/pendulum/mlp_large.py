def play(x):
    h_layer_0_0 = (
        0.12145109969286226 * x[0]
        + -0.5356737723143788 * x[1]
        + 0.19244922998681133 * x[2]
        + 0.7268188904713625
    )
    h_layer_0_0 = max(0.0, h_layer_0_0)
    h_layer_0_1 = (
        0.4026031949776604 * x[0]
        + 0.5360727153129957 * x[1]
        + -0.07099345105115844 * x[2]
        + 0.45512044297944587
    )
    h_layer_0_1 = max(0.0, h_layer_0_1)
    h_layer_0_2 = (
        0.7614984168688947 * x[0]
        + 0.5263011364941643 * x[1]
        + 0.27652729387140723 * x[2]
        + -0.6338376005144699
    )
    h_layer_0_2 = max(0.0, h_layer_0_2)
    h_layer_0_3 = (
        0.8225273850632357 * x[0]
        + 1.323445931321559 * x[1]
        + 0.5885162634118958 * x[2]
        + -0.6983230299259894
    )
    h_layer_0_3 = max(0.0, h_layer_0_3)
    h_layer_0_4 = (
        -0.20181018784113886 * x[0]
        + -0.4770335695193905 * x[1]
        + 0.37052880983463554 * x[2]
        + -0.3673161474962584
    )
    h_layer_0_4 = max(0.0, h_layer_0_4)
    h_layer_0_5 = (
        0.7714484475358475 * x[0]
        + 0.20439532476774455 * x[1]
        + 0.38734437308225783 * x[2]
        + 0.049945710314511074
    )
    h_layer_0_5 = max(0.0, h_layer_0_5)
    h_layer_0_6 = (
        -1.3352689833016116 * x[0]
        + 0.1948885494568629 * x[1]
        + -0.8914906015354781 * x[2]
        + 0.09628490531474158
    )
    h_layer_0_6 = max(0.0, h_layer_0_6)
    h_layer_0_7 = (
        0.048037507176516295 * x[0]
        + -1.4793779948670254 * x[1]
        + -0.3031724044303619 * x[2]
        + -0.005527063487821579
    )
    h_layer_0_7 = max(0.0, h_layer_0_7)
    h_layer_0_8 = (
        0.19528806108219737 * x[0]
        + 0.933655022057254 * x[1]
        + -0.14912891030942427 * x[2]
        + -0.06704096378395487
    )
    h_layer_0_8 = max(0.0, h_layer_0_8)
    h_layer_0_9 = (
        -1.0641102147518002 * x[0]
        + -0.3386567798306583 * x[1]
        + 0.15286411149672458 * x[2]
        + 0.7218869894581632
    )
    h_layer_0_9 = max(0.0, h_layer_0_9)
    h_layer_0_10 = (
        -0.8779838556806076 * x[0]
        + 0.37102651890234245 * x[1]
        + -0.4152254295188948 * x[2]
        + -0.5983575497551062
    )
    h_layer_0_10 = max(0.0, h_layer_0_10)
    h_layer_0_11 = (
        0.6845960334854131 * x[0]
        + -0.5106046415605111 * x[1]
        + -0.2648533270145125 * x[2]
        + -0.6979995919260447
    )
    h_layer_0_11 = max(0.0, h_layer_0_11)
    h_layer_0_12 = (
        -0.714360450489163 * x[0]
        + 0.845973138914767 * x[1]
        + -0.5012191429436441 * x[2]
        + -0.4382249915651351
    )
    h_layer_0_12 = max(0.0, h_layer_0_12)
    h_layer_0_13 = (
        0.6718996506182514 * x[0]
        + -0.823831525163045 * x[1]
        + -0.4491176220202228 * x[2]
        + -0.56506058853271
    )
    h_layer_0_13 = max(0.0, h_layer_0_13)
    h_layer_0_14 = (
        -0.6288470185426672 * x[0]
        + 0.6093166341885151 * x[1]
        + 0.1342259890462307 * x[2]
        + 0.7363193117931633
    )
    h_layer_0_14 = max(0.0, h_layer_0_14)
    h_layer_0_15 = (
        1.1301659655352871 * x[0]
        + 0.6510058640960726 * x[1]
        + 0.1868133845159822 * x[2]
        + 0.044456448927471165
    )
    h_layer_0_15 = max(0.0, h_layer_0_15)

    h_layer_1_0 = (
        0.7825524001863493 * h_layer_0_0
        + 0.24179097633707006 * h_layer_0_1
        + -0.5863571286537655 * h_layer_0_2
        + -0.07779520897032545 * h_layer_0_3
        + 0.4845489056224745 * h_layer_0_4
        + -0.05634504654475388 * h_layer_0_5
        + -0.5576016303582104 * h_layer_0_6
        + 0.1433967262438052 * h_layer_0_7
        + -0.531411740120219 * h_layer_0_8
        + 0.25335607208955774 * h_layer_0_9
        + -0.6965269574959904 * h_layer_0_10
        + 2.1110412006224437 * h_layer_0_11
        + -0.09218558508528925 * h_layer_0_12
        + -0.056177551759802165 * h_layer_0_13
        + 0.35955943304250726 * h_layer_0_14
        + 0.14317359055143966 * h_layer_0_15
        + 0.1322530797302272
    )
    h_layer_1_0 = max(0.0, h_layer_1_0)
    h_layer_1_1 = (
        -0.2946743154253592 * h_layer_0_0
        + 0.44905768497771553 * h_layer_0_1
        + 0.5516583155200359 * h_layer_0_2
        + -0.6302639928564109 * h_layer_0_3
        + -0.0537968078674442 * h_layer_0_4
        + -0.36196283150283703 * h_layer_0_5
        + -0.3639008597940056 * h_layer_0_6
        + 0.13094914852061207 * h_layer_0_7
        + 0.18778295689289368 * h_layer_0_8
        + 0.3717156121210477 * h_layer_0_9
        + 0.26494152807551946 * h_layer_0_10
        + 0.1447160890483911 * h_layer_0_11
        + 0.22812857392449234 * h_layer_0_12
        + 0.4529039151167004 * h_layer_0_13
        + 0.3610564843090785 * h_layer_0_14
        + 0.11294360965107775 * h_layer_0_15
        + 0.5038537558106629
    )
    h_layer_1_1 = max(0.0, h_layer_1_1)
    h_layer_1_2 = (
        -0.08246283268205588 * h_layer_0_0
        + 0.25086055803317026 * h_layer_0_1
        + 0.17337876221998239 * h_layer_0_2
        + 0.4218324348022154 * h_layer_0_3
        + 0.1491625825748254 * h_layer_0_4
        + -0.11182470748102936 * h_layer_0_5
        + 0.413611648249533 * h_layer_0_6
        + 0.20291934478865797 * h_layer_0_7
        + -0.026436150452079893 * h_layer_0_8
        + -0.013413149688076494 * h_layer_0_9
        + -0.1787173035272978 * h_layer_0_10
        + -0.7376046990429669 * h_layer_0_11
        + 0.1503851158947994 * h_layer_0_12
        + 0.04959014207773976 * h_layer_0_13
        + 0.012988458332868264 * h_layer_0_14
        + 0.5276854495707043 * h_layer_0_15
        + 0.13779379854404133
    )
    h_layer_1_2 = max(0.0, h_layer_1_2)
    h_layer_1_3 = (
        -0.23123630985988497 * h_layer_0_0
        + 0.08636358334351094 * h_layer_0_1
        + -0.16567889113301484 * h_layer_0_2
        + 0.4750942378235001 * h_layer_0_3
        + -0.26402323157464436 * h_layer_0_4
        + 0.4528687550713824 * h_layer_0_5
        + 0.5192388075519488 * h_layer_0_6
        + 0.10887958640312012 * h_layer_0_7
        + 0.18163118383798293 * h_layer_0_8
        + -0.08665411364077322 * h_layer_0_9
        + 0.4262386422402336 * h_layer_0_10
        + -1.3851875411812555 * h_layer_0_11
        + -0.08469054104116669 * h_layer_0_12
        + -0.6230647370346539 * h_layer_0_13
        + -0.0021167925915300473 * h_layer_0_14
        + 0.3970780409932516 * h_layer_0_15
        + -0.417875432011124
    )
    h_layer_1_3 = max(0.0, h_layer_1_3)
    h_layer_1_4 = (
        0.41984138608412347 * h_layer_0_0
        + -0.17542827409822737 * h_layer_0_1
        + -1.5679662581958789 * h_layer_0_2
        + -0.7365906571388733 * h_layer_0_3
        + -0.5176152359865704 * h_layer_0_4
        + 0.3339964741243064 * h_layer_0_5
        + 0.10611097044340022 * h_layer_0_6
        + -0.4548734839934853 * h_layer_0_7
        + 0.22875486593893227 * h_layer_0_8
        + -0.40826080608958765 * h_layer_0_9
        + 0.7821560647558979 * h_layer_0_10
        + 1.1860323949348834 * h_layer_0_11
        + 0.7520088072664994 * h_layer_0_12
        + -0.48713687749471873 * h_layer_0_13
        + 0.7761847594571687 * h_layer_0_14
        + 0.0007622512067326873 * h_layer_0_15
        + -0.23213912003082932
    )
    h_layer_1_4 = max(0.0, h_layer_1_4)
    h_layer_1_5 = (
        -0.41846748755621666 * h_layer_0_0
        + 0.1916041481499958 * h_layer_0_1
        + -0.09781783127793564 * h_layer_0_2
        + -0.3962682540195823 * h_layer_0_3
        + -0.15609482477930683 * h_layer_0_4
        + -0.13755268424359438 * h_layer_0_5
        + 0.22694021016562183 * h_layer_0_6
        + -0.16640662549086885 * h_layer_0_7
        + -0.25130191737898283 * h_layer_0_8
        + 0.42829614957687645 * h_layer_0_9
        + 0.513038648732766 * h_layer_0_10
        + -0.518728676468479 * h_layer_0_11
        + -0.2301732326074884 * h_layer_0_12
        + -0.600938387410329 * h_layer_0_13
        + 0.33233436713024805 * h_layer_0_14
        + 0.3819272844723492 * h_layer_0_15
        + 0.3683823161761543
    )
    h_layer_1_5 = max(0.0, h_layer_1_5)
    h_layer_1_6 = (
        0.32481379185601067 * h_layer_0_0
        + 0.11700585213998316 * h_layer_0_1
        + -4.086744138512318 * h_layer_0_2
        + -0.5018282713011791 * h_layer_0_3
        + -0.5386386607670011 * h_layer_0_4
        + -0.02714560952671581 * h_layer_0_5
        + -0.5097427783864957 * h_layer_0_6
        + -0.2740048660215447 * h_layer_0_7
        + -1.6992604715606658 * h_layer_0_8
        + 0.8090996599991445 * h_layer_0_9
        + -2.271686282646531 * h_layer_0_10
        + 0.4386558779889609 * h_layer_0_11
        + -1.204381318231583 * h_layer_0_12
        + 0.22341521968114683 * h_layer_0_13
        + 0.3787776776881721 * h_layer_0_14
        + -0.5851789124411856 * h_layer_0_15
        + 0.3387451577244716
    )
    h_layer_1_6 = max(0.0, h_layer_1_6)
    h_layer_1_7 = (
        -0.01673037847573866 * h_layer_0_0
        + 0.3953870346877406 * h_layer_0_1
        + 0.4410643659967352 * h_layer_0_2
        + 0.3472009547306015 * h_layer_0_3
        + -0.08024350257184706 * h_layer_0_4
        + 0.6153516591540176 * h_layer_0_5
        + 0.39548906778875553 * h_layer_0_6
        + -1.1337366343094488 * h_layer_0_7
        + 0.5076535083924887 * h_layer_0_8
        + -0.30856450044841677 * h_layer_0_9
        + 0.34747922941255294 * h_layer_0_10
        + -1.2441180483216443 * h_layer_0_11
        + -0.20352866576575326 * h_layer_0_12
        + -0.26769322714395305 * h_layer_0_13
        + -0.15171952327684285 * h_layer_0_14
        + 0.041449158279397526 * h_layer_0_15
        + -0.10497505525890984
    )
    h_layer_1_7 = max(0.0, h_layer_1_7)
    h_layer_1_8 = (
        -0.5026594251385783 * h_layer_0_0
        + 0.31755838100194494 * h_layer_0_1
        + 0.07539499684344092 * h_layer_0_2
        + 0.3744871424208432 * h_layer_0_3
        + -0.39174015646510646 * h_layer_0_4
        + 0.2573060429380652 * h_layer_0_5
        + 0.11651611826392329 * h_layer_0_6
        + 0.09526744719985884 * h_layer_0_7
        + -0.24394652614465154 * h_layer_0_8
        + 0.1291106957805707 * h_layer_0_9
        + 0.15683465642134442 * h_layer_0_10
        + -1.143945387737882 * h_layer_0_11
        + 0.40403906418319036 * h_layer_0_12
        + -0.23158103142173175 * h_layer_0_13
        + 0.0642358099305664 * h_layer_0_14
        + 0.07438050357342262 * h_layer_0_15
        + 0.048936633428167925
    )
    h_layer_1_8 = max(0.0, h_layer_1_8)
    h_layer_1_9 = (
        -0.016707017124824718 * h_layer_0_0
        + -0.11986812773270364 * h_layer_0_1
        + 0.4873605020151712 * h_layer_0_2
        + 0.03318428992712829 * h_layer_0_3
        + -0.11060940223348095 * h_layer_0_4
        + -0.1255691975228237 * h_layer_0_5
        + -0.024344529560025998 * h_layer_0_6
        + -1.359398881071608 * h_layer_0_7
        + -0.00563766981087143 * h_layer_0_8
        + 0.30761562460603115 * h_layer_0_9
        + -1.6390077998365518 * h_layer_0_10
        + -1.294728204811512 * h_layer_0_11
        + 0.16588780596210514 * h_layer_0_12
        + 0.06930690823617269 * h_layer_0_13
        + -0.39070055027761513 * h_layer_0_14
        + 0.5267897688711142 * h_layer_0_15
        + 0.404291465381856
    )
    h_layer_1_9 = max(0.0, h_layer_1_9)
    h_layer_1_10 = (
        -0.4309160604385335 * h_layer_0_0
        + 0.4401617879102306 * h_layer_0_1
        + 0.5358772292411282 * h_layer_0_2
        + 0.6050125412349147 * h_layer_0_3
        + -0.14015747312253696 * h_layer_0_4
        + 0.07528219218662369 * h_layer_0_5
        + 0.5258012902112158 * h_layer_0_6
        + 0.37357080020152705 * h_layer_0_7
        + -0.033658127335338656 * h_layer_0_8
        + 0.08322306157865003 * h_layer_0_9
        + -0.7838357276480721 * h_layer_0_10
        + -2.410637197064131 * h_layer_0_11
        + -1.8076557401897893 * h_layer_0_12
        + 0.11565710444501275 * h_layer_0_13
        + 0.29642039989109387 * h_layer_0_14
        + -0.13588836389493544 * h_layer_0_15
        + -0.35249347105585116
    )
    h_layer_1_10 = max(0.0, h_layer_1_10)
    h_layer_1_11 = (
        0.34918289220860665 * h_layer_0_0
        + 0.3195789516430818 * h_layer_0_1
        + -0.21670455364347066 * h_layer_0_2
        + 0.509097899559148 * h_layer_0_3
        + -0.38032513937319123 * h_layer_0_4
        + -0.2689101567748771 * h_layer_0_5
        + -0.17216406829114778 * h_layer_0_6
        + 0.33630585482437003 * h_layer_0_7
        + 0.38562260285606786 * h_layer_0_8
        + 0.16450236890682954 * h_layer_0_9
        + -0.7619378881763196 * h_layer_0_10
        + 0.18936193385275238 * h_layer_0_11
        + -0.42828627051112517 * h_layer_0_12
        + 0.659951502484478 * h_layer_0_13
        + -0.3432738668769473 * h_layer_0_14
        + 0.6538582269900092 * h_layer_0_15
        + 0.015620746808125684
    )
    h_layer_1_11 = max(0.0, h_layer_1_11)
    h_layer_1_12 = (
        0.22827825763536383 * h_layer_0_0
        + 0.5849540715167949 * h_layer_0_1
        + 0.009533329202606368 * h_layer_0_2
        + -0.2591021964196522 * h_layer_0_3
        + -0.35353594343556577 * h_layer_0_4
        + -0.4636831557130262 * h_layer_0_5
        + -0.3846241554098023 * h_layer_0_6
        + 0.3449576577136865 * h_layer_0_7
        + -0.06615118621613274 * h_layer_0_8
        + 0.09114203217355833 * h_layer_0_9
        + 0.22385076985894015 * h_layer_0_10
        + 0.21760617779151933 * h_layer_0_11
        + -0.054310719647598246 * h_layer_0_12
        + 0.5294791935840043 * h_layer_0_13
        + 0.5562424543232939 * h_layer_0_14
        + -0.26500357774482824 * h_layer_0_15
        + 0.25676735001237105
    )
    h_layer_1_12 = max(0.0, h_layer_1_12)
    h_layer_1_13 = (
        0.055122014570394666 * h_layer_0_0
        + 0.27613385846056987 * h_layer_0_1
        + -1.3082581523260155 * h_layer_0_2
        + -0.7966885823017654 * h_layer_0_3
        + 0.7154869180355075 * h_layer_0_4
        + 0.27351687016810233 * h_layer_0_5
        + 0.12829519411060442 * h_layer_0_6
        + -0.07007565049705688 * h_layer_0_7
        + 0.05638175496778207 * h_layer_0_8
        + -0.26550502495419714 * h_layer_0_9
        + 0.34249174978821184 * h_layer_0_10
        + 0.5440259851845101 * h_layer_0_11
        + -0.5115608823137169 * h_layer_0_12
        + 0.6195858975230228 * h_layer_0_13
        + -1.6935140839851301 * h_layer_0_14
        + 0.2260391205703413 * h_layer_0_15
        + -0.02082001580302241
    )
    h_layer_1_13 = max(0.0, h_layer_1_13)
    h_layer_1_14 = (
        -0.38595634600763584 * h_layer_0_0
        + -0.26768322266447986 * h_layer_0_1
        + 0.3975772761409504 * h_layer_0_2
        + -0.14959694100336257 * h_layer_0_3
        + 0.4318096546636654 * h_layer_0_4
        + 0.39832321698401646 * h_layer_0_5
        + 0.28396203859085406 * h_layer_0_6
        + -0.2986568967260086 * h_layer_0_7
        + -0.319397396767385 * h_layer_0_8
        + 0.5810976504542885 * h_layer_0_9
        + 0.5988466815878883 * h_layer_0_10
        + -0.8982192419520736 * h_layer_0_11
        + 0.20893890431975745 * h_layer_0_12
        + -0.44883726600295015 * h_layer_0_13
        + 0.5307522932855988 * h_layer_0_14
        + 0.6800511465707954 * h_layer_0_15
        + -0.034665835001177814
    )
    h_layer_1_14 = max(0.0, h_layer_1_14)
    h_layer_1_15 = (
        0.026432752818696333 * h_layer_0_0
        + 0.12306293155001076 * h_layer_0_1
        + 0.9268273345360092 * h_layer_0_2
        + 0.2843016440651192 * h_layer_0_3
        + -0.10452785959070442 * h_layer_0_4
        + 0.6494494954325497 * h_layer_0_5
        + -0.16324531282021268 * h_layer_0_6
        + -1.4454898960915192 * h_layer_0_7
        + 0.5442887877979394 * h_layer_0_8
        + -0.3285669694540251 * h_layer_0_9
        + 0.29721372593228174 * h_layer_0_10
        + 0.48608889987954984 * h_layer_0_11
        + 0.21499135150817233 * h_layer_0_12
        + 0.1885059462898671 * h_layer_0_13
        + -0.13038950959130474 * h_layer_0_14
        + 0.22127411221041754 * h_layer_0_15
        + -0.10324758943401732
    )
    h_layer_1_15 = max(0.0, h_layer_1_15)

    h_layer_2_0 = (
        -0.33267070541207416 * h_layer_1_0
        + -0.6776836003484137 * h_layer_1_1
        + 0.18499679067839342 * h_layer_1_2
        + -0.7146409350542954 * h_layer_1_3
        + 1.0164237624917285 * h_layer_1_4
        + -0.48379376689057296 * h_layer_1_5
        + 2.2270846039335583 * h_layer_1_6
        + -0.6707927699725236 * h_layer_1_7
        + -0.17791667933073713 * h_layer_1_8
        + -0.6299152385325647 * h_layer_1_9
        + 0.8380184269624951 * h_layer_1_10
        + 0.9022165108138157 * h_layer_1_11
        + -0.834213585610687 * h_layer_1_12
        + 1.4587570312631573 * h_layer_1_13
        + -0.4271748203722824 * h_layer_1_14
        + -0.45008000243169455 * h_layer_1_15
        + 0.4056915240530739
    )
    y_0 = h_layer_2_0

    return [y_0]


metadata =  {"algorithm": "PPO", "env_name": "Pendulum-v1"}
