<div class="thumbnail-view">
    ${foreach item=directory_entry from=directory_entries}
    <div class="item ${out_none value=directory_entry.type xml_escape=True /}-large">
        <p class="name"><a href="${out_none value=directory_entry.name xml_escape=True /}">${out_none value=directory_entry.name xml_escape=True /}</a></p>
    </div>
    ${/foreach}
</div>
