# _*_ coding: utf-8 _*_
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render

def index(request):
    # menu_list = [
    #     # menu
    #     _("Dashboard"),
    #     _("Cluster Management"),
    #     _("Cluster Monitoring"),
    #     _("Server Management"),
    #     _("Openstack Integration"),
    #     _("VSM Management"),
    #     _("VSM")
    # ]

    # panel_list = [
    #     # panel
    #     _("Cluster Status"),
    #     _("Manage Servers"),
    #     _("Manage Devices"),
    #     _("Create Cluster"),
    #     _("Import Cluster"),
    #     _("Ceph Upgrade"),
    #     _("Manage Pools"),
    #     _("Manage EC Profiles"),
    #     _("Manage Storage Group"),
    #     _("Manage Zones"),
    #     _("Storage Group Status"),
    #     _("Pool Status"),
    #     _("OSD Status"),
    #     _("Monitor Status"),
    #     _("MDS Status"),
    #     _("PG Status"),
    #     _("RBD Status"),
    #     _("Manage RBD Pools"),
    #     _("Openstack Access"),
    #     _("Add/Remove User"),
    #     _("Settings")
    # ]

    # login_list = [
    #     _("Logged in as"),
    #     _("Sign Out"),
    # ]

    # manage_server_list = [
    #     _("Add Servers"),
    #     _("Remove Servers"),
    #     _("Add Monitors"),
    #     _("Remove Monitors"),
    #     _("Start Servers"),
    #     _("Stop Servers"),

    #     _("Server List"),
    #     _("ID"),
    #     _("Name"),
    #     _("Management Address"),
    #     _("Public Address"),
    #     _("Cluster Address"),
    #     _("Ceph Version"),
    #     _("OSDs (Data Drives)"),
    #     _("Monitor"),
    #     _("Zone"),
    #     _("Status"),
    # ]

    # manage_device_list = [
    #     _("Restart"),
    #     _("Remove"),
    #     _("Restore"),
    #     _("New"),

    #     _("Device List"),
    #     _("Name"),
    #     _("OSD Status"),
    #     _("Weight"),
    #     _("Server"),
    #     _("Storage Class"),
    #     _("Zone"),
    #     _("Status"),
    #     _("Data Device Status"),
    #     _("Journal Device Status"),
    #     _("Capacity Status"),
    # ]

    # ceph_upgrade_list = [
    #    _("Package URL"),
    #    _("Key URL"),
    #    _("Proxy URL"),
    #    _("SSH User Name"), 
    # ]

    # manage_pool_list = [
    #     _("Add Cache Tier"),
    #     _("Remove Cache Tier"),
    #     _("Create Replicated Pool"),
    #     _("Create EC Pool"),

    #     _("Storage Pools"),
    #     _("ID"),
    #     _("Name"),
    #     _("Storage Group"),
    #     _("Placement Group Count"),
    #     _("Size"),
    #     _("Quota (GB)"),
    #     _("Cache Tier Status"),
    #     _("Erasure Code Status"),
    #     _("Status"),
    #     _("Created By"),
    #     _("Tag"),

    #     _("Pool Name"),
    #     _("Tag"),
    #     _("Storage Group"),
    #     _("Erasure Coded Profile"),
    #     _("Erasure Coded Failure Domain"),
    #     _("Cache Tier Pool"),
    #     _("Select a Cache Tier Pool"),
    # ]

    # ecprofile_mgmt_list = [
    #     _("ID"),
    #     _("Name"),
    #     _("Plugin Name"),
    #     _("Plugin Path"),
    #     _("PG Number"),
    #     _("Key Values Pairs"),
    #     _("EC Profiles List"),
    # ]

    # storage_group_status_list = [
    #     _("Storage Group"),
    #     _("Attached Pools"),
    #     _("Capacity Total (GB)"),
    #     _("Capacity Used (GB)"),
    #     _("Capacity Available (GB)"),
    #     _("Percent Used Capacity(%)"),
    #     _("Largest Node Capacity Used (GB)"),
    #     _("Warning"),
    #     _("Status"),
    #     _("Updated at"),
    # ]

    # pool_status_list = [
    #     _("Ordinal"),
    #     _("Name"),
    #     _("Tag"),
    #     _("Storage Group"),
    #     _("Size"),
    #     _("PG Count"),
    #     _("PgP Count"),
    #     _("Status"),
    #     _("Create By"),
    #     _("KB Used"),
    #     _("Objects"),
    #     _("Clones"),
    #     _("Degraded"),
    #     _("Unfound"),
    #     _("Read Ops"),
    #     _("Read KB"),
    #     _("Write Ops"),
    #     _("Write KB"),
    #     _("Client READ B/S"),
    #     _("Client Write B/S"),
    #     _("Client Ops/s"),
    #     _("Updated at"),

    #     _("Pool List"),
    # ]

    # OSD_status_list = [
    #     _("Ordinal"),
    #     _("OSD Name"),
    #     _("VSM Status"),
    #     _("OSD Status"),
    #     _("Crush Weight"),
    #     _("Capacity Total (MB)"),
    #     _("Capacity Used (MB)"),
    #     _("Capacity Available (MB)"),
    #     _("Percent Used Capacity"),
    #     _("Server"),
    #     _("Storage Group"),
    #     _("Updated at"),

    #     _("OSD List"),
    # ]


    # OSD_status_list = [
    #     _("Ordinal"),
    #     _("Name"),
    #     _("Address"),
    #     _("Health"),
    #     _("Detail"),
    #     _("Skew"),
    #     _("Latency"),
    #     _("MB Total (disk)"),
    #     _("MB Used (disk)"),
    #     _("MB Available (disk)"),
    #     _("Percent Available"),
    #     _("Updated at"),
    # ]

    # MDS_status_list = [
    #     _("Ordinal"),
    #     _("Name"),
    #     _("Gid"),
    #     _("State"),
    #     _("Address"),
    #     _("Updated at"),

    #     _("MDS List"),
    # ]

    # RBD_status_list = [
    #     _("ID"),
    #     _("Pool"),
    #     _("Image Name"),
    #     _("Size(MB)"),
    #     _("Objects"),
    #     _("Order"),
    #     _("Format"),
    #     _("Updated at"),

    #     _("RBD List"),
    # ]

    # RBD_pool_list = [
    #     _("ID"),
    #     _("Name"),
    #     _("Storage Group"),
    #     _("Placement Group Count"),
    #     _("Size"),
    #     _("Status"),
    #     _("Created By"),
    #     _("Tag"),
    #     _("Attach Status"),
    #     _("Manage Openstack RBD Pools"),
    #     _("Present Pools"),

    #     _("Replication Factor"),
    #     _("OpenStack/Region"),
    #     _("Cinder Volume Host"),
    #     _("Present RBD Pools"),
    # ]

    # Openstack_access_list = [
    #     _("Add OpenStack Endpoint"),
    #     _("ID"),
    #     _("Tenant Name"),
    #     _("UserName"),
    #     _("Password"),
    #     _("Auth Url"),
    #     _("Region Name"),
    #     _("SSH User Name"),
    #     _("Connection Status"),
    #     _("LOG INFO"),

    #     _("Manage Openstack Access"),
    # ]

    # User_list = [
    #     _("ID"),
    #     _("Name"),
    #     _("Email"),
    #     _("Enabled"),
    #     _("User List"),
    #     _("Change Password"),
    #     _("Create User"),
    #     _("Update User"),

    #     _("User Name"),
    #     _("Password"),
    #     _("Confirm Password"),
    # ]

    output = _('Today is %s %s.') %("09","19")

    return render(request, 'dashboard/index2.html', {"output": output})
    # return render(request, 
    #             'dashboard/index.html', 
    #             {"menu_list":menu_list, "panel_list":panel_list, "login_list":login_list,
    #              "manage_server_list":manage_server_list,"manage_device_list":manage_device_list,
    #              "ceph_upgrade_list":ceph_upgrade_list,"ecprofile_mgmt_list":ecprofile_mgmt_list,
    #              "storage_group_status_list":storage_group_status_list})
