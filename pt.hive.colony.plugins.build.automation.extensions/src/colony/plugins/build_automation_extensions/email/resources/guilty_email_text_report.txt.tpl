The build is broken and you're a suspect, if you don't want to fix it, at least make sure you're innocent.
build: ${out_none value=build_automation.build /}
artifacts: url ${out_none value=build_automation.repository_url /}
log url: ${out_none value=build_automation.repository_url /}/${out_none value=build_automation.log_file_path /}
