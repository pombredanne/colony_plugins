${foreach item=package from=packages}${out_none prefix="Package: " value=package.name /}
${out_none prefix="Version: " value=package.version /}
${out_none prefix="Architecture: " value=package.architecture /}
${out_none prefix="Essential: " value=package.essential /}
${out_none prefix="Maintainer: " value=package.maintainer /}
${out_none prefix="Installed-Size: " value=package.installed_size /}
${out_none prefix="Pre-Depends: " value=package.pre_dependencies /}
${out_none prefix="Depends: " value=package.dependencies /}
${out_none prefix="Replaces: " value=package.replaces /}
${out_none prefix="Provides: " value=package.provides /}
${out_none prefix="Filename: " value=package.filename /}
${out_none prefix="Size: " value=package.size /}
${out_none prefix="MD5sum: " value=package.md5 /}
${out_none prefix="SHA1: " value=package.sha1 /}
${out_none prefix="SHA256: " value=package.sha256 /}
${out_none prefix="Section: " value=package.section /}
${out_none prefix="Priority: " value=package.priority /}
${out_none prefix="Description: " value=package.description /}

${/foreach}
