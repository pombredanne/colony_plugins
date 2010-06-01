<div id="overlay"></div>
<div id="notification-area" class="right">
    <div id="notification-area-contents"></div>
</div>
<div id="header">
    <div id="logo"></div>
    <div id="account-area-container">
        <ul>
            <li>
                <a id="account-description">${out_none value=session_user_information.username /} @ ${out_none value=session_user_information.company.name /}</a>
                <div id="account-float-panel" class="float-panel">
                    <div class="float-panel-arrow"></div>
                    <div class="float-panel-content">
                        <img src="resources/images/dummy-photo.png" height="64" width="64" alt="" />
                        <h1>${out_none value=session_user_information.username /}</h1>
                        <h2>${out_none value=session_user_information.company.name /}</h2>
                        <a href="#">Editar Perfil</a>
                        <a href="#">Upgrade</a>
                    </div>
                </div>
            </li>
            <li><a href="${out_none value=base_path /}logout">Logout</a></li>
            <li><a href="">My Omni</a></li>
            <li><a href="">Help</a></li>
        </ul>
    </div>
    <div id="menu-bar" class="menu-area-container">
        <ul>
            <li class="active"><a id="global">Global</a></li>
            <li><a id="reports">Reports</a></li>
            <li><a id="configuration">Configuration</a></li>
        </ul>
        <div id="menu-bar-search-field" class="search-field">
             <input class="text" type="text"/>
             <div class="search-button"></div>
        </div>
    </div>
    <div id="global-menu" class="drop-menu">
        <ul>
            <li><a href="#dashboard">Dashboard</a></li>
            <li><a href="#search">Pesquisa</a></li>
        </ul>
    </div>
    <div id="reports-menu" class="drop-menu">
        <ul>
            <li><a href="">Todos os Relatórios</a></li>
            <li><a href="">Todos os Relatórios</a></li>
        </ul>
        <hr/>
        <ul>
            <li><a href="">Relatório de Vendas</a></li>
            <li><a href="">Relatório de Pagamentos</a></li>
            <li><a href="">Relatório de Top de Vendas</a></li>
        </ul>
    </div>
    <div id="configuration-menu" class="drop-menu">
        <ul>
            <li><a href="#plugins">Plugins</a></li>
            <li><a href="#capabilities">Capabilities</a></li>
        </ul>
        <hr/>
        <ul>
            <li><a href="">Export</a></li>
            <li><a href="">Import</a></li>
            <li><a href="">API</a></li>
        </ul>
    </div>
</div>
<div id="filter"></div>
<div id="loading-message"></div>
<div id="environment-variables">
    <div id="base-path">${out_none value=base_path /}</div>
    <div id="ajax-submit">${out_none value=ajax_submit /}</div>
</div>
