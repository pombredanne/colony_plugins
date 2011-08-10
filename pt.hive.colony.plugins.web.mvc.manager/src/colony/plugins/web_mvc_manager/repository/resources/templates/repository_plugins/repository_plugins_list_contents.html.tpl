<div id="includes">
    <div class="javascript">repositories/resources/templates/js/repository_plugins/repository_plugins_list_contents.js</div>
</div>
<div id="meta-data">
    <div class="area">update</div>
    <div class="side-panel">side_panel/update</div>
</div>
<div id="contents">
    <h1>Update</h1>
    <h2>Repository Plugins - ${out_none value=repository.name xml_escape=True /}</h2>
    <div id="repository-plugins-table" class="search-table" provider_url="repositories/${out_none value=repository_index xml_escape=True /}/plugins_partial">
        <table class="table" cellspacing="0" cellpadding="0">
            <thead>
                <tr>
                    <th><span>Plugin ID</span><span class="order-down-inactive"></span></th>
                    <th width="75"><span>Operation</span><span class="order-down-inactive"></span></th>
                </tr>
            </thead>
            <tbody></tbody>
            <tfoot></tfoot>
        </table>
    </div>
</div>
