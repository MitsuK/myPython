curDir=`pwd`
echo ${curDir}
conf=${curDir}"/julius-conf/"
julius -C ${conf}main.jconf -C ${conf}am-gmm.jconf -module
