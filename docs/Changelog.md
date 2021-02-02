Changelog
=========

v2.4 aka 2.4 for ever (current changelog)
------------------------

New
---
- [docs] Added new sub-sections in seperate files that are shared
  between install guides. new: [docs] ethX.md to bring back eth0 new:
  [docs] mail to misp install debian flavored guide new: [docs] ssdeep
  install debian flavored guide new: [docs] viper install debian
  flavored guide new: [docs] sudo/etckeeper install debian flavored
  guide new: [docs] misp dashboard install debian flavored guide. [Steve
  Clement]
- [docs] Added 3 generic documentation files, one where the MISP install
  is completed, A specific centos/etc... one because, well, CentOS.. and
  the generic recommended actions section that kept repeating in all
  guides. chg: [docs] Implemented the above 3 files in all the guides.
  Plus some format changes. [Steve Clement]
- [docs] Added generic notice about community contributed doc
  maintenance. [Steve Clement]
- [docs] Added globalVariables files to be included by all Install
  Guides chg: [tools] Updated dependencies on docs creator chg: [docs]
  Some minor changes to Ubuntu Install guide and added
  VariableglobalVariables chg: [docs] Updated mkdocs.yml with new
  dependencies. [Steve Clement]
- [docs] Added eXperimental RHEL7.6 (BETA) Install Doc. [Steve Clement]
- [tools] Added tool to create MISP INSTALL Docs and push to gh-page,
  plus it fetche latest Changelog.txt. [Steve Clement]
- [docs] Added intial mkdocs directory. [Steve Clement]
- [galaxy] Several changes. [iglocska]

  - moved the current uuid field on cluster level to a new "collection_uuid" field to better represent the actual purpose
  - added new uuid field that actually captures the cluster's uuid
  - upgrade script is multi-execution safe
  - added /galaxy_clusters/view to the API
  - /galaxy_clusters/view can now be queried via the uuid instead of just the ID
- [API] Added CSV as return format for event index. [iglocska]
- [API description] Describe how to run diagnostics on MISP via the API.
  [iglocska]
- [upgrade] Preparing the data for recovery after the object reference
  sync fix. [iglocska]

  - update the timestamps of all events / objcts that are affected and are locked = 0
- [API] Added a way to use the API to throw values at the warninglist
  for quick evaluations of the values. [iglocska]
- [logging] Log why an event could not be pulled. [iglocska]
- [API documentation] Added some missing API templates. [iglocska]
- [API] Added the log index/search to the API. [iglocska]

  - described in the templates / rest client page
- [related tags] View the related tags of attributes on the event view
  (via a toggle) [iglocska]

Changes
-------
- [doc] the venv directory needs usr_t profile. [Steve Clement]
- [doc] Update Centos 6.x and 7.x chg: [doc] re-Added Ubuntu 16.04-LTS
  as an archived/old INSTALL Guide (tested working) chg: [doc] Adapted
  some variables in generic scripts. [Steve Clement]
- [doc] updated Changelog.md to be more markdown friendly chg: [tools]
  Changed the way gen_misp_install_docs.sh parseses the changelog new:
  [tools] Added simple tool for git log sanitizing. [Steve Clement]
- [docs] Added note on RHEL unmaintainability at this point of time, by
  the core team. [Steve Clement]
- [tools] Updated gitchangelog.rc for latest version of toll, added to
  doc generator. [Steve Clement]
- Bump misp-galaxy & taxonomies. [Raphaël Vinot]
- [docs] Added generic sections to debian guides. [Steve Clement]
- [docs] Added a generic directory where all the platform independent
  files should reside. chg: [docs] Added MISP Defaults via the cake
  command to seperate file. [Steve Clement]
- [misp-objects] forensic objects added. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-objects] updated to the latest version (including many new
  objects) [Alexandre Dulaunoy]
- [docs] More formatting updates and evened both versions out. [Steve
  Clement]
- [docs] Compared with bootstrap.sh and added missing dependencies and
  tools. [Steve Clement]
- [docs] Added note on when Kali was last tested working. Added RHEL 7.6
  BETA to index. [Steve Clement]
- [docs] Leveled both install docs, updated debian testing and verified
  working. [Steve Clement]
- [docs] Minor regression, fixed. [Steve Clement]
- [docs] Leveled both guides, 9.5 moved a little closer to testing.
  [Steve Clement]
- [docs] Symlink to rhel7 guide chg: [docs] Made the index a little less
  messy chg: [docs] A minor (but not automated) change to Changelog.
  [Steve Clement]
- [tools] Changed testForBinExec as the x-sharedlib type is not only on
  OpenBSD, Debian has the same type when check if executable. chg:
  [tools] Added typeinfo to the return so you see in the UI what type it
  thinks it is. (In case you forced the parameter on the CLI) [Steve
  Clement]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [docs] More general info about xINSTALL in index. Minor formatting
  touch-up in license. Added missing sections to mkdocs.yml and adapted
  it to reflect official MISP repo. [Steve Clement]
- [docs] Adapted rhel7/Ubuntu18.04/Centos7/UPDATE_Notes to be mkdocs
  compliant. [Steve Clement]
- [tools] Added sed to gen_misp_install_docs.sh to replace some
  formatting tildes which mkdocs does not really understand chg: [docs]
  Minor touch-up to Changelog.md to correct for formatting issues. chg:
  [config] Added correct paths to .gitignore for mkdocs. [Steve Clement]
- [docs] Adapted Debian 9/testing install to mkdocs new: [docs] Added
  old version of Debian + postgresql guide, needs updating. [Steve
  Clement]
- [docs] Added symlinks to new .md to preserve old style for a while.
  chg: [docs] More details in README.md. [Steve Clement]
- [docs] Added some symlinks to migrated files. [Steve Clement]
- [docs] Remove some migrated INSTALL guides, move FreeBSD to old, will
  not be supported in the future. [Steve Clement]
- [docs] Typo in UPGRADE.md. [Steve Clement]
- [docs] Added an old upgrade doc, 2.3 -> 2.4, more as an example then
  anytyhing else. chg: [docs] Added UPGRADE.md notice for future upgrade
  steps. [Steve Clement]
- [docs] Minor formating chage. [Steve Clement]
- [docs] Removed old Debian stable install guide. [Steve Clement]
- [docs] Updated Debian install guide. [Steve Clement]
- [docs] Version bump of OpenBSD to 6.4. [Steve Clement]
- [docs] Added misp-dashboard instruction, but not really working yet.
  [Steve Clement]
- [docs] Another small unattentive typo. [Steve Clement]
- [docs] Small misp-modules virtualenv typo. [Steve Clement]
- [docs] Removed old OpenBSD Docs. [Steve Clement]
- [docs] More or less finalized the Apache2 install. 95% working. [Steve
  Clement]
- [docs] Disable native httpd for now added Apache2 conf. [Steve
  Clement]
- [docs] Better formatting, more information on the current state of
  MISP on OpenBSD. [Steve Clement]
- [docs] Reformated some of the .txt based doc. [Steve Clement]
- [config] Added mkdocs site directory to be ignored. [Steve Clement]
- [tools] Added x-sharedlib clause in testForBinExec if on OpenBSD.
  [Steve Clement]
- [warninglist] warninglists updated, fixes #3775. [iglocska]
- [Galaxy] Updated MISP galaxies. [iglocska]
- Chg: [tools] removed: #@IgnoreInspection BashAddShebang -- Added a
  better globbing opt: ./* [Steve Clement]
- [tools] Updated misp-backup and misp-wipe to be a bit more late 2018
  compliant. [Steve Clement]
- [tools] Added misp-wipe/misp-backup config file to .gitignore. [Steve
  Clement]
- [python] Added and amended varios places where python is called.
  [Steve Clement]
- [fix] Some fixed to the python virtualenv tweaks. [Steve Clement]
- [python] Added initial python virtualenv support, STIX Tests only.
  [www-data]
- [i18n] extracted latest strings to default.pot and cake_dev.pot.
  [Steve Clement]
- [i18n] New strings in Spanish translation. [Steve Clement]
- [i18n] Updated to latest jpn translation, minor changes. [Steve
  Clement]
- [i18n] Added 100% French translation. Thanks to all involved so far.
  wq. [Steve Clement]
- Bump PyMISP & recommended version. [Raphaël Vinot]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]

Fix
---
- [doc] Included git repo of gitchangelog due to Python 3.7 bug fix not
  yet in release: https://github.com/vaab/gitchangelog/issues/107.
  [Steve Clement]
- [stix import] Importing uuids for objects from external sources.
  [chrisr3d]
- [stix import] Importing uuids for STIX files generated via MISP.
  [chrisr3d]
- [stix import] Improved uuid fetching. [chrisr3d]
- [stix import] Better event & attribute distribution parsing.
  [chrisr3d]
- [stix import] Supporting DHS stix files with ais marking. [chrisr3d]
- [stix import] Fixed import of File Objects as single attribute.
  [chrisr3d]
- [stix framing] Fixed Related Package(s) xml field typo. [chrisr3d]
- [stix export] Fixed xml package string replacement. [chrisr3d]
- [stix2 import] Avoiding errors when the imported file name is not
  specified. [chrisr3d]
- [stix2 import] Fixed GalaxyCluster description. [chrisr3d]

  - Since description is optionnal in some STIX 2.0
    objects, we test if the field is there before
    trying to use its value
- [galaxy] added collection uuid capture. [iglocska]
- [view] Added uuids to galaxy cluster view. [iglocska]
- [routes] Added route for .csv parsing. [iglocska]
- \#3769 Att&ck matrix now render multiple kill_chain by column. [Sami
  Mokaddem]
- Check if the format is xml or application/xml on __sendResponse. [Tom
  King]
- [cleanup] Removed debug from the bug fixing session. [iglocska]
- [stix2 import] Fixed MISP event info field when importing STIX2
  without report object. [chrisr3d]
- [stix2 import] Fixed json dict monkey syntax error. [chrisr3d]
- [internal] Sharing group capturing fixed, fixes #3573. [iglocska]

  - As reported by @eCrimeLabs
- [internal] Unneeded model initialisation for
  getDefaultAttachments_dir() [iglocska]
- [internal] getPythonVersion woes. [iglocska]
- [internal] Fix of wonky model function calls across the application
  for getting default attachment directories. [iglocska]
- [Galaxy] Various fixes to blocking issues with the galaxy update
  system, fixes #3773. [iglocska]
- [API] Handle multiple event IDs being queries or not using the event
  ID filter when generating the CSV output file names. [iglocska]
- [internal] Fixes to invalid model function calls. [iglocska]
- [tools] small typo in she-bang line. [Steve Clement]
- [stix2 import] Made NetworkTraffic objects import include all the
  possible cases. [chrisr3d]

  - We were potentially missing some DomainName
    or IP Address objects data, when it is not
    a reference of the NetworkTraffic object.
  - Now we look if we still have some of these
    objects that did not have been parsed, and
    in that case, parse them.
- [stix2 import] Quick change on event loading. [chrisr3d]

  - Specifying the encoding within the file opening
  - Allows to get rid of 1 'encode()' call
- [stix2 import] Better parsing for objects that can be imported as
  either ip-port or network-socket. [chrisr3d]
- [stix2 import] Supporting STIX 2 files with no report object.
  [chrisr3d]
- [stix2 import] Moved the remaining parsing functions from the mapping
  script to the main script. [chrisr3d]

  - Fixing at the same time some AttributeName errors
- [stix2 export] Fixed enumeration errors handling. [chrisr3d]

  - More specific exception types
  - Removed useless try/catch statement
- [stix2 export] Fixed attributes data parsing. [chrisr3d]

  - With json format, base64 & encode/decode
    operations are no longer needed since the base64
    string is already displayed in data
- [stix2 import] Fixed process import. [chrisr3d]

  Fixing import for cases like:
  - single process without parent or child
  - where processes are not referenced as expected
- [stix2 import] Fixed monkey coder issue. [chrisr3d]
- [stix2 import] Added missing uuid fields to attributes and objects
  imported. [chrisr3d]
- [stix2 import] Quick clean-up. [chrisr3d]

  - Using MISPObject class & attributes instead of
    adding a MISP object dealing with a dictionary
  - Using STIX objects attributes instead of
    ditionary keys
  - Removed useless 'continue' statement
- [stix2 import] Parsing file objects in a more generic way between
  classes. [chrisr3d]
- [stix2 import] Moved file object parsing function into the subclass.
  [chrisr3d]

  - Because it is only called by functions of this subclass
- [stix2 import] Removed useless function. [chrisr3d]
- [search] Multiple lines didn't correctly get parsed as separate values
  in the attribute search. [iglocska]
- [workers] manage workers by default defaulted to false (should be
  true) [iglocska]
- [API] Further fixes to the query builder. [iglocska]
- Travis import/export. [Raphaël Vinot]
- [API] Further fixes to the tag handling. [iglocska]
- [API] Handle filters with no valid tags set as filter patterns
  correctly. [iglocska]

Other
-----
- Merge pull request #3802 from SteveClement/guides. [Steve Clement]

  chg: [tools] RHEL7 update status and added gitchangelog to document creation toolchain.
- Merge branch '2.4' into guides. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3803 from garanews/2.4. [Andras Iklody]

  fix accommodate misspelling
- Fix accommodate misspelling. [garanews]

  accommodate vs accomodate
- Merge pull request #3799 from garanews/patch-1. [Alexandre Dulaunoy]

  fix separate misspelling
- Fix separate misspelling. [garanews]

  separate vs seperate
- Merge pull request #3800 from garanews/patch-2. [Alexandre Dulaunoy]

  fix referred misspelling
- Fix referred misspelling. [garanews]

  referred vs refered
- Merge pull request #3798 from SteveClement/guides. [Steve Clement]

  chg: [docs] Major INSTALL Guide update
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3726 from pettai/shibb. [Steve Clement]

  add date_created for provisioned users
- Add date_created for provisioned users. [Fredrik Pettai]

  add date_created then new users are provisioned via shibbauth
- Merge pull request #3794 from SteveClement/guides. [Steve Clement]

  chg: [docs] The debian install docs are now fully functional and quite a few format changes to some of the install guides.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3784 from SteveClement/guides. [Steve Clement]

  new: [docs] Move INSTALL guides formatting to mkdocs
- Merge branch '2.4' into guides. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3771 from P4rs3R/patch-3. [Alexandre Dulaunoy]

  Update INSTALL.rhel7.txt
- Update INSTALL.rhel7.txt. [A. Cristallo]

  Added instruction (at line 109) and updated line 8, minor change.
  Tested on RHEL 7.5 and CentOS 7.5
- Merge pull request #3779 from MISP/att&ckMatrixFix. [Alexandre
  Dulaunoy]

  fix: #3769 Att&ck matrix now render multiple kill_chain by column.
- Merge pull request #3778 from tomking2/2.4. [Andras Iklody]

  Fixes Issue #3633 - Returned XML has application/json Content-Type header
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3768 from devnull-/#3748_download_files. [Andras
  Iklody]

  Fix CSV filename #3740
- Define filename (instead of download.csv) [Amaury Leroy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: [stix2 import] Added an entry to the simple pattern mapping
  dictionary. [chrisr3d]
- Merge pull request #3765 from IFX-CDC/2.4. [Andras Iklody]

  add: workers diagnostics to the server settings
- Fixed workers tab. [netjinho]
- Added workers diagnostics to the server settings. [netjinho]
- Merge pull request #3766 from SteveClement/misp-wipe. [Andras Iklody]

  Misp wipe and backup
- Merge pull request #3762 from SteveClement/py-virtualenv. [Andras
  Iklody]

  chg: [tools] Added the option to have Python Virtualenv support
- Merge branch '2.4' into py-virtualenv. [www-data]
- Merge branch '2.4' into py-virtualenv. [Steve Clement]
- Merge branch '2.4' into py-virtualenv. [www-data]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3760 from cudeso/2.4. [Alexandre Dulaunoy]

  Ubuntu 18 documentation (sudo logrotate, universe repo)
- Ubuntu 18 documentation (sudo logrotate, universe repo) [Koen Van
  Impe]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3757 from rmarsollier/patch-1. [Andras Iklody]

  adding python-maec to the debian9 install
- Adding python-maec to the debian9 install. [RbN]

  adding python-maec to the debian9 install
- Merge pull request #3758 from MISP/chrisr3d_patch. [Christian Studer]

  Chrisr3d patch
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- :construction: [stix2 import] Parsing external Network Socket objects when
  references are hostnames. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Also reusing functions working for both subclasses
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Add: [stix2 import] Added 1 easily parsable pattern type for external
  STIX parsing. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- :construction: [stix2 import] Parsing external observable IPAddr -
  NetworkTraffic - Domain composition objects. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Also reusing functions working for both subclasses
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- :construction: [stix2 import] Parsing external process objects. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Also reusing functions working for both subclasses
- :construction: [stix2 import] Parsing external AS objects. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Also reusing functions working for both subclasses
- :construction: [stix2 import] Parsing external x509 objects. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Also reusing functions working for both subclasses
- :construction: [stix2 import] Parsing external mutex objects. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
- :construction: [stix2 import] Parsing external mac-address objects. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
- :construction: [stix2 import] Parsing external url objects. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Also reusing functions working for both subclasses
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- :construction: [stix2 import] Parsing external regkey objects. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Also reusing functions working for both subclasses
- :construction: [stix2 import] Parsing external email objects. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Also reusing functions working for both subclasses
- :construction: [stix2 import] Parsing domain & domain-ip attributes/objects.
  [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Also reusing code that works for both subclasses
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- :construction: [stix2 import] Included pe & pe-section parsing for file objects.
  [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
  - Including uuid fields
  - Including refactor on some class attributes to
    avoid errors and duplications
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- :construction: [stix2 import] Starting parsing network-traffic objects from
  external files. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged,
        this script may be broken in some cases atm :warning:
- :construction: [stix2 import] Starting parsing observables from external STIX2
  files + moving functions to the main script. [chrisr3d]

  - :warning: :construction:, it is preferable to wait for the branch to be merged, script broken atm :warning:
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3751 from ancailliau/fixes-error-message-
  control_workers. [Andras Iklody]

  Fixes a typo in an error message (control_workers -> manage_workers)
- Fixes a typo in an error message (control_workers -> manage_workers)
  [Antoine Cailliau]
- Merge pull request #3750 from Rafiot/csv_travis. [Raphaël Vinot]

  fix: travis import/export

v2.4.96 (2018-10-09)
--------------------

New
---
- [ReST client] generate python output too. [iglocska]

  - also, nicer toggle!
- [API] Added cache export to export list. [iglocska]
- [ReST Client] added curl output to make everyone's lives a bit easier.
  [iglocska]
- [API] Added returnFormat descriptions in a programmatic way to the API
  info. [iglocska]
- [API] Added a new export that simply hashes all values with a
  requested hash format. [iglocska]
- [API] rework of the searchall/quickFilter parameters. [iglocska]

  Now it correctly works as intended on both attribute and event contexts
- [API] documentation added for the new APIs. [iglocska]
- [export] Further changes required for the reworked export added.
  [iglocska]
- [exports] New export system using restsearch. [iglocska]
- [search] download functionalities added to the search. [iglocska]
- [search] view changes added for the search. [iglocska]
- [search] Search refactored completely to use restsearch. Still needs
  some minor changes. [iglocska]
- [internal] restsearch's bulk code moved to the model for attributes.
  [iglocska]
- [api] CSV export using thin overlay over restsearch. [iglocska]
- [API] attributes/restSearch has received CSV as a new export format.
  [iglocska]

  - added hook to modify parameters based on the export's internal settings
- [API] restsearch's internals moved to event model and reworked.
  [iglocska]

  - better chunking and parameter handling
- [API] events/restSearch reworked, added CSV export. [iglocska]
- [API] CSV export tool completely reworked. [iglocska]
- [API] Improvements to the fetcher. [iglocska]

  - cache several objects that were loaded over and over before on bulk exports
  - includeGranularCorrelations internal flag added to include/exclude correlations from the export for certain types
  - some cleanup
- [internal] Added caching to the sharing group organisations.
  [iglocska]
- [internal] Organisation internal caching added. [iglocska]
- [internal] GalaxyCluster internal caching added. [iglocska]
- [API] added sendFile function to rest response component. [iglocska]
- [API] events/restsearch rework - chunked export for performance gains.
  [iglocska]
- [API] enable/disable warninglists by name substrings instead of IDs,
  fixes #3706. [iglocska]

  - {"name": ["alexa", "iana"], "enabled": 1}
- [freetext] Freetext ingestion is now delegated to the background
  processing. [iglocska]

  - no setup needed
  - data to be ingested dropped to file, background worker ingests and processes the file
- [freetext import] Added detection for AS. [iglocska]
- [Complex type tool] Detection of [1] style refanging. [iglocska]
- [API] Rework of the restSearch APIs. [iglocska]

  - peformance tuning
    - removed some redundant looping
    - internal memory profiling for attributes/restSearch
    - saving the intermediary results to file instead of keeping it all in memory to reduce the memory footprint
  - added the searchall parameter
  - fixed the ignore parameter
  - added the event_timestamp parameter
  - added manual pagination to the attribute level restsearch (limit, page)
- [API] Added API description for the warninglist toggleEnable API.
  [iglocska]
- [API] Toggle the warninglists on/off in a convenient API. [iglocska]

  - via /warninglists/toggleEnable
- [blacklisting] pass parameters via named parameters to filter the
  index. [iglocska]

  - /eventBlacklists/index/event_uuid:[my_event_uuid]
- [API] Correctly handle objects in flat exports and exposed text export
  to event level search. [iglocska]
- [Galaxy] Delete individual clusters. [iglocska]

  - added an API and UI option to delete individual clusters
- [variable tags] Added the ability to load and display variable tags.
  [iglocska]

  - as requested by Siemens
- [API] Added the includeEventTags parameter to the
  /attributes/restSearch API. [iglocska]

  - appends all event level tags to each attribute
- [stix import] Adding object describing the original STIX 1.X / 2.X
  used for import. [chrisr3d]

  - Depending if the variable passed to those scripts
    are not None, then it is the name of the original
    file used to import data
- [API] Added possibility to include the original file while importing
  STIX data. [chrisr3d]
- [API] Tied the RPZ export into the restsearch APIs. [iglocska]

  - also, made the export modules aware of the exhaustive parameter list
- [API] Updated the RPZ export to follow the new API patterns.
  [iglocska]

Changes
-------
- [CSV] Added timestamp in CSV output with include context on the event
  level. [iglocska]
- [version] version bump. [iglocska]
- [automation page] cleanup. [iglocska]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [notice-list] updated to the latest version. [Alexandre Dulaunoy]
- [warning-lists] updated to the latest version. [Alexandre Dulaunoy]
- [taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- Bumped js version. [Sami Mokaddem]
- Bump PyMISP. [Raphaël Vinot]
- [export] Export view correctly fetches the state on whether an export
  includes attachments. [iglocska]
- [API] made the CSV export type less restrictive by default (to_ids /
  published ignored by default) [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- Bump PyMISP. [Raphaël Vinot]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- Bump PyMISP. [Raphaël Vinot]
- [API] new restresponse library addition fixed (send file) [iglocska]
- Bump PyMISP. [Raphaël Vinot]
- [sharing-group] fix typo "Added Organisations" -> "Added Instance"
  [Alexandre Dulaunoy]
- [misp-objects] add the relationship annotates. [Alexandre Dulaunoy]
- Bump PyMISP. [Raphaël Vinot]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-taxonomy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-object] updated to the latest version. [Alexandre Dulaunoy]
- Bump PyMISP. [Raphaël Vinot]
- [stix1 framing] Removed previous stix framing script. [chrisr3d]
- [stix 1&2 export] Using header, footer and separator from the newest
  framing script. [chrisr3d]
- [stix2 export] Using the RestResponse view call instead of having view
  files. [chrisr3d]
- [stix2 export] Avoid Orgc Identity object duplication. [chrisr3d]

  - Orgc uuid returned each time a new one is seen
    in an event
  - All the uuids as parameter of the python script
  - Identity object added only if the current uuid
    is not in the parameters
  - References to the corresponding identity are
    (obviously) maintained for the final stix 2.0
    file
- [stix2 export] Multiple events export prepared in Controller & Model
  side. [chrisr3d]

  - Changes on automation side coming soon
- [debugkit] Added the commented out loading of debugkit for
  convenience. [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [default-feeds] CoinBlockerLists updated - fix #3682. [Alexandre
  Dulaunoy]
- [misp-object] updates to the latest version. [Alexandre Dulaunoy]
- [doc] Moved INSTALL files around to reflect a more acurate support
  landscape. chg: [doc] Update README.md to explain some of the
  folders/files. [Steve Clement]
- [doc] Added zmq, redis, maec python module installations. [Steve
  Clement]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [misp-taxonomy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [stix2 import] 2 main parsing cases split in 2 classes. [chrisr3d]

  --> 2 cases:
          - STIX generated via MISP
          - external STIX
- [Cortex] Don't set the content type header for cortex. [iglocska]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [doc] Added README to install directory. [Steve Clement]
- [doc] Centos 7 Install doc updates, more automation and some auto
  defaults. [Steve Clement]
- [doc] Updated and tested basic MISP functionality under CentOS 7.5.
  [Steve Clement]
- [i18n] Update to languages: Danish (54%) German (17%) Japanese (100%)
  French (67%) Spanish (3%) [Steve Clement]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [misp-warninglists] updated to the latest version. [Alexandre
  Dulaunoy]
- Bump recommended pyMispVersion. [Raphaël Vinot]
- [doc] Point to official misp-book, MISP "User Guide" in main codebase
  is obsolete. [Steve Clement]
- [PyMISP] updated to the latest version. [Alexandre Dulaunoy]

Fix
---
- [sanitisation] Sanitise curl query. [iglocska]
- [stix2 import] Fixed to_ids flag in imported objects. [chrisr3d]
- [API] Fixed broken check for overriding IDS flags via proposals, fixes
  #3748. [iglocska]
- [stix2 export] Fixed process objects export. [chrisr3d]
- [stix2 export] Fixed function call typo. [chrisr3d]
- [Auth] Correctly handle users accounts getting deleted whilst the
  users are logged in. [iglocska]

  - deauthed users would end up in a forced loop having to read the news creating a new blank user with each page refresh
- [stix import] Updated external files import to include related
  indicators. [chrisr3d]
- [stix import] Fixed custom objects import from external files.
  [chrisr3d]
- [Objects] Adding an object would not unpublish the event. [iglocska]
- [stix2 export] Avoiding export of the object related to the original
  file used for import. [chrisr3d]
- [stix export] Avoiding export of the object related to the original
  file used for import. [chrisr3d]
- [stix import] Fixed original imported file Object name. [chrisr3d]
- Sort CSV file before comparing: we do not care what the order of the
  attributes is. [Raphaël Vinot]
- [CSV] boolean fields should be set to 1/0 instead of true/false.
  [iglocska]
- [freetext] tag field not working fixed. [iglocska]
- [stix2 export] Handled case where we have only link attributes to be
  imported. [chrisr3d]
- [restSearch] Avoiding useless stix python script calls on empty files.
  [chrisr3d]
- [stix2] invalid path to script dir. [iglocska]
- [restSearch] Ignoring square brackets around STIX2 objects returned by
  the python script. [chrisr3d]

  Because they are already provided by the framing script
- [stix export] Shortcut passing directly the 'Event' key of an event to
  the parsing functions. [chrisr3d]
- [stix2 export] Avoiding identity object duplication. [chrisr3d]

  - Fixed orgs list, adding each org seen as it was
    intended but forgotten until now
- [restSearch] Fixed return format for STIX formats. [chrisr3d]
- [restSearch] Added STIX 1 & 2 in valid formats. [chrisr3d]

  - Also fixed indentation of the validFormats array
- [restSearch] Fixed failed merge. [chrisr3d]
- [stix2 export] Stopped passing ORGs already parsed as argument of the
  python script. [chrisr3d]
- [restSearch] Changed how data is handled eeeeeeeeeee. [chrisr3d]

  - Criteria was number of events and is now number
    of attributes
  - Writing data in a file until the limit number of
    attributes is reached, then writing in the next
    file and looping again until all data is written
  - Then for each file, calling the python script to
    parse MISP events and translate them into STIX
  - Writing parsed STIX data into 1 file used to
    return the result
- [stix2 export] Fixed event dictionary reading. [chrisr3d]
- [stix2 export] Refactored MISP event format used to improve
  performances. [chrisr3d]

  - For big events, loading json file and parsing it
    as json format is much faster than loading it as
    PyMISP objects
- [stix2 export] Clearer string concatenation in scripts & directories
  names definitions. [chrisr3d]

  - Reuse of variable name instead of string concatening
- [restSearch] Refactored MISP event format used to improve
  performances. [chrisr3d]

  - For big events, loading json file and parsing it
    as json format is much faster than loading it as
    PyMISP objects
- [stix1 export] Fixed baseurl & orgname fetching from scripts
  arguments. [chrisr3d]

  - Replacing empty arguments by default values
- [stix1 export] Including the latest changes on the python script.
  [chrisr3d]
- [stix2 export] Using class variables to define baseurl & orgname.
  [chrisr3d]
- [restSearch] Prettifying stix packages with indents. [chrisr3d]

  - As it is in stix export function from Model/Event.php
- [cleanup] Fixed indentation in restSearch. [chrisr3d]
- Added variable to have attribute with no ids flag from fetchEvent.
  [chrisr3d]
- [restSearch] Fixed variables & indent. [chrisr3d]
- [ACL] Added exportSearch to the ACL. [iglocska]
- [api] Sharing group organisations not iterated if they don't exist.
  [iglocska]
- Headers are case-sentitive, do not strtoupper. [Hannah Ward]
- [distributionGraph] changed condition to support one missing edge
  case. [Sami Mokaddem]
- [distributionGraph] Fixed for loop to be less browser dependent. [Sami
  Mokaddem]
- [internal] Moved validFormats array into a global for the event model.
  [iglocska]
- [ReST] increased ReST client execution time to 300s. [iglocska]
- [Feed] If no data is returned from a freetext feed a notice was
  generated. [iglocska]

  - added more graceful handling
- [log] user zmq logging was always getting the first user instead of
  the actual one. [iglocska]
- Travis tests failing, take 2. [Raphaël Vinot]
- Travis tests failing. [Raphaël Vinot]
- [graph] Made the correlation graph aware of the new correlation
  loading. [iglocska]
- [internal] Organisation caching fixed for the event load. [iglocska]
- [api] close the file after reading it. [iglocska]
- [API documentation] Added missing filters to the restSearch API.
  [iglocska]
- [API] sgReferenceOnly should work via the API too. [iglocska]
- [API] handle empty value fields when running a quick search.
  [iglocska]
- [API] Fixed the quickfilter parameter. [iglocska]
- [cleanup] Some cleanup and fixes to invalid exception invocations.
  [iglocska]
- [eventGraph] Adapted fa icon to match the current installed fa
  package. [Sami Mokaddem]
- [eventGraph] prevents bug if object has no attributes. [Sami Mokaddem]
- [stix2 export] Fixed Indicator & ObservedData arguments to avoid
  syntax error with version < 3.5 of python. [chrisr3d]
- [stix2 export] Fixed string truncation. [chrisr3d]
- [API] handle to_ids better in the restSearch APIs. [iglocska]

  - invalid default settings for text/suricata exports on the event scope fixed
  - 'exclude' re-introduced as a valid value
- [API] handle invalid export module calls gracefully. [iglocska]
- [stix2 export] Fixed unintended syntax error. [chrisr3d]
- [Event] Prevents bug if object has no attributes. [Sami Mokaddem]

  While using the event quick filter, prevents accessing a non existing index
  if the object has no attributes.
- [stix framing] Fixed orgname in stix framing. [chrisr3d]
- [stix framing] Removed monkey printing. [chrisr3d]
- [stix framing] Redefined stix separator. [chrisr3d]

  - Avoid writing 'related package' xml key after
    each python script call
  - Those keys are now defined as separator and
    coming from the framing script
- [stix export] Switched xml 'related packages' writing into the framing
  script. [chrisr3d]

  - Instead of doing it in the php side after the
    framing script is called
- [stix framing] Fixed xml separator. [chrisr3d]
- [API] toggle warninglists now correctly handles name lists as
  parameters instead of just single values, fixes #3706. [iglocska]
- [enrichment] Made the payload of the API enriching an event with a
  list of modules a bit more lax. [iglocska]
- [galaxy UI] clicking on metadata collapsed the galaxy quick view.
  [iglocska]
- [Rest client] fixed invalid serialisation of some fields. [iglocska]
- [cleanup] Fixed missing merge save. [chrisr3d]
- [import modules] Avoiding issues with userConfig when module is
  csvimport. [chrisr3d]

  - If users tick the checkbox to specify there is a
    header in the csv file to import, there should
    not be an error with empty userConfig header
- [stix1 framing] Including RichieB2B's patch. [chrisr3d]
- [stix1 export] Fixed missing change on the framing script call.
  [chrisr3d]
- [stix2 export] Fixed syntax in stix2 function. [chrisr3d]
- [stix2 export] Fixed monkey issue in org uuid to return (in order to
  avoid duplication) [chrisr3d]
- [stix2 export] Added missing view for stix2 json download. [chrisr3d]
- [stix2 export] Fixed event fetching. [chrisr3d]
- [API] Fixed an invalid lookup in the openioc export. [iglocska]
- [API] added catcher for include_event_uuid via /attributes/restSearch.
  [iglocska]

  - affects #3695
- [stix2 export] Variable typo. [chrisr3d]
- [API] malware samples not encoded with withAttachments=1 on the event
  level restSearch. [iglocska]
- [stix2 export] Cleaned up MISP objects parsing. [chrisr3d]

  - Replaced multiple if statements in a for loop by
    a dictionary mapping
- [stix2 export] Removed list of MISP types no longer used. [chrisr3d]
- [stix2 export] Cleaned up MISP attributes parsing. [chrisr3d]

  - Replaced multiple if statements in a for loop by
    a dictionary mapping
- [API] CSV export snafu fixed. [iglocska]

  - perhaps not ignoring the filter parameters and getting the full dataset visible to the current user is a helpful idea
- [API] Added rpz to restsearch API description. [iglocska]

  - also added text to events/restSearch
- [internal] Fixed an issue that prevented all to ids attributes from
  being fetched on the event view. [iglocska]
- [UI] Glaaxy quick view collapse toggle didn't correctly replace the +
  with a - when expanded, fixes #3678. [iglocska]
- [API] Fixed the handling of the to_ids flag. [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [ACL] Appease Travis (admin only function explicitly named) [iglocska]
- [db] Fixed an invalid DB field. [iglocska]
- [stix2 import] Using stix2 library attributes to load and parse STIX
  data. [chrisr3d]
- [stix2 import] Fixed issue with self attribute used before
  declaration. [chrisr3d]
- [stix2 import] Changed 1 function name to a more relevant one.
  [chrisr3d]
- [sync] Invalid model call in the server pull using the update
  technique. [iglocska]
- [diagnostic] Updated cybox reauired default version. [chrisr3d]

  - Since the very latest version is now installed
    on every new machine generated, we can consider
    it as default version
- [stix2 import] Cleaned up duplicate function & Fixed external STIX
  files parsing. [chrisr3d]

  - External STIX files parsing improvement to come
- [stix2 import] Fixed mapping between STIX objects and galaxies fields.
  [chrisr3d]
- [stix2 export] Fixed fields exported from galaxies. [chrisr3d]

  Better mapping regarding the relevance of each field
- [stix2 import] Removed no longer used function. [chrisr3d]
- [cleanup] Loading mapping dictionary only when needed. [chrisr3d]
- [API] various fixes to the timestamp handling. [iglocska]
- [Cortex] Unset cortex content-type header when doing a GET request.
  [iglocska]
- [merge issue] resolved merge issue. [iglocska]
- [API] fixed an invalid dissection of the tag parameter if the
  parameter is not set. [iglocska]
- [cleanup] Cleanup of removed upgrade scripts. [iglocska]
- [upgrade] replay potentially missed updates. [iglocska]
- [sync] Fixed some issues throwing notices when pulling. [iglocska]
- [sync] Fix pull not working caused by the refactor. [0xiso]
- [sync] Fix pull not working. [0xiso]
- [doc] Add an option to checkout submodules recursively. [0xiso]
- Making python 3.5 happy with exception type ImportError. [chrisr3d]
- [stix import] Fixed object_relation field key for the format of the
  original imported file. [chrisr3d]

  - Following the latest changes on the object
- [Sighting] Fixed sighting creation. [chrisr3d]
- [stix1 import] Updated file parsing. [chrisr3d]

  - Including import of single attribute for the
    latest supported STIX file object
  - Including parsing of the STIX file object field
    'full_path' which can be found in any of the
    different STIX object describing files
- [stix import] Avoiding encoding errors on reading file. [chrisr3d]
- [stix import] Quick fix on the new MISP object (for original files
  imported) attributes. [chrisr3d]

  - Following the changes on the object itself
- [API] Quick fix on a dict key to fetch the name of the stix file
  imported. [chrisr3d]
- [stix import] Importing the original file binary using the data field
  in attribute instead of value field. [chrisr3d]
- [stix import] using the decoded binary of the original file imported
  as attachment. [chrisr3d]
- [RPZ] flatten attributes for the RPZ export. [iglocska]
- [API] downloading events in XML format via the UI returns JSON.
  [iglocska]
- [Feeds] Don't try to find caches for feeds that don't have caching
  enabled. [iglocska]
- [REST client] baseurl can now be set optionally in the url. [iglocska]
- [Feeds] I CAN'T MATH. [iglocska]
- [feeds] Feed caching generates a lot of notices. [iglocska]
- [documentation] added missing legacy automation page view. [iglocska]

Other
-----
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3743 from WaryWolf/unmanaged-workers. [Andras
  Iklody]

  Add "manage workers" option.
- Add "manage workers" option. [Anthony Vaccaro]

  This is enabled by default, which replicates the current behaviour of having controls to start, stop and restart workers in the server settings page.
  When set to disabled, these controls are hidden, which allows server administrators to manage the worker processes externally, e.g. via systemd.

  A sample systemd unit file has also been included into the INSTALL directory.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Raphaël Vinot]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Raphaël Vinot]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into
  chrisr3d_restSearch_tests. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into
  chrisr3d_restSearch_tests. [chrisr3d]
- Add: [restSearch] STIX 1 & 2 export for restSearch. [chrisr3d]

  Features to be merged:
  - Export of multiple MISP events
  - Fetching events and writing them into files, each
    file containing at most a number of attributes
    defined by a limit
  - Each file is then parsed instead of parsing each
    event individualy, which reduces the number of
    times the python scripts are called, reducing
    the execution time of the overall process
  - The result is then returned as on single file
    read and displayed
- Merge branch '2.4' of github.com:MISP/MISP into
  chrisr3d_restSearch_tests. [chrisr3d]
- :construction: [stix2 export] Supporting export of multiple MISP events.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into
  chrisr3d_restSearch_tests. [chrisr3d]
- :construction: [restSearch] Passing multiple events to the STIX parsing script.
  [chrisr3d]

  - atm calling the python script every 10 events
    fetched with fetchEvent
- Merge branch '2.4' of github.com:MISP/MISP into
  chrisr3d_restSearch_tests. [chrisr3d]
- :construction: [stix1 export] Supporting export of multiple MISP events.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into
  chrisr3d_restSearch_tests. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into
  chrisr3d_restSearch_tests. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into
  chrisr3d_restSearch_tests. [chrisr3d]
- :construction: [restSearch] Added stix2 export in restSearch. [chrisr3d]
- :construction: [restSearch] Stix1 export for restSearch. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3730 from FloatingGhost/2.4. [Andras Iklody]

  fix: Customauth Headers are case-sentitive, do not strtoupper
- Merge pull request #3731 from RichieB2B/ncsc-nl/show-more. [Andras
  Iklody]

  Only display "Show 2 more" and up
- Only display "Show 2 more" and up. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4. [Sami
  Mokaddem]
- Merge pull request #3729 from RichieB2B/ncsc-nl/trim-merge. [Andras
  Iklody]

  Trim spaces from source_id in merge form
- Trim spaces from source_id in merge form. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4. [Sami
  Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3725 from lhirlimann/2.4. [Alexandre Dulaunoy]

  Unify url for modules, make them usable behind proxies
- Unify url for modules, make them usable behind proxies. [Ludovic]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3723 from pettai/shibb. [Alexandre Dulaunoy]

  fix typo
- Fix docs. [Fredrik Pettai]

  fix docs
  (DefaultRoleId is not implemented in the code)
- Fix typo. [Fredrik Pettai]

  fix typo in error message
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3711 from pettai/install. [Andras Iklody]

  add missing meac dep
- Add missing meac dep. [Fredrik Pettai]

  add missing meac dep
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3707 from Rafiot/2.4. [Raphaël Vinot]

  chg: Bump PyMISP
- Merge branch 'stix2' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- Add: [export] Introduction of a framing script. [chrisr3d]

  - atm returning header, separator and footer for
    both stix 1 & 2 export
  - will do the same for other export formats, as a
    centralized script taking the parameters needed
    for the format in subject and returning the
    corresponding header, footer and separator
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- Add: [stix2 export] Added stix2 export view. [chrisr3d]
- Add: [stix2 export] Added instruction about automation part.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3664 from SteveClement/guides. [Andras Iklody]

  chg: [doc] Moved INSTALL files around to reflect a more accurate support landscape.
- Merge branch '2.4' into guides. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into guides. [Steve
  Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Proposed fix for admin add org with logo. [Sascha Rommelfangen]

  proxied via @iglocska
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Merge branch 'feature/variable_tag_value' into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3626 from 0xiso/fix-pull-progress. [Andras Iklody]

  fix: [sync] Fix pull not working
- Merge pull request #3654 from 0xiso/fix-install-doc. [Andras Iklody]

  fix: [doc] Add an option to checkout submodules recursively
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3631 from SteveClement/i18n. [Steve Clement]

  chg: [i18n] Update to languages: Danish (54%) German (17%) Japanese (100%) French (67%) Spanish (3%)
- Merge remote-tracking branch 'upstream/2.4' into i18n. [Steve Clement]
- Merge pull request #3630 from SteveClement/guides. [Steve Clement]

  chg: [doc] CentOS 7 amendments, basic functionality established
- Merge branch '2.4' into guides. [Steve Clement]
- Merge branch '2.4' into i18n. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- [stix1 import] Changed one of the generic STIX objects parser into a
  return function. [chrisr3d]

  - So we extend the list of results instead of
    having it as a parameter
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into chrisr3d_patch.
  [chrisr3d]
- Fixed bug where popoverChoice was returning undefined values for some
  browser. [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Temporary revert to avoid PGP bug. [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3623 from SteveClement/guides. [Andras Iklody]

  chg: [doc] Guides in the main code base are obosolete
- Merge remote-tracking branch 'upstream/2.4' into guides. [Steve
  Clement]
- Merge branch '2.4' into guides. [Steve Clement]
- Add: [stix1 import] Added STIX 1 object type to the mapping types.
  [chrisr3d]

v2.4.95 (2018-09-05)
--------------------

New
---
- [API] set default behaviour to require to_ids and published set to 1
  to be included in exports. [iglocska]

  - doesn't affect MISP json and xml formats
- [automation description] Added legacy mode toggle. [iglocska]
- [UI] Added an enrichment on-demand pop-up for hover modules.
  [iglocska]
- [REST client] Templating system added to the rest client. [iglocska]
- [REST client] added the api enumeration to the rest client view.
  [iglocska]
- [API] Restresponse component function added to enumerate available
  APIs for the REST client. [iglocska]

  - also, added API descriptions for the restsearch functionalities
- [ACL] Added soft validation for available API enumeration. [iglocska]
- [API] evnet level restsearch switched to new modular conversion
  system. [iglocska]
- [API] fixed two cases where the new filter parameter builder was being
  naughty. [iglocska]

  - copy-pasta fail induced skipping of parameters with only NOT parameters fixed
  - OR/AND/NOT formatted parameters with singular values (such as '{"OR": "foo"}' now handled correctly
- [API] XML export now exports both event and attribute level data.
  [iglocska]

  - relying on the old XMLConverterTool for event level conversions
- [API] OpenIOC export library correctly handles both events and
  attributes as their payload. [iglocska]

  - fixed annoying line breaks in the output
- [API] NIDS exports now correctly support event and attribute level
  exports. [iglocska]

  - also, suricata/snort rules now include both the event and the attribute tags in the metadata
- [API] JSON export library updated to support both attribute and event
  level conversions. [iglocska]

  - relies on the old JSON library for event level conversions
- [REST client] Allow skipping SSL validation. [iglocska]
- [REST client] Resolve urls and show API description if applicable.
  [iglocska]
- [API] Added the libraries for the JSON, XML and Text exports.
  [iglocska]
- [internal] SQL debug API tool added. [iglocska]

  - just pass /sql:1 to any query via the API to see a dump of all queries
  - Response isn't very clean, JSON pushed infront of whatever the output is
  - requires debug mode = 2
- [API] rework of the attribute level restsearch. [iglocska]

  - optmisation, use of external converters
  - one api to rule them all concept / controller
- [API] Made the NIDS export compatible with the new API. [iglocska]
- [API] Added the new XML converter. [iglocska]
- [api] Added new open IOC export system. [iglocska]
- [api] first revision of the attribute export. [iglocska]
- [API] reworked the attribute level restsearch. [iglocska]

  - use the new filter parameters
  - use the new condition building mechanism

  - no more pre-filtering
- [rest client] parsers for JSON/HTML return added. [iglocska]
- [rest client] parser helper css/js added. [iglocska]
- [API] CSV export tool added. [iglocska]
- [API] :construction: work in progress - moving CSV export to standardised
  converter format. [iglocska]
- [API] Added publish filter to restsearch. [iglocska]
- [API] further rework of the restsearch api. [iglocska]

  - move to the new popping filter system
- [API] rework of the event level restSearch (:construction:) [iglocska]
- [internal] Further work on the filtering. [iglocska]
- [internal] Rework of the filter handling internally. [iglocska]
- [internal] Added internal functions to interpret parameters in various
  formats / coming from various sources. [iglocska]
- [internal] Added new internal functions to be used by all export APIs
  in the future. [iglocska]

  - authenticate user via URL params if not already authenticated (to support legacy APIs)
  - harvest parameters in a standardised way for filtering all export APIs
- [API] new centralised parameter system for APIs. [iglocska]
- [refactor] CSV api refactor. [iglocska]

  - performance gains
  - first step in unifying all APIs
  - moved the CSV data lookup into fetchattributes
  - internal pagination is now more clever with a watchdog flag that can prevent unneeded executions by whatever calls fetchattributes
- [API] exposed the server related functionalities to the API.
  [iglocska]

  - server index
  - server push
  - server pull

  - improved logging / error reporting of the sync functionalities
- [i18n] Added German Translation (12%) upd: [i18n] Czech 4%, French
  19%, Danish 48%, Italian 42%, Korean 3%, Portuguese 6% [Steve Clement]
- [performance] disable the checking of expired sessions for automatic
  logouts. [Andras Iklody]
- Add install instructions. [Hannah Ward]
- Add download functionality. [Hannah Ward]
- Add upload/download for attachments. [Hannah Ward]
- Add S3 client class. [Hannah Ward]
- [tool] Generator for types/categories in all the places of MISP.
  [Christophe Vandeplas]
- [feature] Built in REST client added to test / interact with the API
  directly from MISP. [iglocska]

  - no more shitty chrome extensions that crash during trainings, rejoice!

Changes
-------
- [version] Bump. [iglocska]
- [bug] Fixed wrong event lookup in case the uuid is passed as an
  eventId. Previously the code had two mutually exclusive conditions
  `Event.id = uuid and Event.uuid = uuid` so we were getting `Invalid
  event.` error. [chkp-aliaksandrt]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [automation description] Updated the automation page to reflect the
  changes made to the restSearch APIs. [iglocska]
- [UI] made the enrichment sticky popup's trigger button behave like a
  button. [iglocska]
- [misp feed] schema fixed to include caching_enabled field. [Alexandre
  Dulaunoy]
- [misp default feeds] ipspamlist added as a feed provider. [Alexandre
  Dulaunoy]
- [doc] Fixed permissions for logrotate. [Steve Clement]
- [internal] JSONConverterTool's support for the deprecated showorg flag
  removed. [iglocska]
- [API] legacy passing of the api key via URL parameters caused an
  invalid response type. [iglocska]

  - automatically selects json now
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [cleanup] removed leftover converter. [iglocska]
- [internal] not needed conditional cleaned up. [iglocska]
- [whitelisting] Cache the whitelist values in memory for each instance
  of the whitelist model. [iglocska]

  - instead of loading it over and over
- Bump PyMISP. [Raphaël Vinot]
- [rest client] render the response by default. [iglocska]
- [querystring] version bumped. [iglocska]
- [API] Fixed fetchAttributes lookup on value to be only optionally a
  substring search. [iglocska]
- Bump PyMISP. [Raphaël Vinot]
- Try xenial on travis. [Raphaël Vinot]
- [API] further work on the new CSV export. [iglocska]
- Add more tests. [Raphaël Vinot]
- [style] function opening brackets fixed. [iglocska]
- [api] reworked the CSV api to use the new standardised function calls.
  [iglocska]
- [cleanup] removed moved and reworked harvestParameters function.
  [iglocska]
- [restResponse] Updated restResponse library to produce nicer
  exceptions. [iglocska]

  - more in-line with the standard exceptions
- [refactor] Broke contact email function up into parts. [iglocska]
- [cleanup] Removed todos from userscontroller that have become
  irrelevant. [iglocska]
- [internal] Cleanup of the pull function. [iglocska]

  - split into functions based on the concerns it handles
  - separated event download and proposal download into separate functions
- [cleanup] Removed unused view variable. [iglocska]
- [doc] MISP logo b&w only added. [Alexandre Dulaunoy]
- Bump PyMISP. [Raphaël Vinot]
- [PyMISP] updated to the latest version. [Alexandre Dulaunoy]
- [data-model] new bro attribute type to store rule in Bro rule-format.
  [Alexandre Dulaunoy]

  Fixed #3584
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-warninglists] updated to the latest version. [Alexandre
  Dulaunoy]
- [install] Some minor fixes to the install guide. [Andras Iklody]
- [performance] Only check if user is logged in if disable_auto_logout
  is not set. [Andras Iklody]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version including related changes.
  [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-warninglist] updated to the latest version. [Alexandre Dulaunoy]
- [misp-taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [visual] Changed the name of the rest client. [iglocska]

Fix
---
- [description] Typo in serverSetting fixed, fixes #3612. [iglocska]
- [API] using "download" as a returnformat via the URL breaks the
  restSearch API. [iglocska]

  - we have to keep it as a legacy option and map it to json
- [API] Fixed the broken CSV export. [iglocska]
- [stix2 export] Fixed timestamp to datetime conversion for
  'date_sighting', using utc format. [chrisr3d]
- [stix2 import] Fixed Sighting import format. [chrisr3d]
- Create temp folder if it doesn't exist in EventsController::export()
  [Xavier Mehrenberger]
- [stix2 import] Fixed some time-based attribute fields previously
  wrongly imported from STIX object fields. [chrisr3d]
- [stix2 import] Keeping uuids from STIX objects imported as attributes.
  [chrisr3d]
- [REST client] Fixed the order of execution for the various JS
  functions when changing template. [iglocska]
- [REST client] Correctly detect camelised parameters as single values
  instead of lists. [iglocska]
- [REST client] resolved issues with the URL builder for the REST
  queries causing double "/"s after the baseurl. [iglocska]
- [internal] Invalid export format detection now throws an exception
  instead of dying ungracefully. [iglocska]
- [internal] AppController minor fix. [iglocska]

  - fix bug of invalid forcing of JSON export type in certain conditions
- [API] invalid pass by reference parameter not passed as a variable.
  [iglocska]

  - fixes "Cannot pass parameter 1 by reference" bug
- [ACL] getApiInfo added to acl. [iglocska]
- [internal] Org to org_id conversion correctly handled by restSearch
  filters. [iglocska]
- [ACL] exclude afterfilter from the api checks. [iglocska]
- [internal] Whitelist model initialisation copy paste fail. [iglocska]
- [api] Added missing files. [iglocska]
- [REST client] Fixed the url parser for the client not handling named
  params. [iglocska]
- [api] added attributes controller wip changes. [iglocska]
- [internal] removed old restsearch on the attribute level. [iglocska]
- [REST client] Fixed issues with multiple values in the same header.
  [iglocska]
- [merge conflict] added merge conflict resolution. [iglocska]
- [internal] Handle tags passed via parameters not encapsulated in an
  array. [iglocska]
- [API consistency] restsearch on an attribute level should return the
  same format when hits were found and not. [iglocska]
- ['UI bug fixed'] adding an attribute could result in an exception
  after a successful addition. [iglocska]
- [REST client] fix to the JSON prettyfication. [iglocska]
- [internal] Block attributes by tag using the event level restsearch
  API. [iglocska]
- [internal] Changed the type filter function hook. [iglocska]
- [CS] Updated recent changes. [iglocska]
- CSV test. [Raphaël Vinot]
- [internal] Properly detect buggy parameters passed in the "last"
  format. [Raphaël Vinot]
- Improve testing. [Raphaël Vinot]
- Dirty install of python 3.6 on travis. [Raphaël Vinot]
- [internal] Fix to the parameter parsing of the CSV path. [iglocska]
- [API] Class name fixed. [iglocska]
- [internal] uuid filter fixed. [iglocska]

  - copypastafail
- [internal] resolveTimeDelta fixes. [iglocska]

  - handle seconds
  - return the current time as a filter if nothing is matched
- [internal] Fixed incorrect file added in previous commit. [iglocska]
- [internal] publish_timestamp was ignored by the new restsearch.
  [iglocska]
- [internal] resolveTimeDelta() check relaxed to allow for stringified
  timestmaps and floats. [iglocska]
- [internal] removed attribute.timestmap from the event level timestamp
  filters. [iglocska]
- [API] allow other returnFormats besides download to work for
  restsearch. [iglocska]
- [internal] looplimit lowered to 50k for fetchAttributes. [iglocska]

  - maybe we should base this number off the available memory somehow...
- [internal] Fixed an incorrect parameter lookup for the from/to
  timefilter parser. [iglocska]
- [API] copy pasta error in parameter harvester. [iglocska]
- [cleanup] Fixed an assignment in a comparison. [iglocska]
- [stix2 export] Reverted a previous change on timestamps. [chrisr3d]

  - Following the STIX 2.0 requirements
  - Including the latest changes on PyMISP
  - Solution adopted before any other one is found
    (for instance when 2.1 version is released)
- [stix] Timestamps patched. [chrisr3d]

  - Including the latest patches on PyMISP object
    timestamps
  - Some other quick timestamps import cleaned up
- [cleanup] Cleaned up STIX incident creation. [chrisr3d]
- [stix2 export] Fixed some timeline related fields. [chrisr3d]

  - for instance 'valid_from' should not be related
    to timestamp
  - Added the 'created' field in report as well,
    using the event date
- [Taxonomies] Taxonomy update broken if no expanded values are provided
  on the predicate or entry level. [iglocska]
- Old python crap. [Raphaël Vinot]
- [stix2 import] Importing regkey & regkey|value as attribute and not
  regkey object. [chrisr3d]
- [stix1 export] Stripping registry keys and values to avoid spaces.
  [chrisr3d]
- [feeds] Custom headers / authorization broken on csv/freetext feeds,
  fixes #3581. [iglocska]
- [cleanup] Reduced credential objects parsing complexity. [chrisr3d]
- [cleanup] Made Exceptions happy specifying types. [chrisr3d]
- [cleanup] Cleaned up Course of Action parsing. [chrisr3d]
- [cleanup] Made exceptions happy + cleaned up if statement. [chrisr3d]
- [cleanup] Reduced complexity of the email objects parsing. [chrisr3d]
- [cleanup] Cleaned up Exception handling. [chrisr3d]
- [cleanup] Minor cleanup on custom objects parsing functions.
  [chrisr3d]
- [cleanup] Reduced the main function complexity. [chrisr3d]
- [cleanup] Cleaned up libraries import. [chrisr3d]
- [cleanup] Reduced complexity in PE objects parsing. [chrisr3d]
- [cleanup] Cleaned up libraries import. [chrisr3d]
- [i18n] Variables are in no need to be translated, it will break stuff,
  horribly. upd: [i18n] Update default.pot again. [Steve Clement]
- [statistics] Solve the issue with the unfiltered total counters in the
  user and org statistics. [iglocska]
- ['UI bug fixed'] adding an attribute could result in an exception
  after a successful addition. [Andras Iklody]
- [statistics] fixed an issue where the org statistics didn't correctly
  apply the local filters. [iglocska]

  - both local and external just showed the sum totals instead of the individual pools
- [instructions] remove suggestion to check out last tagged version on
  install. [Andras Iklody]
- Use configured attachments_dir instead of app/files/ in
  ShadowAttributesController.php. [Xavier Mehrenberger]
- [typo] in S3 impementation. [Andras Iklody]

  - Thanks @FloatingGhost for noticing
  - I hope your love for PHP will never cease to grow!
- Add PHP SDK install instructions. [Hannah Ward]
- [API] Allow rapid changes to attributes (>1 per second) [iglocska]
- [encryption] broken S/MIME encryption. [iglocska]

  - as reported and pinpointed by @3c7
  - blind fix, awaits confirmation
- [usersStat] allow fetching json of statistics/users. [Sami Mokaddem]
- [cleanup] Improvement of some for loops. [chrisr3d]
- [stix2 import] Fixed uuid of single ip attributes. [chrisr3d]
- [cleanup] Cleaned up duplication of code from the previous commit.
  [chrisr3d]
- [cleanup] Cleaning up objects parsing. [chrisr3d]
- [UI] fixed missing sighting sparklines. [iglocska]
- [bug] fixed a typo preventing the attack matrix from working.
  [iglocska]
- [rest client] corrected the calculation of the rest client duration.
  [iglocska]

  - I can't maff gud
- [API] Some API rearrange issues fixed in events/add. [iglocska]

Other
-----
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3530 from chkp-aliaksandrt/fix-object-add-if-uuid-
  is-passed-as-eventid. [Andras Iklody]

  chg: [bug] Fixed wrong event lookup in case the uuid is passed as an eventId.
- Merge pull request #3518 from zeroq/sync_sightings_on_publish. [Andras
  Iklody]

  Sync sightings on publish
- Provide uuid of new sighting to save function. [jgo]
- Check if sighting with given uuid already exists before saving new
  sighting. [jgo]
- Todo added: do not add sightings that are already there. [jgo]
- Attach found sightings to event item. [jgo]
- Add attribute UUID to sighting item (easier for synchronization) [jgo]
- Merge pull request #3546 from WaryWolf/gpg-clearsign-fix. [Andras
  Iklody]

  Split GPG signing and encrypting of outgoing emails into separate operations
- Split signing/encryption decisions into a separate method. [Anthony
  Vaccaro]
- Split GPG signing and encrypting of outgoing emails into separate
  operations. Allows for plaintext signing of outgoing emails. [Anthony
  Vaccaro]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3610 from RichieB2B/patch-3. [Andras Iklody]

  Prevent STIX export crash
- Prevent STIX export crash. [Richie B2B]

  attribute can be None which causes the STIX conversion to crash
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3609 from SteveClement/2.4. [Steve Clement]

  chg: [doc] Fixed permissions for logrotate
- [chg] fix: Set correct perms for log rotate, faup fixed upstream.
  [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3608 from Lastpixl/fix-export. [Andras Iklody]

  fix: create temp folder if it doesn't exist in EventsController::expo…
- Add: [stix2 import] Parsing 'valid_until' in indicators as expiration
  date in Sightings. [chrisr3d]
- Add: [stix2 export] Parsing expiration date from sightings as
  'valid_until' in indicators. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch 'feature/api_rework2' into 2.4. [iglocska]
- Merge branch 'feature/api_rework' into feature/api_rework2. [iglocska]
- Merge branch 'feature/api_rework' into 2.4. [iglocska]
- Merge branch '2.4' into feature/api_rework. [iglocska]
- Merge branch 'feature/api_rework' of github.com:MISP/MISP into
  feature/api_rework. [iglocska]
- Merge branch 'feature/api_rework' of github.com:MISP/MISP into
  feature/api_rework. [Raphaël Vinot]
- Merge branch '2.4' into feature/api_rework. [iglocska]
- Merge branch 'feature/api_rework' of github.com:MISP/MISP into
  feature/api_rework. [iglocska]
- Merge branch 'feature/api_rework' of github.com:MISP/MISP into
  feature/api_rework. [iglocska]
- Merge branch 'feature/api_rework' of github.com:MISP/MISP into
  feature/api_rework. [Raphaël Vinot]
- Merge branch 'feature/api_rework' of github.com:MISP/MISP into
  feature/api_rework. [iglocska]
- Merge branch '2.4' into feature/api_rework. [iglocska]
- Merge branch 'feature/api_rework' of github.com:MISP/MISP into
  feature/api_rework. [iglocska]
- Merge pull request #3557 from Rafiot/feature/api_rework. [Raphaël
  Vinot]

  Feature/api rework
- Merge pull request #3551 from Rafiot/feature/api_rework. [Raphaël
  Vinot]

  chg: try xenial on travis
- Merge branch '2.4' into feature/api_rework. [iglocska]
- Merge branch '2.4' into feature/refactortime. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into feature/refactortime.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3597 from lcpdn/patch-12. [Alexandre Dulaunoy]

  Add french translation on default.po (18% > 60%)
- Update default.po. [lcpdn]

  Going from 18% to 60% on crowdin with my parts.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3587 from droe/2.4. [Andras Iklody]

  Fix broken timestamps by using 24 hour clock and ISO 8601 date format
- Fix broken timestamps by using 24 hour clock and ISO 8601 date format.
  [Daniel Roethlisberger]

  The event view shows a wrong "Last change", e.g. "2018/08/23 06:01:45"
  for "2018/08/23 18:01:45".  The same problem affects the timestamp in
  the XML generated by IOCExportTool.php.  Fix by correcting the PHP
  date() code "h" to "H".

  While here, also switch to a clearer ISO 8601 date representation for
  "Last change", using dashes instead of slashes for separation of year,
  month and day.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3579 from SteveClement/2.4. [Steve Clement]

  fix: [i18n] Variables are in no need to be translated, it will break stuff.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3578 from SteveClement/2.4. [Steve Clement]

  upd: [i18n] Fixed easy missing __()
- Upd: [i18n] Fixed easy missing __() [Steve Clement]
- Merge pull request #3577 from SteveClement/2.4. [Steve Clement]

  upd: [i18n] Update of default English PO template
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge pull request #3576 from SteveClement/2.4. [Steve Clement]

  new: [i18n] Added German Translation (12%)
- Merge pull request #3575 from SteveClement/2.4. [Steve Clement]

  upd: [i18n] 100% Japanese translation.
- Upd: [i18n] Update of default English PO template. [Steve Clement]
- Upd: [i18n] 100% Japanese translation. [Steve Clement]
- Merge pull request #3570 from Lastpixl/fix_attachments_dir. [Andras
  Iklody]

  fix: use configured attachments_dir instead of app/files/ in ShadowAt…
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3560 from FloatingGhost/malware-to-s3. [Andras
  Iklody]

  Use AWS S3 as an attachment storage
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3556 from mokaddem/fixUserStats. [Alexandre
  Dulaunoy]

  fix: [usersStat] allow fetching json of statistics/users
- Merge pull request #3555 from WaryWolf/change-password-permissions-
  fix. [Alexandre Dulaunoy]

  Add a permission check to the change password page.
- Add a permission check to the change password page. [Anthony Vaccaro]

  The 'MISP.disableUserSelfManagement' config variable is checked
  when rendering the link to the change password page, but is not checked
  when rendering the page itself. This could lead to unauthorised
  password changes by users with existing accounts on the MISP
  instance.
- Merge pull request #3553 from PaoloVecchi/patch-9. [Alexandre
  Dulaunoy]

  Update EventsController.php
- Update EventsController.php. [Paolo Vecchi]

  Just a ) missing.
- Merge pull request #3552 from PaoloVecchi/patch-7. [Alexandre
  Dulaunoy]

  Update AttributesController.php
- Update AttributesController.php. [Paolo Vecchi]

  Just a couple of ')' missing in lines 2105 and 2263
- Merge pull request #3549 from PaoloVecchi/patch-7. [Alexandre
  Dulaunoy]

  Update report_validation_issues_events.ctp
- Update report_validation_issues_events.ctp. [Paolo Vecchi]

  Speling mistake? 'V' of validation outside php tag.
- Merge pull request #3550 from PaoloVecchi/patch-8. [Alexandre
  Dulaunoy]

  Update index.ctp
- Update index.ctp. [Paolo Vecchi]

  Added space between 'events' and 'on'
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3547 from PaoloVecchi/patch-6. [Andras Iklody]

  Update INSTALL.ubuntu1804.with.webmin.txt
- Update INSTALL.ubuntu1804.with.webmin.txt. [Paolo Vecchi]

  systemd sucks!
  ;-)
- Merge pull request #3542 from PaoloVecchi/patch-5. [Andras Iklody]

  Update INSTALL.ubuntu1804.with.webmin.txt
- Update INSTALL.ubuntu1804.with.webmin.txt. [Paolo Vecchi]

  Fixed a few small things
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge remote-tracking branch 'origin/2.4' into 2.4. [Christophe
  Vandeplas]

v2.4.94 (2018-08-09)
--------------------

New
---
- [PGP] Added fingerprint to /users/verifyGPG. [iglocska]
- [internal] Streamlining of the push process. [iglocska]

  - rework of the internals
  - cleaner separation of concerns into more specialised functions
- [internal] Simplication of the push functionality. [iglocska]
- [API] rework of the attribute fetcher. [iglocska]

  - correctly handles attribute tags
  - performance improvements due to rework of the internal pagination
  - fixes to issues with too many hits on a tag search causing queries that are too long
- [internal] subQueryGenerator changes. [iglocska]

  - fixed some issues that made it non-usable before
  - added possibility to run negations (NOT IN)
- [internal] Added helper functions for tag lookups. [iglocska]
- [CLI] Get the API key of a given user using the CLI. [iglocska]

  - simply run /var/www/MISP/app/Console/cake Admin getAuthkey [user_email]
- Added table for user settings. [iglocska]
- [eventGraph] added jpeg export. [Sami Mokaddem]
- [eventGraph] added network preview feature. [Sami Mokaddem]
- [eventGraph] SharingGraph: added skeleton of Model/Controller for
  saving and sharing the network among organisations (+ javascript
  interaction functions) [Sami Mokaddem]
- [eventGraph] DOT Language export. [Sami Mokaddem]
- [eventGraph] Skeleton of network history + capability to add custom
  row button in actionTable. [Sami Mokaddem]
- [eventGraph] Briefly validate imported file + fix node position on
  drag. [Sami Mokaddem]
- [eventGraph] Possibility to import/export (json) event graph. [Sami
  Mokaddem]
- [js_helpers] empty cells and 2 widgets. [Sami Mokaddem]
- [Statistics] Added a new tab to the statistics showing the
  user/organisation additions over the past month/year. [iglocska]
- Add install docs. [Hannah Ward]
- Add ability to log to elasticsearch. [Hannah Ward]
- Add elasticsearch settings. [Hannah Ward]
- [API] Check for malformed JSON requests. [iglocska]
- [attackMatrix] possibility to pick multiple galaxy to attach to the
  event in at the event-level. [Sami Mokaddem]
- [attackMatrix] contextual menu when clicking on a cell in the event
  ATT&CK matrix. [Sami Mokaddem]
- [CLI] Added update commands for Taxonomies, Warning Lists, Notice
  Lists and Object Templates. [Steve Clement]
- [sync] Improvements to the pull mechanism. [iglocska]

  - moved the blacklist event skipping to the negotiation phase
  - no longer need to pull and then discard events that have been blacklisted
  - solves issues with slow syncs when a lot of deletions were involved

  - also, moved the sync negotiation + event retrieval to UUID based lookups instead of ID
- [internal] Added convenience function to get estimated row count for a
  table. [iglocska]
- [API] Updated the timestmap handling in the restSearch APIs to use the
  new smart-system. [iglocska]
- [internal] setTimestampConditions unified and improved. [iglocska]

  - no more separate codepath for setPublishTimestampConditions
  - accept shorthand time descriptions (1d, 5h, etc)
  - always accept single values or arrays with start/end times
- [galaxies] Force update galaxies and update improvements in general.
  [iglocska]

  - passing /1 to the galaxy update function now forces updates on all clusters
  - performance improvements
- [data model] Added support for monero - new type xmr. [iglocska]

  - soft validation
  - secondary validation with warnings for malformed addresses
  - supporting epic facial hair styles
- [edit strategy API] To support a smoother integration with the Hive,
  new API that describes what the edit strategy is for an event.
  [iglocska]

  - GET on /events/getEditStrategy/[id]
    - where id can be either a local ID or a UUID

  - returns a JSON dictionary with the following fields:
    - strategy: edit | extend (edit if it's an own event, extend otherwise)
    - extensions: list of dictionaries with existing extensions created by the user's org (containing the id, uuid, info fields)

  - The algorithms implementing this should prioritise as such:

  1. Check if user can edit the event (strategy == edit) - if yes, edit
  2. If no, check if extensions exist - if yes, edit one of those
  3. If no, create a new extension to the original event
- [sync] Added flag to avoid using the proxy. [iglocska]

  - in some cases you have internal sync between instances in which case going through the proxy is silly
- [Session handling] Force certain session values to fix existing issues
  with misconfigured instances. [iglocska]
- [Session handling] Added checkAgent toggle. [iglocska]
- [API] Added unsafe URL parameter to authenticate users. [iglocska]

  - for legacy tools that cannot pass headers in HTTP requests for some insane reason
  - Needs to be enabled by a site admin - default is that it is disabled
  - MISP's diagnostic tool WILL complain if this is ever enabled

Changes
-------
- [release] Version bump. [iglocska]
- [internal] Refactor of the pull function. [iglocska]

  - the various event ID list collection methods are now decided in an external function
- [cleanup] Removed the 2.3 -> 2.4 upgrade. [iglocska]

  - in case you are reading this and wondering why it's gone:
    - 2.4 came out in 2014
    - If you are still running that version, just upgrade to any prior 2.4 and then upgrade from that version on
    - Also hope that no one will ever find this message relevant, 3+ year old software is just bad.
- [cleanup] Cleanup of the server settings reader. [iglocska]

  - split into more readable functions
- [internal] Rework of the emailing. [iglocska]

  - extracted the encryption functions out from the main e-mailing function
  - simplification of the code in several places
- [cleanup] removed pointless TODOs. [iglocska]
- [cleanup] Removed duplicate capture field definitions. [iglocska]
- [cleanup] removed duplicate branching code to set module setting
  defaults. [iglocska]
- [internal] moved socket / request creation to appmodel. [iglocska]
- [PyMISP] updated to the latest version of describeTypes. [Alexandre
  Dulaunoy]
- [except] Closed the brackets correctly on the throw except. [Steve
  Clement]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [internal] instead of replicating the event level distribution rules,
  the attribute model now inherits the event code. [iglocska]
- [internal] Opened the buildConditions code up to other models.
  [iglocska]
- [cleanup] Removed duplicate httpsocket setups. [iglocska]
- [refactor] Unified event conditions creation. [iglocska]
- [cleanup] removed duplicate logging code. [iglocska]
- [cleanup] added function to check for prio worker's existance in
  Event.php. [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [documenation] Added CLI documentation for the getAuthkey tool.
  [iglocska]
- [PyMISP] updated to the latest version. [Alexandre Dulaunoy]
- [misp-taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [i18n] update from crowdin, French (13%) Danish (43%) Italian (25%)
  Japanese (86%) Korean (2%) Portuguese (6%) Spanish (1%) [Steve
  Clement]
- [csv] added the object_relation field to the CSV export. [iglocska]
- [misp-taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [stix2 import] Preparation for the upcoming changes on stix2 files to
  import due to the multi export. [chrisr3d]
- [form] Give change Password field focus. [Steve Clement]
- [psr-2] Changed view files to space indentation instead of tabs.
  [iglocska]

  - *sniff sniff*
- [CS] Changed to PSR-2. [iglocska]

  - to make contributions easier, adopted PSR-2
  - used php-cs-fixer to rework the style
  - *sniff sniff* Goodbye tab indentation
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [misp-taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [i18n] update default.pot to include all new strings. Updated
  cze/fra/ita/jpn/kor/PT_br new: [i18n] Spanish translation file. [Steve
  Clement]
- [kali] small typo in git config. [Steve Clement]
- [stix2 export] Updated Galaxies parsing. [chrisr3d]
- [stix2 import] Importing pe object custom properties. [chrisr3d]

  - Following the last changes on stix2 export
- [stix2 export] Exporting not mapped attributes from pe objects as
  custom properties. [chrisr3d]
- [kali] redis on boot (for persistent setups) [Steve Clement]
- [kali] added headers to vhost. More automation in rc.local. [Steve
  Clement]
- [kali] added expect to make it work on kali-light. [Steve Clement]
- [debian] Added profile change to take viper/cake into consideration.
  [Steve Clement]
- [stix2 export] Updated galaxy types parsing (improvement + types
  added) [chrisr3d]
- [stix2 export] Parsing Galaxies in attributes level. [chrisr3d]
- [kali] disabled sleep, fixed database.php creation. [Steve Clement]
- [kali] tpm module wants to be loaded before install rng-tools. [Steve
  Clement]
- [kali] Fixed expect, finally, perms for viper fixed too. [Steve
  Clement]
- [kali] make sure the tpm module is laoded for more rng. [Steve
  Clement]
- [kali] use chpasswd to changes password non-interactively. [Steve
  Clement]
- [kali] Shuffle final output. [Steve Clement]
- [kali] Changed the way expect gets data. [Steve Clement]
- [kali] Moved db connection blurb around, tried to fix EOF. [Steve
  Clement]
- [kali] Checked for misp db presence, made misp.local a thing. [Steve
  Clement]
- [kali] Drop user to non-root user. [Steve Clement]
- [kali] Refactor script, everything runs as root now, but MISP user
  will be created. [Steve Clement]
- [kali] Wrapped installer in function. [Steve Clement]
- [kali] Prepared installer for running in a function. [Steve Clement]
- [kali] Fixed if typo. [Steve Clement]
- [doc] Kali script typo. [Steve Clement]
- [doc] Added check for misp user if run twice… [Steve Clement]
- [doc] Add bootstrap function for Kali. [Steve Clement]
- [doc] Kali viper-web improvement. [Steve Clement]
- [doc] More kali linux fixes. [Steve Clement]
- [doc] Added mail2misp fixed some automation. [Steve Clement]
- [doc] Debian tweaks and fix for misp-dashboard. [Steve Clement]
- [i18n] updated fra/ita/jpn/pt new: [i18n] Added initial Czech
  translation. [Steve Clement]
- [i18n] wrap stuff into  __construct( [Steve Clement]
- [i18n] More __(); [Steve Clement]
- [i18n] Added more __()'s. [Steve Clement]
- [i18n] typo. [Steve Clement]
- [i18n] Added __('') where needed/missing. [Steve Clement]
- [stix2 export] Preliminary changes to prepare a multi events stix2
  export coming soon. [chrisr3d]
- [eventGraph] refacto after comments from the Overmind. [Sami Mokaddem]
- [appController] bumped query version. [Sami Mokaddem]
- [eventGraph] removed useless comments and checks. [Sami Mokaddem]
- [eventGraph] renaming EventNetworkHistory into simply EventGraph.
  [Sami Mokaddem]
- [ACL] bumped to reflect networkHistory controller. [Sami Mokaddem]
- [eventGraph] fixed img_preview size, catch keyboard inputs and removed
  useless function. [Sami Mokaddem]
- [eventGraph] removed possibility to import eventGraph. [Sami Mokaddem]
- [eventGraph] Usage of fetchEvent function, refacto + sorting on
  creation date + disabling button if user is not authorized to
  save/delete/.. the network. [Sami Mokaddem]
- [eventGraph] only networkHistory user creator can delete its saved
  network. [Sami Mokaddem]
- [eventGraph] implemented loading graph from the db. [Sami Mokaddem]
- [eventGraph] Implemented saving/deleting feature. [Sami Mokaddem]
- [eventGraph] rightCliking on the graph select undelying node. [Sami
  Mokaddem]

  This allows faster contextualMenu operations
- [eventGraph] better support of hidden event (possibility to show
  hidden item back latter on) [Sami Mokaddem]
- Move elasticsearch to composer "suggest" [Hannah Ward]
- [deps] There is no major difference between 2.1.0.17 and the dev
  version. [Steve Clement]
- [kali] fix. [Steve Clement]
- [kali] fix redis install. [Steve Clement]
- [kali] misp-modules start on install. [Steve Clement]
- [kali] added SSL, removed manual redis install. [Steve Clement]
- [kali] skip dist-upgrade for time reasons. [Steve Clement]
- [kali] Fixed perms at the end. [Steve Clement]
- [doc] Adapted auto messages. [Steve Clement]
- [doc] Updates to Debian guides, mostly cake automation new: [doc]
  Install doc/script for kali linux deployment. [Steve Clement]
- [i18n] Latest jpn translation (94%), Latest French (10%) updated
  default.pot new: [i18n] Initial Italian translation (25%), Spanish
  (1%), Brazilian Portuguese (3%), Korean (1%) [Steve Clement]
- [i18n] updated cake i18n extract --extract-core no --exclude
  Test,Vendor,Lib. [Steve Clement]
- [CLI] Updated admin commands and added FIXMEs. [Steve Clement]
- [misp-warninglists] updated to the latest version. [Alexandre
  Dulaunoy]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [doc] More updates on the debian install guides, small fix on OpenBSD.
  [Steve Clement]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [attackMatrix] UI improvement (contextual menu) [Sami Mokaddem]
- [attackMatrix] UI improvements. [Sami Mokaddem]
- [attackMatrix] support of quick tagging from the attackMatrix at event
  view level. [Sami Mokaddem]
- [attackMatrix] improved CSS and positioning of the contextual menu.
  [Sami Mokaddem]
- [CLI] updated noticelist response for no update needed. [iglocska]
- [stix2 import] Set distribution values to the default ones. [chrisr3d]
- [CLI] added force argument. [Steve Clement]
- [travis] add PHP 7.2 tests. [Alexandre Dulaunoy]
- [PyMISP] updated to latest version. [Alexandre Dulaunoy]
- [stix2 import] Importing file objects attachments (malware-sample)
  [chrisr3d]
- [stix2 export] Exporting file objects attachments (malware-sample)
  [chrisr3d]
- [doc] Added $PATH_TO_MISP where necessary. [Steve Clement]
- [doc] Further debian install guide automation. [Steve Clement]
- [doc] regrouped all the apt install. [Steve Clement]
- [doc] Debian 9/testing updates base MISP now fully working. [Steve
  Clement]
- [doc] Merged changes from stable to testing. [Steve Clement]
- [cleanup] Removed the deprecated GFI sandbox import. [iglocska]

  - Burn the heretic. Kill the mutant. Purge the unclean.
- [stix2] added attachment encoding to the stix2 export. [iglocska]
- Remove unused variable. [Raphaël Vinot]
- [stix2 import] Importing email objects custom properties +
  improvement. [chrisr3d]
- [doc] removed python2 deps. [Steve Clement]
- [guide] More automation on install guide. [Steve Clement]
- [refactor] Fixed an issue where too many events would cause a query
  too large for mysql to handle when querying /events/index via the API,
  fixes #3444. [iglocska]
- Case insensitive sort of organisation list. [Dawid Czarnecki]
- [internal] Don't try to convert shorthand time notations to timestamp
  if the data is already in timestamp format. [iglocska]
- [CLI] Convert "false" and "true" for setSettings to 0 and 1
  respectively, fixes #3408. [iglocska]
- Add shebangs. [Raphaël Vinot]
- Mispzmq -> python3.6. [Raphaël Vinot]
- [stix2 import] Updated asn objects import to include custom
  properties. [chrisr3d]
- [stix2 import] Variable name changed for more clarity with MISP
  objects property 'name' [chrisr3d]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [stix2 export] Exporting not mapped email object attributes as custom
  properties. [chrisr3d]
- [stix2 export] Exporting not mapped asn attributes object as custom
  properties. [chrisr3d]
- [UI] Cleaned up proposal correlations and unified attribute/proposal
  correlation view code. [iglocska]
- [PyMISP] updated to latest version. [Alexandre Dulaunoy]
- [PyMISP] released as 2.4.93. [Alexandre Dulaunoy]
- [Session handling] Added some sane defaults to the session handler.
  [iglocska]
- Move old install guides to a sub directory. Init submodules at the
  right place. [Raphaël Vinot]
- [attackMatrix] Moved the submit button above the Cancel button. [Sami
  Mokaddem]

  making the matrix's UI more consistent with the application's UI.
- [stix2 import] Moved objects parsing dictionary into the main script.
  [chrisr3d]

  - In case wee need to call self in one of the
    functions called by the dictionary
- [stix2 export] Little update on pe-section export as pattern.
  [chrisr3d]

  - Added a section index in the identification part
    of the pattern, to avoid confusions  between
    each section

Fix
---
- [stix1 import] Fixed journal entries parsing fails. [chrisr3d]
- [stix1 import] Copy/paste error fixed. [chrisr3d]
- [cleanup] Some more minor clean up. [chrisr3d]
- [stix1 export] MISP objects parsing improvement. [chrisr3d]
- [sync] Fixed an issue blocking the syncing of edits, fixes #3537.
  [iglocska]
- [pgp] left of changes for the pgp printout. [iglocska]
- [cleanup] Fixed libraries import copy/paste issues. [chrisr3d]
- [stix2 import] Fixed quote error in a dictionary key. [chrisr3d]
- [stix2 import] Fixed some STIX objects parsing, reading them as dict
  in order to avoid error on popping elements. [chrisr3d]
- [stix2 import] Avoided try/catch-ing the loading function so we get
  the error if it fails. [chrisr3d]
- [stix2 import] Removed obsolete parsing function & try/catch for
  custom objects. [chrisr3d]

  - With the 'allow_custom' parameter set to True,
    the parsing function works even with custom
    objects
- [bug] Fixed e-mailing bug introduced during the refactoring.
  [iglocska]
- [bug] Fixed several server settings related issues caused by the
  refactor. [iglocska]
- [sync] typos fixed. [Andras Iklody]
- [sync] Fixed buggy connection test. [iglocska]

  - refactor revealed that the sync user access on the remote was never correctly determined
  - fallback method that has since been removed for 2+ year old instances was always used due to the above issue
- [internal] tightened authkey validation. [iglocska]
- [cleanup] Invalid assignment in conditional cleaned up. [iglocska]
- [cleanup] Cleaned up SMIME certificate validation. [iglocska]

  - merged the two functionalities we've had for it
- [stix2 import] Importing attribute tags from labels. [chrisr3d]
- [stix2 export] Added attribute tags in stix labels. [chrisr3d]
- [stix2 export] Avoiding issues with empty data field in attributes.
  [chrisr3d]
- [internal] removed massive duplicate lookup function. [iglocska]
- [cleanup] removed empty if statement. [iglocska]
- [internal] streamlining the worker removal logging. [iglocska]
- [cleanup] Removed duplicate code. [iglocska]
- [cleanup] Cleaned up exceptions types. [chrisr3d]
- [cleanup] Cleaned up exceptions types, unnecessary else after return
  and multiple statements in single line. [chrisr3d]
- [cleanup] Quick cleanup. [chrisr3d]
- [cleanup] Cleaned up exceptions types, typechecks and other minor
  items. [chrisr3d]
- [cleanup] Cleaned up libraries imports. [chrisr3d]
- [cleanup] cleaned up the setup of httpsockets in the Server.php file.
  [iglocska]
- [internal] removed duplicate logging code. [iglocska]
- [cleanup] removed unneeded concat. [iglocska]
- [internal] cleanup of some junk. [iglocska]
- [internal] serveral unreachable breaks removed. [iglocska]
- [internal] removed unreachable break. [iglocska]
- [internal] Fixed invalid assignment. [iglocska]
- [bug] Fixed cryptic ##COMMA## in error message. [iglocska]
- [tests] CSV export. [Alexandre Dulaunoy]
- [galaxies] Fixed same value across two namespaces causing issues.
  [iglocska]
- [csv] escaped all string fields to fix some oddities. [iglocska]
- [upgrade] fixed incorrect upgrade scripts. [iglocska]
- [stix1 export] Removed try catch statements used before depending on
  the python version. [chrisr3d]

  - Useless now because of python3 forced
- [stix1 export] Fixed missing namespace schema location + various code
  cleaning on framing. [chrisr3d]
- [stix1 export] Removed not used libraries import on framing.
  [chrisr3d]
- [stix2 import] Importing Galaxy Cluster uuid. [chrisr3d]
- [stix2 import] Fixed missing field info, forgotten in the latest
  changes. [chrisr3d]
- [stix2 import] Skipping relationships atm to avoid errors. [chrisr3d]

  - Relationships parsing to come later
- [cleanup] Cleanup of accidental inclusion of a feature in progress.
  [iglocska]
- [API] don't allow the same event tag to be added multiple times via an
  /events/add call, fixes #3507. [iglocska]
- [data model] Preparation for some taxonomy improvements. [iglocska]
- [stix1 export] Fixed indentation. [chrisr3d]
- [stix2 import] Improved file reading in loading function. [chrisr3d]
- [stix2 export] Fixed missing variable assignment. [chrisr3d]
- [install] Changed the install instructions to use CLI commands...
  [Andras Iklody]

  ...instead of updating config.php. The latter can be dangerous if typos pop-up.
- [API] set attribute distribution if it isn't set in the capture
  attribute call. [iglocska]

  - should have worked via the beforevalidate() but it didn't
  - ah well
- [delegation] Attribute tags and objects were not transfered during
  delegation, fixes #3495. [iglocska]

  - The delegation system hasn't been updated since the introduction to the new systems
  - new objects being transferred: objects, attribute tags, object references
- [stix2 import] Fixed relationship import. [chrisr3d]

  - Skipping it at the moment
  - Will have to rebuild a large part of the import
    functions to include relationships after the export
    part is reworked completely
- [stix2 import] Fixed vulnerability import, following the last changes
  on export part. [chrisr3d]
- [stix2 export] Fixed vulnerability export. [chrisr3d]

  - depending on the origin of the object exported:
    attribute/object or galaxy
- [bug] Fixed an invalid count() call on the taxonomies index.
  [iglocska]
- [i18n] Made PO importable into crowdin. [Steve Clement]
- [stix2 export] Fixed relationships mapping typo. [chrisr3d]
- [stix2 export] Watching if a cluster uuid has already been added to be
  exported instead of a galaxy uuid. [chrisr3d]
- [stix2 export] Allowed custom properties for all
  Indicators/ObservedData from MISP objects export. [chrisr3d]
- [stix2 export] Fixed regkey|value attribute export. [chrisr3d]
- [stix2 export] Exporting not mapped attributes of regkey objects as
  custom properties. [chrisr3d]
- [API] Attribute edit via uuid fails as non site admin, fixes #3487.
  [iglocska]
- [AppModel] re-apply the eventGraph SQL query. [Sami Mokaddem]
- [AppModel] added missing comma in SQL update query. [Sami Mokaddem]
- [doc] added sudo verification to guide. [Steve Clement]
- [doc] added sudo verification to guides. [Steve Clement]
- [eventGraph] export now works on firefox. [Sami Mokaddem]
- [i18n] Indentation. [Steve Clement]
- [i18n] added missing %s. [Steve Clement]
- [i18n] added missing echo. [Steve Clement]
- [i18n] Typos and __('Fixes') [Steve Clement]
- [stix2 export] Fixed failing condition on filename|hash composite
  attribute. [chrisr3d]
- [eventGraph] removed 'import' label from the contextual header button.
  [Sami Mokaddem]
- [actionTable] correctly delete row based on id or position + correctly
  handle row_action options. [Sami Mokaddem]
- [mispJS] updated submitDeletion to match the new eventGraph history
  name. [Sami Mokaddem]
- [eventGraph] fix validation and Model class name. [Sami Mokaddem]
- [eventGraph] fixed conditions about determining if loaded graph is the
  latest version. [Sami Mokaddem]
- [eventGraph] catch empty node selection if no underlying node is
  there. [Sami Mokaddem]
- [eventGraph] Object get correct color when exporting in DOT Language.
  [Sami Mokaddem]
- [eventGraph] typo in eventId compatibility validation. [Sami Mokaddem]
- [eventGraph] swapped function call to hide expanded objectAttribute.
  [Sami Mokaddem]
- [eventGraph] canvas menu (right-click) is shown at the correct
  position. [Sami Mokaddem]
- [stix2 import] Fixed custom properties parsing following the last
  changes on x509 object export. [chrisr3d]
- [python3] Updated script to python3 only. [iglocska]
- [python3] Missed python3 call instead of python. [iglocska]
- [i18n] Added default language. [iglocska]
- One final indentation re-align. [Hannah Ward]
- Make indentation line up. [Hannah Ward]
- Use spaces entirely. [Hannah Ward]
- Indentation on ES client. [Hannah Ward]
- [stix2 export] Fixed malware-sample data export as pattern. [chrisr3d]
- [update] checkout the last checked in version of composer.json before
  attempting a pull. [iglocska]
- [zmq] Fixed execution of the ZMQ start/stop commands still being
  python 2. [iglocska]
- Because people use old python. [Raphaël Vinot]

  Should fix #3475
- [kali] Fix RAW URL. [Steve Clement]
- [freetext] parser was detecting any number as a phone number, fixes
  #3469. [iglocska]

  - new requirement: must start with + or contain a -
- [settings] Make travis happy. [iglocska]
- [settings] Attempted fix to appease Travis. [iglocska]
- [CLI] mixup corrected. [Andras Iklody]
- [settings] Default setting for the attachments directory fixed.
  [iglocska]
- Export events csv with CR (fix #3458) [kalyparker]

  Export using automation functionnality for ids does not clean the special char like CRLF.
  When there is a carriage return in the event info, the csv is broken.
- [attackMatrix] pressing ESC dismiss the matrix popup. [Sami Mokaddem]
- [sti2 import] Fixed pe-extension parsing. [chrisr3d]
- [stix2 import] Including import of custom properties for pe & pe-
  section objects. [chrisr3d]
- [stix2 export] Fixed file object references with its contained data
  object. [chrisr3d]
- [stix2 export] Fixed File PE Binary extension. [chrisr3d]
- [sti2 import] Fixed import of some attributes that can contain data.
  [chrisr3d]
- [stix2 import] Removed try catch on adding attribute to event.
  [chrisr3d]
- [UI] Fixed the sighting buttons being (non-functionally) available to
  read only users. [iglocska]
- [API] Removed unused optional field from the organisation API
  descriptions. [iglocska]
- [feed] Invalid lookup when editing events via MISP feeds throws notice
  error, fixes #3366. [iglocska]
- [stix2 export] Fixed parsing of some attributes which can contain
  data. [chrisr3d]
- Fix: [stix2 export] Removed ip @ type parsing function duplication.
  [chrisr3d]
- [CLI] Update noticelists correctly passes the user data. [Andras
  Iklody]
- [PyMISP] updated to the latest version. [Alexandre Dulaunoy]
- [performance] Changed regex clean all function to work in a chunked
  fashion. [iglocska]
- [cleanup] Removed duplicate line, fixes #3448. [iglocska]
- [python version] changed generate_file_objects.py's execution to
  python3. [iglocska]
- [cleanup] Reverted lax baseurl validation. [iglocska]
- [sync] pull giving some weird messages when an event is blocked by
  blacklists. [iglocska]

  - don't warn about failed pulls when the reason is a local blocking of the event.

  - future improvements: remove the blocked events during the negotiation phase
- [adminTools] undeclared variable removal. [Steve Clement]
- [stix2 import] Fixed email object import (screenshot & eml attributes)
  [chrisr3d]

  - Same comments as previous commit for export
  - Also moved parsing functions in subject into the
    main script to avoid importing python libraries
    in the dictionaries script
- [stix2 export] Fixed email object export (screenshot & eml attributes)
  [chrisr3d]

  - Both of these attributes should not be exported
    as part the email body
  - Thus: custom property
- [stix2 import] Improved network socket observable object parsing loop.
  [chrisr3d]
- [stix2 import] Removed print. [chrisr3d]
- [stix2 import] Fixed Custom Object type parsing. [chrisr3d]

  - Unlike usual STIX2 objects, Custom Objects do not
    have their own type. They are dict and have thus
    no callable attributes
- [stix2 export] Fixed custom object type. [chrisr3d]

  - Custom Object type cannot accept capital letters
- [stix2 import] Fixed pattern parsing following the lastupdate on
  pattern export. [chrisr3d]
- [stix2 export] Fixed pattern apostrophes typo. [chrisr3d]
- [stix2 export] Fixed export of email attachment, eml & screenshot.
  [chrisr3d]
- Decode redis in ZMQ. [Steve Clement]
- [zmq] Backwards compatbility with python 3.4. [Steve Clement]
- [cleanup] removed obsolete code. [iglocska]
- [galaxies] Force galaxy update now correctly updates the galaxy
  itself, not just the contents. [iglocska]
- [bug] Fixed route to /regexp/admin_index. [iglocska]
- [galaxy] Further fixes with the saving of the galaxy update data.
  [iglocska]
- [bug] Removed unused field from galaxy update. [iglocska]
- [UI] added galaxy force update to the side menu. [iglocska]
- Compatibility with python 3.4. [Raphaël Vinot]
- Set shebangs, cleanup. [Raphaël Vinot]
- [stix2 import] Removed shitty looping test. [chrisr3d]
- [stix2 import] Fixed asn object pattern keys. [chrisr3d]
- [stix2 import] Fixed stix2 'parse' function (from library) parameters.
  [chrisr3d]
- [stix2 import] if statement typo. [chrisr3d]
- [API] Fixed object view API. [iglocska]
- [UI] fixed typo causing exceptions in the att&ck add function, fixes
  #3426. [iglocska]
- [bug] Potential fix for SQL return size limit reached when fetching a
  list of attributes. [iglocska]
- [stix2 export] Fixed parameter called while mapping object names.
  [chrisr3d]
- [Session handling] Make sure that the autoregenerate setting changes
  are actually saved. [iglocska]
- [update] recursively init and update submodules. [Andras Iklody]
- [attackMatrix] Better popup position for small screen. [Sami Mokaddem]

  Dynamically change popup position and placement for smaller screen,
  forcing that each cell have a minimum width and that the window is
  scrollable to reveal the remaining of the popup.
- [attackMatrix] No longer set the modal position to fixed when the
  viewport is small. [Sami Mokaddem]

  Under a viewport of 1400px, the modal's position is set to absolute
  alowing the user to use the scrollbar for navigation.
- [stix2 import] Fixed object name while importing file with pe &
  sections. [chrisr3d]
- [stix2 export] Fixed observable object of File with PE extension.
  [chrisr3d]
- [stix2 export] Quick fix of issues on files related to PEs. [chrisr3d]
- [CSRF] Don't run the CSRF form protection on the attribute search.
  [iglocska]

Other
-----
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3535 from PaoloVecchi/patch-4. [Andras Iklody]

  INSTALL.ubuntu18.04.01.with.webmin.txt
- INSTALL.ubuntu18.04.01.with.webmin.txt. [Paolo Vecchi]

  Added Virtualmin install and repository update for mariadb
- Merge pull request #3536 from StefanKelm/2.4. [Andras Iklody]

  Default sort order for Id and Date
- Update proposal_event_index.ctp. [StefanKelm]
- Default sort order for ID and Date: desc. [StefanKelm]
- Default sort order for timesamps: desc. [StefanKelm]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Fixes missing hostname|port in network activity mapping. [Christophe
  Vandeplas]

  The hostname|port has default category "Network Activity" , but was not allowed by the mapping.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3526 from SteveClement/2.4. [Steve Clement]

  chg: [typo] Minor typo
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3520 from ater49/patch-5. [Alexandre Dulaunoy]

  Update of french translation
- Update default.po. [ater49]

  Adding some translations
- Merge pull request #3517 from RichieB2B/ncsc-nl/stix-orgname.
  [Christian Studer]

  Use original orgname at stix-header:title
- Use original orgname at stix-header:title. [Richard van den Berg]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3515 from SteveClement/2.4. [Steve Clement]

  chg: [i18n] update from crowdin, French (13%) Danish (43%) Italian (25%) Japanese (86%) Korean (2%) Portuguese (6%) Spanish (1%)
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3512 from ater49/patch-3. [Alexandre Dulaunoy]

  Update default.po
- Update default.po. [ater49]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3510 from ater49/patch-1. [Andras Iklody]

  Update default.po
- Update default.po. [ater49]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3502 from SteveClement/2.4. [Andras Iklody]

  chg: [form] Give change Password field focus.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3500 from SteveClement/2.4. [Steve Clement]

  chg: [i18n] update default.pot to include all new strings
- Merge pull request #3499 from SteveClement/2.4. [Steve Clement]

  fix: [i18n] Made PO importable into crowdin.
- Merge pull request #3498 from eCrimeLabs/2.4. [Andras Iklody]

  Fix related to Concerns PR #3492
- Fix related to Concerns PR #3492. [Dennis Rand]
- Merge pull request #3493 from SteveClement/guides. [Steve Clement]

  chg: [kali] small typo in git config
- Add: [stix2 export] Added relationships between SDOs. [chrisr3d]

  - Mostly relationships defined by the official
    STIX2.0 Relationships Mapping
  - Further changes on relationships to come
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3492 from eCrimeLabs/2.4. [Andras Iklody]

  Danish translation attempt. It does miss some changes but it should b…
- Danish translation attempt. It does miss some changes but it should be
  a good start. [Dennis Rand]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3490 from SteveClement/guides. [Steve Clement]

  chg: [kali] redis on boot (for persistent setups)
- Merge pull request #3489 from SteveClement/guides. [Steve Clement]

  chg: [kali] added headers to vhost. More automation in rc.local
- Merge pull request #3488 from SteveClement/guides. [Steve Clement]

  chg: [doc] Various updates to Debian and Kali Linux install files.
- Merge branch '2.4' into guides. [Steve Clement]
- Merge pull request #3486 from mokaddem/fix-eventGraphDBUpdate. [Andras
  Iklody]

  Fix event graph db update
- Merge branch '2.4' into guides. [Steve Clement]
- Merge pull request #3483 from SteveClement/2.4. [Andras Iklody]

  chg: [i18n] Added a lot of __('s for our i18n effort
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:SteveClement/MISP into 2.4. [Steve
  Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3449 from mokaddem/sharingGraph. [Andras Iklody]

  EventGraph history
- Merge remote-tracking branch 'upstream/2.4' into sharingGraph. [Sami
  Mokaddem]
- Merge remote-tracking branch 'upstream/2.4' into sharingGraph. [Sami
  Mokaddem]
- Merge remote-tracking branch 'upstream/2.4' into sharingGraph. [Sami
  Mokaddem]
- Merge remote-tracking branch 'upstream/2.4' into sharingGraph. [Sami
  Mokaddem]
- Merge remote-tracking branch 'upstream/2.4' into sharingGraph. [Sami
  Mokaddem]
- Merge remote-tracking branch 'upstream/2.4' into sharingGraph. [Sami
  Mokaddem]
- Add: [stix2 export] Exporting not mapped attributes from x509 object
  as custom properties. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3479 from FloatingGhost/feature-send-logs-to-
  elasticsearch. [Andras Iklody]
- Merge pull request #2890 from truckydev/patch-7. [Steve Clement]

  new: [i18n] Create cake_dev.pot for FR_fr
- Update cake_dev.po. [truckydev]
- Remane pot to po. [truckydev]
- Create cake_dev.pot. [truckydev]
- Merge pull request #3478 from SteveClement/2.4. [Steve Clement]

  chg: [deps] Set the correct and working version of Cybox in diagnostics
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- [stix2 export] Slight data field reading improvement. [chrisr3d]
- [stix2 export] Clarified galaxies condition test parsing. [chrisr3d]
- [stix2 export] Ip-port object export improvement. [chrisr3d]
- Merge pull request #3474 from SteveClement/2.4. [Steve Clement]

  new: [kali] Added initial kali linux script that can install a MISP instance with "one click"
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3471 from SteveClement/2.4. [Steve Clement]

  chg: [i18n] added and updated various LOCALE files
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3470 from SteveClement/2.4. [Steve Clement]

  chg: [doc] Debian guides updated
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3462 from SteveClement/2.4. [Steve Clement]

  chg: [CLI] update/WarningLists/NoticeLists/ObjectTemplates/Galaxies to Admin CLI
- Merge pull request #2 from iglocska/patch-2. [Steve Clement]

  fix: [CLI] mixup corrected
- Merge branch '2.4' of github.com:SteveClement/MISP into 2.4. [Steve
  Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge pull request #3461 from mokaddem/update/attackMatrix. [Andras
  Iklody]

  new: [attackMatrix] possibility to pick multiple galaxies (event-level)
- Merge remote-tracking branch 'upstream/2.4' into update/attackMatrix.
  [Sami Mokaddem]
- Merge pull request #3460 from kalyparker/fix-export-events-csv.
  [Andras Iklody]

  fix: export events csv with CR (fix #3458)
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3455 from mokaddem/update/attackMatrix. [Andras
  Iklody]

  Update/attack matrix
- Merge remote-tracking branch 'upstream/2.4' into update/attackMatrix.
  [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3457 from StefanKelm/2.4. [Andras Iklody]

  Sod the bloody typos
- Typo. [StefanKelm]
- Add: [stix2 import] Importing email-attachment attributes. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: [stix2 export] Exporting email-attachment attributes. [chrisr3d]
- Merge pull request #1 from iglocska/patch-1. [Steve Clement]

  fix: [CLI] Update noticelists correctly passes the user data
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3447 from SteveClement/2.4. [Steve Clement]

  chg: [doc] debian testing/stable install guide updates
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3445 from SteveClement/2.4. [Steve Clement]

  chg: [doc] debian install guide updates
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge pull request #3443 from SteveClement/2.4. [Steve Clement]

  fix: [ZMQ] support for all python versions
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3436 from SteveClement/2.4. [Steve Clement]

  Re-work of the Debian Install Guide
- Merge branch '2.4' of github.com:SteveClement/MISP into 2.4. [Steve
  Clement]
- Merge branch '2.4' of github.com:SteveClement/MISP into 2.4. [Steve
  Clement]
- Merge branch '2.4' of github.com:SteveClement/MISP into 2.4. [Steve
  Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- - Quick command to update galaxies. [Steve Clement]
- - Final merge, 90% in line. - More automation - ToDo: Seperate
  optional features from the essential. [Steve Clement]
- - Merged more changes from both files. [Steve Clement]
- - Merge debian-stable and debian-testing instructions. [Steve Clement]
- - Added env variables to make the install less painful when it comes
  to variables - Remove apache2.2 instructions, 2.4 is default - Add
  some automation to do replacements in php.ini. [Steve Clement]
- - Added things that do not work. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3439 from dawid-czarnecki/2.4. [Andras Iklody]

  chg: Case insensitive sort of organisation list
- Merge pull request #3433 from 0xtf/patch-1. [Andras Iklody]

  Change 16.04 reference to 18.04 on install guide
- Change 16.04 reference to 18.04. [Tiago Faria]
- Merge pull request #3435 from SteveClement/2.4. [Andras Iklody]

  OpenBSD and FreeBSD Install instructions updated
- - More instructions on OpenBSD Install. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:SteveClement/MISP into 2.4. [Steve
  Clement]
- - A more working FreeBSD Install Instruction. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3432 from dak-csis/patch-1. [Andras Iklody]

  Fix php blank page on Debian 9 and Ubuntu 16.04
- Update misp. [Daniel Akulenok]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3405 from Rafiot/ditchpy2. [Andras Iklody]

  Arbitrary move to python3.6
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3427 from StefanKelm/2.4. [Andras Iklody]

  Change --force to --recursive in update/upgrade documentation
- Change --force to --recursive. [StefanKelm]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch 'attributeFetcherFix' into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3417 from SteveClement/2.4. [Steve Clement]

  Added initial internationalization for: French (6%), Japanese (21%)
  Updated FreeBSD and added OpenBSD Install document (:construction:-pre-alpha)
- - Rudimentary support for apache2, login works. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- - Partially works, again, but still CSS issues. [Steve Clement]
- - FreeBSD OpenBSD install updates. [Steve Clement]
- - Initial OpenBSD install procedure, based on httpd. [Steve Clement]
- - Added initial internationalization for: French (6%), Japanese (21%)
  -- Please support our translation teams:
  https://crowdin.com/project/misp -- Other Languages in progress:
  Italian (9%), Korean (1%), Portuguese (1%) [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Raphaël Vinot]
- Update core.default.php. [Steve Clement]

  flipped 'autoRegenerate' sessions. This setting wants to be off for production machines.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3410 from mokaddem/attackMatrixLayout. [Alexandre
  Dulaunoy]

  Attack matrix layout
- Merge remote-tracking branch 'upstream/2.4' into attackMatrixLayout.
  [Sami Mokaddem]
- Merge pull request #3382 from MISP/Rafiot-patch-1. [Alexandre
  Dulaunoy]

  Simplify the wording in the warning.
- Improvement. [Raphaël Vinot]
- Simplify the wording in the warning. [Raphaël Vinot]
- Merge pull request #3399 from StefanKelm/2.4. [Andras Iklody]

  Default sort order for timestamp in attribute view
- Default sort order for timestamp: desc. [StefanKelm]
- Add: [stix2 import] Importing files with pe & pe_sections objects.
  [chrisr3d]
- [stix2 import] Improved file observable object parsing. [chrisr3d]

v2.4.93 (2018-06-27)
--------------------

New
---
- [attackMatrix] Skeleton of multiple galaxy picking. [Sami Mokaddem]
- [stix2 export] Starting exporting PE binary files. [chrisr3d]

  --> file, pe & pe-section objects linked with
  references
- [CLI] Added CLI tool to downgrade DB version. [iglocska]
- [i18n] Added tools to switch between languages via the server
  settings. [iglocska]
- [attackMatrix] Also consider attack galaxy at event level in the
  heatmap fix: [attackMatrix] Typo in ATT&CK + division by 0 in
  gradiendTool. [Sami Mokaddem]
- [attackMatrix] added instance UUID in rest response. [Sami Mokaddem]
- [attackMatrix] statistic about attack tags used in the instance chg:
  [attackMatrix] moved functions in to model and matrix view into
  elements. [Sami Mokaddem]
- [attackMatrix] Possibility to highlight cell matching the typeahead
  field's value. [Sami Mokaddem]
- [AttackMatrix] added Mobile/Pre-Attack Matrix support, UI improvements
  and code refacto. [Sami Mokaddem]
- [GalaxyPicking] Choose the galaxy namespace first before showing
  related galaxies. [Sami Mokaddem]
- [attackMatrix] Ability to attach Mitre att&ck galaxy from the matrix.
  [Sami Mokaddem]
- [attackMatrix] legend scale of the heatmap with dynamic updates. [Sami
  Mokaddem]
- [attackMatrix] force kill chaine header order. [Sami Mokaddem]
- [attackMatrix] addition of heatmap on tiles depending on occurence of
  the tag. [Sami Mokaddem]
- Initial skeleton of Mitre attack matrix. [Sami Mokaddem]
- [internal] Added convenience method to find the ID of an SG via it's
  UUID. [iglocska]
- [functionality] Kick user out if the session is expired instead of
  only doing it on a page load. [iglocska]
- [UI/UX] Event lock initial version. [iglocska]

  - Show if another user is editing the event you're viewing (same org only)
- Add email field autofocus on login page. [Dawid Czarnecki]
- Added event lock functionality. [iglocska]
- Added event lock table. [iglocska]

  - also added missing permission for ZMQ publisher role
- Add schema for feed-metadata. [Raphaël Vinot]

Changes
-------
- [version] Version bump. [iglocska]
- [misp-galaxy] updated to the latest version (including CFR test)
  [Alexandre Dulaunoy]
- [stix1 import] Improved parameters. [chrisr3d]
- [attackMatrix] removed forgotten debug cmd. [Sami Mokaddem]
- [attackMatrix] Definitively removed typeahead + code cleanup. [Sami
  Mokaddem]
- [misp-taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [misp-warninglists] updatd to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [attackMatrix] ATT&CK Tactic is put at the top when picking galaxies
  and is shown in All namespace mode. [Sami Mokaddem]
- [diagnostics] Make the STIX diagnostics a bit less cryptic. [iglocska]
- [API] Changed the default exportable setting for tags that don't
  contain the field pushed via the API to true. [iglocska]
- [clarity] Made the file path validationfailing more obvious when
  adding local feeds. [iglocska]

  - Warning to catch issues that arise due to Steve's fat fingers
- [stix1 import] Updated message diplayed in case of import error.
  [chrisr3d]
- [stix1 import] Properly catching loading errors and returning the
  corresponding output value. [chrisr3d]
- [stix1 import] Changed relationship for the header of a pe. [chrisr3d]

  - atm better mapping in export for event imported
    with this change
  - may change if we decide to create something new
    to represent headers separately
- [i18n] Updated pot files. [iglocska]
- [i18n] Made the strings more i18n friendly across the application.
  [iglocska]
- [attackMatrix] added some comments. [Sami Mokaddem]
- [attackMatrix] Support of JS for interaction in the statistics page.
  [Sami Mokaddem]
- [attackMatrix] removed console logging. [Sami Mokaddem]
- [attackMatrix] Restrict view to be ajax only. [Sami Mokaddem]
- [attackMatrix] search capabilities and table auto resize. [Sami
  Mokaddem]
- [attackMatrix] UI improvement. [Sami Mokaddem]
- [misp-object] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [travis] setuptools need to be updated too. [Alexandre Dulaunoy]
- [travis] sudo because Travis said so... [Alexandre Dulaunoy]
- [travis] Sami influenced me by adding random numerical value at the
  end of Python packages. [Alexandre Dulaunoy]
- [travis] self update of pip3 to update pip3. [Alexandre Dulaunoy]
- [tests] stix 1.2.0.6 python requirements updated. [Alexandre Dulaunoy]
- [favicon] Changed the favicon. [Sami Mokaddem]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [version bump] querystring bumped. [iglocska]
- [Diagnostic View] Updated Diagnostic View for STIX1 related python
  libraries. [chrisr3d]
- [misp-object] updated to the latest version. [Alexandre Dulaunoy]
- Add enums in feed-metadata schema. [Raphaël Vinot]

Fix
---
- [stix1 import] Fixed Monkey typo. [chrisr3d]
- [stix1 import] Fixed missing self call. [chrisr3d]
- [bug] Typo in the event before validate hook. [Andras Iklody]

  As pointed out by @To-om
- [sync] Fix to the attribute level filters not being applied correctly
  on a full push. [iglocska]

  - Found during the investigation of #3378
- [stix1 export] Fixed MISP objects export. [chrisr3d]

  - handle the case when there is no pe & pe-section
    objects
  - 'resolve_objects2parse' should then be optional
    considering this case
- Bump query_version and updated queryACL. [Sami Mokaddem]
- [attackMatrix] only return the result for the last attached galaxy.
  [Sami Mokaddem]

  If a galaxy is already attached, just skip the message.
  (The return value is a string, we don't want to compare the string value for
  each galaxy to be attached)
- [attackMatrix] Multiple galaxy attach operations are now support at
  attribute level. [Sami Mokaddem]

  Previsouly, only 1 INSERT INTO command was executed, the others were
  UPDATE commands
- [UI] fixed Event lock breaking the restoration of soft deleted
  attributes. [iglocska]
- Correlation popup format. [iglocska]
- Left off view file. [iglocska]
- [UI] Fixed a bug with galaxies not being addable. [iglocska]
- Fixed an issue where tags couldn't be added anymore since the last
  commit. [iglocska]
- [API] tag capture fixed on newly created objects via the API, fixes
  MISP/PyMISP#236. [iglocska]
- [stix diagnostic] Returning the correct 'success' value in case of
  error with maec. [chrisr3d]
- :lock: Brute force protection can be bypased with a PUT request.
  [iglocska]

  - fixes an issue where brute forcing the login would work by using PUT requests
  - as reported by Silver Saks from CCDCOE
- [stix1 export] Fixed pe & pe-section export when the header is not
  distinct from the other sections. [chrisr3d]
- Fixed a bug where users couldn't add galaxies after
  paginating/filtering on event attributes. [iglocska]
- Fixed broken correlation toggle on the event view. [iglocska]
- [stix1 import] Fixed indent that imported some objects split.
  [chrisr3d]
- [sync] pull not working due to invalid lookup against galaxies.
  [iglocska]
- [error messages] made some of the error messages a bit more uniform.
  [iglocska]
- [upgrade] Made an older upgrade script more friendly towards MySQL.
  [iglocska]
- [galaxies] Fixed query causing MYSQL errors due to group by not
  containing a silently loaded field. [iglocska]
- Don't require API users to acept the terms / change password to get
  going. [iglocska]

  - to get the API key they need to log in anyway via the interface
- Use common code-path for user init via the login page and the CLI.
  [iglocska]

  - also, be consistent with initial settings
- [setup] Brought MYSQL.sql up to date, fixes #3357, fixes #3358.
  [iglocska]
- [stix1 import] Started fixing to_ids flags for imported
  attributes/objects. [chrisr3d]
- [Cortex] fixed Cortex auth issue. [Andras Iklody]
- [attackMatrix] prevent trowing an error if mitre attack galaxy is not
  there. [Sami Mokaddem]
- [attackMatrix] added aggressive sanitization (just to be sure) [Sami
  Mokaddem]
- [attackMatrix] added missing entries in ACL component. [Sami Mokaddem]
- [attackMatrix] Prevent hovering listener to overwrite each other.
  [Sami Mokaddem]
- [attackMatrix] prevent multiple listener on matrix widgets. [Sami
  Mokaddem]
- [attackMatrix] cluster ATT&CK Tactic is shown in Mitre namespace only.
  [Sami Mokaddem]
- [AttackMatrix] picking Att&ck tactic correctly redirect on the matrix.
  [Sami Mokaddem]
- [eventView] Hide galaxy tags after search. [Sami Mokaddem]
- [travis] update to the latest version of requests. [Alexandre
  Dulaunoy]
- [Docs] some install guide clarifications. [Andras Iklody]
- [bug] fixed version comparison for old vs new db versions. [iglocska]
- [UI] Event lock message update eating flash messages fixed. [iglocska]
- [SG/sync] fixed an issue where if a sync user was not allowed to
  modify a sharing group, it also couldn't create events with said SG
  attached. [iglocska]

  - correctly capture the sharing group, without still being able to modify it, but to extract the ID and link it to the event to be created
- [stix2 export] Fixed attribute value type issue with AS numbers.
  [chrisr3d]
- [stix1 export] Fixed AS attribute value export. [chrisr3d]

  - 'number' field in STIX object side if the value is
    only digits
  - 'handle' if it starts with 'AS'
  - + same parsing as the one recently pushed for STIX2
    regarding 'value' and 'comment' fields on MISP side
- [stix2 export] Checking AS attributes value. [chrisr3d]

  - Because it went out that some people sometimes put
    the AS value in comment and an ip address as value
- Fixed the annoying getcorrelation errors in the logs if someone has
  the jobs index open and times out, fixes #3339. [iglocska]
- [UI] Preserve settings on events add form if anything goes wrong with
  the validation. [iglocska]
- [UI] Fixed default value of threat level id. [iglocska]
- [sg bug] Fixed a bug where a user that should be allowed to extend a
  sharing group is blocked if they are also a sync user. [iglocska]

  - conditions requires that the sharing group has been synchronised from a remote by a different sync user
- [bug] Fixed a copy pasta fail preventing the adding of galaxies.
  [iglocska]
- [stix2 export] Fixed regkey observable creation. [chrisr3d]
- [stix2 export] Fixed network socket observable creation. [chrisr3d]
- [stix2 export] Fixing issues due to the oddity of some enumeration
  lists for observable objects. [chrisr3d]
- [stix2 export] Fixed pattern of protocol value in network socket
  object creation. [chrisr3d]
- Don't throw users out if debug is enabled with the new check.
  [iglocska]
- [bug] Endless loop when terms are not accepted / password not reset
  fixed, fixes #3336. [iglocska]
- Fixed premission on a view level for add tags. [iglocska]
- Fixed permission check for adding tags to an event. [iglocska]
- [ACL] added new functions to the ACL. [iglocska]
- [bug] invalid function call for the event lock via the objects
  controller. [iglocska]
- [extended events] Correctly handle event extensions via event ID
  instead of UUID, fixes #3332. [iglocska]
- [stix1 export] Fixed some credential object attributes export.
  [chrisr3d]

  Following the latest update on the import part
  which include credential objects import, and in
  order to avoid duplicate attribute export and
  create authentication STIX Objects more properly:
  - Parsing authentication type to avoid as much as
    possible to associate passwords with not relevant
    authentication types.
  - If only one authentication type -> distributing
    it to all the passwords (as well as it is the
    case for the authentication format).
- Added impfuzzy validation. [iglocska]
- [Diagnostic] Fixed typo in python libraries testing. [chrisr3d]
- Made sure that object edit buttons are only visible to those that can
  edit them. [iglocska]

  - also, some cleanup in the code to make it more readable
- [EventView] Still allows object edition event if the event hasn't been
  published. [Sami Mokaddem]

Other
-----
- Add: [stix1 import] Parsing x509 raw certificate in x509 object.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3384 from MISP/Rafiot-patch-2. [Alexandre
  Dulaunoy]

  Makes more sense.
- Makes more sense. [Raphaël Vinot]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: [stix1 import] Added default distribution values in events
  imported. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3372 from mokaddem/attackMatrix. [Andras Iklody]

  Multiple pick in ATT&CK matrix
- Merge branch '2.4' of https://github.com/MISP/MISP into attackMatrix.
  [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- [stix2 export] Improved x509 attributes parsing. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3368 from mokaddem/attackMatrix. [Alexandre
  Dulaunoy]

  ATT&CK Tactic Matrix at the top!
- Merge branch '2.4' of https://github.com/MISP/MISP into attackMatrix.
  [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3367 from SteveClement/2.4. [Steve Clement]

  Various updates to INSTALL instructions
- - remove dupe python3-pip from apt install. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- - Added more automation to install procedure. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: [stix1 export] Exporting pe with its section and the related
  file. [chrisr3d]

  - --> WinExecutableFileObject
  - next to the generic loop parsing all objects
    because of the relations between file, pe, and
    pe-section that should be parsed
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch 'set_db_version' into 2.4. [iglocska]
- Merge pull request #3355 from StefanKelm/2.4. [Andras Iklody]

  Typos within Event graph view
- Update event-graph.js. [StefanKelm]
- Typos... [StefanKelm]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3352 from axpatito/patch-1. [Andras Iklody]

  Update INSTALL.rhel7.txt
- Update INSTALL.rhel7.txt. [axpatito]
- Merge pull request #3350 from mokaddem/attack. [Alexandre Dulaunoy]

  Attack
- Merge remote-tracking branch 'upstream/2.4' into attack. [Sami
  Mokaddem]
- Merge pull request #3347 from mokaddem/attack. [Alexandre Dulaunoy]

  Mitre ATT&CK Tactic
- Merge remote-tracking branch 'upstream/2.4' into attack. [Sami
  Mokaddem]
- Merge remote-tracking branch 'upstream/2.4' into attack. [Sami
  Mokaddem]
- Add: [stix] Added test files for stix (1 & 2) import & export.
  [chrisr3d]

  Including:
  - MISP events that can be tested in export
  - STIX 1 & 2 files resulting from the export of
    the MISP events, that can be used as well in
    order to test the import scripts
- Add: [stix2 import] Importing asn objects. [chrisr3d]
- Add: [stix1 import] Importing AS STIX objects. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3345 from mokaddem/favicon. [Andras Iklody]

  Favicon
- Merge branch '2.4' of https://github.com/MISP/MISP into favicon. [Sami
  Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: [stix2 export] Exporting asn MISP objects. [chrisr3d]
- Add: [stix1 export] Exporting asn object. [chrisr3d]
- [stix2 export] Removed intermediary 1 line functions. [chrisr3d]
- [stix2 export] Improved some dictionary use/call. [chrisr3d]
- Add: [stix2 export] Exporting stix2-pattern MISP objects. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: [stix1 import] Importing Account Objects as credential MISP
  Objects. [chrisr3d]
- Add: [stix1 export] Exporting credential MISP objects. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3330 from dawid-czarnecki/2.4. [Andras Iklody]

  new: Add email field autofocus on login page
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: [Diagnostic] Added maec python library requirements. [chrisr3d]
- Merge branch 'samimagic' into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Raphaël Vinot]
- Merge pull request #3323 from RichieB2B/ncsc-nl/rhel-python3.
  [Alexandre Dulaunoy]

  Enable python3 for php-fpm for RHEL/CentOS
- Enable python3 for php-fpm for RHEL/CentOS. [Richard van den Berg]

v2.4.92 (2018-06-07)
--------------------

New
---
- [ACL] Added new role permission: publish_zmq. [iglocska]

  - permission flag to use the "publish to ZMQ" button
- [performance] Made the deadlock fix optional. [iglocska]

  - old behaviour by default or if the setting is disabled
  - new behaviour with non transactional attribute add / correlation add
- Batch delete should hard delete if event hasn't been published yet,
  fixes #3311. [iglocska]
- [API] objects/add now supports uuids and the version number.
  [iglocska]

  - API: /objects/add/[template_id]/[version]
    - template_id can be a UUID
    - version is an optional parameter to select the specific version of a template if searching by uuid
- Hard delete attributes when event was never published, fixes #3311.
  [iglocska]
- [performance] Massive performance gains for the warninglists.
  [iglocska]
- [tooling] Added benchmark tool to AppModel. [iglocska]

  - create name benchmark runs
  - start at different levels of the code's execution
  - aggregated mode allows summed execution times over many iterations of a code path
  - show peak memory usage or full memory usage timeline of the execution history
- Added CyberCure Blocked IP,Blocked URL & Malware hash feeds
  (http://docs.cybercure.ai/) [Mona]
- Stricter validation of baseurl when coming via the API tool.
  [iglocska]
- Show galaxy namespaces and allow the loading of the new field.
  [iglocska]
- New flash message system, fixes #3252. [iglocska]

  - 3 types of flash messages (success, error, warning)
  - uses bootstrap's own classes/structure

Changes
-------
- [version] VERSION bump. [iglocska]
- Bump PyMISP version. [Raphaël Vinot]
- Bump PyMISP. [Raphaël Vinot]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-warninglists] updated to the latest version. [Alexandre
  Dulaunoy]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [API] Adding a tag will no longer throw exceptions if the tag already
  exists. [iglocska]

  - instead the existing tag is returned for further reuse along with a HTTP code of 200
- [misp-object] updated to the latest version. [Alexandre Dulaunoy]
- [cleanup] Benchmarking calls removed. [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [stix1 export] Improved journal entries function. [chrisr3d]
- Added remaining parts of the pymisp / new stix diagnostic tool.
  [iglocska]
- Allow symlinks for public keys in footer. [Xavier Mehrenberger]

  Allows replacing public GPG & SMIME keys (gpg.asc &
  public_certificate.pem) with symbolic links, to store the actual files
  in another format. This allows clean separation of MISP code (in
  webroot) from configuration data.

  Our use case: run MISP on top of kubernetes, storing configurations and
  secrets in dedicated volumes, rather than in the Docker image.
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- New stixtest.py is a bit more granular and adds a check for pymisp.
  [iglocska]
- [stix1 export] Updated x509 objects export to use the appropriate STIX
  object. [chrisr3d]
- [stix1 export] Updated object attributes parsing functions. [chrisr3d]
- [misp-taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [UI Filtering] Do not set searchFor in the URL if no value. [Sami
  Mokaddem]

  After a discussion with iglocksa, it is better to fix it js side than
  server side.
- [documentation] Better description of command line APIs / automation.
  [iglocska]
- [misp-taxonomies] copine scale added. [Alexandre Dulaunoy]
- [stix1 export] Now using python3 as default for stix1 export.
  [chrisr3d]
- [misp-galaxy] updated to the latest version with namespaces galaxy.
  [Alexandre Dulaunoy]
- Version bump for galaxies. [iglocska]
- [Galaxy] Galaxies updated. [iglocska]
- [misp-taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]

Fix
---
- Removed debug breaking update. [iglocska]
- [API] Fixed a black hole on API actions via the Objects controller,
  fixes #3271. [iglocska]

  - Blanket disabling the security component due to the changes in cakePHP for API requests had the side effect that explicit security component stance changes would lead to exceptions
- Potential fix for the deadlock issue addressing #3264. [iglocska]

  - This will mean a performance hit for correlations / adding attributes in general, but let's see how it goes
- [stix1 import] Removed errors catching to let the logs have it.
  [chrisr3d]
- [object references] Object references can be added to deleted
  objects/attributes, fixes #3312. [iglocska]
- [performance] Fixed a serious performance issue with object heavy
  events. [iglocska]
- [javascript] Fixed JS broken in IE11 #3306. [Christophe Vandeplas]
- [stix1 export] Quick fix on attribute data field. [chrisr3d]
- [stix1 import] Fixed email object import. [chrisr3d]
- [stix1 import] Fixed Artifact STIX objects import. [chrisr3d]

  following the last update on export script
- [stix1 export] Fixed and improved some attributes parsing. [chrisr3d]
- [performance API] fix performance issues with warninglists via the
  API. [iglocska]
- [performance] slight tuning for the fetchEvent() function. [iglocska]
- [validation] Fixed urlOrExistingFilepath validation script no longer
  uses hard-coded error messages. [iglocska]
- [cleanup] Removed non-sensical line. [iglocska]
- [stix1 import] Fixed some Galaxy & GalaxyCluster fields. [chrisr3d]
- [stix1 import] Fixed event loading function. [chrisr3d]

  - Fixed errors if the event has no 'ttps' field
- [stix1 import] Fixed whois object name mapping. [chrisr3d]
- [stix1 export] Quick fix of set_tlp function. [chrisr3d]
- [stix1 export] Fixed Tags journal entries. [chrisr3d]
- [stix2 export] Cosmetic fix of stix2 report labels. [chrisr3d]
- [stix2 import] Fixed 'from' attribute type mapping for email object.
  [chrisr3d]
- [stix1 import] Fixed Whois object attributes import. [chrisr3d]

  - Following the latest changes on Whois object export
- Typo fixed in the tag element, preventing the quick filter from
  working. [iglocska]
- Allow updateDatabase to accept numbers. [iglocska]
- Added missing lookup for pymisp versions via the diagnostics.
  [iglocska]
- Reflected XSS via the event view. [iglocska]

  - users arriving on an event view via a malicious URL with a javascript payload and then clicking on the show deleted attributes tab would trigger the payload

  - as reported by Jarek Kozluk from zbp.pl
- [stix2 import] Fixed Custom object import attribute type. [chrisr3d]
- [stix2 import] Fixed custom object import type defining for composite
  attributes. [chrisr3d]
- [stix1 import] Fixed objects name common case definition. [chrisr3d]
- [stix1 import] Fixed x509 object name mapping. [chrisr3d]
- [stix2 export] Fixed class variable call. [chrisr3d]
- [stix1 export] Fixed dictionary comma. [chrisr3d]
- [stix2 import] Improved process object parsing. [chrisr3d]
- [stix2 export] Improved regkey objects mapping. [chrisr3d]
- [stix2 export] Fixed Custom object type typo. [chrisr3d]
- [stix2 export] Added forgotten processes related function call.
  [chrisr3d]
- [stix2 import] Removed useless return functions. [chrisr3d]
- [stix1 import] Fixed object relations for attributes of network
  connection object. [chrisr3d]
- [stix2 import] Fixed event loading. [chrisr3d]
- [stix2 export] Fixed observable object creation for port & ip|port
  attributes. [chrisr3d]
- [stix1 export] To be sure we're always using utf-8. [chrisr3d]
- [CLI] Allow for empty baseurl via the CLI. [iglocska]
- [UI] Fixed the annoying galaxy collapse issues. [iglocska]
- [UI] Fix to the galaxy cluster expand. [iglocska]
- [UI] automation page cleanup. [iglocska]
- [UI] fixed broken collapse/expand of galaxy clusters. [iglocska]
- [API] Add object request has been black-holed. #3271. [iglocska]

  - blanket disabling the security component for API requests clashes with explicit disabling of certain security component features in the objects controller causing exceptions
- [UI filtering] be sure that '0' is not interpreted as empty. [Sami
  Mokaddem]
- [API] Add object request has been black-holed. #3271. [iglocska]

  - blanket disabling the security component for API requests clashes with explicit disabling of certain security component features in the objects controller causing exceptions
- Invalid flash message fixed when editing an attribute. [iglocska]

  - was showing an error on success
- [UI filtering] Attribute quick filter broke all the tabbed filters,
  fixes #3247. [iglocska]
- Fixed endlessly spinning loading animation when fetching a PGP key
  that cannot be found. [iglocska]
- [cleanup] removed debug, fixes #3257. [iglocska]
- [stix1] Updated install & update instructions for stix, cybox & mixbox
  libraries. [chrisr3d]
- Fixed editing servers to add a server certificate not saving said
  certificate. [iglocska]
- Fixed a DOM based XSS with cortex type attributes. [iglocska]

  - as reported by Dawid Czarnecki (dawid@pz.pl)
- Various fixes to the add feed action/view. [iglocska]
- Ignore camelised vs underscored controller name differences in the
  ACL. [iglocska]
- User add form loses checkbox settings on failed submission when
  returning the user to the form. [iglocska]
- Invalid pluralisation. [iglocska]
- Fixed layout. [iglocska]
- Fixed some menu misalignment with debug mode off. [iglocska]
- Minor cleanup of the default layout. [iglocska]
- Fixed some issues with the new notifications. [iglocska]
- [stix1 import] Fixed uuid fetching when a STIX object has no id.
  [chrisr3d]
- [stix1 import] Fixed test to define if a STIX file is from MISP.
  [chrisr3d]
- [stix1 export] Atm skipping objects not mapped yet for export.
  [chrisr3d]
- [stix1 export] Fixed reference creation for process object when the
  reference is an attribute. [chrisr3d]
- [stix1 import] Commented atm not used attribute in object process.
  [chrisr3d]
- [stix1 import] Fixed name of MISP objects parsing for import.
  [chrisr3d]
- [stix1 export] Quick fix on variables. [chrisr3d]
- [stix1 export] Cleaned indentation typo. [chrisr3d]
- Fixed invalid org lookup on the attribute index resulting in some
  notices thrown. [iglocska]

Other
-----
- Bump recommended version of PyMISP. [Raphaël Vinot]
- Merge pull request #3316 from jezkerwin/2.4. [Andras Iklody]

  Quoted scl commands to properly execute python3 + cwd for Cake Install
- Quoted scl commands to properly execute python3 + cwd for Cake
  Install. [jezkerwin]

  Installing Cybox and STIX libraries, the SCL command to install won't properly run unless being quoted.
  Added command to change working directory to /var/www/MISP before installing Cake
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch 'deadlockfix' into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3310 from jezkerwin/2.4. [Andras Iklody]

  Remove contact details, they don't really need to be in there
- Remove contact details, they don't really need to be in there.
  [jezkerwin]
- Merge branch 'performance_benchmarking' into 2.4. [iglocska]
- Test: [benchmark] Added benchmarks for warninglist runs. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3307 from cvandeplas/2.4. [Andras Iklody]

  fix: [javascript] Fixed JS broken in IE11 #3306
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3301 from LDO-CERT/2.4. [Alexandre Dulaunoy]

  fix Typo in MISP settings
- Fix Typo in MISP settings. [garanews]

  fix Typo in MISP settings
- Fix Typo in MISP settings. [garanews]

  fix Typo in MISP settings
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: [stix1 import] Importing Galaxies & Tags from journal entries.
  [chrisr3d]
- Add: [stix1 import] Importing Event threat level. [chrisr3d]
- Add: [stix1 import] Importing vulnerability attributes. [chrisr3d]
- Add: [stix1 import] Parsing link attributes in information_source
  references. [chrisr3d]
- Add: [stix1 import] Parsing attributes from journal entries.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: [stix1 export] Exporting Whois MISP objects. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3269 from Lastpixl/2.4. [Andras Iklody]

  chg: allow symlinks for public keys in footer
- Merge pull request #3287 from StefanKelm/2.4. [Andras Iklody]

  Default sort order for timestamp / date reversed on click for Feed preview index
- Update preview_index.ctp. [StefanKelm]
- Merge pull request #3288 from RichieB2B/ncsc-nl/python3. [Andras
  Iklody]

  Update installation instructions for STIX export
- Install pymisp for python3. [Richard van den Berg]
- Use python3 to install stix/cybox/mixbox libraries. [Richard van den
  Berg]
- [stix1 export][stix2 import] Kept only usefull pymisp library import.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: [stix1 import] Importing x509 Certificate objects. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3283 from SteveClement/2.4. [Andras Iklody]

  Very small change to give the user a hint that multiple attachments can be uploaded
- - reAdded Debian Testing instructions… [Steve Clement]
- - Make allusion to the fact that you can select multiple files in in
  the browse window. [Steve Clement]
- Add: [stix2 import] Importing network-socket objects. [chrisr3d]
- Add: [stix2 export] Exporting network-socket objects. [chrisr3d]
- Add: [stix2 import] Added AS in the list of parsed attributes.
  [chrisr3d]
- Add: [stix2 import] Importing process stix2 objects. [chrisr3d]
- Add: [stix2 export] Exporting process MISP object. [chrisr3d]
- Add: [stix2 export] Added AS in the mapped attributes. [chrisr3d]
- Add: [stix1 export] Added x509 Certificate STIX object namespaces.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3280 from 0x150/remove-leading-tab. [Andras
  Iklody]

  Remove leading tab
- Remove leading tab. [iso]
- Merge pull request #3281 from cryptba1/cybercure-feeds. [Alexandre
  Dulaunoy]

  new: Added CyberCure Blocked IP,Blocked URL & Malware hash feeds (htt…
- Merge pull request #3279 from RichieB2B/ncsc-nl/stixfixes. [Alexandre
  Dulaunoy]

  Add timestamp to outer STIX_Package
- Add timestamp to outer STIX_Package. [Richard van den Berg]
- Merge pull request #3277 from RichieB2B/ncsc-nl/stixfixes. [Alexandre
  Dulaunoy]

  Fix STIX export corner cases
- Support multiple AttributedThreatActors correctly. [Richard van den
  Berg]
- Fix spaces. [Richard van den Berg]
- Initialize incident.attributed_threat_actors when not set. [Richard
  van den Berg]
- Fix tabs. [Richard van den Berg]
- Do not break when observable creation fails. [Richard van den Berg]
- Fix STIX TestMechanisms. [Richard van den Berg]
- Do not fail on unknown attribute types. [Richard van den Berg]
- Write STIX json in text mode. [Richard van den Berg]
- Do not catch exceptions that should go to exec-errors.log. [Richard
  van den Berg]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3262 from RichieB2B/ncsc-nl/stix-python3.
  [Christian Studer]

  Use python3 interpreter for STIX exports
- Write STIX file in utf8. [Richard van den Berg]
- Fix STIX diagnostics: use python3. [Richard van den Berg]
- Merge pull request #3268 from SteveClement/2.4. [Steve Clement]

  Debian Testing install
- - Fixed curl. [Steve Clement]
- - Added curl to update
  galaxies/taxonomies/warninglists/objectTemplates. [Steve Clement]
- - Added yara. [Steve Clement]
- - Checkout "default" it's 2.4 at what you really want. [Steve Clement]
- - Added misp-dashboard. [Steve Clement]
- - Remove > /dev/null foo. [Steve Clement]
- - Added pymisp and modules as well as cake CLI commands. [Steve
  Clement]
- - Debian testing install. [Steve Clement]
- Merge pull request #3267 from mokaddem/issue_3247. [Andras Iklody]

  fix: [UI filtering] be sure that '0' is not interpreted as empty.
- Git push origin 2.4 Merge branch '2.4' of github.com:MISP/MISP into
  2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: [stix1 export] Supporting export of not mapped MISP objects as
  STIX Custom object. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- [stix1 export] typo. [chrisr3d]
- Add: [stix1 export] Added namespaces for WindowsService object.
  [chrisr3d]

  - goes with commit eaedccb3f64bfa3a704c68f0e4a42b6df99d29dd
  - forgot to include it with the commit \o/
- Add: [stix1 export] Supporting windows-service-name attribute export.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3250 from WaryWolf/gpg-agent-fix. [Alexandre
  Dulaunoy]

  Add config mapping for 'gpgconf' option in Crypt_GPG library.
- Add config mapping for 'gpgconf' option in Crypt_GPG library. [Anthony
  Vaccaro]

  This option not only sets the location of the gpgconf binary, but
  if set to false, disables behaviour that shuts down running agents
  when a Crypt_GPG object is destroyed. This behaviour would also
  kill any long-running or daemonised agents that are running and
  configured in the gpg.homedir directory.
- [stix1 export] Edited indicator id. [chrisr3d]
- Add: [stix1 export] Added reference between process and other objects.
  [chrisr3d]
- Add: [stix1 import] Little update following the process object export
  support. [chrisr3d]
- Add: [stix1 export] Exporting Process MISP objects. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: [stix1 export] Exporting network-socket MISP objects. [chrisr3d]
- Add: [stix1 export] Exporting network connection MISP objects.
  [chrisr3d]

v2.4.91 (2018-05-15)
--------------------

New
---
- Remove galaxy cluster information from the sync mechanism for now.
  [iglocska]

  - currently galaxy clusters aren't shared anyway, no point in blowing up the data size / processing time
- Added attribute level galaxy clusters. [iglocska]
- Added option to include base64 encoded attachments in the ZMQ output,
  fixes #3169. [iglocska]
- [stix1 import] Starting parsing related observables in documents from
  misp. [chrisr3d]
- [Export] Added a secondary CSV export that includes more context to
  the UI download tool. [iglocska]
- First implementation of the Noticelist system ready. [iglocska]
- Added noticelist view. [iglocska]
- Noticelist system added. [iglocska]
- Refactor of the warning message for the add attribute view. [iglocska]
- Added chartjs dependency. [Sami Mokaddem]
- Possibility to show/hide distribution repartition of
  event/attr/objAttr chg: layout adaptation. [Sami Mokaddem]
- Show elements having a distribution lower than the event distribution
  in the distribution graph. [Sami Mokaddem]
- Possibility to view connected communities and concerned sharing groups
  in distribution graph's tooltip. [Sami Mokaddem]
- Added warning about missing warninglists used for TLD resolution in
  the freetext import tool. [iglocska]

  - following the twitter feedback
- Added event enrichment functionality. [iglocska]

  - select and run a set of enrichments on all applicable attributes of the event
  - exposed to the API
  - exposed to the command line tool
  - adheres to attribute distributions
- Added Feed management API. [iglocska]

  - add/edit/delete feeds via the API
  - new APIs are RestResponseComponent aware
  - GET on add/edit to receive usage information

Changes
-------
- [PyMISP] updated to latest version. [Alexandre Dulaunoy]
- [stix1 export] Added object name in observable composition id.
  [chrisr3d]

  For an easier import
- [stix1 import] Better distinction in the  parsing between indicators &
  observables. [chrisr3d]

  Following the latest changes on stix1 export (avoiding systematic
  observable compositions for MISP objects representation)
- [stix1 import] Improved regkey object parsing. [chrisr3d]
- [stix1 export] Exporting ip|port & hostname|port as socket address
  object. [chrisr3d]

  Instead of creating an observable composition
- [misp-warninglists] updated to the latest version. [Alexandre
  Dulaunoy]
- [stix1 export] Better parsing MISP objects. [chrisr3d]
- [stix1 export] Improvement of some functions. [chrisr3d]
- [API] Attaching a tag to an object no longer throws an exception if
  the tag already exists, fixes #3245. [iglocska]

  - just emits positive vibes by saying that no changes had to be made
- [misp-object] updated to the latest version. [Alexandre Dulaunoy]
- [validation] Change the unique validation for attributes to be escaped
  if an object ID is set, as opposed to an object relation. [iglocska]
- [debug] Added debug of failed mass edits to returned JSON. [iglocska]
- Only run the automatic worker restart on upgrade if background
  processing is enabled. [iglocska]
- Allow /objects/edit/id to accept a UUID instead of a local ID.
  [iglocska]
- Modified how network socket are parsed using the latest created misp
  object. [chrisr3d]
- [Controllers] sets the ajax variable globally. [Sami Mokaddem]

  As well as removing useless set in controllers and accessing it instead
  of passing through the request.
- Added misp noticelists as a submodule. [iglocska]
- [DistributionGraph] addition of tooltip. [Sami Mokaddem]

  Replaced percentage text in the sharing group progressbar by a tooltip
  giving more information
- [EventController] replaced if/else by ternary condition. [Sami
  Mokaddem]
- Trying not to break the MVC pattern. [Sami Mokaddem]

  Server model is not passed to the constructor anymore, as well as the
  Organisation model.
- [DistributionGraph] added ``distribution description`` text in the
  info popup. [Sami Mokaddem]
- [distributionGraph] support of the sharing group event distribution
  chg: [distributionGraph] code cleanup. [Sami Mokaddem]
- Update __query version. [Sami Mokaddem]
- Show all by default. [Sami Mokaddem]
- Doughnut part color. [Sami Mokaddem]
- Updated description tooltip text. [Sami Mokaddem]
- Sanitization of data for distribution graph. [Sami Mokaddem]
- Add additional distribution info about to whom we are sharing even if
  we don't have element on this distribution level. [Sami Mokaddem]
- Replaced radar chart to doughnut chart. [Sami Mokaddem]
- Moved sharing group outside of the distribution progressbar (as it is
  a special case), distribution range is displayed when clicking on the
  pb labels and lots of minor improvements. [Sami Mokaddem]
- Changed distribution graph popover title. [Sami Mokaddem]
- Removed useless prints. [Sami Mokaddem]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- Bump PyMISP. [Raphaël Vinot]
- First round of refactoring of the side menu. [iglocska]
- Changed the org admin role to not have sync privileges by default.
  [iglocska]

Fix
---
- Detaching galaxy clusters from attributes was using the old function
  name. [iglocska]
- Attachcluster to object attributes fails due to no flattening.
  [iglocska]
- Validation issue for objects fixed. [iglocska]
- Fixed an invalid link when attaching a cluster via all galaxies.
  [iglocska]
- Version bump. [iglocska]
- [stix1 import] Catching port type while importing ip-port MISP
  objects. [chrisr3d]
- [stix1 import] Testing if related_indicators/observables is in a
  document before watching it. [chrisr3d]
- [stix1 import] Fixed distinction between atttribute values. [chrisr3d]

  - MISP attributes can be INT sometimes, so read the 2nd comment

  - Previously an INT attribute value did not satisfy the condition,
    which made it considered as objects attributes and tried to
    create a MISP object instead of a single attribute
- [stix1 export] Fixed objects and observables IDs generation.
  [chrisr3d]
- [stix1 import] Fixed missing self argument. [chrisr3d]
- [stix1 import] Fixed some attribute parsing function calls. [chrisr3d]
- Some cleanup. [iglocska]
- Added documentation of server setting modifications via the console.
  [iglocska]

  - also added left-off server setting for enabling attachments via ZMQ
- [stix1 export] Fixed my omission of ids flag parsing for x509 MISP
  objects. [chrisr3d]
- [stix1 export] Quick fix on attribute data field test. [chrisr3d]
- Fixed the enabled field missing for non site admin users in
  warninglsits / noticelists. [iglocska]
- [validation] Fixed an issue with the unique attribute validation rule
  blocking legitimate use-cases. [iglocska]

  - adding an attribute with a matching pair or category/type/value in an existing object-contained attribute would be incorrectly flagged as violating the attribute uniqueness rule
- Don't lowercase the controllername for the ACL Component. [iglocska]
- [UI] Fixed the field name for input source in the feed edit view.
  [iglocska]
- [Feed caching] Readded the feed correlations for non correlating
  attributes. [iglocska]

  - it was breaking the indexing for the attached correlations
- [ACL] Fixed the side menu url to the correct capitalisation for the
  populate from button. [iglocska]
- [ACL] Made the ACL system's behaviour more lax when it comes to
  capitalisation mistakes in the URL, fixes #3240. [iglocska]
- [API] Tightened the disabling of the security component to counter the
  effects of cakephp 2.10.x. [iglocska]
- Bumped noticelist version. [iglocska]
- Restart the workers due to the new cakephp version causing issues.
  [iglocska]
- Remove form tampering for REST requests. [iglocska]

  - makes MISP compatible with 2.10.x
  - No point in running the security component's test since no form is submitted via REST anyway.
- Changed filepath of noticelist not reflected in update script.
  [iglocska]
- Cakephp version bumped to latest 2.x. [iglocska]

  - also gets rid of the stupid mcrypt requirement that breaks compatibility with newer ubuntu versions
- Edge case with empty objects caused *barf* [iglocska]
- Account for alternate format for /objects/edit. [iglocska]

  - I need to take a shower after this fix
- Fixed invalid indeces in the feed lookup via the event view.
  [iglocska]
- Fixed broken objects/edit. [iglocska]
- Fixed object add. [iglocska]
- Fixed name change of variable breaking /objects/add. [iglocska]
- Added the missing schemaloc namespace for system objects. [chrisr3d]
- Handle no template being passed to objects/add correctly. [iglocska]
- Fixed object->attribute references not being captured correctly.
  [iglocska]
- [DistributionGraph] include metadata for all distribution level. [Sami
  Mokaddem]

  When fetching distribution graph data, returns information about all
  distribution level (even not concerned).
- Removed break point *cough* [iglocska]
- Don't redirect users to terms page if no terms page is set. [iglocska]
- [CorrelationGraph] set the undefined ajax variable when pivoting from
  a taxonomy tag / galaxy cluster in fullscreen. [Sami Mokaddem]
- Fixed an issue with the notice message container showing invalid
  default data. [iglocska]
- Fixed regkey value string. [chrisr3d]
- Added missing space after the taxonomy name on the taxonomy view.
  [iglocska]
- Fixed email observable type parsing. [chrisr3d]
- Using an existing relationship between a process and its network
  connections. [chrisr3d]
- Directly take the sharing group name from the event. [Sami Mokaddem]

  Do not fetch the sharing group name as it is already included in the
  event.
  + fixed a css glitch
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [DistributionGraph] incorrect number in the sg progressbar tooltip.
  [Sami Mokaddem]

  Set the correct number of involved sharing instead of the sum of sharing
  group in the sg progressbar tooltip
- Fixed a bug that prevented servers from being added. [iglocska]
- [DistributionGraph] sharing group search and uniqueness of results.
  [Sami Mokaddem]

  fix a bug where filtering per sharing group was not inlcuding inherit
  attributes.
  Enforce uniqueness of involved entities.
- Fixed distribution level swapping when filtering from the distribution
  chg: moved styling into css new: Loading gif when building the
  distribution graph. [Sami Mokaddem]
- Avoid redrawin distribution graph when closin its popover + reset pb
  ticks offset at each draw. [Sami Mokaddem]
- Replaced hardcoded eventID by the real event id. [Sami Mokaddem]
- Support of filtering for distribution=0 (empty(0) is true ini php).
  Also, only consider attr and obj_attr (ignoring object as they only
  carry meta-data) [Sami Mokaddem]
- Honour `MISP.completely_disable_correlation` on attribute/event
  save/delete action. [Eugenio Paolantonio]
- Typo. [chrisr3d]
- Fixed typo of a string function. [chrisr3d]
- Attribute values that are too long for mysql text fields don't
  generate warnings and just truncate, fixes #3196. [iglocska]

  added validation error
- Removing galaxy filters in the galaxy view would redirect to an
  invalid url, fixes #3201. [iglocska]
- Allow "json" not to be set when adding a server via the API.
  [iglocska]
- Fixed /servers/add via REST API not working, fixes #3202. [iglocska]

  - corrected list of parameters
  - added sane defaults so that only the minimum list of fields is actually required
  - fixed a bunch of stuff that was just plain broken with this API
- Low timeout added for module introspection to fix performance
  bottlenecks. [iglocska]
- Testing if references before looping on it. [chrisr3d]
- Inverted 2 type values of a DNS Record. [chrisr3d]
- Fixed events from MISP recognition. [chrisr3d]
- Fixed copy pasta fail. [Andras Iklody]

  As reported by @truckydev
- Fixed path / filename split case. [chrisr3d]
- Fixed InformationSource references in STIX incident object. [chrisr3d]
- Source Format -> Input Source (C/P mistake) [Raphaël Vinot]
- Function object typo. [chrisr3d]
- Fixed library import. [chrisr3d]
- Don't correlate attribute to feeds if the correlations are disabled on
  the attribute. [iglocska]
- Fixed a typo in the side menu rework. [iglocska]
- Allow filename as an alternative for parsed domains/hostnames.
  [iglocska]
- PyMISP version 2.4.90. [Alexandre Dulaunoy]
- Added some sanitisation to the new view. [iglocska]
- Fixed namespaces (causing bugs if not set) [chrisr3d]
- Fixed external ids field type. [chrisr3d]
- Object templates updated to the latest version. [Alexandre Dulaunoy]
- Fixed weird error message if an ajax query goes wrong. [iglocska]
- Hide buttons to create proposals for read only users, fixes #3187.
  [iglocska]
- Added event enrichment to the ACL. [iglocska]
- Editing an attribute was not setting the distribution level to the
  previous value. [Sami Mokaddem]
- Changed "xhtml:body" into "xhtml:div", to avoid creating a body DOM
  which cause listener on the original body to bug. Incremented js
  number and check if request is ajax or not in ObjectController. [Sami
  Mokaddem]
- MISP warning-lists updated to latest version. [Alexandre Dulaunoy]
- Removed print. [chrisr3d]
- Fixed an issue where attribute searches via the UI would incorrectly
  return all visible data. [iglocska]
- Fail gracefully during single user PGP key checks on the user view.
  [iglocska]
- Fixed relationships in object references. [chrisr3d]
- Fixed editing feeds via the UI. [iglocska]
- Session.cookie_timeout could not be saved correctly, fixes #3182,
  fixes #3171. [iglocska]
- Downasides -> downsides. [Raphaël Vinot]
- Fixed empty event tags on the event index api. [iglocska]
- After adding a tag via the API MISP would always return the first tag,
  fixes #3159. [Andras Iklody]
- Cull empty event tags for event index. [iglocska]
- Fixed previewing image attachments via the feeds. [iglocska]
- Fixed some obscure translation errors between python 2 & 3. [chrisr3d]
- Fixed monkey copy paste errors. [chrisr3d]
- Fixed some mapping issues. [chrisr3d]

  -> Threat level name & incident status name mapping
- Fixed color mapping issue that avoided Marking creation. [chrisr3d]

Other
-----
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Version bump. [iglocska]
- Add: [stix1 import] Now importing MISP objects from related
  observables. [chrisr3d]
- Add: [stix1 import] Added CustomObjects parsing. [chrisr3d]
- Add: [stix1 export] Added socket address object namespace. [chrisr3d]
- [stix1 export] Removed no longer used observable composition for
  ip|port. [chrisr3d]
- [stix1 export] Reusing little functions. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: [stix1 import] Importing reply-to attributes. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3237 from StefanKelm/2.4. [Andras Iklody]

  Update attributeConfirmationForm.ctp
- Update attributeConfirmationForm.ctp. [StefanKelm]

  Match message text with what is being displayed at event view
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Added description for the latest functions created. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch 'global_ajax' into 2.4. [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch 'smallfixes' into 2.4. [iglocska]
- Add: Parsing hostname while importing network connection or socket
  object. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3233 from mokaddem/global_ajax. [Andras Iklody]

  chg: [Controllers] sets the ajax variable globally
- Add: Importing System objects containing mac addresses. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: Added namespace for the latest STIX object supported in our
  exporter. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: Parsing email-reply-to attributes. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3232 from SteveClement/2.4. [Steve Clement]

  Amended Ubuntu ssdeep instructions - Added 18.04 install file
- - Added Ubuntu 18.04 instructions. [Steve Clement]
- - updated ssdeep instructions. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: Exporting mac-addresses. [chrisr3d]
- [doc] features about new correlation engine added. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3223 from SteveClement/2.4. [Steve Clement]

  - Added mascot drafts
- - Added mascot drafts. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Sami Mokaddem]
- Merge remote-tracking branch 'upstream/2.4' into
  distributionGraphDonut. [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3214 from mokaddem/distributionGraphDonut. [Andras
  Iklody]

  Distribution graph
- Merge remote-tracking branch 'upstream/2.4' into
  distributionGraphDonut. [Sami Mokaddem]
- Merge remote-tracking branch 'upstream/2.4' into distributionGraph.
  [Sami Mokaddem]
- Changed distribution label in distribution graph (removed distribution
  number) [Sami Mokaddem]
- Center distribution graph inside the popover. [Sami Mokaddem]
- Changed behavior of distribution progressbar: Display event
  distribution along with the maximum distribution level of the items
  inside the event. [Sami Mokaddem]
- Changed distribution graph popover title. [Sami Mokaddem]
- Removed useless codes. [Sami Mokaddem]
- Updated ACLComponent. [Sami Mokaddem]
- Feature: progress bar showing the range of the maximum distribution of
  all items. Moved radar graph and  progressbar in a popover. [Sami
  Mokaddem]
- Possibility to filter valueInFieldAttribute with multiple value.
  distribution graph support inherit distribution level. [Sami Mokaddem]
- Allow filtering attributes based on specific columns (previsouly not
  accessible) like distribution. Partial support of onClick for
  distribution graph. [Sami Mokaddem]
- Merge remote-tracking branch 'upstream/2.4' into distributionGraph.
  [Sami Mokaddem]
- Initial version of the distribution graph. [Sami Mokaddem]
- Add: Parsing network connections in process objects. [chrisr3d]
- Add: Starting parsing process objects. [chrisr3d]
- Merge pull request #3215 from ts-way/for-upstream/disable-
  correlations-fix. [Andras Iklody]

  Honour `MISP.completely_disable_correlation` on attribute/event save/delete action
- Merge branch '2.4' of github.com:MISP/MISP into stix. [chrisr3d]
- Merge pull request #3212 from StefanKelm/2.4. [Alexandre Dulaunoy]

  Update event-graph.js
- Update event-graph.js. [StefanKelm]
- MISP taxonomies updated. [Alexandre Dulaunoy]
- Add: Starting parsing network socket objects. [chrisr3d]
- Add: Starting parsing network connection objects. [chrisr3d]
- Merge branch 'stix' into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3205 from stephengroat/patch-1. [Alexandre
  Dulaunoy]

  cleanup travis and move to requirements.txt
- Cleanup travis and move to requirements.txt. [Stephen]
- Add: MISP objects template updated to the latest version. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: Now resolving domain/uri with relationship 'Resolved_To' to ip
  addresses. [chrisr3d]
- Fixed an absent-mindedness due to my chocolate consumption. [chrisr3d]
- Better DNS objects parsing. [chrisr3d]
- Add: Starting parsing some DNS record objects. [chrisr3d]

  - atm parsing attributes that exist in MISP (domain & ip)

  - able to parse DNS related attributes but need to define
    how to map it in MISP
- Updated stix header title. [chrisr3d]

  The header is actually skipped in MISP and the one
  from misp2stix_framing is used, but usefull for
  command line tests
- Merge branch '2.4' of github.com:MISP/MISP into stix. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch 'stix' into 2.4. [chrisr3d]
- Removed print... [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Atm set the version to 1.1.1 to keep compatibility. [chrisr3d]

  ... with the previous misp2stix script
- Merge branch '2.4' of github.com:MISP/MISP into stix. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into stix. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3190 from MISP/quickfix-eventGraph-popover.
  [Andras Iklody]

  fix: Do not append popover content (from event graph) into body
- Feature-contextualMenu: Possibility to specify the container in which
  to append the menu. [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3188 from
  mokaddem/edit_attribute_distribution_fix. [Andras Iklody]

  quickfix: editing an attribute was resetting its distribution level
- Merge branch 'correlation_integration' into 2.4. [iglocska]
- Sanitize event_id + bit refacto. [Sami Mokaddem]
- Slight ui adjustement. [Sami Mokaddem]
- Feature: Support of fullscreen in correlation graph in the event view.
  [Sami Mokaddem]
- Correlation graph in event view. [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Precising error type to better catch where an error is. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Args & string formatting typo. [chrisr3d]
- Merge pull request #3183 from StefanKelm/2.4. [Andras Iklody]

  Update Log.php
- Update Log.php. [StefanKelm]

  Alphabetically sort list of Actions pull-down menu within "Search Logs"
- Add: Making references between objects in the event created while
  importing STIX. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: Added Windows Service objects parsing. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Added dedscription for each function. [chrisr3d]
- Added return statement. [chrisr3d]
- Turned ttps into class object in order to clean parameters. [chrisr3d]
- Removed self repetition when not required. [chrisr3d]
- Making the module work for both python 2 & 3. [chrisr3d]
- Removed print & added confirmation message at the end. [chrisr3d]
- Removed dependencies modules merged in this one. [chrisr3d]
- MISP to stix, cybox & ciq in 1 module (class methods) [chrisr3d]
- MISP to STIX export refactored & updated to work with python3.
  [chrisr3d]

v2.4.90 (2018-04-21)
--------------------

New
---
- Add download buttons for user profiles. [iglocska]
- Added the extended event lookup to the edit event view. [iglocska]
- Preview the extended event ID / UUID. [iglocska]

  - Also, cleanup of the nasty event tag code
- Added the cookie_timeout setting. [iglocska]

  - still needs some back-end changes for it to be active
- Made the threat_level_id filter for the attribute search more
  flexible. [iglocska]
- Added new field threat_level_id to /attributes/restSearch. [iglocska]
- Added getEventInfoById API. [iglocska]
- Added warning and link to the console tasks to the Task index.
  [iglocska]

  - let's deprecate this crap
- Added section that describes the command line functions to the
  automation page. [iglocska]
- Cleanup of server push, feed fetch, fed cache console commands.
  [iglocska]
- Rework of the server/feed command line tools, :construction:. [iglocska]
- Added improvements to the Cortex settings. [iglocska]

  - allow for configuring SSL options for Cortex
  - previously the API key was not passed to Cortex on GET requests only on POST, breaking Cortex 2 compatibility
- Added event_timestamp parameter to attributes restsearch. [iglocska]
- Extended event first iteration added. [iglocska]

  - when adding/editing an event, add another event's UUID as an extended event UUID to extend the targeted event with the current
  - extender events can be viewed in the merged event view
- Added event/attribute add/edit to the restresponse describe
  functionality. [iglocska]
- Added server setting management via the command line. [iglocska]

  - Usage:

    - /var/www/MISP/app/Console/cake Admin getSetting [setting]
      - setting is optional, if none set "all" is assumed
      - returns all or a specific setting's current value and metadata

    - /var/www/MISP/app/Console/cake Admin setSetting [setting] [value]
      - set a given server setting by full setting name
      - for example the following will enable the import services:
        -  /var/www/MISP/app/Console/cake Admin setSetting "Plugin.Import_services_enable" 1

  - This feature was created in support of the CIRCL global conglomerate's APAC HQ in Tokyo
- Cleanup of role permissions. [iglocska]

  - fixed name of admin -> org admin
  - changed order of org admin <-> site admin
  - descriptions updated and now visible by hovering over any permissions' titles
- Added separation between enabled feeds and feeds enabled for caching.
  [iglocska]
- Add authorization header for Cortex 2 integration. [iglocska]
- Add event last modified to the event view. [iglocska]
- Added a small diagnostic tool to debug the impact of a bug fixed in
  2.4.89. [iglocska]
- Allow further role settings. [iglocska]

  - exclude a role from non site admin assignment
  - set max memory usage and execution time / role

Changes
-------
- Version bump. [iglocska]
- Changed the extended event lookup box's colour. [iglocska]

  - to appease @adulau
- Shorten the links on the galaxy references. [iglocska]

  - show the full link in the hover over
- Added [:] to the refanging options. [iglocska]
- File path parsing updated following some file MISP object updates.
  [chrisr3d]
- Changed the parameter order for the push server shell. [iglocska]
- Renamed the cachefeeds console command to cachefeed for consistency's
  sake. [iglocska]
- Moved the command line functions' description to the server model.
  [iglocska]
- Added the command line functions to the automation page's parameters
  via the controller. [iglocska]
- Bump PyMISP. [Raphaël Vinot]
- Renamed the mapping module (which is no longer only a dictionaries
  file) [chrisr3d]
- Added x509 fingerprints parsing for MISP objects. [chrisr3d]
- Dictionaries update to go with the module update. [chrisr3d]
- Added uuid to the org quick filter. [iglocska]
- Documented new attributes/restSearch parameters. Also added an
  example. [iglocska]
- Refactor of the complex type tool. [iglocska]

  - makes it more readable
- Removed a succession of conditional statements using a dictionary.
  [chrisr3d]

Fix
---
- Z-index popover issue in event graph. [Sami Mokaddem]
- MISP galaxy updated. [Alexandre Dulaunoy]
- Tag removal fixed. [iglocska]
- Fixed the text of the cookie_timeout setting. [iglocska]
- Added missing view file. [iglocska]
- Enforcewarninglist can still accidentally convert the attribute list
  to an attribute dictionary using attribute fetchAttributes(), fixes
  #3166. [iglocska]
- Log seach should allow form resubmissions. [iglocska]
- Fix to the invalid refanging (Third time's the charm) [iglocska]
- Fixed invalid refanging. [iglocska]
- + changed to . in url. [iglocska]
- Bug when plotting event without attribute or object. [Sami Mokaddem]
- Set correct (previous) phyisic state after dragging. [Sami Mokaddem]
- Fitting the network more than once can make the camera bug. [Sami
  Mokaddem]
- Changed 'removing' text to 'hide' text to avoid confusion. [Sami
  Mokaddem]
- Label was not set when display filter was empty. [Sami Mokaddem]
- Switching back and forth between layout is behaving as expected. [Sami
  Mokaddem]
- Physics no longer reset when the layout change. [Sami Mokaddem]
- Fixed new namespaces definition, in case of issue with namespaces.
  [chrisr3d]
- Fixed some random mixbox namespaces issues while using python3.
  [chrisr3d]
- Fixed an edge case where an attribute could be created that is tied to
  an object but has no object relation. [iglocska]
- Avoiding import fails caused by unparsed STIX types. [chrisr3d]
- Avoid importing empty objects. [chrisr3d]
- Extends field now correctly shows a plain uuid if no event was found /
  visible. [iglocska]
- Removed the validity check for the event UUID in the extended UUID
  field. [iglocska]
- If no extension uuid is added to an event the editing via the UI would
  fail. [iglocska]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Removed actual file path from the command line functions path.
  [iglocska]
- Default behaviour of download_attachments_on_load fixed. [iglocska]
- Handling the case of some files that are not read because of special
  caracters. [chrisr3d]
- Fixed a bug where background jobs for feeds would not work correctly
  due to headers not being passed along with the feed object. [iglocska]
- Various fixes to the server shell. [iglocska]
- Copy pasta fixed. [iglocska]
- Fixed mess-up with the cortex settings. [iglocska]
- Fixing some report parsing possible issues. [chrisr3d]
- Fixed GalaxyCluster import format. [chrisr3d]
- Fixed STIX objects parsing to avoid errors with not parsable objects.
  [chrisr3d]
- Added description parsing as MISP attribute comment. [chrisr3d]
- Fixed ip-port observable import. [chrisr3d]
- Fixed ip-port observable export. [chrisr3d]
- Fixed custom objects parsing. [chrisr3d]
- Fixed custom object arguments & added exception to create a custom
  object. [chrisr3d]
- Fixed duplication of some attributes with unintended values.
  [chrisr3d]
- Avoid skipping domain & port values in url object export. [chrisr3d]
- Fixed pattern from MISP objects parsing separator to avoid unintended
  spaces. [chrisr3d]
- Fixed patterns parsing to avoid useless special caracters import.
  [chrisr3d]
- Fixed hash type parsing. [chrisr3d]
- Added misp label to distinguish misp stix2 files. [chrisr3d]
- Handle a non existent case error for the dictionary to return.
  [chrisr3d]
- Fixed some dictionary functions bugs. [chrisr3d]
- Handling the stix file title None case. [chrisr3d]
- Changed United States -> United States of America in the org
  nationality list. [iglocska]
- Potentially fix an issue if no extended UUID is passed on edit.
  [iglocska]
- Autoregenerate causes intermittent logouts, changed the setting
  description and guidance in the server settings to reflect this.
  [iglocska]
- Fixed info field for import from external STIX. [chrisr3d]
- Added domain restrictions to the possible org index filters, fixes
  #3147. [iglocska]
- Added organisation domain restrictions to the org index, partially
  fixes issue #3147. [iglocska]
- MISP object templates updated to latest version. [Alexandre Dulaunoy]
- Some minor fixes. [iglocska]
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- ValueNotEmpty() switched to stringNotEmpty for the attribute value
  validation. [iglocska]

  - Core 1+2 of the new laptop
- MISP galaxy clusters updated to the latest version. [Alexandre
  Dulaunoy]
- Fixed issues with non string server settings when changing them via
  the console. [iglocska]
- Unknown meta-category do not longer raise an exception (use a default
  value instead) [Sami Mokaddem]
- Fixed missing reason for failure if the freetext import had a single
  attribute fail during the saving process, fixes #3141. [iglocska]
- Fix wrong object's deletion buttons title depending on the `deleted`
  property. [chkp-aliaksandrt]
- Editing an object "loses" comment, fixes #3133. [iglocska]
- Don't try to run the testBaseURL server setting check if the user
  comes from the CLI. [iglocska]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Tranformed function not using self as staticmethod as it should be.
  [chrisr3d]
- Skipping ttps parsing from external stix atm to avoid bugs. [chrisr3d]
- IDS flag not set when editing attribute, fixes #3126. [iglocska]
- Date order fixed in event view. [iglocska]

  - Now time for fika
- Fixed the contactination issue from before. [iglocska]
- Fixed a crappy event concatination bug for restsearch. [iglocska]
- Added missing changes in evnet.php. [iglocska]
- Financial tool result included in event. [iglocska]

  - also removing trailing . from domain names
- Added pre-fix to cortex2 authorization header. [iglocska]
- Tied the new diagnostic tool into the ACL. [iglocska]
- Handling case of stix events without labels. [chrisr3d]

Other
-----
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3170 from mokaddem/ref_graph. [Andras Iklody]

  Extended event support and tag filtergin in the event graph
- Added confirmation box to draw the network based on a threshold. [Sami
  Mokaddem]
- Perf: unset filtered data instead of adding them to a new array (thus,
  reducing memory consumption by a factor of 2) [Sami Mokaddem]
- Being consistent with indentation + removed useless comment. [Sami
  Mokaddem]
- Feature: Possibility to filter on tags. [Sami Mokaddem]
- Added comment. [Sami Mokaddem]
- Do not clusturize if filtering is enabled + only draw hull around
  extendeding event in reference scope. [Sami Mokaddem]
- Added source from where the original jarvis march algorithm was taken.
  [Sami Mokaddem]
- Feature: Better support of extended event in event graph - Added a
  colored region for each event extending the current event scope. [Sami
  Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3161 from lucamemini/patch-1. [Andras Iklody]

  added current server timestamp
- Added current server timestamp. [lucamemini]

  Addded, on footer, current server timestamp (MySQL Format).
  Little usability enhanced during debug session, task scheduler edit and log analisys (my server time is UTC, my workstation time is Italy localtime)
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Arguments cleaned up. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3154 from mokaddem/ref_graph. [Alexandre Dulaunoy]

  New features for event graph
- Updated ACLComponent. [Sami Mokaddem]
- Added custom library used by eventGraph (may be added as a submodule
  in the future) [Sami Mokaddem]
- Feature: Added support of extended event in event graph. [Sami
  Mokaddem]
- Merge branch '2.4' of https://github.com/MISP/MISP into ref_graph.
  [Sami Mokaddem]
- Replaced scope rotation key typeahead by selector + removed trailling
  spaces. [Sami Mokaddem]
- Stop physics simulation on node drag. [Sami Mokaddem]
- Moved event graph into its own view file. [Sami Mokaddem]
- Ui: Added shortcuts as background. [Sami Mokaddem]
- Feature: Canvas contextual menu allowing to hide/edit/expand/collapse
  the selection. [Sami Mokaddem]
- Added filtering based on authorized JSON key + JSON key is displayed
  in the header scope badge. [Sami Mokaddem]
- Support of graph per JSON key (using typeahead) [Sami Mokaddem]
- Feature: Draft of generic graphing from any key. [Sami Mokaddem]
- Feature: Support of Tags in the event graph. [Sami Mokaddem]
- Added scope badge and minor css changes. [Sami Mokaddem]
- Merge branch 'quick-fix-metacategory-graph' into ref_graph. [Sami
  Mokaddem]
- UI: swap of icon-text for header graph button. [Sami Mokaddem]
- Draft of filtering per attribute value. [Sami Mokaddem]
- Moved reference logique server-side + First draft of filtering
  capabilities. [Sami Mokaddem]
- Compute graph serverside. [Sami Mokaddem]
- Moved layout into Display tab + Created scope and filters (uses
  action_table js not added yet) DOM. [Sami Mokaddem]
- Usage of bootstrap popover instead of floating contextual menu. [Sami
  Mokaddem]
- Possibility to choose the number of character to display in the label.
  [Sami Mokaddem]
- Possibility to choose physics solver in eventGraph. [Sami Mokaddem]
- Added expand/collapse all in eventGraph->display. [Sami Mokaddem]
- Possibility to search for object_relation in the event graph. [Sami
  Mokaddem]
- Possibility to choose the object_relation to be displayed in the
  object's label. [Sami Mokaddem]
- Added retreiving of object templates in order to let the user choose
  the field we want to see in the event graph. [Sami Mokaddem]
- Added possibility to change physics on the fly. [Sami Mokaddem]
- Added physics toogle button for event graph. [Sami Mokaddem]
- Fix #3074: Edit button vanishes on cancelled delete. [Sami Mokaddem]
- Better support of hierachical view and clutering unreferenced nodes.
  [Sami Mokaddem]
- First draft of hierarchical layout. [Sami Mokaddem]
- Fixed bug where the node focus was not performed if the node was
  already displayed. [Sami Mokaddem]
- When searching for a clustered item, it will uncluster it and focus
  the camera to it. [Sami Mokaddem]
- Set correct number of childs in root node label. [Sami Mokaddem]
- Added clustering of unreferenced attributes/objects. [Sami Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch 'disable_auto_download' into 2.4. [iglocska]
- Made the auto download of attachments when loaded in the browser
  configurable. [John Doe]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3152 from StefanKelm/2.4. [Andras Iklody]

  Default sort order for id / date reversed on click for Server preview index
- Update preview_index.ctp. [StefanKelm]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Parsing course of action related observables. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- Parsing more types of external pattern. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- Merge pull request #3149 from StefanKelm/2.4. [Andras Iklody]

  Changes to allowed CVE format and hover output being displayed on top of the attribute
- Update Attribute.php. [StefanKelm]

  According to https://cve.mitre.org/news/archives/2014/news.html#jan152014_New_CVE_ID_Format_in_Effect_as_of_January_1_2014 the four-fixed-digits requirement has been dropped
- Update misp.js. [StefanKelm]

  Hover output on top, not to the left
- Add: Importing course of action stix objects as new course of action
  MISP objects. [chrisr3d]
- Starting parsing some easy patterns. [chrisr3d]
- Add: Added course-of-action object parsing. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- Add: Added the stix version attribute in stix2-pattern objects.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- Added description to galaxies. [chrisr3d]
- Parsing STIX objects that are imported as Galaxies. [chrisr3d]
- Importing vulnerabilities. [chrisr3d]
- STIX2 import Refactor. [chrisr3d]
- Re-enabled loading event function try/catch procedure. [chrisr3d]
- Importing external indicators as stix2-pattern objects. [chrisr3d]

  Now on the same state as the current used import module
- :construction: Import module importing things, but need to fix few attributes
  loss. [chrisr3d]
- :construction: Parsing patterns representing MISP objects. [chrisr3d]
- :construction: Parsing observable objects representing MISP objects. [chrisr3d]
- :construction: Parsing STIX2 objects that give MISP attributes with the import.
  [chrisr3d]
- :construction: Starting parsing STIX2 from MISP. [chrisr3d]
- STIX2 export refactored. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- Parsing ip-port objects. [chrisr3d]

  - Observable added
  - Observable & pattern tested
- :construction: Parsing file objects. [chrisr3d]

  - observable added
  - observable & pattern tested
- :construction: Parsing email objects. [chrisr3d]

  - observable added
  - observable & pattern tested
- :construction: Parsing url objects (observable added & tested + pattern tested)
  [chrisr3d]
- :construction: Parsing x509 objects (observable added + pattern & observable
  tested) [chrisr3d]
- :construction: Regkey object parsing + Fix on observable object creation.
  [chrisr3d]
- :construction: Implementing observable objects generation for MISP objects.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- :construction: Should now be able to create indicators for MISP objects.
  [chrisr3d]

  - Patterns generation to be tested
- :construction: Parsing Galaxies. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stix2. [chrisr3d]
- :construction: Fixed typo of some attribute values to delete spaces. [chrisr3d]
- :construction: Catching errors on indicators and observed data, and creating
  custom objects instead. [chrisr3d]
- :construction: Fixed typo & bugs. [chrisr3d]

  - tests made for indicators
- :construction: Dictionary for attributes mapping should be ok. [chrisr3d]
- :construction: Always better with a stix package builder and the output file
  saved. [chrisr3d]
- :construction: Handling special misp types. [chrisr3d]
- :construction: Should  be able to export attributes. [chrisr3d]
- :construction: Refactoring to be continued. [chrisr3d]
- :construction: Dictionary update to go with stix2 export refactoring. [chrisr3d]
- :construction: Refactoring stix2 export & performance improvement. [chrisr3d]
- :construction: First try of refactored stix2 parsing. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3148 from StefanKelm/2.4. [Andras Iklody]

  Update row_attribute.ctp
- Update row_attribute.ctp. [StefanKelm]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Better ttps parsing. [chrisr3d]
- Fixed typo. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: Added Course of Action parsing. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #3144 from geertdr/patch-1. [Andras Iklody]

  Spelling error update
- Spelling error update. [Geert De Ron]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3139 from mokaddem/quick-fix-metacategory-graph.
  [Andras Iklody]

  fix: Event graph stalling when object has unknown-category
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3134 from chkp-aliaksandrt/fix-object-deletion-
  buttons-title. [Andras Iklody]

  fix: Fix wrong object's deletion buttons title
- Merge pull request #3135 from StefanKelm/2.4. [Andras Iklody]

  Update EventShell.php
- Update EventShell.php. [StefanKelm]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3125 from StefanKelm/2.4. [Alexandre Dulaunoy]

  Removed trustedsec.com and openbl.org
- Removed trustedsec.com and openbl.org. [StefanKelm]

  Removed https://www.trustedsec.com/banlist.txt and http://www.openbl.org as per https://github.com/MISP/MISP/issues/2541
- Merge pull request #3119 from 3c7/bugfix/url_default_category.
  [Raphaël Vinot]

  Different category in typeDefinition / defaultCategory
- Assigned "Network activity" as default category for url in
  $typeDefiitions as defined in $defaultCategories. [Nils Kuhnert]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3123 from ldelavaissiere/patch-1. [Alexandre
  Dulaunoy]

  Update INSTALL.ubuntu1604.txt to install pip3
- Update INSTALL.ubuntu1604.txt to install pip3. [Laurent de la V]

  System complains about missing pip3 when attempting to install support for STIX 2.0 (cf. line 88):

  ubuntu@misp:/var/www/MISP/app/files/scripts/mixbox$ pip3 install stix2
  The program 'pip3' is currently not installed. You can install it by typing:
  sudo apt install python3-pip

  Therefore suggest to include installation of python3-pip in previous instance of apt-get usage (line 69)
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3106 from ldelavaissiere/patch-1. [Andras Iklody]

  Update default.ctp in order to fix issue #3105
- Update default.ctp in order to fix issue #3105. [Laurent de la V]

  Re: https://github.com/MISP/MISP/issues/3105
  Adding a <meta> viewport element giving the browser instructions to set the width of the page to follow the screen-width of the device fixes the issue
- Merge pull request #3100 from StefanKelm/2.4. [Andras Iklody]

  Use GnuPG consistently
- Update default.pot. [StefanKelm]
- Update user_management.ctp. [StefanKelm]
- Update Server.php. [StefanKelm]
- Update default.pot. [StefanKelm]
- Update verify_g_p_g.ctp. [StefanKelm]
- Update edit.ctp. [StefanKelm]
- Update check_and_correct_pgps.ctp. [StefanKelm]
- Update admin_email.ctp. [StefanKelm]
- Update admin_edit.ctp. [StefanKelm]
- Update admin_add.ctp. [StefanKelm]
- Update user_management.ctp. [StefanKelm]
- Update administration.ctp. [StefanKelm]
- Update User.php. [StefanKelm]
- Update Server.php. [StefanKelm]
- Update ServersController.php. [StefanKelm]
- Update EventsController.php. [StefanKelm]
- Update AppController.php. [StefanKelm]
- Update default.pot. [StefanKelm]
- Update fetchpgpkey.ctp. [StefanKelm]
- Update README.md. [StefanKelm]
- Update CONTRIBUTING.md. [StefanKelm]
- Update default.pot. [StefanKelm]
- Update misp.js. [StefanKelm]
- Update view.ctp. [StefanKelm]
- Update edit.ctp. [StefanKelm]
- Update admin_view.ctp. [StefanKelm]
- Update admin_edit.ctp. [StefanKelm]
- Update admin_add.ctp. [StefanKelm]
- Update user_management.ctp. [StefanKelm]
- Update administration.ctp. [StefanKelm]
- Update diagnostics.ctp. [StefanKelm]
- Update footer.ctp. [StefanKelm]
- Update User.php. [StefanKelm]
- Update Server.php. [StefanKelm]
- Update Event.php. [StefanKelm]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3071 from AJohnDoe/pass-uuid. [Alexandre Dulaunoy]

  Pass attribute UUID to enrichment modules
- Pass attribute uuid to enrichment modules. [John Doe]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3064 from 3c7/urlhaus-feed. [Alexandre Dulaunoy]

  Added URLhaus (http://urlhaus.abuse.ch) malware urls as feed.
- Added URLhaus (http://urlhaus.abuse.ch) malware urls as feed. [Nils
  Kuhnert]
- Removed variables copied/pasted from stix1 but unused in Stix2.
  [chrisr3d]
- Changed imports & only kept only used pymisp functions. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]

v2.4.89 (2018-03-23)
--------------------

New
---
- Added STIX 2.x import to the GUI. [iglocska]
- Purge all/completed jobs via the job index, fixes #3024. [iglocska]
- Describe the new changes to the deleteAttributes API. [iglocska]
- Added self-description of the deleteAttributes API to the api
  component. [iglocska]
- Open up the attributes/deleteSelected action to the API. [iglocska]
- Allow the searching of organisations by uuid on the event index (via
  the API) [iglocska]
- Finished the first version of the recovery tool. [iglocska]
- Object reconstruction after, resolving the ID bug, :construction:. [iglocska]
- Temp diagnostic tool for orphaned object attributes. [iglocska]
- RestResponse::describe() now uses generic URLs with optional url
  parameters instead of showing the currently accessed ID. [iglocska]
- Include the attribute UUID in the attribute level restsearch.
  [iglocska]

  - simply pass the `includeAttributeUuid` flag and set it to 1 via the API
- Allow requesting of misp standard format for the export modules.
  [iglocska]

  - just set the `require_standard_format` to true in the moduleinfo disctionary

Changes
-------
- Version bump. [iglocska]
- Query string bumped. [iglocska]
- Updates to the deleteAttributes API. [iglocska]

  - Allow passing the "all" wildcard value to the attribute id filter
  - Allow passing the "allow_hard_delete" flag to indicate that hard-deletion of soft-deleted attributes is allowed
- Allow the passing of the event ID via the JSON object for the
  deleteSelected API. [iglocska]
- Use <> as delimiters for the freetext import too, fixes #2978.
  [iglocska]
- Allow GETing the /tags/edit API. [iglocska]

  - will describe itself
  - no ID needs to be passed for the description

Fix
---
- Added annoying missing space between the password field's label and
  it's tooltip. [iglocska]
- Handling case of stix events without timestamp. [chrisr3d]
- Revert one part of timestamp conversion failing. [chrisr3d]
- Quick fix on timestamps comversion. [chrisr3d]
- Critical API integrity bug, potentially allowing users to delete
  attributes of other events. [iglocska]

  - a crafted edit for an event (without attribute UUIDs but attribute IDs set) could overwrite an existing attribute
- Get rid of keyboard shortcut footer tool when debug mode is enabled.
  [iglocska]
- Handle edge case scenarios where orphaned correlations would throw
  notices in the event view. [iglocska]
- PyMISP version is 2.4.89. [Alexandre Dulaunoy]
- PyMISP recommended version fixed. [Alexandre Dulaunoy]
- PyMISP updated to the latest revision. [Alexandre Dulaunoy]
- Various cleanups of the event preview via feeds. [iglocska]
- Support is isSiteAdmin + undeclared var + z-index. [Sami Mokaddem]
- Collapse on object_reference + create object_reference close to the
  parent node when expanding. [Sami Mokaddem]
- Fixed various potential XSS issues in the resolved attributes view.
  [iglocska]

  - potentially exposed XSS if a malicious MISP module was loaded on the instance

  - as reported by Christophe Vandeplas (@cvandeplas)
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- MISP taxonomies updated. [Alexandre Dulaunoy]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- MISP objects updated to the latest version. [Alexandre Dulaunoy]
- Warning lists updated to the latest version. [Alexandre Dulaunoy]
- Added test to check the presence of a timestamp before trying to
  assign it to a variable. [chrisr3d]
- Fixed FileObjectType None values handling. [chrisr3d]
- Added missing space between the password and the info icon. [iglocska]

  - my OCD demands it.
- Fixed password complexity popover in the change password view.
  [iglocska]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Fixed error message if an attribute fails validation via the freetext
  import tool, fixes #3052. [iglocska]
- Fixed PDFFileObjectType parsing. [chrisr3d]

  (waiting for metadata attributes parsing)
- Fixed misp object parsing for cases where there is only 1 attribute.
  [chrisr3d]
- Changed recognition of stix from MISP files. [chrisr3d]

  - Fixed the problem of empty events (for stix from MISP)
    in the API
  - Also removed not used json event loader which would
    not have worked in this refactored version
- Quick fix on object_relation field for port attributes. [chrisr3d]
- Parsing composite attribute types. [chrisr3d]
- Added email-attachment to parsed email properties types. [chrisr3d]
- Fixed various issues with the template views, fixes #3050 among
  others. [iglocska]
- Object values reset when set to a custom value from a sane default
  list, fixes #3049. [iglocska]
- MISP objects updated to the latest version. [Alexandre Dulaunoy]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Fixed view bug causing object reference deletions to fail, fixes
  #3041. [iglocska]
- Parsing pe sections. [chrisr3d]
- Fixed pe filename value parsing. [chrisr3d]
- Updated whois parsing function following recent update on whois
  Object. [chrisr3d]
- Removed console debug output. [iglocska]
- Fixed invalid removal of attributes based on blocked tags using the
  /attributes/restSearch API. [iglocska]
- Tied the clearjobs function into the ACL and fixed a small text error.
  [iglocska]
- Correctly fail validation for invalid composite attributes, instead of
  throwing an exception, fixes #3025. [iglocska]
- Fix notice error when attribute is added with no correlation flag set
  either way. [iglocska]
- MISP taxonomies updated. [Alexandre Dulaunoy]
- MISP objects updated. [Alexandre Dulaunoy]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Fixed invalid object deletion text, fixes #3015. [iglocska]
- Added uuid to organisations in the event index. [iglocska]

  - also unset empty sharing groups from the output
- Fixes an issue where invalid offsets where inspected within the event
  add function, fixes #3006. [iglocska]
- Empty events are created when pulling empty feeds, fixes #3008.
  [iglocska]

  - as described by Emanuele Acri (@crossbowerbt)
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Added sightings to object attributes in the JSON output, fixes #3007.
  [iglocska]
- Added menu option for object reconstruction in the diagnostics page.
  [iglocska]
- Added missing view file for the new object reconstruction tool.
  [iglocska]
- Add misp objects to log search filter. [iglocska]
- Only check the server's publish email flag if the adding of an event
  comes from a remote server. [iglocska]
- Emergency fix for objects getting overwritten on a pull in certain
  situations. [iglocska]

  - object IDs not purged on pull can lead to a local object being overwritten
  - the patch fixes the capture function to purge the object IDs

  - as discovered and reported by TS-WAY (@TS_WAY_SRL)
- Fixed issue blocking the creation of tags, fixes #2989. [iglocska]

  - as described by @Res260
- /attributes/text should allow more than one type to be downloaded.
  [iglocska]

  - simply pass something such as:

  {
    "type": ["ip-src", "ip-dst"]
  }
- Object templates updated. [Alexandre Dulaunoy]
- Warning lists updated to the latest version. [Alexandre Dulaunoy]
- Allow parameters for the /attributs/text endpoint to be passed as a
  JSON object. [iglocska]
- Reworked the way tags are attached to events on the index. [iglocska]

  - solves issues with the preview when an instance has an extremely high number of events
- Fixed issues with to_json() not supporting datetime objects.
  [chrisr3d]
- Fixed an issue with no disable_correlation key existing for an event
  in after save correlation. [iglocska]
- Throw an exception of no ID is passed to /threads/viewEvent, fixes
  #2977. [iglocska]
- Fixed missing index errors on attribute index. [iglocska]
- Open up /attributes/index to the API, fixes #2975. [iglocska]
- Handle the no modules enabled error more gracefully. [iglocska]
- Made the name field required on tags - prevents the error to be thrown
  by the DB instead of the validation. [iglocska]
- Fix tags/add on a GET request via the API. [iglocska]
- Added /tags/add to restresponse. [iglocska]
- Nicer error message when trying to add a tag to an event that doesn't
  exist. [iglocska]
- Changed stupid parameter name to better reflec what it does.
  [iglocska]

  - affects /attributes/restSearch
  - includeAttributeUuid => includeEventUuid
- GUI: Listing Attributes creates many debug.log entries fixes #2969.
  [iglocska]
- Fixed an invalid translation in the attributeRestorationForm causing
  the confirmation to throw an exception, fixes #2967. [iglocska]
- Fixes an issue where editing an object with an attachment contained
  within would soft-delete said attachment, fixes #2966. [iglocska]
- Reverted PR with alternate way of starting scheduler worker.
  [iglocska]
- Don't try to refang filepaths, fixes #2926. [iglocska]
- Misleading failure message when failing to create Attributes partially
  fixes #2955. [iglocska]
- Typo fixed for the previous commit. [iglocska]

  - apparently can't spell distribution
- No distribution set on the server should default to inherit for object
  attributes. [iglocska]
- MISP objects updated. [Alexandre Dulaunoy]
- Attribute distribution defaults fixed for adding objects. [iglocska]
- Disable_correlation now works correctly as expected. [iglocska]
- Warning lists updated to the latest version. [Alexandre Dulaunoy]
- Fixed annoying download list only having one side clickable.
  [iglocska]

  - it was annoying to brigadier general @adulau
- Removed left in debug/thrown exception. [iglocska]

Other
-----
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Update event-graph.js. [Sami Mokaddem]

  Fixed typo in fa-mapping hex value
- Merge pull request #3063 from mokaddem/ref_graph. [Alexandre Dulaunoy]

  Event graph viewer editor
- Registrered funciton in ACLComponent. [Sami Mokaddem]
- Renamed script again. [Sami Mokaddem]
- Renamed script from references-graph to event-graph. [Sami Mokaddem]
- Directly call the callback function in edit_reference so that tha
  manipulation UI get back to normal directly (vis.js iiner behavior)
  [Sami Mokaddem]
- Check if input-search has focus before executing global keyboard
  shortcut. [Sami Mokaddem]
- Restaured stabilization on first load. [Sami Mokaddem]
- Added possibility to edit references on the fly + edit objects on
  their dedicated webpage. [Sami Mokaddem]
- Replaced on/off event function by the once function. [Sami Mokaddem]
- Simplified condition checking on expanding and collapsing nodes. [Sami
  Mokaddem]
- Removed useless progressbar and simplified loading popup information.
  [Sami Mokaddem]
- Improved FIXME comment. [Sami Mokaddem]
- First iteration of refactoring (reference_graph.js): moved functions
  into classes. [Sami Mokaddem]
- Check if the reference is valid before performing the request. [Sami
  Mokaddem]
- Added fullscreen + typeahead feature to network graph. [Sami Mokaddem]
- Added characters limitation in nodes + edit shortcut. [Sami Mokaddem]
- Iglocska's magic (Added kind of ajax support in attribute/edit) [Sami
  Mokaddem]

  C
   (\.   \      ,/)
    \(   |\     )/
    //\  | \   /\\
   (/ /\_#oo#_/\ \)
    \/\  ####  /\/
         `##'
  Ojo
- Improved UX (Generic popup callback + loading and progressbar) + Added
  shortcuts. [Sami Mokaddem]
- Added generic popup callback + Support of item deletion in network
  graph. [Sami Mokaddem]
- Added basic popover for item addition in relation_graph. [Sami
  Mokaddem]
- Reset_view() fits network instead of moving to center only. [Sami
  Mokaddem]
- Typos. [Sami Mokaddem]
- Updated centralGravity so that all nodes are closer to the center.
  [Sami Mokaddem]
- Camera fits the view after initial load. [Sami Mokaddem]
- Added call back parameter in GenericPopup. [Sami Mokaddem]
- Initial references graphs commit. [root]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3057 from jezkerwin/2.4. [Alexandre Dulaunoy]

  Fixed spelling errors for mysql command and php version.
- Fixed spelling errors for mysql command and php version. [jezkerwin]

  Also changed git clone command for lief installation.
- Typo. [chrisr3d]
- Quick fix on filename / filepath parsing. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Quick fix with indicator's timestamp. [chrisr3d]
- Quick variable fix. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Updated comments: removed commented unused code & added documentation.
  [chrisr3d]
- Stix2misp refactor & update !! [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into stiximport. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: Parsing attachments. [chrisr3d]
- :construction: Starting parsing portable executables. [chrisr3d]
- :construction: Added description parsing for stix objects without properties.
  [chrisr3d]
- :construction: Whois parsing function improved. [chrisr3d]

  Still need some tests with proper examples to finish this part
- :construction: Starting parsing Whois Objects. [chrisr3d]

  But need some examples to parse properly !!!!
- :construction: Rebuilt hashes & files parsing functions. [chrisr3d]

  Also handling more properly when to import a stix
  object as a MISP Object or as Attribute
- Merge pull request #3029 from chrisr3d/stiximport. [Christian Studer]

  Refactor stiximport
- Merge branch 'stiximport' of github.com:MISP/MISP into stiximport.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #3017 from AJohnDoe/fix/module-select. [Andras
  Iklody]

  Fixes display of <select> (dropdown) in import module, closes #3005
- Fixes display of <select> (dropdown), closes #3005. [John Doe]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Display "event" instead of "organisation" - Org Blacklist, fixes
  #2473. [Andras Iklody]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Fixed key value that was not correct. [chrisr3d]
- :construction: More types supported & functions clarified. [chrisr3d]
- :construction: Starting to import external stix. [chrisr3d]
- :construction: Supporting more Object types. [chrisr3d]
- :construction: handling malware-sample in file objects. [chrisr3d]
- :construction: Supporting more attribute types. [chrisr3d]
- :construction: Parsing more attribute types & objects. [chrisr3d]

  - More attribute types and objects to come with events testing
- First version parsing some attributes. [chrisr3d]

  - More attribute types to be added
  - Objects to be parsed as well
- :construction: Refactor of  stix2misp - only a beginning atm. [chrisr3d]
- Merge pull request #3012 from Res260/feature_keyboard_navigation.
  [Andras Iklody]

  Add keyboard navigation when choosing tags for an event
- Added a delay before doing the request when searching for tags in the
  taxonomy choice. This reduces the possibility of losing characters
  when typing fast. [Émilio Gonzalez]
- - Added keyboard navigation with arrows/pageUp/pageDown/enter for tag
  selection ( Issue #3001 ) - The color when hovering over a modal
  element is now grey, to differentiate from blue when choosing tags
  using keyboard. [Émilio Gonzalez]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #3004 from RichieB2B/ncsc-nl/empty-stix. [Andras
  Iklody]

  Allow empty STIX files to be returned, closes #2478
- Avoid 'Invalid argument supplied for foreach()' warning. [Richard van
  den Berg]
- Allow empty STIX files to be returned, closes #2478. [Richard van den
  Berg]
- Merge pull request #3002 from P4rs3R/patch-2. [Alexandre Dulaunoy]

  pecl and phpenmod need root privileges
- Pecl and phpenmod need root privileges. [x41\x43]

  [line 329] According to stat -c "%U %G" /usr/share/php/.channels/pecl.php.net, the owner is root, so you can't edit this file as normal user,
  [line 333] As above, both directories (/etc/php/7.0/cli/conf.d/ and /var/lib/php/modules/7.0/cli/enabled_by_admin/) are "root root": "Permission denied" while creating symbolic link or touching file.
  Tested on Ubuntu server x64 16.04 LTS
- Merge branch 'feature/objectreconstruction' into 2.4. [iglocska]
- Merge branch '2.4' into feature/objectreconstruction. [iglocska]
- Merge pull request #2997 from 0xmilkmix/validate_suricata_rules.
  [Andras Iklody]

  Validate suricata rules
- Removed tests from class. [milkmix]
- Finished http validation function using sticky and modifiers.
  [milkmix]
- Wrote dns validation func, checking modifier after dns_query keyword.
  [milkmix]
- Added options extraction function. [milkmix]
- Added validation function for global syntax. [milkmix]
- Initial regexp to match rule pattern. [milkmix]
- Merge pull request #2996 from Res260/fix_IE11. [Andras Iklody]

  Fix IE11 final: remove arrow function (ecmascript6 stuff)
- Fix IE11 final: remove arrow function (ecmascript6 stuff) [Émilio
  Gonzalez]
- Merge pull request #2995 from Res260/fix_IE11. [Alexandre Dulaunoy]

  Part 3: Fix IE11 by surrounding a new Promise call with try/catch
- Part 3: Fix IE11 by surrounding a new Promise call with try/catch.
  [Émilio Gonzalez]
- Merge pull request #2993 from Res260/fix_IE11. [Andras Iklody]

  Actually remove keyboard shortcuts from MISP.js
- Actually remove keyboard shortcuts from MISP.js. [Émilio Gonzalez]
- Merge pull request #2992 from P4rs3R/patch-1. [Andras Iklody]

  sudo issue while installing mixbox
- Sudo issue while installing mixbox. [x41\x43]

  sudo -u www-data [#83 and #85]
  sudo [#86]
  Tested on Ubuntu Server x64 16.04.4 LTS
- Merge pull request #2991 from LDO-CERT/2.4. [Andras Iklody]

  Fixed publish_without_email for server sync
- Fixup if statemant for mail and log message  cleanup. [lucamemini]

  fixup if statemant for mail and log message  cleanup
- Delete Event.php. [lucamemini]
- Fixup if statement for log message. [lucamemini]

  Fixup if statement for log message
- Fixed publish_without_email for remove server event. [lucamemini]

  Fixed broken support for publish_without_email to block email notification when event is pulled from remote server and flag "Publish Without Email" is enabled.
- Merge pull request #1 from MISP/2.4. [lucamemini]

  Refresh from upstream
- Merge pull request #2990 from Res260/fix_IE11. [Andras Iklody]

  Move keyboard shortcuts from misp.js to its own file (to regain compatibility with IE11)
- Move keyboard shortcuts from misp.js to its own file (to regain
  compatibility with IE11) [Émilio Gonzalez]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2985 from Res260/fix_filename_ssdeep_import.
  [Andras Iklody]

  Fixed a bug regarding filename|ssdeep attributes importing using FreeTextImport
- Fixed a bug regarding filename|ssdeep attributes importing using
  FreeTextImport. See Issue #2971. [Émilio Gonzalez]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2979 from SteveClement/2.4. [Alexandre Dulaunoy]

  Added install step to make sure submodule permissions are ignored
- - Added install step to make sure all the submodules ignore
  permissions. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:SteveClement/MISP into 2.4. [Steve
  Clement]
- Merge remote-tracking branch 'origin/i18n_prep' into 2.4. [Steve
  Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2962 from Res260/add_pointer_triangle. [Andras
  Iklody]

  Small keyboard shortcuts changes
- Add attribute shortcut now triggers the popup instead of changing page
  + bottom right triangle now with pointer cursor. [Émilio Gonzalez]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]

v2.4.88 (2018-02-21)
--------------------

New
---
- Add API response for /sightings/listSightings. [Andras Iklody]
- Reowkred organisation merge workflow, #fixes 2931. [iglocska]

  - Organisation merge is now offered to the user by the edit page if a UUID was used to edit an organisation that is already in use
  - Merging a local org with 1+ user(s) into an external organisation converts the target organisation into a local one
  - Merging a local organisation with a logo into an organisation without one will move the current logo to over
    - caveat: this will only happen for organisations already using the new logo naming ([id].png as opposed to [name].png)
- ModulesQueryAPI. [Juan C. Montes]

  ModulesQuery controller to can communicate from MISP API to misp_modules
- ModulesQueryAPI. [Juan C. Montes]

  ModulesQuery controller to can communicate from MISP API to misp_modules
- ModulesQueryAPI. [Juan C. Montes]

  ModulesQuery controller to can communicate from MISP API to misp_modules
- ModulesQueryAPI. [Juan C. Montes]

  ModulesQuery controller to can communicate from MISP API to misp_modules
- ModulesQueryAPI. [Juan C. Montes]

  ModulesQuery controller to can communicate from MISP API to misp_modules
- ModulesQueryAPI. [Juan C. Montes]

  ModulesQuery controller to can communicate from MISP API to misp_modules
- ModulesQueryAPI. [Juan C. Montes]

  ModulesQuery controller to can communicate from MISP API to misp_modules
- ModulesQueryAPI. [Juan C. Montes]

  ModulesQuery controller to can communicate from MISP API to misp_modules
- Added ssdeep threshold setting. [iglocska]

  - set the ssdeep value at which to consider two ssdeep hashes as correlating
- First iteration of ssdeep correlation. [iglocska]
- Added supporting structures for the new STIX API. [iglocska]
- Added STIX import directly to the UI. [iglocska]
- Add search shortcut for events and attributes + fix bug that triggered
  shortcuts when dropdown menus were focused. [Émilio Gonzalez]
- Add keyboard shortcuts application-wide, managed using JSON files.
  [Émilio Gonzalez]
- Add a "search all tags" input field on the taxonomy modal when adding
  a tag to an event. [Émilio Gonzalez]
- Added returnMetaAttributes flag to the /events/freeTextImport API.
  [iglocska]

  - directly returns the raw parsing data instead of creating the attributes if set
  - 177 days, 23 hours 40 minutes faster implementation than expected by @ilmoka - #PMD
- New APIs to add/remove orgs and servers from sharing groups, fixes
  #2888. [iglocska]

  - added functions to manage the additions/removals of objects from sharing groups
  - the following APIs are included:
    - /sharingGroups/addOrg/[sg_id]/[org_id]/[extend]
    - /sharingGroups/removeOrg/[sg_id]/[org_id]
    - /sharingGroups/addServer/[sg_id]/[server_id]/[all_orgs]
    - /sharingGroups/removeServer/[sg_id]/[server_id]

  - All parameters are optional and can instead be passed as JSON objects such as:

    {
      "org_uuid": "55f6ea5e-2c60-40e5-964f-47a8950d210f",
      "sg_id": "49",
      "extend": 1
    }

  - The API is extremely flexible with how to name objects, the following parameters are allowed:
    - Organisations:
      - org_id (The organisation's local instance ID)
      - org_uuid (The organisation's global UUID)
      - org_name (The organisation's identifier as known to the curent instance)
    - Server:
      - server_id (The server's local instance ID)
      - server_url (The URL of the server)
      - server_name (The local name of the server as assigned when adding the server)

  The sharing groups can also be addressed by ID or UUID.
- Allow overriding the action names in the stringified restresponse
  messages. [iglocska]

  - for example: 'addOrg' => 'add Organisation to'

Changes
-------
- Version bump. [Alexandre Dulaunoy]
- Bump PyMISP. [Raphaël Vinot]
- Updated documentation. [iglocska]
- Bump PyMISP to 2.4.87. [Raphaël Vinot]
- Bump PyMISP recommended version. [Raphaël Vinot]
- Bump PyMISP, again. [Raphaël Vinot]
- Bump PyMISP. [Raphaël Vinot]

Fix
---
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- PyMISP fixed to the latest version. [Alexandre Dulaunoy]
- Ssdeep is now updated on PECL - installation updated. [Alexandre
  Dulaunoy]
- Warning-lists updated to the latest version. [Alexandre Dulaunoy]
- Typo in README. [Alexandre Dulaunoy]
- Resolved a potentially breaking issue for feed fetches with malformed
  objects. [iglocska]
- Keep the original org name if merging an org into a newer copy with a
  number appended (such as _1111) [iglocska]

  - no need to edit the resulting merge anymore
- Add org with known remote UUID fails silently, fixes #2930. [iglocska]
- Various fixes to the module api. [iglocska]

  - query function renamed to query enrichment
  - added check for disabled modules and for modules that the current user is not allowed to use
  - removed the module config from the index function to avoid exposing API keys / credentials to users
  - some formating fixes
- ModulesController. [Juan C. Montes]
- Searching for exact values not possible via the attribute search,
  fixes #2946. [iglocska]

  - Attribute search now returns only exact matches unless encapsulates between '%' characters
- Now supporting stix objects with only description text. [chrisr3d]

  - These objects are indicators or observables
  - Description text in imported as misp attribute 'text'
- Fixed an issue where events wouldn't get properly unpublished when
  accepting a proposal, fixes #2943. [iglocska]

  - only happened when a proposed new attribute was accepted, masking the issue
- Fixed command execution for site admins. [iglocska]

  - a server setting allowing the override of the path variable for esoteric RHEL systems allowed site admins to inject arbitrary commands
  - impact was limited by the setting being only accessible to the site administrator

  - as reported by Michael Grolimund from Swiss Post (@grolinet)

  - CVE-2018-6926
- Fixed invalid pgp url for fetching keys from the remote server.
  [iglocska]
- Removed debug code, added cleanup for edits/deletes. [iglocska]
- Fixed the attribute selection on the event view. [iglocska]

  - Correctly select sections even on sort or other effects changing the order of elements
  - Part of the keep @rommelfs happy package ;)
- Do not try to decrement attribute count below 0. [iglocska]
- Fixed mass delete for soft-deleted attributes. [iglocska]
- Make soft vs hard deletes more obvious. [iglocska]
- Hop over commented out functions in the queryACL tests. [iglocska]
- Parsing more types. [chrisr3d]

  - ignoring whois atm

  - creating object "file" in case of multiple hashes
    in only one observable / indicator object
- PyMISP latest version. [Alexandre Dulaunoy]
- Changed the condition to recognize stix from misp. [chrisr3d]
- Add a baseurl if none is set for the stix framing. [iglocska]

  - otherwise we end up with a namespace leading to an empty URL which apparently is the STIX library's kwqryptonite
- Removed the truncating of output file names for the stix2misp script.
  [iglocska]
- Fixes to several cases of handling blocked access incorrectly / non-
  gracefully. [iglocska]

  - As reported by Christophe Vandeplas

  - stix export: Ungraceful handling of attempted access of unauthorised event (no unauthorised data returned)
  - import module: Allows creation of proposals to unauthorised events (no unauthorised data returned, proposals are for new attributes only meaning no automatic override triggered)
  - saveFreetext: same as import module
- Don't uppercase the shortcuts as the shortcuts are lowercase.
  [Alexandre Dulaunoy]
- CVE en dash converted to '-' [iglocska]
- Fixed extension name of imported files. [chrisr3d]
- Fixed wrong dictionary key call causing empty import. [chrisr3d]
- Updated to the latest version of PyMISP. [Alexandre Dulaunoy]
- Removed object template element changes from logging system.
  [iglocska]

  - temporary fix for the model name being too long...
- Escaping user controlled variable. [Andras Iklody]
- Run the db update before trying to add users/orgs. [iglocska]
- Added missing db field to users. [iglocska]

  - fixes a nasty issue with saving users failing when ZMQ is enabled on instances installed after 2.4.69
  - fixes a typo that caused invalid user changes being pushed to the ZMQ channel
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- Added new APIs to ACL component. [iglocska]

  - wooooops
- Set the default PGP keyserver to pgp.circl.lu (faster than
  pgp.mit.edu) [Alexandre Dulaunoy]

  TODO: A configuration for setting up the PGP keyserver at the MISP
  instance setting.
- MISP objects latest version imported (fix ip-port issue with domain)
  [Alexandre Dulaunoy]
- User_id in tag table was not included in MYSQL.sql. [iglocska]

  - added it to the initial db bootstrap along with an upgrade script for existing MISPs missing the field
- Galaxy updated to the latest version. [Alexandre Dulaunoy]
- Fix adding tags via the API fails if not encapsulated in "Tag":{},
  fixes #2897. [iglocska]

  - also, add proper response instead of a redirect to make testing a bit more friendly
- Taxonomies updated. [Alexandre Dulaunoy]
- MISP objects updated. [Alexandre Dulaunoy]
- Fix an invalid call to saving a log entry without initialising the
  class first. [iglocska]
- Graceful handling of gnupg not being set up on an instnace. [iglocska]

Other
-----
- Update list_sightings.ctp. [Andras Iklody]
- Add: Updated to the latest version of taxonomies including new ones.
  [Alexandre Dulaunoy]
- Merge branch 'galaxySearch' into 2.4. [iglocska]
- Add filter on GalaxyCluster description too ^^ [truckydev]
- Apply filter to pagination :) [root]
- Add field filter for galaxy cluster. [root]
- Merge pull request #2934 from cvandeplas/fix/modules-api. [Andras
  Iklody]

  fix - allows upload of files using the misp-modules API
- Fix - allows upload of files using the misp-modules API. [Christophe
  Vandeplas]

  See also #2719
- Merge pull request #2950 from eCrimeLabs/2.4. [Andras Iklody]

  Update start.sh
- Update start.sh. [eCrimeLabs]

  Fixed bug in scheduler line
- Merge branch 'modulesQuery' into 2.4. [iglocska]
- Merge branch 'ModulesQueryAPI' of https://github.com/juancmontes/MISP
  into ModulesQueryAPI. [Juan C. Montes]
- Update ModulesQueryController. [Juan C. Montes]

  Fix the format of the code
- Update ModulesQueryController. [Juan C. Montes]

  Support options (credentials) from config.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2944 from truckydev/patch-10. [Andras Iklody]

  Add the value in the field when filled in.
- Add the value in the field when filled in. [truckydev]

  add the value in the field when filled in on event view.
- Merge pull request #2945 from truckydev/patch-11. [Andras Iklody]

  don't exlude attributes with non-exportable tag
- Don't exlude attributes with non-exportable tag. [truckydev]

  exclude filter on attributes when tag is non-exportable
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2941 from
  MattCarothers/fix_log_table_model_column_length. [Andras Iklody]

  Update model column length to 80 characters in the MySQL install file
- Updated model column length to 80 characters. [Matt Carothers]
- Add: new feeds from CoinBlockerLists added. [Alexandre Dulaunoy]
- Merge branch 'feature/ssdeep_correlations' into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Add: mime-type attribute added. [Alexandre Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #2908 from Res260/fix_keyboard_shortcut_focus.
  [Andras Iklody]

  new: Add search shortcut for events and attributes + small bugfix
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2906 from Res260/feature_keyboard_shortcuts.
  [Alexandre Dulaunoy]

  new: Add keyboard shortcuts application-wide, managed using JSON files
- Add: identity-card-number attribute type to better support goAML.
  [Alexandre Dulaunoy]
- Merge pull request #2902 from
  Res260/feature_search_tags_on_taxonomy_modal. [Andras Iklody]

  Make search bar available in the "Select Tag Source" modal
- Added vendor and CakeResque folders to gitignore. [Émilio Gonzalez]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: a default category for GENE attribute type. [Alexandre Dulaunoy]
- Add: GENE: Go Evtx sigNature Engine attribute type added. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2899 from RichieB2B/ncsc-nl/misp-wipe-update.
  [Andras Iklody]

  Wipe objects & update lists after wipe
- - wipe objects - update taxonomies, warninglists, galaxies and
  objectTemplates after wipe. [Richard van den Berg]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2886 from MISP/Bump-PyMISP. [Raphaël Vinot]

  chg: Bump PyMISP recommended version
- Merge pull request #2883 from Rafiot/travis. [Raphaël Vinot]

  chg: Bump PyMISP

v2.4.87 (2018-01-28)
--------------------

New
---
- Mispzmq.py updated with new topic (tags) [iglocska]
- Added boolean attribute type. [iglocska]
- New upgrade system. [iglocska]

  - decouple db changes from version number
- Tie tags into PubSub channel. [iglocska]

  - Reset the catastrophic @ilmoka enrage timer for another 5 days
- Add restore script. [Jérôme Leonard]
- Add regex type to warninglists. [iglocska]
- New BasicAuth header generator for the feed add/edit views. [iglocska]
- Use the new OrgImg helper for fetching org logos in a more consistent
  fashion. [iglocska]
- OrgImgHelper - lookup org logoes in a similified helper, accounting
  for old and new style logo filenames. [iglocska]
- Allow passing headers along with feeds. [iglocska]

  - add any arbitrary header to a feed
  - can be used for authentication via basic auth for example
- Tell users about our lord and saviour, MISP-objects if they try to add
  a composite attribute. [iglocska]
- Filter the event index on sharing group IDs, fixes #2845. [iglocska]
- First export of pot files. [iglocska]
- Automatic cateory switching based on currently selected types for the
  freetext import/module triage screen. [iglocska]

Changes
-------
- Version bump. [iglocska]
- Rework of the event history view, no more crazy slow parsing of all
  strings in the log table. [iglocska]
- Allow the "uuid" key to work as an alternate for "id" when adding
  sightings. [iglocska]
- Various fixes to the way organisations are handled. [iglocska]

  - fix a bunch of issues with the org displays
  - hide organisation view from users if they haven't yet contributed data and Security.hide_organisation_index_from_users is enabled
- Add MISP book phrase to Readme. [Andras Iklody]
- Save org logos based on the org ID not the org Name. [iglocska]
- Get rid of the weird http:// baseurls and set some helper variables
  for the views. [iglocska]

  - Also load the new OrgImg helper
  - @SteveClement wubs global view variables
- Tuned the freetext import tool, fixes #2822. [iglocska]

  - refang e-mail addresses
  - add [@] refanging
- Clarified feed action buttons. [iglocska]

Fix
---
- Removed the crazy complex lookup for attribute tag counts from the tag
  index. [iglocska]

  - Users will see the total count without any context avoiding ACL - however, they are still limited to seeing the actual data tagged that they can see anyway.
- Fixed double json decoding due to recent changes to galaxy clusters.
  [iglocska]
- View issue fixed caused by previous commit. [iglocska]
- Fixed some galaxy cluster inconsistencies. [iglocska]
- Latest version of MISP galaxy. [Alexandre Dulaunoy]
- Resolved an issue where attaching tags to attributes via the generic
  attachToObject() function was throwing an error. [iglocska]
- Reduced memory usage of tags index when requesting it via the API.
  [iglocska]
- Load orgc data after attributes are loaded in search csv export.
  [iglocska]

  - functionality still needs further fixes, :construction:
- Graceful handling of removed users in discussion boards. [iglocska]
- Suricata export URL encodes an IPv6 between [], fixes #2872.
  [iglocska]
- Fixed an issue where searching for a non-existing organisation in the
  attribute search returned any visible attributes no matter the org.
  [iglocska]
- Fixed messed up org logos in attribute search. [iglocska]
- Default sort order for id / date reversed on click for #2723.
  [iglocska]
- Improved feedback when importing a blacklisted event, fixes #2859.
  [iglocska]
- New mutex object, updated person object and improved registry-key
  object. [Alexandre Dulaunoy]
- Fixed a TLP marking issue. [chrisr3d]

  (related to github issue #2623)
  Marking is no longer influenced by distribution
  level whenever Tags are set:
  - in the current attribute
  - in the event
- Object deletion view was bugged and non-functional. [iglocska]
- Retain the distribution level / sharing group ID when doing advanced
  attachment extraction, fixes #2865. [iglocska]
- Clarifies the scope of a BIC code in the financial sector. [Alexandre
  Dulaunoy]

  The Business Identifier Codes (also known as SWIFT-BIC, BIC, SWIFT ID
  or SWIFT code)...
- Added missing things for the new org image loader. [iglocska]
- Make hover enrichments work again within objects, fixes #2793.
  [iglocska]
- Fixes the object issues pointed out in #2543. [iglocska]

  - Shoutout to the debug hero finding them: @StefanKelm
- Added missing switch to the new OrgImg helper for the proposal index.
  [iglocska]
- Fix editing of an organisation that has domain restrictions set.
  [iglocska]
- Fixed an issue with invalid termination for a php block in HTML.
  [iglocska]
- Fixed an issue where mass accepting proposals didn't unpublish the
  event. [iglocska]

  - @rommelfs sees all
- Don't listen to David and Andras together ;-) [Alexandre Dulaunoy]
- Fixed a set of issues with sharing groups that lead to synced events
  not saving/updating. [iglocska]
- Add timestamp to the CSV api. [iglocska]
- Fixed invalid lookup when a non site admin searches for attributes,
  fixes #2849. [iglocska]
- Clarify timestmap parameter for attributes. [iglocska]
- Add flatten to advanced sightings add within objects. [iglocska]

  - without the flattening the advanced sighting add functionality couldn't be loaded
- Don't block email headers from being added if they have a line break
  in them. [iglocska]
- Superfluous > [iglocska]
- Fixed invalid syntax. [iglocska]
- Add alternative x509 fingerprint hashes to the freetext import tool,
  fixes #2821. [iglocska]
- Aadmin settings version updated. [iglocska]
- Fixed the inversed confirmation warning for enabling/disabling feeds.
  [iglocska]
- PyMISP updated to latest version. [Alexandre Dulaunoy]
- Missing action added to ACL system. [iglocska]

Other
-----
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: MISP galaxy updated. [Alexandre Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Add: update to the latest version of MISP objects templates.
  [Alexandre Dulaunoy]
- Some clarifications of unclear descriptions. [Andras Iklody]
- Merge pull request #1969 from devnull-/GPG_sign_option. [Andras
  Iklody]

  Add a option to sign GPG emails
- Merge branch '2.4' into GPG_sign_option. [devnull-]
- Implement 'sign' option. [devnull-]
- Description of the option 'sign' [devnull-]
- Add option 'sign' in GPG section. [devnull-]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2869 from jeromeleonard/backup_restore. [Andras
  Iklody]

  Backup and restore MISP configuration and database
- Update: add information for misp-restore.sh script. [Jérôme Leonard]
- Update: add Config php files to backup. [Jérôme Leonard]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2850 from eurodude/patch-1. [Andras Iklody]

  #2788 Corrected Dependencies in documentation
- Corrected Dependencies. [Fabien Mathey]

  Added additional information for installation (Python 3 for stix2, a2enmod headers)

  Additionally, line 120 should not be needed as it should be covered by line 119 but I left it in for the time as it does no harm
- Merge branch 'i18n' into 2.4. [iglocska]
- Merge branch '2.4' into i18n. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2847 from Deventual/patch-13. [Andras Iklody]

  fix permissions commands
- Fix permissions commands. [Deventual]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2832 from treed593/patch-1. [Andras Iklody]

  Update README.md
- Update README.md. [Trevor Reed]
- Merge pull request #2848 from SteveClement/i18n_prep. [Steve Clement]

  I18n - re-Sync
- Merge branch '2.4' into i18n_prep. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Update index.ctp. [Andras Iklody]
- Merge pull request #2831 from MattCarothers/fix_null_job_input_field.
  [Andras Iklody]

  Set job_input explicitly to an empty string for cache feed jobs
- Set job_input explicitly to an empty string for cache feed jobs Older
  MISP deployments may interpret a missing field as a null value instead
  of an empty string, which causes the NOT NULL restriction on the
  jobs.job_input field to raise an error.  Fixes issue #2804. [Matt
  Carothers]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2791 from SteveClement/i18n_prep. [Steve Clement]

  Merging i18n preparations from fork to branch.
- Merge remote-tracking branch 'origin/2.4' into i18n_prep. [Steve
  Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- - Feeds/compare_feeds.ctp. [Steve Clement]
- - Fixed various typos/omissions etc. [Steve Clement]
- - Closing parenthesis mistake. [Steve Clement]
- View/SharingGroups -> __(' [Steve Clement]
- View/Sightings -> __(' [Steve Clement]
- View/Taxonomies -> __(' [Steve Clement]
- View/Tasks -> __(' [Steve Clement]
- View/Templates -> __(' [Steve Clement]
- View/ShadowAttributes -> __(' [Steve Clement]
- View/Tags -> __(' [Steve Clement]
- View/Events -> __(' [Steve Clement]
- - View/TemplateElements -> __(' to be completed. [Steve Clement]
- - View/Taxonomies -> __(' to be completed. [Steve Clement]
- - View/Threads -> __(' to be completed. [Steve Clement]
- - View/Users -> __(' to be completed. [Steve Clement]
- - __(' round 1, done. [Steve Clement]
- - View/Warninglists -> __(' to be completed. [Steve Clement]
- - View/Whitelists -> __(' to be completed. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into i18n_prep. [Steve
  Clement]
- - View/Pages -> __(' (Except using_the_system.ctp) [Steve Clement]
- - This is another textual beast… [Steve Clement]
- - Fixed automation.ctp parser errors. [Steve Clement]
- View/Organisations -> __(' [Steve Clement]
- - View/Pages -> __(' to be completed. [Steve Clement]
- - View/OrgBlacklists -> __(' done. [Steve Clement]
- - View/Objects -> __(' done. [Steve Clement]
- - View/Regexp -> __(' done. [Steve Clement]
- - View/Servers -> __(' done. [Steve Clement]
- - View/Roles -> __(' done. [Steve Clement]
- - View/Posts -> __(' done. [Steve Clement]
- Merge branch 'i18n_prep' of github.com:SteveClement/MISP into
  i18n_prep. [Steve Clement]
- - View/Objects -> __(' [Steve Clement]
- - View/Layouts -> __(' [Steve Clement]
- - Added remaining __(' - needs double checking. [Steve Clement]
- - View/ObjectTemplateElements -> __(' done. [Steve Clement]
- - View/Helper -> __(' done. [Steve Clement]
- - View/News -> __(' done. [Steve Clement]
- - View/Logs -> __(' done. [Steve Clement]
- - View/Jobs -> __(' done. [Steve Clement]
- - Some typo fixes and formatting amendments. [Steve Clement]
- - View/Galaxies -> __(' done. [Steve Clement]
- - View/ObjectReferences -> __(' done. [Steve Clement]
- - View/ObjectTemplates -> __(' done. [Steve Clement]
- - app/View/Elements/ --> __(' [Steve Clement]
- - Refactor format string. [Steve Clement]
- - app/View/Events/ --> __(' [Steve Clement]
- - View/Events/automation.ctp -> Partially done, a lot needs to be
  __('-ized. [Steve Clement]
- - View/Feeds -> __(' done. [Steve Clement]
- - View/EventDelegations/ajax -> __(' done. [Steve Clement]
- - View/Errors -> __(' done. [Steve Clement]
- - View/EventBlacklists -> __(' done. [Steve Clement]
- Merge branch 'i18n_prep' of github.com:SteveClement/MISP into
  i18n_prep. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into i18n_prep. [Steve
  Clement]
- - Elements/templateElements/populateTemplateAttribute.ctp -> __('
  [Steve Clement]
- - Elements/Users/userIndexTable.ctp  -> __(' [Steve Clement]
- - Elements/ajaxAttributeTags.ctp Elements/ajaxTags.ctp
  Elements/ajaxTemplateTag.ctp -> __(' [Steve Clement]
- - Events/view.ctp -> __(' [Steve Clement]
- - Elements/side_menu.ctp -> __(' [Steve Clement]
- - Elements/histogram.ctp -> __(' [Steve Clement]
- - Elements/Servers -> __(' [Steve Clement]
- - Fixed typo, added __(' where missing. [Steve Clement]
- - Fixed typo and spacing. [Steve Clement]
- - Elements/Events/eventIndexTable.ctp -> __(' [Steve Clement]
- - Elements/healthElements -> __(' [Steve Clement]
- - Elements/Events/View -> __(' [Steve Clement]
- - Replaced random '.......' with '…' - __(' where neeeded. [Steve
  Clement]
- - View/Events/index.ctp -> __(' [Steve Clement]
- - View/Servers -> __(' done. [Steve Clement]
- - View/Elements/Feeds -> __(' checked and added where needed. [Steve
  Clement]
- Merge remote-tracking branch 'upstream/2.4' into i18n_prep. [Steve
  Clement]
- Merge remote-tracking branch 'origin' into i18n_prep. [Steve Clement]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Steve Clement]
- Merge branch 'i18n_prep' of github.com:SteveClement/MISP into 2.4.
  [Steve Clement]
- Merge remote-tracking branch 'origin' into i18n_prep. [Steve Clement]
- - __(' -> Added where needed. [Steve Clement]
- - Typo. [Steve Clement]
- - __(' where needed - fixed Typo 'C' [Steve Clement]
- - View/Elements/dashboard -> __(' -> Done! #i18n_prep. [Steve Clement]
- - Removed Sublime fail :( [Steve Clement]
- - Final files in View/Attributes … for now. - Most views tested and
  known working as expected. [Steve Clement]
- - Removed some echo ('foo') / echo('bar') -> Coding rules want: echo
  foo - Added numerous __(' for i18n. [Steve Clement]
- - __(' added where needed. [Steve Clement]
- - Attributes folder scavenged for Translatables… [Steve Clement]
- - __('')-ized labels, buttons, styles. [Steve Clement]

v2.4.86 (2018-01-16)
--------------------

New
---
- Mass enable/disable feeds. [iglocska]

  - protecting the sanity of MISP admins since 2012!
- Disable the viewing of a full organisation list by normal users.
  [iglocska]

  - Only site admins and sharing group editors can see organisation lists
    - this includes the org index and various statistics
  - Keep in mind: Sharing group editors CAN see the full organisation list - otherwise they wouldn't be able to create sharing groups.
  - Also, users CAN enumerate organisations that have created ANY data on the instance by looking at the given data
    - this includes events, proposals, discussion entries, etc
- Expose the Sharing Groups to the API, fixes #2767. [iglocska]

  - Add/Edit/Index/View now exposed to the API
  - rework of the sharing group capturing process
  - fix to an issue that could potentially block sharing groups from being synced (the creator org of the sharing group wasn't directly exposed and an edit to the organisation's UUID after creating the SG could make the SG non-syncable)

  - various fixes to edge cases
  - descriptors to the add/edit APIs via restresponse

  - Operation "Just relaxing and looking at stuff for the baby online" - the x-mas covert development patch(tm)
- Limit modules to a single organisation. [iglocska]

  - new settings in serverSettings
- Add API description to sightings/add, fixes #2806. [iglocska]
- Allow the collapsing of related events on the event view. [iglocska]

Changes
-------
- Version bumped. [iglocska]
- Warninglists updated. [iglocska]
- Performance tuning. [iglocska]

  - improved performance of inserting batch attributes / passing a large number of attributes to attributes/add
    - reworked algorithm to a two phase bulk insertion (validation -> mass insert) instead of looping through all attributes
    - removed the build in counter cache for incrementing attribute counts on events in favour of a more lightweight solution
    - performance gains on test data set: 50+ seconds -> 32 seconds

  - Greatly improved attribute index / attribute search performance
    - fixed an issue that caused the lookup to avoid using indeces
    - performance gains on test data when paginating: 11 seconds -> 1 second
- Add hybrid analysis to the freetext import tool, fixes #2797. [Andras
  Iklody]
- Bump PyMISP. [Raphaël Vinot]
- Show x more attributes collapse toggle on the attribute correlations
  now in brackets so people don't accidentally mix the count up with
  event IDs. [iglocska]

Fix
---
- Remove the option for disabling sightings - it's an integral feature
  of the MISP core. Fixes #2820. [iglocska]
- Fixed image element. [iglocska]
- Changed name of server settings -> server settings & maintenance,
  fixes #2817. [iglocska]
- Fixed various visual feed issues, fixes #2818, fixes #2819. [iglocska]
- Fixed a bug that caused sharing groups within objects to not be
  captured correctly, fixes #2816. [iglocska]
- Added missing view. [iglocska]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Updated to the latest version of the taxonomies. [Alexandre Dulaunoy]
- Latest version of the MISP galaxy updated. [Alexandre Dulaunoy]
- Sharing group ID set to the correct value if set implicitly by setting
  the ID instead of passing a full sharing group object along, fixes
  #2814. [iglocska]

  - also, fail if no valid sharing group was found.
- Added missing local field to fetched sharing groups, fixes #2812.
  [iglocska]
- Parsing more stix doc structures. [chrisr3d]
- Invalid algorithm used for warninglist. [iglocska]
- Objects not purged correctly when deleting an event, fixes #2810.
  [iglocska]

  - correctly included objects now in the quick delete function
  - new upgrade script that purges existing orphaned objects
- Removed debug. [iglocska]
- Clarify scope for filter options in quick search. [iglocska]
- Better attribute add feedback on validation fail and fix to a failing
  attribute index listing for normal users. [iglocska]
- Fixed misaligned org view. [iglocska]
- Fix to invalid role check preventing users from seeing the org index,
  even if they should have access. [iglocska]
- Fixed weird eating of event titles on certain unicode characters.
  [iglocska]

  - substr choked on them and produced empty strings
- Fixed typo. [iglocska]
- Removed a small slice of stupidity. [iglocska]
- Changed checks from isSiteAdmin to isAclSharingGroup for the org index
  anonymisation. [iglocska]
- Better error handling when previewing csv/freetext feeds if no valid
  data is returned. [iglocska]
- Better handling of something going wrong whilst fetching a MISP feed's
  manifest. [iglocska]
- Removed loading of roboto font css - as it hasn't actually been used
  for years. [iglocska]
- Fixed proposal add not setting valid types for each category
  automatically. [iglocska]
- Rework of the restresponse URL generator. [iglocska]

  - correctly handle multi-word controllers
- Fixed some UI wonkyness. [iglocska]
- Don't render logo images if they don't exist. [iglocska]
- FetchAttributes() now correctly adheres to object distributions.
  [iglocska]
- Removed the https url rule for now. [iglocska]
- Broken Suricata rules due to removed https branch. [iglocska]

  - possible fix, mimicing contents of https://[ip]
- Correctly show advanced sightings for object attributes. [iglocska]
- Sanitise the list of fields fetched for the admin user index.
  [iglocska]

  - as reported by @deralexxx
- We are in 2018. [Alexandre Dulaunoy]
- Taxonomies updated to the latest version. [Alexandre Dulaunoy]
- MISP objects updated to the latest version. [Alexandre Dulaunoy]
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Fixed xml stix files loading. [chrisr3d]

  (our stix files at least)
- Fixed object_relation for some specific types. [chrisr3d]
- Supporting objects import. [chrisr3d]

  More object types will be added progressively
- Fixed event delete controller choice. [iglocska]

  - was using the current action's controller instead of locking in the events controller
- Stix 1.X import is now supporting more types. [chrisr3d]

  Still need to:
  - test some specific types
  - include 'object_relation' field to properly support
    objects import
- Quickfilter should include attribute level tags too. [iglocska]
- Fixed misaligned feed hits on the attribute list in the event view.
  [iglocska]
- Pagination on event attributes didn't load the feed correlations.
  [iglocska]
- Fixed image element sizes. [iglocska]
- Updated to the latest version of MISP objects including annotation and
  vulnerability objects: [Alexandre Dulaunoy]

  https://www.misp-project.org/objects.html#_annotation
  https://www.misp-project.org/objects.html#_vulnerability
- Opcache_reset() doesn't always exist on our favourite distro - only
  execute it if the function exists, fixes #2792. [iglocska]
- Fix to the previous issue with emptying the object_relation in
  attributes on fetch. [iglocska]
- Cleaner handling of failed connections during
  checkVersionCompatibility, fixes #2786. [iglocska]

  - log the real reason why the connection test failed in case of an exception (such as invalid certificate)
- Fixed null entry for object_relation, fixes #2773. [iglocska]
- Fixed output of batch import errors not correctly showing the failed
  attribute positions, fixes #2779. [iglocska]
- Changes following the recent PyMisp updates. [chrisr3d]
- Recursively follow redirects for feeds, fixes #2774. [iglocska]
- Fixed default to_ids setting for proposal edits (should reuse old
  setting) [iglocska]
- Fixed additional : in type field. [iglocska]
- Missing / in closing a tag. [iglocska]
- Update to the latest version of the objects template. [Alexandre
  Dulaunoy]
- Add a clarification if you have multiple MISP instances to not forget
  to change the default Redis port of CakeResque to avoid conflicts
  between different CakeResque. [Alexandre Dulaunoy]
- Misp-modules optional installation added. [Alexandre Dulaunoy]
- Sighting anonymisiation should properly remove the org names from the
  advanced sighting view. [iglocska]

  - as reported by @hel10world
- Updated to the latest version of the taxonomies. [Alexandre Dulaunoy]
- Travis link fixed. [Alexandre Dulaunoy]
- Warning-lists updated to the latest version. [Alexandre Dulaunoy]
- Naive fix for an issue with tab separated feeds being broken by the
  switch to str_getcsv. [iglocska]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]

Other
-----
- Merge pull request #2422 from panzertime/add-button-fetch-all-feeds.
  [Andras Iklody]

  Added a button to fetch all enabled feeds
- Added a "fetch all" button to the feeds page. [RT Hatfield]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- 1st version of TTPs parsing function. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch 'feature/sg_api' into 2.4. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Starting to parse external xml stix files. [chrisr3d]

  Will test and adapt with data from different sources
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2789 from MISP/pymisp_test2. [Raphaël Vinot]

  chg: Bump PyMISP
- :construction: Some updates on pattern import. [chrisr3d]

  Will work on pattern parser soon
- Merge pull request #2785 from atluxity/patch-1. [Alexandre Dulaunoy]

  Update INSTALL.rhel7.txt
- Update INSTALL.rhel7.txt. [Hans-Petter Fjeld]
- Merge pull request #2787 from dewiestr/2.4. [Andras Iklody]

  Update NidsSuricataExport.php
- Update NidsSuricataExport.php. [dewiestr]

  Removed the ':' from the suricata msg as it removes the message after it in squert.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2782 from SteveClement/i18n_prep. [Andras Iklody]

  i18n prep - small commits…
- - Attributes -> Search Template, __('')-ized. [Steve Clement]
- - test entry. [Steve Clement]
- Add: new default feeds added. [Alexandre Dulaunoy]

  - abuse.ch SSL IPBL
      - abuse.ch Dyre SSL IPBL
      - cybercrime-tracker.net hashlist
      - cybercrime-tracker.net gatelist
      - hpHosts - GRM only
      - blocklist.greensnow.co
      - conficker all domains generated
- Merge pull request #2771 from SteveClement/2.4. [Alexandre Dulaunoy]

  Updated FreeBSD install documentation
- - Updated FreeBSD install to: [Steve Clement]

  -- Do the entire install with binaries (no /usr/ports required)
  -- Fixed some Ubuntu remenants
  -- Fixed config typos
  -- Added all missing dependencies

v2.4.85 (2017-12-22)
--------------------

New
---
- Limit the max amount of time spent fetching the latest commit ID to 3
  seconds max. [iglocska]

  - should help avoid the unresponsive diagnostic page issue
- Update config.php template with the option whether to chase LDAP
  referrals. [Tomi Juntunen]
- Add a way to filter out attributes from being added by enforcing the
  warninglists via /attributes/add. [iglocska]

  - either pass the url param /enforceWarninglist:1 or set the "enforceWarninglist":1 key on individual attributes to be checked
- Allow configuring whether to chase LDAP referrals in
  ApacheAuthenticate module. [Tomi Juntunen]
- Add console command to reset user's authkey. [iglocska]

  /var/www/MISP/app/Console/cake Authkey [email@of.user]

  - sets a new random authkey and returns it in the output
- Add tag restrictions for a single user. [iglocska]

Changes
-------
- PyMISP bump. [iglocska]
- Version bumps for everyone! [iglocska]
- Support the changes about registry-key for import as well. [chrisr3d]
- Update following the last changes on registry-key objects. [chrisr3d]
- Show connector tag on the cluster view. [iglocska]
- Check if the stix2 file is from MISP export. [chrisr3d]
- Display names are now fully exported as custom objects. [chrisr3d]
- MISP objects updated to include registrant-org. [Alexandre Dulaunoy]
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- Changed output file name to .stix2. [Andras Iklody]
- Added sane default org_id to users/add API. [iglocska]

  - takes current user's org_id as the default
- Some cleanup of the event index. [iglocska]

  - removed threat level and analysis from the index as they're eclipsed by the taxonomies for most use-cases
  - Changed the behaviour when users click on org logoes (redirect to filtered index)
- Added category field information into labels. [chrisr3d]

  So we have categories while importing stix2 into MISP
- Bump PyMISP. [Raphaël Vinot]
- Add MISP (obj, attr, or galaxy) type in label. [chrisr3d]

  This change avoid losing information about some MISP types
  during the export.
  For instance:
  - hostname and domain --> domain-name in Stix2
  - url and uri --> url in Stix2
- Now able to distinguish src addr and dst addr. [chrisr3d]

  This change includes ip and email addresses
  Also changed a bit Custom Objects

Fix
---
- Fixed z-index of correlation popovers. [iglocska]
- Fixed stupidly slow cluster selection list. [iglocska]

  - thanks to sort being inside the loop. If you do something expensive, make sure you do it as often as possible!
- Latest version of misp warning-lists. [Alexandre Dulaunoy]
- Collapse attribute correlations. [iglocska]
- Feed quick sync added. [iglocska]
- Warning-lists updated to the latest version. [Alexandre Dulaunoy]
- Some fixes to the hostname parsing for warninglists. [iglocska]
- Warninglists updated. [iglocska]
- Warning-lists updated to the latest version. [Alexandre Dulaunoy]
- Fixed various warninglist performance issues for updating. [iglocska]
- Warninglist bump. [iglocska]
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- I ate too much chocolate ;-) [Alexandre Dulaunoy]
- Tie warninglist delete into the ACL. [iglocska]
- Fixed various warninglist issues. [iglocska]

  - no more mysql packet size issues on ingestion
  - much hfaster ingestion of warninglists
  - delete warninglists from the UI
- MISP galaxy updated. [Alexandre Dulaunoy]
- MISP objects updated to the latest version. [Alexandre Dulaunoy]
- Fixed missing flatten for advanced sightings view. [iglocska]

  - attributes within objects couldn't generate the advanced sightings view
- Fixed an issue where adding an attribute to an existing object isn't
  handled correctly via the API / sync, fixes #2760. [iglocska]
- Cleanup of setting the local server url in sharing groups over and
  over in the same request. [iglocska]
- Removed copy pasta fail. [iglocska]
- Correctly attach sharing groups to objects / attributes within
  objects. [iglocska]
- Fixed an abusive use of Identity SDO. [chrisr3d]

  - When the attribute category is not 'Person', it
  is not always justified to use Identity
- Inverted check on filterwarninglistAttributes causing the warninglist
  not to be adhered to correctly. [iglocska]
- Match the rate of the pulisher in the subscriber as default.
  [iglocska]
- Remove trailing slash from MISP.baseurl. [Jan Skalny]
- Fixed a tag lookup scope error in attributes/restSearch. [iglocska]

  - searching for an attribute tag returned all attributes contained within the event holding the located attributes

  - for example: Event with 3 attributes, one having the tag "test"
    - query /attributes/restSearch with "tags":["test"] returned 3 attributes instead of 1
- Capture tags on an object-attribute level as expected, fixes #2752.
  [iglocska]

  - The tag capturing ignored object attributes prior to this patch

  - emergency patch before the wrath of @ilmoka reaches us
- Add install of stix2 packages to support STIX 2.0 export. [Alexandre
  Dulaunoy]
- Add install of stix2 packages to support STIX 2.0 export. [Alexandre
  Dulaunoy]
- STIX2 export is no more experimental and can be safely used.
  [Alexandre Dulaunoy]
- For the events with no tag. [Christian Studer]
- Misp-object updated to the latest version. [Alexandre Dulaunoy]
- Fixed issue for events with no attributes. [chrisr3d]
- Dictionary key in registry key object. [chrisr3d]
- Issue about ip|port observable objects. [chrisr3d]
- Avoid using the original dictionary for types. [chrisr3d]

  - Deepcopy makes we use each time a fresh copy and
  modify only this copy instead of the original dict
- Object attributes calls. [chrisr3d]

  Matching with the last PyMISP release
- Error with SDO's IDs (from Galaxy) [chrisr3d]
- Fixed an issue where url parameters for restsearch didn't block
  attributes. [iglocska]

  - url parameters are bad
  - shame
  - SHAME
- For tag filters, ignore capitalisation. [iglocska]
- X-mailer variable that was wrong. [chrisr3d]
- Some keys of hashes. [chrisr3d]

  For instance shaXXX type is automatically changed in
  SHA-XXX by stix2 and needs to be identified with its
  new format
- Fixed an issue with opcache not being used yet opcache_reset() being
  called, fixes #2727. [iglocska]
- Fixed a condition where adding objects through /events/edit would
  fail. [iglocska]
- Fixed an issue with the log model being referenced incorrectly in
  MispObject. [iglocska]
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- 'port' key of 'ip-src|port' attribute. [chrisr3d]

  Was set to 'dst_port' but is actually 'src_port'
- Added user restrictions for tags to the tag index. [iglocska]
- Fixed the invalid default TLDs if no warninglist is loaded. [iglocska]
- Fixed the disable correlation flags for the objec templates.
  [iglocska]

  - also added a force update for individual templates
- Follow up to the previous patch on disable_correlations in object
  templates. [iglocska]
- Fixed typo in field name for the object templates. [iglocska]

  - disable_correlation(s) - s was a mistake and it caused the feature in the templates not to work
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- :construction: parsing external Stix2 documents. [chrisr3d]

  - atm: read patterns and create a stix2-pattern
  Object with the pattern as attribute
  - will try to parser pattern & observable objects
  for the next updates
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Warninglists updated. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Add: stix2-pattern type added to support the STIX 2 patterning format.
  [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2644 from jonas-koeritz/2.4. [Andras Iklody]

  Added an option to customize the page title
- Removed ?? operator to support PHP < 7.0. [Jonas Köritz]
- Added an option to customize the page title. [Jonas Köritz]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2754 from cvandeplas/2.4. [Andras Iklody]

  fixes bug where Server model might not yet be loaded
- Fixes bug where Server model might not yet be loaded. [Christophe
  Vandeplas]
- Merge pull request #2753 from anerani/feature/ldap-referral-in-config-
  template. [Andras Iklody]

  new: Update config.php with the option of chasing LDAP referrals
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Fix; Fixed the rate of the zmq publishing. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2750 from anerani/allow-ldap-referrals. [Andras
  Iklody]

  new: Allow configuring whether to chase LDAP referrals
- Merge pull request #2684 from JanSkalny/fix_baseurl_trailing_slash.
  [Andras Iklody]

  fix: remove trailing slash from MISP.baseurl
- Merge pull request #2719 from cvandeplas/2.4. [Andras Iklody]

  basic support for misp-modules via API
- Basic support for misp-modules via API. [Christophe Vandeplas]

  - mini cleanup of FileAccessTool that's not needed
  - basic support for misp-modules via API (malware-samples not supported yet)
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #2751 from jezkerwin/rhel_install_documentation.
  [Andras Iklody]

  Creation of install documentation for Red Hat Enterprise Linux (RHEL) 7.x
- Fixed centos7.txt file that was accidently modified. [Jeremy Kerwin]
- Changed RHEL version in title from 7.4 > 7.x. [Jeremy Kerwin]
- Note about issue surround lief compliation. [Jeremy Kerwin]
- Added disclaimer about additional issues after completion of install.
  [Jeremy Kerwin]
- Added install instruction for lief and known issues section. [Jeremy
  Kerwin]
- Up to the log rotation section. [Jeremy Kerwin]
- Completed the dependencies section. [Jeremy Kerwin]
- Renamed the file to be more generic to RHEL 7. [Jeremy Kerwin]
- More changes. [Jeremy Kerwin]
- Changes around the format a little bit. [Jeremy Kerwin]
- Spelling mistake. [Jeremy Kerwin]
- More updates to the install. Added overview and assumptions. [Jeremy
  Kerwin]
- Changes the inital commit to more of a Table of Contents format.
  [Jeremy Kerwin]
- Initial Commit. [Jeremy Kerwin]
- Add: parsing malware-sample from our stix2 files. [chrisr3d]

  (Following the latest update on the export module)
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: label to recognize malware samples. [chrisr3d]

  For SDOs generated from Objects
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Add: whois-registrant-org attribute type added. [Alexandre Dulaunoy]

  As requested in https://github.com/MISP/misp-objects/issues/55
- Add: the last object types that missed before. [chrisr3d]

  - The documents generated by our Stix2 export should
  be imported without any problem (otherwise I'll fix it)
  - Random Stix2 documents may have problems to be imported
  at the moment (depending on the possible observable objects
  jungle in observed-data SDOs) - indicators should be ok
- Removed 1 useless test on observable. [chrisr3d]
- Removed a testing print. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- :construction: Includes category import. [chrisr3d]

  Still need to include the missing types of object
  not supported yet.
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #2739 from zachsis/patch-1. [Alexandre Dulaunoy]

  Update xINSTALL.centos7.txt
- Update xINSTALL.centos7.txt. [zachsis]

  added  `rh-php56-php-opcache` as part of the `yum install` for CentOS7
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Add: new types added for X509 certificate fingerprint: [Alexandre
  Dulaunoy]

  - x509-fingerprint-md5
  - x509-fingerprint-sha256

  This is required to ensure consistent export while hashes are used.  The
  associated x509 object template has been fixed to reflect the 3 fingerprint types
  instead of the generic hash types. This would allow different export types.

  https://github.com/MISP/misp-objects/commit/b85438fc45b212a21b72d6d2e0df619758fa1444
- Simplified generation of SDOs from Galaxy. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- :construction: fixed bugs that appeared with Objects support. [chrisr3d]
- Add: new feed VXvault - URL List added. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Parsing SDOs from 'email' Object. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #2731 from SteveClement/2.4. [Andras Iklody]

  - Initial FreeBSD install document
- - Initial FreeBSD install document. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- :construction: Parsing patterns for Objects. [chrisr3d]

  Also little fixes & updates
- Added label with the type for Identity object. [chrisr3d]

  As well as it is done for all the other types
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- :construction: Import module from STIX2. [chrisr3d]

  Functional but improvements still needed.
  Not all the fields of Stix2 events supported
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2716 from cvandeplas/2.4. [Andras Iklody]

  fixes issue #2698 - malware-sample fails with import modules
- Fixes issue #2698 - malware-sample fails with import modules.
  [Christophe Vandeplas]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Added custom object for MISP Objects. [chrisr3d]

v2.4.84 (2017-12-06)
--------------------

Fix
---
- Fixed a critical issue introduced in 2.4.83 blocking the
  synchronisation of edits in certain situations. [iglocska]

  - events being edited didn't set the locked = 1 flag on push

  - as reported by SIEMENS

Other
-----
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Added label to recognize malware-sample attributes. [chrisr3d]

v2.4.83 (2017-12-06)
--------------------

New
---
- Various improvements to the CSV export. [iglocska]

  - The @FloatingCode and @ilmoka care package
  - Improved CSV performance for instances with large number of events
  - Added "value" filter for CSV (use-case: I want all indicators for this value with context)
  - Added attribute tags to the output of the CSV export
- Add restrictions for e-mail addresses to certain domains. [iglocska]
- Add attribute tag filters to the fetchEvents() functionality.
  [iglocska]

  - tag filters now filter on:
    - all events cotaining matching tags on event + attribute level (positive lookup)
    - all events not containing matching tags (negative lookup)
    - filter attributes within a matched event for blocked attributes (negative lookup)

  - moved tag filtering to subquery filtering - should improve performance massively on larger instances when filtering on tags

  - first round of implementations, more on the way
- Various improvements. [iglocska]

  - use the feed uuid caches to link directly to affected MISP events
  - various UI improvements
  - Feed preview pagination / POSTed event ID filters added
- Add the possibility to limit fields for the CSV export via POST
  requests. [iglocska]
- Added mac-address and mac-eui-64 attribute types. [iglocska]
- Added full audit logging to ZMQ and Syslog, fixes #2635. [iglocska]

  - syslog now includes all audit log entries and it's separated into proper severity levels
  - ZMQ logging and syslog logging are both optional features
- Added phone number recognition to the freetext import tool. [iglocska]

  - also, changed the massaging of phone number type attributes to replace 00 with +
- Include user action in zmq. [iglocska]
- Added logging to galaxy attach/detach tasks. [iglocska]
- Push the action for user updates/creations/logins along with the user
  object to the ZMQ channel. [iglocska]

Changes
-------
- Version strings updated. [iglocska]
- Bump PyMISP, again. [Raphaël Vinot]
- Bump PyMISP. [Raphaël Vinot]
- Wip. [chrisr3d]
- Make misp to stix export work with MISP json formatted. [chrisr3d]
- Push MISP json formatted events to the stix exporter (pending rework)
  instead of the direct output of fetchEvents() [iglocska]
- Push the full user object to the ZMQ feed. [iglocska]

Fix
---
- Updated pyMISP recommended version. [iglocska]
- PyMISP updated. [iglocska]
- Removed the requirement for a comment from the import modules.
  [iglocska]

  - if the comment field is set don't override it
- Fixed PyMISP version. [iglocska]
- Removed unused variable. [iglocska]
- Latest version of the MISP galaxy. [Alexandre Dulaunoy]
- Latest version of MISP objects. [Alexandre Dulaunoy]
- Documentation to enable cortex services. [Raphaël Vinot]
- Don't cull the list of possible models based on existing data for the
  search logs view. [iglocska]

  - slow and useless
- Fixed a bug with the resolved attributes list for freetext import /
  module imports. [iglocska]
- Fixed CSV content type. [iglocska]
- Changed name of export popup. [iglocska]
- Moved attribute_tags in the CSV export to the includeContext flag
  instead of the toggle-able attributes. [iglocska]
- Fixed some issues with the related feeds. [iglocska]
- Fix epic snafu in Event->_add() thanks to last minute save by the
  Travis tests. [iglocska]
- Some minor fixes to the attribute filtering. [iglocska]
- Fixed an issue where sharing groups were not properly attached to
  events for sync users, potentially fixes #2653. [iglocska]
- Added new field to MYSQL.sql. [iglocska]
- Added db changes needed for the user domain restrictions along with
  restricting the user self edit action. [iglocska]
- Fixed an issue where proposal quick edits didn't work for normal
  users, fixes #2685. [iglocska]
- Fixed update warninglists button being available to non site admin
  users. [iglocska]

  - functionality was blocked by ACL, but button shouldn't be shown in the first place
- Block the addition of same type/category/value attributes in one shot
  to the same event. [iglocska]

  - via the /events/add api
- Enforce server push rules on a sync user when viewing the events.
  [iglocska]

  - user not seeing the data is a side-effect, not the intended effect
  - serves to enforce the synchronisation rules
  - sync user can still view the hidden attributes via attribute searches etc. Whether we want to remove this in the future is still to be decided, but for now the sync enforcement is the only intended effect.
- Mac-eui-64 not accepted by stix validator. [chrisr3d]

  By the way, it is accepted by the validator at creation..
  .
- Latest version of the MISP objects template imported. [Alexandre
  Dulaunoy]
- MISP objects updated to the latest version. [Alexandre Dulaunoy]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Dns-soa-email didn't have a category. [iglocska]
- Fixed missing entries for mac-eui-64. [iglocska]
- Made CSV parser for freetext import tool / feed ingestion compatible
  with escaped CSVs. [iglocska]

  - "" now handled correctly
- Vulnerability (CVE) should correlate (CIRCL and NCSC-NL are supporting
  it) fix #2691. [Alexandre Dulaunoy]
- Ambiguity removed from some sharing group related queries. [iglocska]
- Graceful handling of no response during getVersion pre-sync test.
  [iglocska]
- Fix an issue with a double quoted integer in the correlation update
  script during publishing, fixes #2540. [iglocska]
- Trimp the org uuid upon entering it to avoid copy-pasta issues.
  [iglocska]
- Updated the duplicate attribute removal tool to actually remove
  instead of trying to deduplicate. [iglocska]
- Fixes notices of no SharingGroupOrg being set due to a bug in the
  sharing group cacher for normal users. [iglocska]
- Fixes to various issues with adding proposals via the freetext import
  tool. [iglocska]

  - no feedback on whether the resulting dataset will be stored as attributes/proposals
  - unpublishing of the event when proposals get entered
  - alerting the event creator of new proposals if coming from the freetext import tool
- Quotes issue fixed. [chrisr3d]
- MISP objects updated. [Alexandre Dulaunoy]
- Leaking of hashed passwords in the audit logs fixed. [iglocska]

  - Scope was limited due to the audit log access restrictions to site/org admins
- Expose /users/view/me to the API, fixes #2679. [iglocska]
- Don't verify peer name on self signed certs; don't verify self signed
  peer if cert is missing. [Milan Pikula]
- Settings editor not working on touch devices. [Milan Pikula]
- Refresh rows in settings editor. [Jan Skalny]
- Relaxed email validation. [iglocska]

  - because unicode tlds / domains are such a great idea
- Disabled pretty argument. [chrisr3d]

  used while stringifying the final Bundle
- Fixed invalid timestamp generation. [iglocska]
- If no distribution level set, don't try to check if it's set to
  sharing group on the attribute level. [iglocska]

  - Attribute->editAttribute()
- MISP object updated to the latest version to fix the unusable ASN
  template. [Alexandre Dulaunoy]
- Attribute deletes are again synced correctly. [iglocska]
- Fixes an issue where assigning sharing groups based on existing IDs
  didn't work for event creation via the API. [iglocska]

  - expected full sharing groups as provided by the sync, references didn't work
- Fixed the broken feed preview. [iglocska]
- Fixed the new path for the stix files. [iglocska]
- Moved the conversion to JSON after the massage of the data for stix.
  [iglocska]
- Add galaxy to valid log action list. [iglocska]
- Shebang mixup. [Steffen Sauler]

  /!bin/sh to !/bin/sh
- 984732984th time is the charm... [iglocska]
- Reduced the user data to just a partial user object and organisation
  object for the zmq push. [iglocska]
- Fixed the pubsub user push if the user object is not contained within
  a User key. [iglocska]
- Previous commit didn't trigger in all cases. [iglocska]
- MISP objects updated to the latest version. [Alexandre Dulaunoy]
- Fixed slow /tags/index calls using the API. [iglocska]

  - burned the stupid out of the API
- Fixed the downloadSamples API. [iglocska]
- Fixed silly lookup with injected event IDs on the export page for
  normal users. [iglocska]

  - broke instances with a few hundred k events
- Fixed a reflected XSS in the sharing group creator tool. [iglocska]

  - Fixed a reflected XSS in the sharing group editor that requires malicious organisation names

  - Low impact due to the following requirements:
    - organisation names with malicious org names (JS in the orgname)
    - sharing group editor user has to manually add an organisation to the list that has javascript in the org name
    - only vulnerable view is the editor itself, so the impact is limited to
      users that manually add organisations with malicious names to the list themselves / edit such sharing groups

  - As reported by Dawid Czarnecki

Other
-----
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2706 from Rafiot/cortex_doc. [Raphaël Vinot]

  fix: documentation to enable cortex services
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch 'feature/tag_filter_rework' into 2.4. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into
  feature/tag_filter_rework. [iglocska]
- Merge branch '2.4' into feature/tag_filter_rework. [iglocska]
- Little change about SDOs generated from Galaxy. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Add: a new set of logos for the MISP project. [Alexandre Dulaunoy]

  There are 3 type of logos in the set:

  - core software
  - community
  - standard

  The objective is not to replace the existing the logo but
  to provide a clear logo when this is referencing a specific
  sub-part of the MISP project.
- Fixed vulnerability type. [chrisr3d]

  Was generated as custom object because of a change
  in the attributes reading function
- Fixed assignment issues for attributes from Object. [chrisr3d]

  Multiple use of the same part of the dictionary caused
  assignment errors. Using the 'copy()' method avoid that error.
- Added mac-eui-64 type. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #2701 from RichieB2B/ncsc-nl/stixfix. [Andras
  Iklody]

  Fix STIX export format
- Use threat level name instead of id in STIX. [Richard van den Berg]
- Use new MISP JSON format (no more AttributeTags) [Richard van den
  Berg]
- Merge pull request #2700 from Rafiot/testdescribe2. [Raphaël Vinot]

  chg: bump PyMISP, again
- Add: MISP distributed overview in SVG format. [Alexandre Dulaunoy]
- Merge pull request #2697 from Rafiot/testdescribe. [Raphaël Vinot]

  chg: bump PyMISP
- Little fix with 'info' field in Events. [chrisr3d]
- Added a label to separate SDOs from Objects. [chrisr3d]

  This distinction will probably be helpful for the
  Stix2 import module to separate Attributes from
  Objects
- Fixed issues with dictionary keys and some objects. [chrisr3d]
- Added Org & Orgc information for the import. [chrisr3d]

  Also clarified a little part of the code
- Added xml files parsing. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Added mac-address type. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Fixed issues about observable objects and patterns. [chrisr3d]
- Parsing attachment attributes. [chrisr3d]

  Also fixed some specific issues with single quotes
- :construction: Import of some of the most common attributes. [chrisr3d]

  Work still in progress in order to:
  - Support as many attribute types as possible
  - Fix simple quotes (that are not json parsable)
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #2672 from CenturyLinkCIRT/freetext-target-email.
  [Andras Iklody]

  added target-email to FreeText Import types
- Added target-email to FreeText Import types. [Thomas Gardner]
- Misp-object templates updated to latest version. [Alexandre Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into stix2experiments.
  [chrisr3d]
- Merge pull request #2671 from milankowww/return-to-orig-url. [Andras
  Iklody]

  change behavior of login page to return to original page after authen…
- Change behavior of login page to return to original page after
  authentication. [Milan Pikula]
- Merge pull request #2670 from milankowww/self-signed-certificate-
  verification. [Andras Iklody]

  fix: self signed cert verification
- Merge pull request #2669 from milankowww/support-touch-screens.
  [Andras Iklody]

  fix: settings editor not working on touch devices
- MISP objects updated to the latest version. [Alexandre Dulaunoy]
- Merge pull request #2668 from JanSkalny/fix_settings_editor. [Andras
  Iklody]

  fix: refresh rows in settings editor
- Merge branch '2.4' of github.com:MISP/MISP into stix2experiments.
  [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- New relationships added. [Alexandre Dulaunoy]
- Starting to parse info for a stix import. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [iglocska]
- Merge pull request #2651 from ppanero/sso_org_fix. [Andras Iklody]

  Added possibility to use always default org for new users
- Added possibility to use always default org for new users. [Pablo
  Panero]
- Merge branch 'feature/stixunclutter' into 2.4. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2295 from norpol/patch-1. [Andras Iklody]

  Fix gpgv2+ key generation
- Fix gpgv2+ key generation. [Phi|eas |ebada]

  This resolves failing of gpgv2 key generation with the following error message:
  ```
  gpg: agent_genkey failed: Permission denied
  Key generation failed: Permission denied
  ```

  # Explanation
  gpgv2's `pinentry-curses` requires access to a current `tty`. If you `su` or `sudo` between users, your tty's permission will stay the same as the initial login user (see illustrating below). You could, in general, work around issues like this by:
   - `old_perms=$(stat -c "%U:%G" $(tty)); chown "www-data:tty" "$(tty)" && { sudo -u www-data gpg --gen-key; chown "${old_perms}" "$(tty)"; }` (uncertain security implications and won't probably work)
   - starting screen/tmux within the newuser and then running `gpg --gen-key`
   - starting a script session

  But first point can't really be recommended, latter two will fail because www-data login shell is `/usr/sbin/nologin`.

  Just for illustrating the problem better for you:
  ```
  ssh alice@somehost:
  stat -c "%U:%G $(tty)" $(tty)
  alice:tty /dev/pts/1
  su - root
  stat -c "%U:%G $(tty)" $(tty)
  alice:tty /dev/pts/1
  `
- Merge pull request #2640 from SHSauler/patch-4. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Added reg-key objects parsing for observed data. [chrisr3d]

  Still not tested as registry-key objects seem to have an issue in MISP
- Support email objects parsing into observed data. [chrisr3d]

  Currently skipping display names in observed data email-addr objects
- Merge pull request #2639 from truckydev/patch-4. [Alexandre Dulaunoy]

  update args.sleep on typeError
- Force int for --sleep. [truckydev]

  ^^
- Update args.sleep on typeError. [truckydev]

  Convert string to int for time.sleep when sub.py use with -t
- Merge pull request #2633 from dawid-czarnecki/patch-1. [Andras Iklody]

  Download terms redirect fix
- Download terms redirect fix. [dawid-czarnecki]

  When server setting MISP.terms_download=true and MISP.terms_file exists under MISP/app/files/terms directory user wasn't able to download terms and conditions before accepting it.
- Merge pull request #2632 from PaoloVecchi/2.4. [Alexandre Dulaunoy]

  Create INSTALL.ubuntu1604.with.webmin.txt
- Create INSTALL.ubuntu1604.with.webmin.txt. [Paolo Vecchi]

  Some, maybe a friend, can't be asked to configure and manage all the services on an Ubuntu 16.04 so Webmin could be useful.
  Tested with:
  MISP 2.4.82
  Webmin 1.860
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #2630 from treyka/2.4. [Andras Iklody]

  add cti-python-stix2 to .gitmodules
- Add cti-python-stix2. [Trey Darley]
- Merge pull request #2629 from treyka/2.4. [Andras Iklody]

  typo fixen
- Typo fixen. [Trey Darley]
- Merge pull request #2628 from Delta-Sierra/2.4. [Andras Iklody]

  display "Fetch this event" button function in Servers and Feeds preview index
- Uppercase to be consistent. [Deborah Servili]
- Display "Fetch this event" button function in Servers and Feeds
  preview index. [Deborah Servili]
- Some other object types supported in Observed Data. [chrisr3d]

  Object types still not supported (not in 'objectsMapping'
  dictionary, from misp2stix2_dictionaries module) are set
  to a basic value until the next update, so they do not
  generate errors in Stix2 functions
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- 2017 even if it's not 2049 ;-) [Alexandre Dulaunoy]
- Quick fixes. [chrisr3d]

v2.4.82 (2017-11-10)
--------------------

New
---
- Various features. [iglocska]

  - Added quickhashing to the feed generator
  - Objects added to feed preview for MISP feeds
  - Attribute tags added to MISP feeds
- Sightings ingested on import/sync. [iglocska]
- Added object references to ZMQ. [iglocska]
- First version of the zmq reimplementation. [iglocska]
- Rework of the feed correlation lookups for the event view. [iglocska]

  - massive performance boost by using redis pipelining
  - for events with 10k+ attributes, show truncated feed correlation lookups, informing the user about the number of correlating attributes and a boolean flag on attributes saying that they correlate
  - The overall feed correlation counter also allows users to pivot to a view that loads all correlations, though it should be used with some caution as it can be somewhat heavy

Changes
-------
- PyMISP version bump. [iglocska]
- Pass event_id to import modules, fixes #2612. [Andras Iklody]

  As described by @Vince147
- Version bump. [iglocska]
- Added some sane default headers to the apache .conf files. [iglocska]

  - protection against clickjacking
  - nosniff

  - as reported by Or Hanuka (PALANTIR)

Fix
---
- 3rd time is the charm (PyMISP updated) [iglocska]
- PyMISP version. [iglocska]
- Warning list updated to the latest version. [Alexandre Dulaunoy]
- Taxonomy updated to the latest version. [Alexandre Dulaunoy]
- MISP object updated to the latest version. [Alexandre Dulaunoy]
- Latest version of the galaxy added. [Alexandre Dulaunoy]
- Added sharing group data to the new ACL functions. [iglocska]
- Rework of tags index / galaxy view. [iglocska]

  - performance tweaks
  - no more silly queries
  - added sharing group aware ACL to the event/attribute counters
- Added context  to the sightings zmq feed. [iglocska]
- Fixed the tags/index performance snafu. [iglocska]
- Ugly fix for the float issues. [iglocska]
- Potential reflected XSS on older browsers in the histogram. [iglocska]

  - As reported by Dawid Czarnecki
- Histogram rework. [iglocska]

  - removed junk debug
  - fixed group by issue
  - better performance
- Enable auto select for new object rows when adding additional ones via
  the multiple expand. [iglocska]
- Minor tuning of suricata rules. [iglocska]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- MISP objects updated to the latest version. [Alexandre Dulaunoy]
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Changed relationship name of filesize in add attachments to size-in-
  byte. [iglocska]
- Fixed default distribution for upload_sample(), fixes #2608.
  [iglocska]
- Invalid redirect when viewing /roles/index as a normal user, fixes
  #2606. [iglocska]
- Potential fix to sync issues with sharing groups and pushes, fixes
  #2601. [iglocska]
- Convert - to _ in csv headers. [iglocska]

  - to match the previous output
- Add the object fields by default to the CSV export. [iglocska]
- Fixed tag names in the CSV export. [iglocska]
- Fixed escaping of CSV. [iglocska]
- Fixed the CSV field name for date. [iglocska]
- Fixed an issue with the CVE export if no field parameters were passed.
  [iglocska]
- Fixed an issue preventing attributes in objects from being edited.
  [iglocska]
- Further fixes to the new zmq system. [iglocska]
- Fixed a bug where sightings couldn't be added to objects. [iglocska]
- Updated sub.py. [iglocska]
- Org field not being hot potatoed to resolvAttributes()  in the stix
  export. [iglocska]
- Added missing parameter org to resolvAttributes() call in the stix
  exporter. [iglocska]
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Fixed empty emails. [iglocska]
- Added initialisation of Log model in the editAttribute() function if
  the save fails. [iglocska]
- Change 2/2 for fixing the feed scheduler fixes #2503. [Andras Iklody]

  As described by @lucamemini
- Change 1/2 for fixing the feed scheduler fixes #2503. [Andras Iklody]

  As described by @lucamemini
- Allow proposing changes to object attributes. [iglocska]
- Attribute type list when editing should be the category's one if
  already selected. [ppanero]
- Added default category for gender. [iglocska]
- Added missing IP field to logs. [iglocska]
- Misp-objects updated to the latest version. [Alexandre Dulaunoy]
- Added comment field to objects, fixes #2560. [iglocska]
- Added email-message-id's default category. [iglocska]
- Fixed an issue that caused an event edit to fail due to the invalid
  refresh of the correlations. [iglocska]
- Fixed a bug with the restSearch API. [iglocska]

Other
-----
- Supporting Observed Data SDOs from event Objects. [chrisr3d]

  Objects currently supported:
  - domain-ip
  - file
  - ip|port
  Currently working on the other ones
- Merge branch '2.4' of github.com:MISP/MISP into stix2experiments.
  [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into stix2experiments.
  [chrisr3d]
- Fixed typo for custom objects' type. [chrisr3d]

  In order to keep the initial type of the attribute
- Previous version of the dictionary no longer used. [chrisr3d]

  Double quotes seem to not be validated in stix2 patterns
- Fixed an issue with patterns. [chrisr3d]

  Caused by the previous dictionary format
  (double and simple quotes management)
- Merge branch '2.4' of github.com:MISP/MISP into stix2experiments.
  [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into stix2experiments.
  [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Patterning for Indicators from Objects. [chrisr3d]
- First version with some objects parsed. [chrisr3d]

  Will continue parsing some other ones
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2603 from wotschel/2.4. [Alexandre Dulaunoy]

  Minor changes and additions to Deb 9 Inst. Guide
- Merge pull request #1 from wotschel/wotschel-INSTALL.debian9.
  [wotschel]

  Some minor changes and additions Deb 9 Inst. Guide
- Some minor changes and additions. [wotschel]
- Merge branch 'customcve' into 2.4. [iglocska]
- Merge branch '2.4' into customcve. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch 'feature/zmq_rework' into 2.4. [iglocska]
- The last useless coma. [Cédric Bonhomme]
- Harmonizes arrays initializations. [Cédric Bonhomme]
- Enables the user to select the attributes to be included in the CSV
  export (event and object attributes). [Cédric Bonhomme]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Added custom objects. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Parsing Identity SDOs for 'Person' category attributes. [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #2589 from jurg/attrtypefix. [Andras Iklody]

  bugfix for selecting type in adding / editing attribute
- Bugfix for selecting type in adding / editing attribute. [Jorgen
  Bohnsdalen]
- Using PyMISP attributes. [chrisr3d]

  wip: Waiting for some PyMISP issues to be fixed
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Raphaël Vinot]
- Merge pull request #2585 from ppanero/2.4. [Andras Iklody]

  Beautify edit object validation
- Merge branch '2.4' into 2.4. [Andras Iklody]
- Merge pull request #2588 from ppanero/bugfix. [Andras Iklody]

  bugfix for listing types when editing non object attrs
- Bugfix for listing types when editing non object attrs. [ppanero]
- Bug fix for listing types when editing non object attr. [ppanero]
- Beautify object edit validattion. [ppanero]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2587 from RichieB2B/ncsc-nl/stixorgs. [Andras
  Iklody]

  Add Reporter and Producer fields to STIX
- Add Reporter to STIX Indicent Add Producer to STIX Indicator. [Richard
  van den Berg]
- Revert "Fix: Attribute type list when editing should be the category's
  one if already selected" [iglocska]

  This reverts commit 27f30aae3bf6f30af1ecbf5dcf6d237aafa66b81.
- Merge pull request #2584 from RichieB2B/ncsc-nl/searchtag. [Andras
  Iklody]

  Speed up tag searches
- Speed up tag searches, fixes #2407. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2582 from ppanero/2.4. [Andras Iklody]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Using PyMISP MISPEvent class to parse events. [Raphaël Vinot]
- Merge pull request #2576 from 98Giraffe/fix-type-o-in-diagnostics-
  settings. [Andras Iklody]

  Fixed type-o in  Server Settings -> Diagnostics -> Advanced attachmen…
- Fixed type-o in  Server Settings -> Diagnostics -> Advanced attachment
  handler, when referencing pymisp the message stated pydeep. [Joseph
  Dane]
- Added exploit-kit as a Tool SDO. [chrisr3d]
- Removed a nonexistent 'non_indicator_attribute' [chrisr3d]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #2568 from bambenek/2.4. [Alexandre Dulaunoy]

  Take 2: Changing which bambenek consulting DGA feeds are pulled in defaults.json
- Typofix. [John Bambenek]
- Making changes to feed file to point to different bambenek consulting
  DGA feeds. [John Bambenek]
- Added Course of Action SDO. [chrisr3d]
- Added some Galaxy objects that can be easily mapped. [chrisr3d]
- Merge pull request #2565 from RichieB2B/ncsc-nl/fix-2561. [Andras
  Iklody]

  Add file objects to STIX 1 export
- Handle filename only attributes. [Richard van den Berg]
- Skip non-observable indicator, fixes #2561. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Added malware-sample case. [chrisr3d]

  Also fixed some 'pattern' fields in the dictionary
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [chrisr3d]
- Merge pull request #2563 from RichieB2B/ncsc-nl/stix-tlp. [Andras
  Iklody]

  Use MISP TLP tags to set STIX tlpMarking
- Use MISP TLP tags to set STIX tlpMarking. [Richard van den Berg]
- Added a dictionary to manage patterns and observable objects.
  [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]

v2.4.81 (2017-10-10)
--------------------

New
---
- Added first experimental STIX 2 export implementation. [iglocska]

  - kudos to @chrisr3d for digging into the deepest bowels of the scary beast that is STIX2

  - PoC, definitely needs further improvements/mapping. Let us know about issues you find!
- First round of updates to the correlation engine ready. [iglocska]

  - node deletion temporarily disabled until a bug is resolved
- Further progress on the graphing. [iglocska]

  - also, added new icon field to galaxies
- Further work on the graphing engine. [iglocska]
- First iteration of the graphing engine rework. [iglocska]
- Rework of the attachment uploader. [iglocska]

  - add attachments and upload_sample now share code
  - allow the same features via upload_sample (object creation / use of advanced add attachments)
  - new flag: advanced

  - example:

    POST to mymisp/events/upload_sample
    BODY:
  {"request":{"files": [{"filename": "bla.exe", "data": "U3RhckNyYWZ0IElJIGZvcmV2ZXI="}], "distribution": 1, "advanced":1, "info":"bla"}}

  - this commit was brought to you by CEF and

  MMH = -.  . ,-,,-,.         :H@H  =;;++$HH+XX$%+X%+$++=:=.XH@@@HMMMMMMMMH@@@@@@@HHX$   ,X@@@@@@@HHHHHHHHHHXXXXXXXXXXXXXX
  - -- ,,,  --,. -                 , ,; +$XHH@@@@HHH@@@HHHH+$+$X+HH+$$+ ;  ;=  .    %   +  ,+$X+++XXXXXXXXXXXXX++HH+++++++
  ---==,,--,-,-., :     .          -,,:/ $XHH@HMMMMMMMMMM@HHX$H@MHHHHX+H%%$%+H/:.%. $. @,,,. $$XXXXXXXXXXXXXXXXXXXXXXXXXX+
    =  - --,,   , --   ..             =/ +$+H@@HMMMMMMMMH+H+++HHHHHHHH@+++++H+X++X+$$  = ,,, - $$XXXXX$$$$X$$$$$$$$$$$$$$X
   :==-===-,. ,., ==   .           :;; +++%$+H@HMMMMMMM%$%$$$+H@@+HH@MMMMMM@@@@HHH++H. .,,-,,--=/+$$%%%%%%%%$+%%$$$$$XXXXX
  ,  =  ==- -  .  ==             . =; ++++%++HHHHHHHHHH++%$$X+@@H+HHHMMMMMMHH@@@+X+    , ,,,,-  , ,$$$$$$$+++++$$$$XXXXX$$
  == --, -- =--, ,,=          .    ./++$$++$+X$+/++$$XXXX$$$$XXXXXXH+HH+H+X$%%/     .,,,,,,    ..  ..    ,. ,,,-=+%+++ /++
  +   -- -  -,,-  .,    .  . .      = +$$++++HH+.  ,+$$+++++++$XX$X$XHHH+X$$+      ..--,-    .. .        .    ,-, = ======
  MH - ---- --,,,    .       .. ,      %++$$X++++ +%++++++++%++$$$$$+H++X$$+        --,    .         .   .        =  .====
  MM+ ,----,,,,              , .. ,.      +++X+HH+++++%++$++++$$+HHH+++$$          ,-          ,   .       .   : ;/ +%+.
  MMH ,-,-,, ,,.        .    -,     =     = +$+H@HH++++$$X$$+++HHH+++$                       ,    ..       ,  +++++++%%+%+
  M@@== ,,,  ,                               ++++XX++HHHHHH++HHH+,              ,         ,  .  ....     . +$+%%%%%%+%%%%%
  @H+,-,,.....       .                          .,.;; ++$$X+%+:-              ,  .     .,,,  .  ...   . XXX$$$%%%%%%+%%%%%
  $+     .                                ===:; ++++ ++++-,.  ,                       ,-,          .  $X+XX+XXX$$+%++%%%%%
  ++: ,. .                         ,-,,-==:; %%%%%+%$$%$$X$$$+%+:==        .        . ,,           ..+X$XXXXXX$$$+%%$$%%%%
   ,                          ,---, =:;/++$$XX$$$$$$X+H@H@HHH$%%%$X$++;===== .      .,            .. +%%+$++$%$$$$$$%%++%+
                                 ===; +++$$$$+ +%+++%+HH@@@@HH+++ ++%+$+,  ===      ..             ,=;   +++++++++..   :;;
                        .   =:;   /++%$$++,  ,++HHMMHH@@@@HHHH@HH++++++ ,+$$+ .     ..                :=;;:;;;;;==========
                    .,,-==;;;+%  %%+$$$$ /+++@@@@@@@@@@HH@M@MH@@@HHHHH$$% /%$XXX$X  .                -=====::::=========::
  H@HHHH#M#M#MHHHM#MMMMMMMHHHH@H@H++@H$+++HHM#MMMMHMMH@@HHHHHH%+++++%%%+++    ,  .
  %%%%%%%%%%%%%%++++%%++   ..   ...  ..  .                                   +++%+++++++%++++%+++++++++%+%++%+%%++%++++++%
- Change server settings via the API. [iglocska]

  Usage:

  Viewing current setting value:

  GET /servers/serverSettingsEdit/[mysetting]
- Allow POSTing search parameters to the /tags/index API. [iglocska]

  - to filter the tags index simply POST to /tags/index the following payload:

  {"filter": "malware_classification:malware-category"}
- Added object relations to the CSV export. [iglocska]

Changes
-------
- Submodules updated. [iglocska]
- Replaced the correlation graph icon to something more appropriate.
  [iglocska]
- ACL updated. [iglocska]
- If no object ID is set in the URL for adding an object reference,
  check the payload for the object_uuid. [iglocska]
- Added .onion to the TLD list for the complext type tool. [iglocska]

Fix
---
- Skipping composite objects. [chrisr3d]
- STIX 2.0 report doesn't require labels but the python-stix2 requires
  one. [Alexandre Dulaunoy]
- Mixbox and cybox not required then it's removed. [Alexandre Dulaunoy]
- PyMISP and warninglists updated. [iglocska]
- Fix a rare issue with zombie sighting data throwing a notice.
  [iglocska]
- Fix to a potential reflected XSS on the quickDelete. [iglocska]

  - low impact, XSS required user confirmation of malicious payload

  - as reported by Or Hanuka (PALANTIR)
- Small fix to a missing ajax check. [iglocska]

  - ajax forms opened full screen look bad
- Various UI fixes. [iglocska]

  - no more walk of shame after demoing MISP on a potato quality projector (beamer for our Belgian/Dutch/German friends)
- Removed debug output from adding object references. [iglocska]

  - caused the spinning loading of doom
- Indicators added in addition to observed data + misp tag for IDS.
  [chrisr3d]
- Galaxies updated. [iglocska]
- Fix notice if invalid taxonomy is viewed. [iglocska]
- Some cleanup of the attribute filtering. [iglocska]
- Potential fix to missing proposals during sync. [iglocska]

  - rather stupid adherence to push rules removed for proposal sync
- Fixed wonky object pre-save view. [iglocska]

  - showed numeric distributiion level for attributes
  - showed numeric sharing group ID for attributes
  - showed currently selected sharing group ID even if the distribution was ultimately not set to sharing groups
- Fix some restsearch filters fetching the same event more than once.
  [iglocska]
- Corrected filename for array of events. [iglocska]
- Internal reference: type with a uuid of an event converts to a
  clickable link. [iglocska]
- Sanitise all the things for XML, fixes #2522. [iglocska]

  - Sanitise all the things!

  ─────────────────────────────▄██▄
  ─────────────────────────────▀███
  ────────────────────────────────█
  ───────────────▄▄▄▄▄────────────█
  ──────────────▀▄────▀▄──────────█
  ──────────▄▀▀▀▄─█▄▄▄▄█▄▄─▄▀▀▀▄──█
  ─────────█──▄──█────────█───▄─█─█
  ─────────▀▄───▄▀────────▀▄───▄▀─█
  ──────────█▀▀▀────────────▀▀▀─█─█
  ──────────█───────────────────█─█
  ▄▀▄▄▀▄────█──▄█▀█▀█▀█▀█▀█▄────█─█
  █▒▒▒▒█────█──█████████████▄───█─█
  █▒▒▒▒█────█──██████████████▄──█─█
  █▒▒▒▒█────█───██████████████▄─█─█
  █▒▒▒▒█────█────██████████████─█─█
  █▒▒▒▒█────█───██████████████▀─█─█
  █▒▒▒▒█───██───██████████████──█─█
  ▀████▀──██▀█──█████████████▀──█▄█
  ──██───██──▀█──█▄█▄█▄█▄█▄█▀──▄█▀
  ──██──██────▀█─────────────▄▀▓█
  ──██─██──────▀█▀▄▄▄▄▄▄▄▄▄▀▀▓▓▓█
  ──████────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
  ──███─────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
  ──██──────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
  ──██─────────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
  ──██────────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
  ──██───────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
  ──██──────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
  ──██─────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
  ──██────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
- Fixed potential double hashing of samples with the encrypt flag.
  [iglocska]
- Invalid uuid used in the objectreferences add form. [iglocska]
- Fixed an invalid uuid in the object reference. [iglocska]
- Flatten events for the correlation graph. [iglocska]
- Fixed some weird editing issues. [iglocska]
- IP|Port in Gui, fixes #2505. [iglocska]
- Flatten the events for the restSearch API's lookup functions.
  [iglocska]

  - otherwise valid events that only contain objects get blocked
- Fixed an issue with pushing a sample via the API / add attachments
  when no object templates are loaded. [iglocska]
- Fixed a bug where normal users couldn't add object references.
  [iglocska]

  - as reported by @deralexxx
- Added ObjectTemplateElements to the objectTemplate view via the API.
  [iglocska]
- Only lower case search terms work in tags/index's filter. [iglocska]
- Port added to network activity. [iglocska]

Other
-----
- Replaced placeholder label with threat-report. [Andras Iklody]
- Merge branch '2.4.81' into 2.4. [iglocska]
- Merge branch '2.4.81' of github.com:MISP/MISP into 2.4.81. [chrisr3d]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Added Tags as labels and links as external_references (both properties
  of Reports) [chrisr3d]

  Will also add custom objects later, and handle the precision issues
  for 'created' and 'modified' properties of all the STIX Objects
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Add: First :construction: STIX 2.0 export from MISP JSON standard format.
  [chrisr3d]

  This is an early stage export from MISP JSON into the STIX 2.0
  (still unpublished). Some attributes type are missing, galaxy and
  objects needs to be exported into custom object due to the current
  limited state of STIX 2.0. Tags will be added later as labels and link
  as external_references (open points with OASIS CTI ongoing discussions).
- Merge pull request #2539 from RichieB2B/ncsc-nl/certauth. [Andras
  Iklody]

  Allow creating users with CertAuth via userDefaults
- Allow creating users with CertAuth via userDefaults, fixes #2538.
  [Richard van den Berg]
- Merge branch 'attributefiltering' into 2.4. [iglocska]
- Add an imput for search on all attributes in an event. field to search
  can be modify in administration page. [Tristan METAYER]
- Merge pull request #2536 from RichieB2B/stix-mispobjects. [Andras
  Iklody]

  Add MISP objects to STIX export
- Add MISP objects to STIX export. [Richard van den Berg]
- Merge pull request #2537 from RichieB2B/ncsc-nl/stix-conditions.
  [Andras Iklody]

  Add Condition attribute to HTTP_Method STIX export
- Add Condition attribute to HTTP_Method STIX export. [Richard van den
  Berg]
- Merge pull request #2533 from RichieB2B/stix-composites. [Andras
  Iklody]

  Add ip-src|port and ip-dst|port attributes to STIX export
- Add ip-src|port and ip-dst|port attributes to STIX export. [Richard
  van den Berg]
- Merge pull request #2529 from SHSauler/patch-3. [Andras Iklody]
- Removed duplicates from $categoryDefinitions. [Steffen Sauler]

  Payload delivery/ip-dst|port
  Payload delivery/ip-src|port
  Support Tool/text
- Merge pull request #2517 from truckydev/patch-2. [Andras Iklody]

  user right update
- User right update. [truckydev]

  Make all user access to /attributes/describeTypes.json
- Merge pull request #2515 from c-goes/emailregex. [Andras Iklody]

  Allow $ in email addresses
- Allow $ in email addresses. [c-goes]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- MISP galaxy added in the feature list. [Alexandre Dulaunoy]
- MISP objects added. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2502 from aparriel/tag_on_attribute_restSearch.
  [Andras Iklody]

  Fix Tag json format
- Fix Tag json format. [Alexandre Parriel]
- Merge pull request #2495 from arnydo/2.4. [Andras Iklody]

  new: added alternate nameserver option to rpzexport
- Move ns_alt parameter to end of api list. [arnydo]
- RPZExport - Alternate NS. [Kyle Parrish]

  Added option to add an alternate nameserver to RPZ export.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2500 from aparriel/tag_on_attribute_restSearch.
  [Andras Iklody]

  Add Tag field for restSearch on attributes, Fixes #2497
- Add Tag field for restSearch on attributes, Fixes #2497. [Alexandre
  Parriel]
- Merge pull request #2498 from Rafiot/travis3. [Andras Iklody]

  fix: travis file
- Up: Bump PyMISP. [Raphaël Vinot]
- Up: test file. [Raphaël Vinot]

v2.4.80 (2017-09-19)
--------------------

New
---
- Various object template improvements. [iglocska]

  - allow multiple versions of a template to be stored at the same time
  - select which version is the primary version of a template
  - disable/enable templates
  - edit objects with one of the older versions of a template if the object's version requires that

  - various UI / bug fixes
- Objects tied into e-mailing. [iglocska]
- Add way to flatten attributes for certain exports (hids, nids)
  [iglocska]
- Added objects to object preview. [iglocska]
- Added diagnostics for the new attachment tools. [iglocska]
- Further progress on the synchronisation. [iglocska]
- Added phone-number attribute type. [iglocska]

  - Just the yugest attribute types for @rommelfs
- Expose the caching jobs / getProgress to the API. [iglocska]
- Massive performance improvements to the restSearch API. [iglocska]

  - smarter choice of pre-filtering gives a huge boost for non attribute level parameters
  - caching the results of certain parts of the algorithm
  - cleaned up some inefficient looping merges
- Sync with objects wip. [iglocska]

  - add/edit of full events now capture all object related structures
  - restructuring of the edit/add functionalities into clearly divided subsections
- Further work on the objects. [iglocska]

  - uuids of both sides saved in references
  - attachment adding fixed
- Several new features. [iglocska]

  - added multiple flag among other things
- Added first iteration of new add attachment functionality. [iglocska]

  - still :construction:
- Added back referencing from a referenced object. [iglocska]

  - also fixed some view file issues
- Various new features for the objects. [iglocska]
- Added object relations. [iglocska]
- Added first iteration of object references and other changes.
  [iglocska]

  - various fixes
  - rework of the pagination library
- Progress on the Objects. [iglocska]

  - Fixed UI elements in the event view
  - Added object-aware filtering to the event view
  - Objects can now be deleted and viewed once deleted
    - object sanitisation if the setting is set is implemented
  - Edit objects directly from the interface (if the template exists)
  - Various other fixes
- Collapsible object metadata. [iglocska]
- Further work on the object UI. [iglocska]

  - refactoring
  - added objects fields to object rows
  - nested rows within the object
  - massive cleanup
- :construction: - change to model aliasing to solve the reserved class name.
  [iglocska]

  - Internal name is now MispObject for the model, but it is used Aliased, removing the need to do any data massaging
  - Added :construction: edit function
- Added objects submodule. [iglocska]
- Further progress with the objects. [iglocska]

  - added option to populate event with an object to the side menu
  - multiselect popup for objects added
  - redirect after adding object fixed
- More work on the objects. [iglocska]

  - mostly on adding / validating / saving objects including the UI for it
- Further progress on the objects. [iglocska]

Changes
-------
- Version bumps all around. [iglocska]
- Updated taxonomies. [iglocska]
- PyMISP updated. [iglocska]
- Some tuning to the freetext import tool. [iglocska]
- Cakephp updated. [iglocska]
- Rename two fields in the object references. [iglocska]

  - source_uuid => object_uuid
  - destination_uuid => referenced_uuid
- Removed default distribution for attributes in object - tkaen over by
  the pre-validation script. [iglocska]
- Sane defaults set by pre-validation script as a fallback (attributes)
  [iglocska]
- Added empty row after each object / attribute-proposal block.
  [iglocska]
- Updated object definitions. [iglocska]
- Changed Object to MispObject internally. [iglocska]
- Changed frequency to ui-priority. [iglocska]
- Further work on the objects. [iglocska]

  - view events with objects via the API
  - Further improvements to adding objects
- Added new tables to appmodel upgrade script. [iglocska]
- Added new fields to mysql. [iglocska]

Fix
---
- Reverted CakePHP version. [iglocska]
- Fixed the XML view. [iglocska]

  - please stop using XML, for your own sanity, I beg of you!
- Fixed query string and pymisp version. [iglocska]
- Fixed no specification of the tinyint length for the objects in
  MYSQL.sql. [iglocska]
- Fixed double attachment of hashes for malware-samples. [iglocska]
- Updated PyMISP. [iglocska]
- Added an upper limit for max correlations / event. [iglocska]

  - super edge-case test instance got crushed by memory usage
- Correlation improvements. [iglocska]
- Some minor bug fixes. [iglocska]
- Avoid compatibility issue with AGPL license and its warranty clause.
  [Alexandre Dulaunoy]
- Capitalisation of default tlp tag didn't match the ones coming from
  taxonomies in the event alert e-mail subject. [iglocska]
- Fix to certauth pains. [iglocska]
- Added better debugging to the password shell. [iglocska]
- Corrected a copy paste mistake. [iglocska]
- Fix to an issue blocking the JSON download of single events.
  [iglocska]
- Fixes various issues with the certauth. [iglocska]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Fixes to various issues with the cert auth. [iglocska]
- Fixed the favourite tags not showing up in the tag index. [iglocska]
- ACL updated. [iglocska]
- When deleting an attirbute/objects, object references to it are not
  deleted, fixes #2477. [iglocska]

  - force a reference deletion on attribute/object deletion
  - changed it to match deletion type
    - soft-deleting an attribute/object soft-deletes all references to it
    - hard-deleting an attribute/object hard-deletes all references to it
- Fixed notices described in #2482. [iglocska]
- No attributes set in the objects add form makes MISP barf up notices
  instead of gracefully showing an error - fixes #2476. [iglocska]
- Referenced by counter fixed, fixes #2479. [iglocska]
- Fixed the missing refresh on attribute tags when a new tag is added.
  [iglocska]
- Unpublish event on object add. [iglocska]
- Updated the xml export tool to support objects. [iglocska]

  - though why do we still support XML?...
- Various fixes for the objects. [iglocska]
- Fixed the add attachments functionalities. [iglocska]
- Fixed the timestamp of object references not being set. [iglocska]
- Fixed the object reference's timestamp not being updated. [iglocska]
- Fixed the empty event warning if an event only has objects but no
  attributes. [iglocska]
- Various fixes with object reference editing. [iglocska]
- Fixing various issues with the pull. [iglocska]
- Fixed an invalid user field lookup. [iglocska]
- Removed an invalid line left in from a debug session. [iglocska]

  - caused galaxy cluster not to show up on event view
- Fixed an invalid user call in the paginator. [iglocska]
- Added upload logo functionality to org add form. [iglocska]

  - Forgetfullness correlates directly with age apparently
- Reverted a change from yesterday that breaks the event index.
  [iglocska]
- Fixed some parameter issues. [iglocska]
- Some realignment on the attribute add view. [iglocska]
- Fixed array level mess-up. [iglocska]

  derp
- Fixed invalid variable name. [iglocska]
- Fixed invalid lookup for adding object references. [iglocska]
- Added missing object row change. [iglocska]
- Fixed the saving of objects. [iglocska]
- Updated the new ajax methods to follow the new JSON rules. [iglocska]
- Various fixes. [iglocska]
- Fixed an outdated index pointing to a now non-existant field.
  [iglocska]
- Ommit object template elements with invalid attribute types.
  [iglocska]

  - and warn users
  - shout out to all C-level managers at SHA2017
- Fixed event view issue for empty events. [iglocska]
- Added description field to object template elements. [iglocska]
- Fixed previous commit. [iglocska]
- Missing field in object template elements added to match upgrade
  script. [iglocska]
- Updated fields. [iglocska]
- Object renamed to MispObject in form. [iglocska]
- Cakephp updated. [iglocska]
- Removed obsolete table. [iglocska]
- Fixed object references table. [iglocska]
- Add object functions to ACL. [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2493 from RichieB2B/patch-2. [Andras Iklody]

  Use sanitized orgname in STIX header
- Use sanitized orgname in STIX header. [Richie B2B]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2490 from ealtintas/2.4. [Andras Iklody]

  Update README.md
- Update README.md. [Ergin ALTINTAS]

  Fix the typo: "Network Detection Intrusion System" -> "Network Intrusion Detection System"
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2489 from truckydev/patch-1. [Andras Iklody]

  bugfix for freetextimport and email
- Bugfix for freetextimport and email. [truckydev]

  Correction for a bug when you add an email in freeTextImport.

  When you select 'whois-registrant-email' attribut never created and an error is displayed.

  because :
  'whois-registrant-email' not in 'Social network'  and 'Payload delivery' but only in 'Attribution'.

  This PR add the type 'whois-registrant-email' in 'Social network'  and 'Payload delivery' category.

  #### What does it do?

  no issue has been created.

  #### Questions

  - [ ] Does it require a DB change?
  - [ ] Are you using it in production?
  - [ ] Does it require a change in the API (PyMISP for example)?

  #### Release Type:
  - [ ] Major
  - [ ] Minor
  - [X] Patch
- Merge pull request #2457 from Delta-Sierra/2.4. [Andras Iklody]

  remove old text from documentation
- Remove old text from fdocumentation. [Deborah Servili]
- Merge branch 'objects_wip' into 2.4. [iglocska]
- Merge branch '2.4' into objects_wip. [iglocska]
- Merge pull request #2483 from obert01/accessibility-fix. [Andras
  Iklody]

  Accessibility improvement: ARIA properties for the "Add new cluster" button - events/view
- Accessibility improvement: Given the "button" role and appropriate
  aria-label to the "Add new cluster" button in the "galaxy quick
  preview" on an events/view page. [Olivier BERT]
- Merge pull request #2480 from RichieB2B/empty-stix. [Andras Iklody]

  Return empty STIX when no data
- Return empty STIX when no data, fixes #2478. [Richard van den Berg]
- Merge pull request #2474 from obert01/task-accessibility. [Andras
  Iklody]

  Improved the accessibility of the "Scheduled tasks" page for screen readers
- Improved the accessibility of the "Scheduled tasks" page for screen
  reader. The "aria-label" of the buttons for each tasks (frequency,
  time, date) should be set to their value rather than their meaning. In
  fact, the meaning of the value is given by the header of the column,
  which is already perfectly read by all screen reader I have tested.
  [Olivier BERT]
- Merge pull request #2469 from panzertime/2.4. [Andras Iklody]

  fix for issue #2458
- Fix for issue #2458. [RT Hatfield]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Security vulnerability reporting about "high number of published CVEs
  vs a few swept under the rug" [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2428 from cedricbonhomme/make-vagrant-a-submodule.
  [Andras Iklody]

  Make vagrant a submodule
- Added misp-vagrant module. [Cédric Bonhomme]
- Removed vagrant folder. [Cédric Bonhomme]
- Merge pull request #2453 from panzertime/2.4. [Andras Iklody]

  Fixing bug in feed-fetch sched. task
- Fixing bug in feed-fetch sched. task. [RT Hatfield]
- Merge branch '2.4' into objects_wip. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' into objects_wip. [iglocska]
- Merge branch '2.4' into feature/objects. [iglocska]

v2.4.79 (2017-08-28)
--------------------

New
---
- Feeds added to the scheduled jobs. [iglocska]
- Opened up the taxonomies actions to the API: [iglocska]

  valid APIs:

  index, view, enable, disable
- Exposed Feed previews to the API. [iglocska]

  - The following can now be fetched via the API (requires site admin access):
    CSV, Freetext, MISP feeds: /feeds/previewEvent/[feed_id]
    MISP feeds: /feeds/previewIndex/[feed_id]/[event_uuid]
- Added command line tool to enable/disable misp. [iglocska]

  - /var/www/MISP/app/Console/cake Live [0|1]
  - sets the MISP.live directive
- Add a baseurl changer for shell scripts. [iglocska]

  - cake /var/www/MISP/app/Console Baseurl [new baseurl]

Changes
-------
- Update for the version release. [iglocska]

  - querystring bump
  - version bump
  - PyMISP version bump
- PyMISP updated. [iglocska]
- Made the current password confirmation requirement for any user
  profile edits optional. [iglocska]

  - default setting is having it off
  - incredibly frustrating feature is now only enabled on demand
- MISP-galaxies updated. [iglocska]
- Restrict tag editor permission to only create tags. [iglocska]

  - deleting/eding tags indirectly modifies events created by others
  - reduced to site admin only functionality
- Added exit 0 to start.sh to make vagrant happy. [iglocska]

Fix
---
- Removed url -> tls_cert_subject rule conversion for the suricata
  export, fixes #2396. [Andras Iklody]
- Fixed a bug where /events/uuid would return the incorrect event.
  [iglocska]
- Only try to look for feed correlations for a proposal if the proposal
  list isn't empty. [iglocska]
- MISP taxonomy updated. [Alexandre Dulaunoy]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Fix to the max items displayed / page using the custom pagination
  tool. [iglocska]
- Slight improvement to event uuid lookup on the event view. [iglocska]
- Follow redirect from feed pull if the response is a 302. [iglocska]
- Cleanup for feeds fixed. [iglocska]
- Possible fix to the newsread = null issue. [iglocska]
- Fixed a potential persistent cross site scripting in the comments.
  [iglocska]

  - new tag parser for the comments implemented
  - Parser now cleanly pre-constructs the replacement items after finding tag pairs

  - This only impacts users of the same instance, as comments are not synchronised

  - as reported by Jurgen Jans and Cedric Van Bockhaven from Deloitte
- Further Event index UI fixes. [iglocska]
- Fixed event index for non site admins. [iglocska]
- Attribute view also accessible via UUID. [iglocska]
- Fetch PGP key button goes into endless loading if no key was found.
  [iglocska]
- Fixed an obviously dumb validation rule, fixes #2394. [iglocska]

  - derp
- Fixed a group by issue with the event filter overlay. [iglocska]
- Misaligned event index for read only users fixed, fixes #2397.
  [iglocska]
- Fixed mistyped field. [iglocska]
- Fixes to the galaxy import tool. [iglocska]
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Fix double pagination of data in the taxonomies controller, fixes
  #2399. [iglocska]
- Added event_uuid to attribute view. [iglocska]
- Remove the notice thrown if no valid user exists for the given e-mail.
  [iglocska]
- Fixed the XML output for the restresponse library. [iglocska]
- Fixes to several issues with the template editor, fixes #2387, fixes
  #2388. [iglocska]
- Several fixes to the template editor. [iglocska]
- Fixes to issues introduced by the ajax JSON rework, fixes #2384.
  [iglocska]
- Tightening the sanitisation of indicators for the e-mail alerts.
  [iglocska]
- Fixes to several cases of reflected XSS, fixes #2381. [iglocska]

  - as reported by @import-au

  - Additionally enforce content-type on all async APIs called by the UI using CakeResponse

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2419 from RichieB2B/patch-1. [Andras Iklody]

  Make newsread numeric instead of boolean
- Make newsread numeric instead of boolean. [Richie B2B]

  Fixes #2394
- Merge pull request #2415 from CheYenBzh/2.4. [Andras Iklody]

  Baseurl miss in events filter
- Baseurl miss in events filter. [Antoine Callac]

  Minor change, adding baseurl for events search
- Merge pull request #2412 from cedricbonhomme/vagrant-dev-environment.
  [Alexandre Dulaunoy]

  Vagrant dev environment
- Updated default values for OpenSSL and GPG. [Cédric Bonhomme]
- Merge pull request #2410 from cedricbonhomme/vagrant-dev-environment.
  [Andras Iklody]

  Introduction of a development environment based on Vagrant
- Fixed group owner of the MISP installation. [Cédric Bonhomme]
- Updateg .gitignore: ignore Vagrant log files and VM related files.
  [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Added Vagrant configuration files for a development environment.
  [Cédric Bonhomme]
- Added Vagrant configuration files for a development environment.
  [Cédric Bonhomme]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2405 from RichieB2B/patch-3. [Andras Iklody]

  Add Change Password link to profile view
- Add Change Password link to profile view. [Richie B2B]

  Make it easier for users to change their password
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2404 from RichieB2B/patch-2. [Andras Iklody]

  Initialize $abortPost in edit()
- Initialize $abortPost in edit() [Richie B2B]

  Avoid notices about "Undefined variable: abortPost" in debug.log
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2402 from RichieB2B/patch-1. [Andras Iklody]

  Rebuild _authenticateObjects cache in mixed authentication setups
- Rebuild _authenticateObjects cache in mixed authentication setups.
  [Richie B2B]

  When CertAuth is mixed with normal FormAuthentication the upgrade from Simple to Blowfish did not happen because of the internal _authenticateObjects cache. Calling constructAuthenticate() rebuilds this cache.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2389 from truckydev/expose-galaxies-lit-to-api.
  [Andras Iklody]

  Expose galaxies lit to api
- Update GalaxiesController.php. [truckydev]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2385 from cedricbonhomme/fix-command-line-tool-to-
  enable-disable-MISP. [Andras Iklody]

  Fixed error: 'Value is not a boolean, make sure that you convert 'tru…
- Fixed error: 'Value is not a boolean, make sure that you convert
  'true' to true for example.' when enabling/disabling MISP with the
  command line tool. [Cédric Bonhomme]

v2.4.78 (2017-08-06)
--------------------

New
---
- Exposed Roles to the API. [iglocska]

  - valid commands via the API
    - /admin/roles/add [GET, POST]
    - /admin/roles/delete/{id} [POST, DELETE]
    - /admin/roles/edit/{id} [GET, POST]
    - /admin/roles/index [GET]
    - /admin/roles/set_default/{id} [POST]
    - /roles/index [GET]

Changes
-------
- Version bump. [iglocska]
- Updated misp galaxies. [iglocska]
- Updated warninglists. [iglocska]

Fix
---
- Fixed capitalisation of "throw" in templateElementsController.
  [iglocska]
- Fixes the lookup of attributes in the UI attribute search to correctly
  adhere to sharing groups. [iglocska]

  - Attribute search was not correctly adhering to sharing group rules as it wasn't using the centralised lookup method

  - As reported by Helge Aksdal
- PyMISP version bump. [iglocska]
- Nicer response for the API to push events to ZMQ. [iglocska]
- Fixed a typo in the pushEventToZMQ function. [iglocska]
- Only add the permission description to the Role fetcher if the
  permission level is queried. [iglocska]
- Added constants to role permissions for the API. [iglocska]

  - Permission now accepts a constant [read|manage_own|manage_org|publish] in addition to a numeric value [0|1|2|3]
  - Querying a role via the API returns the constant additionally to the numeric value in the permission_description field

  - Added /roles/view/{id} to the API
- Previous commit was incorrect, empty filters contain null not false.
  [iglocska]
- Fixed "published":0 filter for restsearch. [iglocska]

  - also removed an empty function
- Added put/post to role deletion. [iglocska]
- Invalid model used to push ZMQ messages for discussion posts.
  [iglocska]
- Potential fix to the template element adding issue throwing ajax only
  exceptions. [iglocska]
- Changed the validation of newsread and change_pw to boolean. [Andras
  Iklody]
- Fixed an issue with the roles model failing on stricter MySQL settings
  due to missing group by. [iglocska]

Other
-----
- Fixed org logos in attribute index. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2364 from strikaco/patch-1. [Alexandre Dulaunoy]

  Adds missing sudo invocation
- Adds missing sudo invocation. [Johnny]
- Fix #2347 - cookie attribute type. [Alexandre Dulaunoy]

  HTTP cookie as often stored on the web client and can be authentication
  or even session cookie.
- Merge pull request #2340 from Rafiot/travis. [Alexandre Dulaunoy]

  Update travis file.
- Update travis file, use composer for all PHP deps. [Raphaël Vinot]
- MISP website links and references updated. [Alexandre Dulaunoy]
- A link to the CONTRIBUTING page added. [Alexandre Dulaunoy]

v2.4.77 (2017-07-12)
--------------------

New
---
- Added php ini path. [iglocska]

Changes
-------
- PyMISP version bump. [iglocska]
- Redacted certain server settings that could be considered sensitive.
  [iglocska]

  - Encryption passwords as well as redis password are now redacted from the server settings
  - Also includes the JSON dump of the server settings

  - Thanks to cert.govt.nz for the security report.
- Version bump. [iglocska]

Fix
---
- Remove delegation request once event delegation is accepted.
  [iglocska]

  - TODO, cleanup of zombie delegation requests
- Updated pyMisp and querystring versions. [iglocska]
- Added user password length change to the MYSQL.sql file. [iglocska]
- Tightened the sanitisation of the filenames in the template uploader.
  [iglocska]

  - Data from retained uploaded files when re-editing a template popuplation prior to submission was loaded into the JS directly without sanitisation
  - Whilst there was no way found to exploit this, introduced tighter sanitisation for the file data

  - Thanks to cert.govt.nz for the security report.
- Fixed some missing css/scripts from the iframe for the template
  uploader. [iglocska]
- GFI uploaded archives don't throw exceptions on failed parsing,
  instead simply show an error banner after redirect. [iglocska]

  - in situations with misconfigured MISPs (debug enabled), a parsing error
    exception thrown while parsing a maliciously malformed archive could include
    arbitrary files in the stacktrace accessed from within the apache user's
    scope if a symlinked file was uploaded in the archive

  - Thanks to cert.govt.nz for the security report.
- Upgraded hashing algorithm used and added requirement to confirm
  password for user profile changes. [iglocska]

  - Added method to upgrade all passwords to blowfish transparently
  - All profile edit pages (/users/edit, /admin/users/edit, /users/change_pw) now require the user's password to be confirmed

  - Thanks to cert.govt.nz for the security report.
- Added screenshots to attribute index/attribute search, fixes #2338.
  [iglocska]

  - Flickr can start quivering in its boots!
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Value1 and value2 removed from attributes/view/id. [iglocska]
- The server settings page (servers/serverSettings) was crashing when
  the redis connection wasn't properly working. [Cédric Bonhomme]
- Further performance tweaks to the feed fetcher. [iglocska]
- Made the feed pull for CSV/Freetext feeds much faster for large feeds.
  [iglocska]

  - value de-duplication is now a lot more efficient
- Massive performance boost when adding attributes to an already large
  event. [iglocska]
- Return json dict instead of string when queuing a feed pull job.
  [iglocska]
- Fix the massive hover popover for modules that keeps breaking the
  layout at trainings. [iglocska]

  (ノ°Д°）ノ︵ ┻━┻
- Fixed TC import. [iglocska]
- Removed unused fulltext index in favour of 255 length index.
  [iglocska]
- Fixed a potential issue with galaxy clusters with no elements causing
  notices. [iglocska]
- Accessing a pivoted event view URL without having the pivot path
  tracked in the session threw a notice. [iglocska]
- Added missing ServersController.php change that populates $php_ini.
  [iglocska]

  - faildev forgot to commit the file
- Don't run the regexp replaces on sigma rules. [iglocska]
- JSON export via the UI should download a file, not render the JSON.
  [iglocska]
- Invalid redirect from adding attachments when hitting post size limit.
  [iglocska]
- Cleanup/sync of installation guides. [SHSauler]
- Fixed the invalid CSV download filename. [iglocska]
- MISP taxonomies updated to the latest version (DML added) [Alexandre
  Dulaunoy]
- Fixed sanitisation of feed correlation fields. [iglocska]
- New dataplane.org feeds added. [Alexandre Dulaunoy]
- Meta field in galaxy cluster should be a dict even if empty in the
  JSON output, fixes #2280. [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2327 from kallix/attachments_dir-settings. [Andras
  Iklody]

  Add an optional setting attachments_dir, and adapt existing code to use this setting
- Attachments_dir: Default value queried through a function to
  workaround PHP inability to have anything useful stored in a class
  property. [Kevin Allix]
- Add an optional setting attachments_dir, and adapt existing code to
  use that setting. [Kevin Allix]
- Merge pull request #2332 from Deventual/patch-12. [Alexandre Dulaunoy]

  minor adjustments
- Minor adjustments. [Deventual]
- Merge pull request #2329 from Deventual/patch-10. [Alexandre Dulaunoy]

  added mixbox update instructions
- Merge branch '2.4' into patch-10. [Alexandre Dulaunoy]
- Merge pull request #2330 from Deventual/patch-11. [Alexandre Dulaunoy]

  fix minor instructions
- Fix minor instructions. [Deventual]
- Added mixbox update instructions. [Deventual]
- Merge remote-tracking branch 'origin' into 2.4. [iglocska]
- Merge pull request #2325 from cedricbonhomme/fix-bug-when-redis-
  connection-fails. [Andras Iklody]

  fix: The server settings page (servers/serverSettings) was crashing w…
- Merge pull request #2314 from kallix/redis_password. [Andras Iklody]

  Allow Redis to be password-protected
- Merge branch 'redis_password' into 2.4. [iglocska]
- Allow a setting to NOT define a 'test' function. [Kevin Allix]
- Add MISP.redis_password option. [Kevin Allix]
- Use a password to connect to Redis if MISP.redis_password is set in
  config.php. [Kevin Allix]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2307 from edhoedt/patch-2. [Andras Iklody]

  Attribute tags: fixing automatic refresh after deleting/adding a tag
- Attribute tags: fixing automatic refresh after deleting/adding a tag.
  [edhoedt]

  Attribute_id_tr class should actually be ShadowAttribute_id_tr
- Merge pull request #2306 from edhoedt/patch-1. [Andras Iklody]

  Fixing crash on Event Tag delete+refresh on recent MySQL version
- Fixing crash on Event Tag delete+refresh on recent MySQL version.
  [edhoedt]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2294 from garanews/2.4. [Andras Iklody]

  Show the welcome_text in tab title
- Show the welcome_text in tab title. [garanews]

  Show MISP.welcome_text_top value also in the tab title.
  Useful when managing many MISP instances.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2293 from FIRSTdotorg/2.4. [Andras Iklody]

  Fixed empty user creation and user updates when org changes
- Fixed issue #2036. [Guilherme Capilé]
- Bugfixes in certificate authentication. [Guilherme Capilé]
- Merge pull request #1 from MISP/2.4. [Guilherme Capilé]

  updating FIRST MISP repository
- Merge pull request #2292 from SHSauler/doc. [Andras Iklody]

  fix: cleanup/sync of installation guides
- Merge pull request #2284 from MISP/revert-2283-getpgid. [Andras
  Iklody]

  Revert "Use posix_getpgid to check whether a pid is running"
- Revert "Use posix_getpgid to check whether a pid is running" [Andras
  Iklody]
- Merge pull request #2283 from kallix/getpgid. [Andras Iklody]

  Use posix_getpgid to check whether a pid is running
- Use posix_getpgid to check whether a pid is running. [Kevin Allix]
- Merge pull request #2282 from kallix/ps_grep. [Andras Iklody]

  Fix for a small bug: MISP can report mispzmq.py is running when it's not running
- Grepping the output of ps: the grep pattern should be ^pid_value$
  [Kevin Allix]
- Merge pull request #2281 from kallix/portability. [Andras Iklody]

  Change shebang to /usr/bin/env xxx for better portability
- Change (where needed) shebang to /usr/bin/env xxx for better
  portability. [Kevin Allix]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2279 from ninSmith/2.4. [Andras Iklody]

  New apache directive with apache 2.4
- Fixes #2278. [dc]
- Merge pull request #2276 from FafnerKeyZee/2.4. [Andras Iklody]

  Install Debian 9 (Stretch)
- Update INSTALL.debian9.txt. [Fafner [_KeyZee_]]
- Create INSTALL.debian9.txt. [Fafner [_KeyZee_]]
- Merge remote-tracking branch 'upstream/2.4' into 2.4. [Fafner
  [_KeyZee_]]
- Merge pull request #2 from MISP/2.4. [Fafner [_KeyZee_]]

  update

v2.4.76 (2017-06-20)
--------------------

New
---
- Feed http://cinsscore.com/list/ci-badguys.txt added. [Alexandre
  Dulaunoy]
- Contributing guidelines added following the initial wiki document.
  [Alexandre Dulaunoy]
- Caching of the CIDR blocks to boost the advanced correlation
  performance. [iglocska]

  - massive boost to performance when using advanced correlations
- Push new Discussion items to ZMQ Under the topic
  misp_json_conversation. [Hannah Ward]
- Performance improvements for the pub-sub modules. [iglocska]

  - Only load and open connection to redis for the pub-sub connection once.
  - Massive performance boost when the ZMQ functionality is enabled
- Add adhereToWarninglists as a JSON parameter to the freetextImport
  API. [iglocska]

Changes
-------
- VERSION bump. [iglocska]
- Some small changes to the discussion ZMQ integration. [iglocska]

  - tied into new way of invoking the ZMQ module
  - added some context fields to the messages being pushed (orgname, user email, etc)

Fix
---
- Warning-lists updated to the latest version. [Alexandre Dulaunoy]
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Prevent form from being submitted when changing a template element,
  fixes #2274. [iglocska]
- Error handling of proposal sync. [iglocska]

  - don't log errors if no proposals are found
  - don't throw an exception if no proposals are found
- Allow triggering the fetch feed from the API. [iglocska]
- Changed the colour of the git output to something more soothing.
  [iglocska]
- Fixed an issue in the XML export due to neglect. [iglocska]
- Fixed a group by issue. [iglocska]
- Removed silly duplicate queries from the event index. [iglocska]
- Fixed indexing of the value field for certain instances. [iglocska]
- Moved attachment access diagnostic tool to attributes controller.
  [iglocska]
- Yes is not Yee. [Alexandre Dulaunoy]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Possible fix for a massive performance bug on older MYSQL versions
  when entering attributes. [iglocska]
- Fix to the CIDR caching. [iglocska]
- Follow up to the previous patch, also for the individual events'
  stixification. [iglocska]
- Throw the STIX errors to file, fixes #2266. [iglocska]

  - saved to /var/www/MISP/app/tmp/logs/exec-errors.log
- Further fixes to the delete attribute length. [iglocska]
- Fix the delete proposal's length based on the number of fields in the
  table. [iglocska]
- Explanation regarding meaning of variables. [Steffen Sauler]

  Default OutputDirName (current dir) led to error for me on Ubuntu 16.04, tar 1.28. Provided works and is neater.
- Further performance improvements to the zmq module. [iglocska]

  - should make inserting data faster
- Fixed the duplicate sighting save that kept popping up in the ZMQ
  feed. [iglocska]
- Fixed error messages for the CSV export API. [iglocska]
- Don't return the mixbox version if no mixbox is installed. [iglocska]
- New way of checking for API access. [iglocska]

  - meant to resolve some issues such as being redirected to the news page if a new news item exists while running a CSV export via the API
- Possible fix to the stix export for various STIX versions / python
  versions. [iglocska]
- Fixed the mixbox version lookup. [iglocska]
- Added Mixbox to the STIX installation, fixes #2262 ##comma## fixes
  2261. [iglocska]

  - provided by @newdominic
- Corrected range of valid port numbers for the attribute validation.
  [iglocska]

  - as pointed out by @MattCarothers
- Validation for port attribute The logical check for a valid port was
  backwards.  It looked for an integer outside the range of 1-65535
  rather than inside. [Matt Carothers]
- Added cache feeds to the gitignore. [iglocska]
- Fixed a notice error in the taxonomy view. [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2182 from ppanero/2.4. [Andras Iklody]

  newsread attribute fixed for user registration via sso
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4. [Pablo
  Panero]
- Merge branch 'badattch' into 2.4. [iglocska]
- Changing some texts. [root]
- Adding small diagnostic on Server Setting > Diagnostics page to check
  if some attachments referenced in database doesn't exist on
  filesystem. [root]
- Merge pull request #2032 from dmaciejak/dmaciejak-patch-2. [Andras
  Iklody]

  Remove duplicated h() calls
- Merge branch '2.4' into dmaciejak-patch-2. [Andras Iklody]
- Merge pull request #2267 from RichieB2B/nscs-nl/fixframe. [Andras
  Iklody]

  Keep misp2stix Python 2.6 compatible
- Keep misp2stix Python 2.6 compatible. [Richard van den Berg]
- Merge pull request #2209 from tk-hendrik/fix/apache_auth. [Andras
  Iklody]

  Fix invalid newsread
- Merge branch '2.4' into fix/apache_auth. [Andras Iklody]
- Add: reputation.alienvault.com feed added. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2243 from SHSauler/patch-2. [Andras Iklody]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2264 from FloatingGhost/2.4. [Andras Iklody]

  Push Conversation items to a ZMQ topic
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4. [Hannah
  Ward]
- Merge pull request #2260 from
  MattCarothers/fix_backwards_port_validation. [Andras Iklody]
- Fix invalid newsread. [Hendrik]
- Merge branch '2.4' into dmaciejak-patch-2. [David Maciejak]
- Remove duplicated h() calls. [David Maciejak]

v2.4.75 (2017-06-13)
--------------------

New
---
- First round of massive performance tuning (tm)(c) [iglocska]

  - Make MISP fast again
- Export default feed list in Markdown format. [Alexandre Dulaunoy]

  Simple Python script to dump the default feed list in a Markdown list.
  The script is to be used for the automatic generation of the
  misp-website and documentation to keep an up-to-date list of feeds in
  the various public places of the MISP project.
- Mass delete events. [iglocska]

  - simply use the multi select on the event index via the UI
  - for the API, simply POST to /events/delete with a payload in the following format:
    `{"id": [15, 16, 17]}`

  - if you've accidentally deleted all your events using this functionality, feel free to contact @rommelfs or contact the NSA for backups
- Added Font Awesome for greater glory. [iglocska]
- Added email-body attribute type, fixes #1062. [iglocska]

Changes
-------
- Version bump. [iglocska]
- Performance tuning: Custom pagination tool. [iglocska]

  - changed set operation to a more performance alternative
- Added event info in feed correlations via a popover. [iglocska]

Fix
---
- Fixed an error causing combined feed cache issues. [iglocska]
- Relaxed UUID4 requirement for UUID validation. [iglocska]

  - we shouldn't enforce anything beyond the basic format
- Allow browsing events that have a failed full fetch. [iglocska]
- Removed port numbers from correlating, fixes #2141. [iglocska]
- Fixes a feed caching issue introduced by the performance tweaks.
  [iglocska]

  - moved the combined feed generation for the fast lookups to the feed caching algorigthms as opposed to an on an on-the-fly merge
- Fixed invalid looping to pick up feed correlation event info fields.
  [iglocska]
- Fixes a missing method needed for CIDR correlation, fixes #2256.
  [iglocska]

  - CIDR correlation for IPv6 was utterly broken and broke the entry of ip attributes
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Added missing view file. [iglocska]
- Typo fixed. [iglocska]
- GPG vs PGP key naming snafu fixed. [iglocska]
- Fixed the proposal event index view showing org IDs instead of org
  names, fixes #2248. [iglocska]
- Truncate log descriptions that are over 65532 character long.
  [iglocska]
- No commit message. [iglocska]

  - cleanup refactoring of pub sub tool
  - better handling of no access to redis
- Added download buttong for the feed settings in JSON format, fixes
  #1895. [iglocska]
- Fixed issues with feeds that time out causing failures. [iglocska]
- Forgot to catch for weird STIX version. [Hannah Ward]
- Another IDGen thing. [Hannah Ward]
- Added empty string as default for feed data. [iglocska]

  - to handle cases where no data is returned.
- Removed second publish button from the menu. [iglocska]

  - copy pasta fail FTL
- Alignment issue fixed. [iglocska]
- New and improved child-lock. [iglocska]
- Use IDGen from literally any module that has it. [Hannah Ward]
- Added child-protection for the mass select on the event index.
  [iglocska]

  - only site admins can mass select + delete now.
- Fixed a silly issue in the ZMQ publisher. [iglocska]

  - was setting up the socket and tearing it down for each message, derp
  - as reported by @RichieB2B
- Made Python 3 happy with the ZMQ scripts. [iglocska]
- Added missing css loader from the layout. [iglocska]
- Email-attachment and email-body now accept line breaks. [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2207 from RichieB2B/ncsc-nl/mixbox. [Alexandre
  Dulaunoy]

  Also test for mixbox version
- Merge branch '2.4' into ncsc-nl/mixbox. [Alexandre Dulaunoy]
- Merge pull request #2251 from stinnux/feature/ApacheAuth-AllowUpdate.
  [Andras Iklody]

  Feature/apache auth allow update
- Remove Debugging. [Thomas Stinner]
- Disable user in case he has no roles. [Thomas Stinner]
- Allow Updating existing users. [Thomas Stinner]
- Also test for mixbox version. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2244 from FloatingGhost/2.4. [Alexandre Dulaunoy]

  fix: forgot to catch for weird STIX version
- Merge pull request #2242 from MISP/MURDER_STIX. [Alexandre Dulaunoy]

  fix: Another IDGen thing
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2240 from FloatingGhost/2.4. [Alexandre Dulaunoy]

  fix: Use IDGen from literally any module that has it
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Two new feeds from @bambenek added in the default JSON feed.
  [Alexandre Dulaunoy]

v2.4.74 (2017-05-30)
--------------------

New
---
- Added default feed list. [iglocska]
- Publish event to ZMQ on demand and beaconing of ZMQ tool. [iglocska]
- Auto load the default feeds from file. [iglocska]
- Added User and Organisation addition/change data to the ZMQ feed.
  [iglocska]
- Added filtering to the tag index. [iglocska]

  - also globally fixed the filter issues when filtering from an index with a different pagination position than the first page
- Added sightings to ZMQ pub sub system. [iglocska]
- Added attribute JSONs to pubsub system. [iglocska]

  - also made mispzmq a but more generic
- Add instance uuid. [iglocska]

Changes
-------
- VERSION bump. [iglocska]
- Querystring version bump. [iglocska]
- Also store the lookup_visible field from the field import. [iglocska]
- Allow for \t to be used as a CSV feed delimiter. [iglocska]

Fix
---
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Logrotate, database.php settings explanation. [Steffen Sauler]
- Clarified ZMQ start button (it doesn't restart anything anyway)
  [iglocska]
- Made the mispzmq.py script less crap. [iglocska]
- Gitignore updated. [iglocska]
- Initial password reset functionality. [iglocska]

  - invalid parameters sent for new users in the on-demand reset
  - been bugged for 4 months, but became somewhat obsolete with the automatic notification so no one noticed
- Added missing topics to the mispzmq.py script. [iglocska]
- Fix a copy paste bug. [iglocska]
- [misp-zmq] add a Poller for future multi-SUBscriber in ZMQ. [Alexandre
  Dulaunoy]
- Fixed an issue with false positive sightings throwing notice errors on
  the event view. [iglocska]

  - caused by the false positive sightings data being aggregated in the event level sparkline without the correct dates being set
  - solution is to remove the false positive data from being entered in the sparkline, the goal of it is only to show sightings anyway.
- Truncate the change field in log entries if it becomes humongous.
  [iglocska]

  - solves a rare situation with massive PGP keys breaking user additions / edits
- Some cleanup in the mispzmq script. [iglocska]
- Misp-taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Misp-galaxy latest version updated. [Alexandre Dulaunoy]
- Skip the import of mixbox for users of older stix libraries.
  [Alexandre Dulaunoy]

  If you rely on old idgen from previous stix libraries, mixbox is not installed.
  This completes the fix #2186 and should be fine for old and new stix libraries.

  A partial lyric has been included in this commit to ease the pain to work ##comma##:

  Money for nothin' and your stix for free
  Money for nothin' and stix for free
- Fixed a notice issue with the feed index if no cache has been
  generated yet. [iglocska]
- GUI bug/inconsistency (Explore remote server), fixes #2203. [iglocska]

  - Removed the link from the published sign, it was indeed silly
- Fixed a few silly issues with the hids export. [iglocska]

  - allow POSTed parameters
  - simpler response always responds with txt type, won't complain about view not being set for incorrect accept headers
- Hids api threw error on empty result. [iglocska]
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Update to the MISP galaxy latest version. [Alexandre Dulaunoy]
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Deal with all the weird and "wonderful" stix versions Tries to fix
  #2181. [Hannah Ward]
- Move idgen call to mixbox. [Hannah Ward]
- Fixed an issue with the freetext importer failing if no tags were set.
  [iglocska]
- Fixed a condition where no proposals downloaded generated a warning in
  the debug log. [iglocska]
- Added default comment to event blacklists, fixes #2080. [iglocska]
- Updated cakephp solving TLS 1.2 issues. [iglocska]
- Fixed an API vs documentation mismatch for the nids exports.
  [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2232 from SHSauler/patch-1. [Andras Iklody]

  fix: logrotate, database.php settings explanation
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2230 from ppanero/sso_fix. [Andras Iklody]

  newsread attribute fixed for user registration via sso
- Newsread attribute fixed for user registration via sso. [Pablo Panero]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Remove crap introduced by rope project. [Alexandre Dulaunoy]
- Add rope project in the gitignore. [Alexandre Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- First version of a Python ZMQ client to get messages from a MISP
  instance. [Alexandre Dulaunoy]

  usage: sub.py [-h] [-s] [-p PORT] [-r HOST] [-o ONLY] [-t SLEEP]

  Generic ZMQ client to gather events, attributes and sighting updates from a
  MISP instance

  optional arguments:
    -h, --help            show this help message and exit
    -s, --stats           print regular statistics on stderr
    -p PORT, --port PORT  set TCP port of the MISP ZMQ (default: 50000)
    -r HOST, --host HOST  set host of the MISP ZMQ (default: 127.0.0.1)
    -o ONLY, --only ONLY  set filter (misp_json, misp_json_attribute or
                          misp_json_sighting) to limit the output a specific
                          type (default: no filter)
    -t SLEEP, --sleep SLEEP
                          sleep time (default: 2)
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2211 from kajogo777/2205. [Andras Iklody]

  FIX #2205 attachTagToObject permissions so that tagger role are able …
- FIX #2205 attachTagToObject permissions so that tagger role are able
  to tag objects where obj.orgc_id != user.org_id fixes. [George]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2200 from RichieB2B/ncsc-nl/openioc. [Andras
  Iklody]

  Several fixes for OpenIOC importer
- Set OpenIOC attribute distribution to 'Inherit' by default. [Richard
  van den Berg]
- Accept RouteEntryItem strings. [Richard van den Berg]
- Test for 'success' key, fixes #2198. [Richard van den Berg]
- Merge pull request #2190 from FloatingGhost/2.4. [Alexandre Dulaunoy]

  Deal with the stupid errors STIX thinks it's ok to just throw
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4. [Hannah
  Ward]
- Merge pull request #2186 from FloatingGhost/2.4. [Andras Iklody]

  fix: Move idgen call to mixbox
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2179 from truckydev/2.4. [Andras Iklody]

  add possibility to define tags for import module.
- Add possibility to define tags for import module. Add possibility to
  desable validation for String field when empty. [Tristan METAYER]

v2.4.73 (2017-05-10)
--------------------

New
---
- Update all the json structures in MISP via the API, fixes #2168.
  [iglocska]

  - Just post to the following APIs as a site admin:
    - /warninglists/update
    - /galaxies/update
    - /taxonomies/update
- First implementation of the feed analysis system. [iglocska]
- Cortex objects shown in popup. [iglocska]
- New module type: Cortex. [iglocska]

  - similar to Enrichment modules except for not having the options to run hover
- New type - cortex. [iglocska]

  - raw cortex output json
- Use /events/freeTextImport/eventid via the API to directly parse and
  create attributes from the input. [iglocska]

  - expected format is {"value": "my_string_to_parse"} with "distribution" being an optional value (otherwise instnace defaults are assumed)

Changes
-------
- Version bump on the queryVersion. [iglocska]
- In preparation of the various taxonomy types, only update event type
  taxonomies or ones without a type. [iglocska]
- Added scroll bar to large cortex object popups. [iglocska]
- Change to the CIRCL pgp keyserver instead of the slowpoke MIT one.
  [iglocska]
- Added attribute count to the event view's meta fields too, fixes
  #2151. [iglocska]
- Show number of attributes on the all filter in the event view, fixes
  #2151. [iglocska]
- Added distribution as a possible module output field. [iglocska]

Fix
---
- Removed two duplicate fields from MYSQL.sql. [iglocska]
- Added missing fields causing pulled events to not contain attributes,
  fixes #2171. [iglocska]
- Fixed two small bugs. [iglocska]
- Don't show links to feeds on the event view to normal users.
  [iglocska]
- Several fixes to the feed overlay matrix. [iglocska]

  - lookup was broken for csv/freetext feeds
  - allow users to see the feeds if the admin allows it
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- Misp-taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Make redis optional (for now) [iglocska]
- Fixed two looping issues in the feed analysis matrix. [iglocska]

  - fixed cache age counter going ape****
  - fixed the overlap value counters in the graph popovers
- Removed an invalid check causing travis to fail. [iglocska]
- Version bump. [iglocska]
- Several feed fixes. [iglocska]
- Added overlap count to the feed analysis hover. [iglocska]
- Added unpublish_event not being loaded. [iglocska]
- Better centering of the cortex object popup. [iglocska]
- Missing parameters for getenabledmodules. [iglocska]
- Fixed a failure with cortex modules (hopefully) [iglocska]
- Set a default colour for tags in the feed preview that don't have a
  colour set. [iglocska]
- Reduced the data pushed to the view for the tag index, potentially
  resolves #2156. [iglocska]
- Set the content header for module lookups. [iglocska]
- Add event_blacklists and org_blacklists in POSTGRESQL install scripts.
  [Adrien RAFFIN]

  Also fix small bug in imported MYSQL syntax

  WARNING: NOT tested in production

  Tests were only done to create database structure, MISP wasn't run with
  this database. It still could have incompatibilities with Model
- Add event_blacklists and org_blacklists in MYSQL install scripts.
  [Adrien RAFFIN]
- Fixed an issue where certain filters removed some elements from the
  object counter, fixes #2151. [iglocska]
- Left off controller changes in the previous commit. [iglocska]
- Removed the automatic sorting from fetchEvent to improve performance.
  [iglocska]
- Allow event edits even if the "Event" container isn't set. [iglocska]
- Fixed the publishtimestamp filter issues with the event index.
  [iglocska]

  - allow for publishtimestmap and publish_timestamp due to some documentation issues
  - fixed the lookup to be greater than by default instad of lower than
  - added the option to pass a range by passing an array with a start and end publish timestamp
- Re-added missing config settings to the export modules. [iglocska]
- Added missing distribution defaults to the import modules. [iglocska]
- Bug: Ip-dst attribute should not be able to include a "/", fixes
  #2138. [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #2128 from deloittem/2.4. [Andras Iklody]

  Snort attribute generation rule now contains the initial msg field
- Update rule generation for attribute snort: generated rule now
  contains the initial snort rule msg. [deloittem]
- Merge branch '2164' into 2.4. [iglocska]
- Remove extraneous </div> [Ángel González]
- Reorder </div> and </form> to be properly nested. [Ángel González]
- Cosmetic changes. [Ángel González]

  Change space indents to tabs
  Remove ?> at end of file
  Add or remove some indentation where appropriate
- Minor tweaking of comments. [Ángel González]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2163 from ppanero/bro_export. [Andras Iklody]

  [:construction:] - BroExport types updeted
- BroExport types updeted. [Pablo Panero]
- Merge pull request #2161 from Keisial/2158. [Andras Iklody]

  Change feedback about email notification on sending proposals
- Change feedback about email notification on sending proposals. [Ángel
  González]

  Move from a “Failed for at least one recipient” warning notification
  to warn when it was not sent to anyone, which is more interesting for
  the user sending the proposal.

  Fixes #2158
- Merge branch 'feature/feedanalysis' into 2.4. [iglocska]
- Merge branch 'feature/cortex' into 2.4. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2154 from truckydev/2.4. [Andras Iklody]

  Add filename key for import modules
- Add test for empty filename. [Tristan METAYER]
- Add filename key for import modules. [Tristan METAYER]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1947 from SekoiaLab/fix/install_sql. [Andras
  Iklody]

  Fix/install sql
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Markdown typo fixed. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1809 from devnull-/issues_1643. [Andras Iklody]

  Issues 1643
- Merge branch '2.4' into issues_1643. [devnull-]
- Quick & Dirty 'without_email' & 'Unpublish_event' options for Sync
  Server. [devnull-]
- Update the database schema unpublish_event (servers) &
  PublishWithoutEmail (servers) [devnull-]
- Update the database schema unpublish_event (servers) [devnull-]
- Update the database schema PublishWithoutEmail (servers) [devnull-]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2137 from juju4/2.4. [Andras Iklody]

  Remove default value for column comment
- Remove default value for column comment ERROR 1101 (42000) at line 20:
  BLOB, TEXT, GEOMETRY or JSON column 'comment' can't have a default
  value https://travis-ci.org/juju4/ansible-MISP/jobs/222624828#L7561
  (ubuntu xenial, mysql 5.7)
  https://dev.mysql.com/doc/refman/5.7/en/blob.html. [juju4]

  Strangely, this does not affect centos7 and mariadb 5.5 even if corresponding documentation states the same.
  https://travis-ci.org/juju4/ansible-MISP/jobs/222624827#L4862

v2.4.72 (2017-04-14)
--------------------

New
---
- Disable taxonomy tags. [iglocska]
- Added attributes / event average to statistics. [iglocska]
- Minimal flag added to the event index. [iglocska]

  - used by the sync, greatly reduces the data fetched / transfered on the initial sync negotiation
- Added JS dev doc. [Hannah Ward]
- Added watchify for on-the-fly dev. [Hannah Ward]
- Add build script for JS new: Add es6 version of misp.js chg: Removed
  plain JS. [Hannah Ward]
- Added package.json file. [Hannah Ward]
- Added new flag to events/restSearch to disable sharing group loading.
  [iglocska]

  - sgReferenceOnly: Will only load the sharing_group_id not the actual sharing group data

Changes
-------
- Version bump. [iglocska]
- Querystring bump. [iglocska]
- Make the extension .js for people's syntax highlighters. [Hannah Ward]
- Add npm instructions in install. [Hannah Ward]

Fix
---
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Enforce the hide tag directive. [iglocska]
- Toggling an attribute's correlation won't reload the page anymore.
  [iglocska]

  - Part of the 2017 saving @adulau's sanity initiative(tm)
- Removed sharing group option from the quick distribution edit, fixes
  #2116. [iglocska]
- Fixed an issue with the org blacklisting. [iglocska]
- Fixed an issue where a proposal not having an assigned organisation
  broke the synchronisation on a pull. [iglocska]
- Fixed a format issue with the minimal index. [iglocska]
- No notify field set in user creation throws error. [iglocska]
- Reverted JS changes for now. [iglocska]
- Further JS fixes. [iglocska]
- Further fixes to the JS. [iglocska]
- Several js fixes. [iglocska]
- Left off changes to misp.js. [iglocska]
- Fixed a missing variable initialisation. [iglocska]
- Fixed uninitialised variable. [iglocska]
- Un-minified JS. Don't bully me. [Hannah Ward]
- Remove now unneeded JS deps. [Hannah Ward]
- Added 'var' in front of new variables. [Hannah Ward]
- Assign global functions to window. [Hannah Ward]
- Added uglifyjs for minified JS. [Hannah Ward]
- Don't try to use the react preset ;) [Hannah Ward]
- Only require node for development purposes - compiles to JS. [Hannah
  Ward]
- Ignore the *right* node folder. [Hannah Ward]
- Avoid undefined calls to .value. [Hannah Ward]
- Updated JS to fix Infinite loading when adding an attribute fails,
  fixes #2102. [iglocska]
- Removed unnecesary part of the previous fix. [iglocska]
- Fixed a mass attribute edit issue if no sharing groups are created on
  the instnace. [iglocska]
- Added fallback for getallheaders() missing for some systems.
  [iglocska]
- Missing ; added. [iglocska]
- Query string version bump. [iglocska]
- Added logging to the testconnection post-test. [iglocska]

  - also, fixed the inverted error codes as noted by @ppanero
- Fix to the correlation graph after the relatedevent format changes.
  [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch 'jsfix' into 2.4. [iglocska]
- Ignore node packages in gitignore. [Hannah Ward]

v2.4.71 (2017-04-11)
--------------------

New
---
- Set distribution level in freetext results / module import results,
  fixes #2023. [iglocska]
- Password complexity defaults tightened, also passowrd requirements
  shown to users, fixes #2117. [iglocska]
- Check is user is sudo before wiping misp. [Hannah Ward]
- Rework of the restsearch APIs. [iglocska]

  - allows for alternate download types (supported for now: openioc)
  - major refactor of the openioc export
  - refactor of the CIDR tool

Changes
-------
- Org blacklisting enabled by default. [iglocska]
- Bumped versions. [iglocska]

  - pymisp
  - query string version
  - php recommended version
- Version bump. [iglocska]
- DB changes pre-loaded for 2.4.71. [iglocska]
- Default password policy now includes a 16 char+ string option as an
  alternative to the short 3/4, fixes #2117. [iglocska]
- Added the proposal to delete flag to the API output, fixes #2105.
  [iglocska]
- Automation page updated to reflect the changes to the search APIs.
  [iglocska]

  - If your name is Raphael, move along nothing to see here *cough*

Fix
---
- Invalid lookup in the upgrade script causing the two default entries
  for the org blacklist to not populate. [iglocska]
- PyMISP version bump. [iglocska]
- Fixed the missing brace. [iglocska]
- Fixed the upgrade script to 2.4.71. [iglocska]
- Removed obsolete file. [iglocska]
- Removed obsolete js file. [iglocska]
- Cleanup of the role add/edit checkboxes. [iglocska]
- Better error handling for failing to attach tags. [iglocska]
- Added password complexity popover to the password change dialogue.
  [iglocska]
- Misp-taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Misp-warninglists updated to the latest version. [Alexandre Dulaunoy]
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Set comment field to an empty string in the attribute pre-validation.
  [iglocska]
- DB changes preloaded for 2.4.71. [iglocska]
- Invalid key lookup for roaming in checkIfServerInSG() [iglocska]
- Invalid lookup for the queryversion. [iglocska]
- Fixed a typo in the previous commit. [iglocska]
- Remove sharing groups from json output if empty. [iglocska]
- Slight change of the related events format in the JSON to be more
  consistent. [iglocska]

  - Org and Orgc moved within the relatedEvent->Event
- Updated to the latest version of misp-galaxy. [Alexandre Dulaunoy]
- Fixed a small issue that could lead to a failed event push using
  sharing groups. [iglocska]
- Enforce the uuid creation on the UI. [iglocska]
- Enforce adding a UUID for external organisations too. [iglocska]

  - No need to support 2.3 any longer
- Default value for the tag exportable field added. [iglocska]
- Fixed the attribute level restsearch returning a weirdly formatted
  empty array. [iglocska]
- Do not echo password on misp-wipe. [Hannah Ward]
- History is now available via the API, fixes #2111. [iglocska]
- Whitelist entries being removed breaks the indexing of attribute
  arrays. [iglocska]

  - caused issues with JSON serialisation as lists turned into dicts
- Fixed an invalid JSON serialisation for restSearch. [iglocska]
- Minor issue - duplicate style tag, fixes #2106. [iglocska]
- CSRF issue when adding an attribute via the popover. [iglocska]
- Min width added to resolved attribute value. [iglocska]

  - looked terrible on low res screens
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Misp-taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Fixed issues with popups across the board for low res displays, fixes
  #2101. [iglocska]

  - Popups get scrollbars / realligned for potato resolutions
  - General cleanup of popup related functions in the JS
  - Added version querystring to the css files, no more ctrl+f5ing after some updates
- Removed ajax containers from views since they are already provided by
  the layout, fixes #1753. [iglocska]

  - resolves some issues with popups not showing up after certain actions
- Rearrange the data for adding proposals. [iglocska]

  - if no ShadowAttribute container is found, encapsulate the posted data
- NotFoundException when no events found by restSearch, fixes #2096.
  [iglocska]

  - changed to just return an empty set
    - returns {"request":[]} for events/restSearch
    - returns [] for events/restSearch
- Removed unused field from user edit view. [iglocska]
- Correction to previous commit. [iglocska]

  - correlations can now be disabled by site admins, no matter who created the event
- Allow disabling correlation for events not owned by the user if the
  user is a site admin. [iglocska]
- Freetext import shouldn't require the TLD containing warninglists to
  be enabled. [iglocska]

  - as long as it exists it will be used, no need to enable it any longer
- Fixed an issue where discarding a delegation request tried to redirect
  to the event view. [iglocska]

  - however, users lose access to the event once they discard the delegation request
  - redirects to the index instead now
- Managing Delegation Request - wrong organisation in popup fixed, fixes
  #2079. [iglocska]
- Missing JS file for the template file upload re-added, fixes #2084.
  [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Add blob in the url. [Raphaël Vinot]
- Major rewrite of the JSON schema. [Raphaël Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2112 from FloatingGhost/2.4. [Andras Iklody]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2091 from jhopp1e/patch-1. [Alexandre Dulaunoy]

  Update xINSTALL.centos6.txt
- Merge branch '2.4' into patch-1. [Alexandre Dulaunoy]
- Update xINSTALL.centos6.txt. [Justin Hopple]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2000 from devnull-/bulk-email. [Andras Iklody]

  Bulk email
- Add 'Precedence: bulk' in email header. [devnull-]
- Merge pull request #2 from MISP/2.4. [devnull-]

  Pull Update
- Merge branch '2.4' into 2.4. [devnull-]

v2.4.70 (2017-03-26)
--------------------

New
---
- Added 2 new types. [iglocska]

  - hex and sigma
- Sync logging to debug issues. [iglocska]
- Added a POST server connection test. [iglocska]

  - hopefully it should help debug some issues
- Update MISP from the diagnostics page. [iglocska]

  - right now it's pretty dumb, it simply pulls the same branch that the current user is on
  - Any failure is shown but not acted upon, if the git pull fails the user will see it but it needs to be resolved via the command line
- Allow for several attributes to be added in one go via
  /attributes/add. [iglocska]

  - Also a rework of the internals
  - All entry vectors are now handled the same way
  - syntax for adding several attributes is [{attribute1}, {attribute2}]
  - Sane defaults used automatically, making {"value":"1.2.3.4", "type":"ip-dst"} a valid attribute

Changes
-------
- Changed js query string. [iglocska]
- Version bump. [iglocska]
- Edit and delete attributes now accept uuids as parameters instead of
  IDs. [iglocska]
- Finished round 1 of all accessibility changes. [iglocska]
- Further work on the accessibility changes. [iglocska]
- Further progress. [iglocska]
- Further work on the accessibility changes. [iglocska]

Fix
---
- Spring cleaning. [iglocska]

  - removal of debug from the syncdebug
  - cleanup of the fixes that resulted from it
  - removal of the mangle sync from 2.4->2.3 (if you still have partners running 2 year old versions, time to notify them, stop syncing and unfriend on facebook)
- Potential fix for the sync issue. [iglocska]
- Some further fixes. [iglocska]

  - includes a fix to a compatibility test failure causing all instances to test as a legacy MISP
- Added missing ACL entry. [iglocska]
- Added missing popup view file. [iglocska]

  - Also added a new test string in a file for the POST connection test
- Fixed an issue with a notice error when adding a new attribute.
  [iglocska]
- Better error handling for partially failed attribute collection POSTs
  to /attributes/add. [iglocska]
- Missing echo caused the aria-label of import choices not to be
  populated properly, fixes #2038. [iglocska]
- Missing comma added. [iglocska]
- PyMISP to the latest version. [Alexandre Dulaunoy]
- Second round of accessibility changes. [iglocska]
- First round of Accessibility issues resolved with span links.
  [iglocska]

Other
-----
- Merge branch 'syncdebug' into 2.4. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2073 from deloittem/2.4. [Andras Iklody]

  Manage attributes IP-SRC|PORT and IP-DST|PORT when exporting nids rules
- Manage the new attributes IP-SRC|PORT and IP-DST|PORT when exporting
  NIDS rules. [Mathieu Deloitte]
- Merge pull request #2069 from deloittem/2.4. [Andras Iklody]

  All tag cannot be included in export functions such as suricata rules
- New variable includeAllTags added to NIDS export: even not exportable
  tags could be included in NIDS export. [Mathieu Deloitte]
- Merge pull request #2068 from ppanero/regex_bugfix. [Andras Iklody]

  testForPath regex fixed in Server.php
- TestForPath regex fixed in Server.php. [Pablo Panero]
- Merge pull request #2057 from RichieB2B/nscs-nl/wipe. [Alexandre
  Dulaunoy]

  misp-wipe.sh fixes
- Merge branch '2.4' into nscs-nl/wipe. [Alexandre Dulaunoy]
- Merge pull request #2055 from dspruell/riskiq_logo. [Andras Iklody]

  Riskiq logo
- Remove logo path (probably unneeded to have added to .gitignore)
  [Darren Spruell]
- Add org logo for RiskIQ. [Darren Spruell]
- Merge pull request #2056 from RichieB2B/ncsc-nl/perm-sightings.
  [Andras Iklody]

  Add perm_sighting to initial database and roles
- Add perm_sighting to initial database and roles. [Richard van den
  Berg]
- Merge branch '2.4' into nscs-nl/wipe. [Alexandre Dulaunoy]
- * misp-wipe.sh does not backup, so no outputdir is needed * clear data
  model cache upon wiping misp. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1984 from SekoiaLab/feature/serversApi. [Andras
  Iklody]

  Adds an api to add and edit servers in MISP
- Feature: Adds the api support to ServersController to edit servers.
  [Sebastien Quioc]
- Refactor(controllers): adds checks for input parameters before editing
  a server. [Sebastien Quioc]
- Feature: Adds the api support to ServersController to add new servers.
  [Sebastien Quioc]
- Merge pull request #2049 from sebdraven/2.4. [Andras Iklody]

  add impfuzzy
- Add impfuzzy. [Sébastien Larinier]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]

v2.4.69 (2017-03-10)
--------------------

Changes
-------
- Some changes to the users. [iglocska]

  - added date created/modified in the backend
  - added date created in the users index
  - passowrd reset for a user now shows a warning if no pgp/smime key are set and the user might not be getting the email
- PyMISP update. [iglocska]

Fix
---
- Version bump. [iglocska]
- Fixed a typo in an upgrade script. [Iglocska]
- Readded the failing entry caused by a typo in the upgrade system.
  [iglocska]
- JS version bump. [iglocska]
- Fixed the upload of proposal attachments via the data field, fixes
  #2037. [iglocska]
- Changed the main misp js file name and switched to using query strings
  to invalidate cached versions on update. [iglocska]

  - stops MISP from disclosing the version string on the login page

  - as reported by Tien Phan and David Maciejak of Fortinet's FortiGuard Labs
- Removed the loading of the main js file from the login page.
  [iglocska]

  - stops MISP from disclosing the version string on the login page

  - as reported by Tien Phan and David Maciejak of Fortinet's FortiGuard Labs
- Tightened sanitisation in some view elements - on the index filter
  tool - organisation landing page. [iglocska]

  as reported by Tien Phan and David Maciejak of Fortinet's FortiGuard Labs
- Tightened sanitisation in some view elements - on the index filter
  tool - organisation landing page. [iglocska]

  as reported by Tien Phan and David Maciejak of Fortinet's FortiGuard Labs.
- Fixed an issue that could under certain conditions lead to empty
  events being pushed when synchronising. [iglocska]
- Removed unnecessary implode() code. [David Maciejak]
- Normalised the attirbutes/add and attributes/edit apis. [iglocska]
- Fixed a potential issue causing the attribute validation to fail.
  [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #2033 from rmarsollier/2.4. [Andras Iklody]

  minor bugfix on TagsController.php
- Minor bugfix on TagsController.php. [rmarsollier]
- Merge pull request #2019 from dmaciejak/patch-1. [Andras Iklody]

  fix: remove unnecessary implode() call
- Merge pull request #2031 from deloittem/2.4. [Andras Iklody]

  Suricata export update
- Only display the tag name if the array contains values (depending if
  the tag is exportable or not) [Mathieu Deloitte]
- Add the attribute tags to the msg field (Suricata rule) to sort easier
  the raised alerts. [Mathieu Deloitte]
- Initialize host to empty value when the URL is formed incorrectly.
  [Mathieu Deloitte]

v2.4.68 (2017-03-08)
--------------------

New
---
- Added float as a new attribute type. [iglocska]
- Added a way to upload org logos directly from the org add/edit view.
  [iglocska]
- Enable sync permission for read only accounts. [iglocska]
- Added a way to disable cached exports server wide for low disk space
  instnaces. [iglocska]

  - But please consider just adding some more space instead..

Changes
-------
- Added some language clarifying the filter rule relations, fixes #2011.
  [iglocska]
- Cakephp updated. [iglocska]
- PyMISP updated. [iglocska]
- Quick deletion of events. [iglocska]

  - uses prepared statements instead of the framework's cascading delete
  - utterly massive performance boost
- Add the version number to the headers for sync requests. [iglocska]

Fix
---
- Fixed sql fail. [iglocska]
- AttachTagToObject and removeTagFromObject now accept posted JSON
  objects. [iglocska]
- Fixed some default value issues with taxonomy colours. [iglocska]
- Several blacklist related fixes. [iglocska]

  - turned the functionality to a default on feature
  - added indexes
  - fixed some default values
- Added default value to proposal_to_delete. [iglocska]
- Additional logging when an attribute can't be added. [iglocska]
- Misp-taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Typo fixed. [iglocska]
- Missing file added. [iglocska]
- Some ACL tightening. [iglocska]
- PushProposals requires that the user has perm_add permissions.
  [iglocska]
- Potential fix for a weird issue blocking the editing of users, fixes
  #1992. [iglocska]
- Fixed an issue with the baseurl diagnostic. [iglocska]
- Added missing network indicators to the network filter tab in the
  event view. [iglocska]
- Truncating the title of a log entry at 65KB for some pretty rare edge
  cases. [iglocska]
- Misp-galaxy updated to the latest version. [Alexandre Dulaunoy]
- Relaxed TLD validation for hostname|port, domain|ip, jabber-id, fixes
  #1977. [Iglocska]
- Allow the disabling of the correlation of an event / attribute on
  event add, fixes #1991. [iglocska]
- Fixed several issues with the sightings. [Iglocska]

  - Main issue was the expensive and potentially large query used to find all sightings for a list of tags (used on the tag and galaxy cluster index)

  potentially fixes #1993

Other
-----
- Merge branch 'hotfix-2.4.68' into 2.4. [iglocska]
- Version bump. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch 'feature/readonlysync' into 2.4. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1996 from kx499/2.4. [Andras Iklody]

  Updated comment for enrichment modules to reference value used for enri…
- Updated comment for enrichment modules to refence value used for
  enrichment for added context. [kx499]
- Merge pull request #2002 from ppanero/branch_cleanup. [Andras Iklody]

  bro to_IDS and published flags fix on query. Now supporting block_eve…
- Bro to_IDS and published flags fix on query. Now supporting
  block_event_proposals. [ppanero]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]

v2.4.67 (2017-02-24)
--------------------

New
---
- Add reverse proxy support for test of baseurl. [Adrien RAFFIN]
- Added activity charts to tag and galaxy cluster indeces. [iglocska]

  - bunch of small improvements additionally
- Added advanced sightings and sparkline to the event itself. [iglocska]
- User management convenience functions added. [iglocska]

  - quick e-mail: send an e-mail to a user quickly
  - orgadmin: see the org admins of a user and contact them
  - pgp key issues shown on the user view
  - pgp fingerprint shown on the user view
  - copy paste auth keys and pgp keys quickly by clicking on them
- Added PGP fingerprint and PGP key status to user view. [iglocska]
- Sightings column added to sightings table. [iglocska]

Changes
-------
- Removed superfluous style. [iglocska]
- On event create page add a notice #1973. [iglocska]
- Added warnings about the user's encryption status in the quick mailer.
  [iglocska]
- Better error message for invalid types when posting sightings.
  [iglocska]

  - sent before doing the lookup against existing attributes
- Made the role add/edit forms a bit more sane. [iglocska]

  - allow for some permissions to be given out to read only users
  - hide the permissions that can't be selected for the given access level
- Sightings role added to ACL. [iglocska]

Fix
---
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- More invalid MySQL fields fixed. [iglocska]
- Fixed a mysql issue. [iglocska]
- PyMISP updated. [Alexandre Dulaunoy]
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- Fixed an issue displaying events without sghting data. [iglocska]
- Added a fix to growing arrays in the ApacheSecureAuth settings, fixes
  #1981. [iglocska]
- Relaxed the TLD validation for domains / hostnames, fixes #1977.
  [iglocska]
- Typo fixed in the advanced add sighting interface, fixes #1975.
  [iglocska]
- Fixed some visual issues with the attribution/targeting data warning
  in add attributes. [iglocska]
- Some fixes for the new user admin features. [iglocska]
- Mergeing removal of deprecated JS in the new role creation. [iglocska]
- Small fix for an invalid error message in the sightings. [iglocska]
- Throw an error if the local feed file is not found. [iglocska]
- Re-added the accidentally removed code in a merge, fixes #1965.
  [iglocska]

  - affects f0e1a27b7dca2e6d36f904ef52d4976649ccefa3
- Added validation for sighting type and fixed responses for adding
  sightings. [iglocska]

Other
-----
- Version bump. [iglocska]
- Merge branch '2.4.67' into 2.4. [iglocska]
- Merge branch '2.4' into 2.4.67. [iglocska]
- Merge pull request #1988 from RichieB2B/ncsc-nl/misp-wipe. [Andras
  Iklody]

  Script to wipe (reset) a MISP installation
- Clear tables that can be re-populated. [Richard van den Berg]
- Additional table wipes. [Richard van den Berg]
- Remove unneeded config.php variables, keep user 3. [Richard van den
  Berg]
- Added misp-wipe.sh. [Richard van den Berg]
- Merge pull request #1982 from ppanero/patch-2. [Andras Iklody]

  Update Server.php
- Update Server.php. [Pablo Panero]

  Duplicate entry of property
- Merge pull request #1980 from SteveClement/2.4. [Andras Iklody]

  Minor update to start.sh
- - Added root check - Added comment about bash quirk. [Steve Clement]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #1971 from SekoiaLab/feature/AddAuthkeyAtCreate.
  [Andras Iklody]

  feature: Add support for user creation with authkey
- Feature: Add support for user creation with authkey. [Adrien RAFFIN]
- Merge pull request #1972 from
  SekoiaLab/feature/ImproveReverseProxyChecks. [Andras Iklody]

  new: Add reverse proxy support for test of baseurl
- Merge pull request #1974 from ppanero/patch-1. [Andras Iklody]

  Update README.md
- Update README.md. [Pablo Panero]

  Updated readme with apache config for API/Syncs filtering from SSO
- Merge branch '2.4' into 2.4.67. [iglocska]
- PyMISP updated. [iglocska]
- Merge branch '2.4' into 2.4.67. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1967 from truckydev/2.4. [Andras Iklody]

  Code for issue : https://github.com/MISP/MISP/issues/1965
- Code for issue : https://github.com/MISP/MISP/issues/1965. [truckydev]

v2.4.66 (2017-02-19)
--------------------

New
---
- Added links to all events that match sightings sources in the
  sightings top list. [iglocska]
- Added sighting top list to the statistics. [iglocska]
- Various fixes to the sightings. [iglocska]

  - sparkline got its own column
  - delete sightings in the sighting details
- First revision of the new sightings system. [iglocska]
- First iteration of the improved sightings. [iglocska]

Changes
-------
- Work on the sightings. [iglocska]
- Added default to shadow_attributes old_id. [iglocska]

Fix
---
- Fixed an issue that prevented < 2.4.63 from being upgraded to the
  latest version. [Iglocska]
- Version bump 2.4.66. [Alexandre Dulaunoy]
- Added eventids to the toplist API. [iglocska]
- Left off view file added. [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- Sightings are in fact not galaxies (heading changed) [iglocska]

  - derp
- Fixed a JS error causing a feed edit to not populate the filter
  popover, fixes #1959. [iglocska]
- Fixed some permission issues preventing non site admins from using
  some functionalities correctly. [iglocska]
- ACL updated. [iglocska]
- Enforce longer value fields on the event view. [iglocska]
- Added missing column in MYSQL.sql and some indexing. [iglocska]
- Typo. [iglocska]
- MYSQL.sql brought up to date. [iglocska]
- Changed name of the activity sparkline graphs. [iglocska]
- Fixed an annoying effect when adding a sighting. [iglocska]

  - also, js file renamed to current version
- Fixed an issue with the advanced correlation. [iglocska]
- Fixed some view issues with the sightings. [iglocska]
- Execute the cach cleaning before the indexing too. [iglocska]
- Fixed a possible issue with the upgrade mechanism. [iglocska]

  - indexer expecting new indeces
- IP:port attribute types should not be line separated. [iglocska]
- Execute upgrade script. [iglocska]
- Several fixes to the new sightings. [iglocska]
- Some bug fixes. [iglocska]
- Added composer's license. [iglocska]
- Update default field of organisation when creating new accounts.
  [Adrien RAFFIN]
- Changed installation behaviour of composer. [iglocska]

  - no longer requires the live download and execution of the composer package
    - compromising https://getcomposer.org/ could lead to RCE for new MISP installations during the installation

  - As reported by Trey Darley (@treyka)
- Urlencode the user's event list lookup to prevent oddities. [iglocska]
- Fixed a bug with the freetext import that broke the detection of IP
  addresses. [iglocska]
- Added correct recognition of ip:port indicators to the freetext import
  tool, fixes #1919. [iglocska]
- Added (dot) to the refanging. [iglocska]
- Incorect IF statment in app/Model/AppModel.php, fixes #1891.
  [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch 'feature/enhanced_sightings' into 2.4. [iglocska]
- Merge branch '2.4' into feature/enhanced_sightings. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into
  feature/enhanced_sightings. [iglocska]
- Merge pull request #1958 from devnull-/ssl_client. [Andras Iklody]

  Client SSL Certificate Authentication improvements
- Clean & improve README.md of CertAuth. [devnull-]
- Don't login or create an empty account if the user doesn't exist.
  [devnull-]
- Missing 'the' in comment. [devnull-]
- Add details in client SSL authentication comments. [devnull-]
- Merge pull request #1 from MISP/2.4. [devnull-]

  Update fetch upstream
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1955 from treyka/patch-3. [Andras Iklody]

  remove spurious php5-xml
- Remove spurious php5-xml. [Trey Darley]

  php5-xml is not a separate package; it's included with libapache2-mod-php5.
- Merge pull request #1942 from Deventual/patch-5. [Andras Iklody]

  fixed install instructions
- Update INSTALL.debian7.txt. [Deventual]
- Fixed install instructions. [Deventual]

  Added php-xml, without it this issue can rise:
  Class 'DOMDocument' not found in [/var/www/MISP/app/Lib/cakephp/lib/Cake/Utility/Xml.php
- Merge pull request #1944 from Deventual/patch-7. [Andras Iklody]

  fixed install instructions
- Fixed install instructions. [Deventual]

  Added php-xml, without it this issue can rise:
  Class 'DOMDocument' not found in [/var/www/MISP/app/Lib/cakephp/lib/Cake/Utility/Xml.php
- Merge pull request #1945 from Deventual/patch-8. [Andras Iklody]

  Fixed install instructions
- Fixed install instructions. [Deventual]

  Added php-xml, without it this issue can rise:
  Class 'DOMDocument' not found in [/var/www/MISP/app/Lib/cakephp/lib/Cake/Utility/Xml.php
- Merge pull request #1943 from Deventual/patch-6. [Andras Iklody]

  fixed install instructions
- Fixed install instructions. [Deventual]

  Added php-xml, without it this issue can rise:
  Class 'DOMDocument' not found in [/var/www/MISP/app/Lib/cakephp/lib/Cake/Utility/Xml.php
- Merge pull request #1937 from Deventual/patch-4. [Andras Iklody]

  Fixed install instructions
- Fixed install instructions. [Deventual]

  Added php-xml, without it this issue can rise:
  Class 'DOMDocument' not found in [/var/www/MISP/app/Lib/cakephp/lib/Cake/Utility/Xml.php
- Merge pull request #1936 from Deventual/patch-3. [Andras Iklody]

  fixed install instructions
- Fixed install instructions. [Deventual]

  Added php-xml, without it this issue can rise:
  Class 'DOMDocument' not found in [/var/www/MISP/app/Lib/cakephp/lib/Cake/Utility/Xml.php
- Merge pull request #1941 from SekoiaLab/fix/organisation. [Andras
  Iklody]

  fix: update default field of organisation when creating new accounts
- Merge pull request #1912 from deloittem/2.4. [Andras Iklody]

  NidsSuricataExport refactoring for attribute *URL*
- Merge branch '2.4' into 2.4. [Alexandre Dulaunoy]
- NidsSuricataExport refactoring for attribute *URL* [Mathieu Deloitte]
- Merge pull request #1928 from cvandeplas/2.4. [Andras Iklody]

  eventview - cluster id fields
- Eventview - cluster class field. [Christophe Vandeplas]

  use class instead of id
- Eventview - cluster id fields. [Christophe Vandeplas]

  Allows custom CSS to manage the cluster info fields. (example: #cluster_country { display: none; } )
- Merge pull request #1924 from RichieB2B/nscs-nl/sudo. [Alexandre
  Dulaunoy]

  Add sudo for cp logrotate
- Add sudo for cp logrotate. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Update PyMISP. [Raphaël Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Update PyMISP. [Raphaël Vinot]

v2.4.65 (2017-02-09)
--------------------

Changes
-------
- Allow the creation of read only auth users/auditors. [iglocska]

  - also add creator email to json output for auditors

Fix
---
- Fixed the new indexer generating a notice on a successful indexing.
  [iglocska]
- Import whitelist - add a description to make it clearer, fixes #1902.
  [iglocska]
- Labels in Add/Edit feed, fixes #1913. [iglocska]
- Remove possible duplicate entries coming from a freetext feed import.
  [iglocska]

  - Since we use saveMany() for saving attributes from the freetext/csv feed import the unique attribute constraint was ineffective
  - The constraint checks if the event already has a similar type/category/value combination

  - TODO: Refactor this, each insert is also an expensive non buffered SELECT query besides the correlation creation!
- Fix several strict issues. [iglocska]
- Fix to the advanced correlation when no hits are found. [iglocska]
- API request : "An Internal Error Has Occurred." if no Thread for an
  event fixes #1900. [iglocska]

  - also, some cleanup of the eventView api
- Fix to a strict mySQL issue with the feed table. [iglocska]
- Fixed several issues with the indexer in the upgrade algorithm.
  [iglocska]

  - also, rerun the recent indexing rules

Other
-----
- Version bump. [iglocska]
- Merge branch 'auditor' into 2.4. [iglocska]
- Merge branch '2.4' into 2.4. [truckydev]
- Check if auditor have good "org_id" [truckydev]
- Merge branch '2.4' into 2.4. [truckydev]
- Get email creator user for auditor users. [Tristan METAYER]
- Add auditor user        auditor user can see event_creator_id.
  [Tristan METAYER]

v2.4.64 (2017-02-06)
--------------------

New
---
- Lookup organisations by uuid using organisations/view. [iglocska]
- Advanced correlations. [iglocska]

  - experimental feature, correlate on CIDR
  - can be turned on/off in the server settings
  - For the emperor
- Added mass tagging to attributes on the event view. [iglocska]

  - Oooh yes.
- New setting to sanitise attributes on delete. [iglocska]

  - if enabled server wide, any delete of an attribute will not just set the deleted flag, but also sanitise the content fields
  - fields sanitised: category, type, value, comment, to_ids
- Send out credentials directly during user creation. [iglocska]
- Added API access to the statistics. [iglocska]

  - first iteration, this is a bit more complex to get it right than this implementation
  - data cleanup to make the results somewhat more useful
  - raw data needs to be documented

  - available APIs:
    - /users/statistics/data.json
    - /users/statistics/orgs.json
    - /users/statistics/tags.json
    - /users/statistics/attributehistogram.json

Changes
-------
- Version bump. [iglocska]
- Added default log org entry. [iglocska]
- Added ids to the server index. [iglocska]

Fix
---
- Fixed a bug retrieving an org with no users. [iglocska]
- MISP galaxy updated. [Alexandre Dulaunoy]
- MISP taxonomy to the latest version. [Alexandre Dulaunoy]
- Fixes an issue with tags missing on push. [iglocska]
- Fixes to several issues with the setting change upgrade hooks.
  [iglocska]

  - also removed the not null restriction from a problematic field with no default entry, fixes #1853
- Set IDS flag for all attributes added via Email Import module fixes
  MISP/misp-modules#98. [iglocska]
- Added default values for some problematic log columns. [iglocska]
- Simplification of the proposal sync. [iglocska]
- Warning-list for empty hashes doesn't work on malware-sample even if
  the warning list is for ALL, fixes #1837. [iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1896 from RichieB2B/ncsc-nl/logrotate. [Andras
  Iklody]

  Add logrotation for MISP workers output
- Add logrotation for MISP workers output. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1888 from RichieB2B/ncsc-nl/permissions-comment.
  [Andras Iklody]

  Clarify permissions, see #1886
- Clarify permissions, see #1886. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1886 from cvandeplas/text_export. [Andras Iklody]

  attributes/text - optionally export attributes from not published events
- Attributes/text - optionally export attributes from not published
  events. [Christophe Vandeplas]
- Merge branch 'feature/passwordSending' into 2.4. [iglocska]

v2.4.63 (2017-02-01)
--------------------

New
---
- Small rework of the thread functionalities. [iglocska]

  - API get /threads/view/<thread_id> and /threads/viewEvent/<event_id>
  - Added new setting to show post count on the event index including a notification if it has a post newer than 24 hours
- Add and remove tags from object by uuid. [iglocska]

  - /tags/attachTagToObject/uuid/tag
  - /tags/removeTagFromObject/uuid/tag

  - tag can be tag ID or tag name (must be an exact match)
  - Affects events and attributes

Changes
-------
- Changes to the email notification. [iglocska]

  - added attribute tags
- Version bump and changed default session engine to php. [iglocska]
- Misp-galaxy update. [iglocska]

Fix
---
- Fixing a notice introduced in the last commit. [iglocska]
- Warning list updated to the latest version. [Alexandre Dulaunoy]
- Composite attributes displayed in 2 lines. [iglocska]
- Fixed a bug causing CSRF issues for tag removal. [iglocska]

  - at least I hope it did for others.
- Added missing view file, some small fixes, pymisp version bump.
  [iglocska]
- Added new functionality to the ACL. [iglocska]
- Cosmetic copy pasta issue fixed. [iglocska]
- [misp-galaxy] updated to the latest version including ransomware.
  [Alexandre Dulaunoy]
- Fixed an attribute type description. [iglocska]
- Removing tags now spans its own CSRF tokens in the confirmation popup.
  [iglocska]

  - fixes some CSRF issues
  - improves rendering performance
- Galaxy source should act as a link if a link is provided. [iglocska]
- Remove the admin setting changes too using the prune job. [iglocska]
- Fix and cleanup script for a specific bug. [iglocska]

  - rare occurance, but some MISP servers enter an upgrade loop causing massive amounts of log entries
  - this patch cleans up the bug preventing further upgrade loops as well as offers a script to clean up the fallout
- Fixed a bug that didn't correctly handle validation errors on the
  attribute add popup, fixes #1875. [iglocska]
- Removed malware-sample and attachment from the attribute type options.
  [iglocska]

  - should not be possible to select these via the add/edit attribute functions
- Fixed various tagging issues. [iglocska]

  - event tag when editing an event wasn't added correctly
  - tags that were not exportable returned weird empty lists via the API

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch 'feature/db_fix' into 2.4. [iglocska]

v2.4.62 (2017-01-26)
--------------------

New
---
- Added the option to delete files after ingestion of local feed.
  [iglocska]
- Local feeds. [iglocska]

  - still needs testing
- Added two new parameters for the attribute restsearch. [iglocska]

  - to_ids, with the following options
    - false (default): include all attributes, no matter the to_ids flag
    - true: include only to_ids attributes
    - "exclude": exclude attributes marked to_ids

  - deleted with the following options
    - false (default): only include non deleted attributes
    - true: include deleted attributes
    - "only": ONLY include deleted attributes

Changes
-------
- Version bump. [iglocska]
- Added validation errors for a local feed pointing to the wrong
  resource. [iglocska]

  - should be a file for non misp feeds
  - should be a directory for misp feeds

Fix
---
- PyMISP version bump. [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- Fixed an invalid lookup for the site admin debug. [iglocska]
- Fixed an issue where setting site admin debug to false resulted in a
  critical warning. [iglocska]
- Empty delimiter for CSV feeds causing grief. [iglocska]
- Fixed an issue that prevented a feed to be convertable between types.
  [iglocska]
- Fixed an issue with the feed url validation. [iglocska]
- Fixed an old bug returning an invalid feed pull result. [iglocska]

  - no new events / nothing to update returned an error before
- Views left off. [iglocska]

Other
-----
- Merge branch 'feature/localfeeds' into 2.4. [iglocska]
- Merge branch '2.4' into feature/localfeeds. [iglocska]
- Add: Code of conduct added to the MISP Project - fix #1858. [Alexandre
  Dulaunoy]
- Add: Code of conduct added to the MISP Project - fix #1858. [Alexandre
  Dulaunoy]
- Merge pull request #1860 from RichieB2B/ncsc-nl/brobesitas. [Alexandre
  Dulaunoy]

  Truncate bro cached export files
- Truncate bro cached export files. [Richard van den Berg]

v2.4.61 (2017-01-22)
--------------------

New
---
- New warninglist type: hostname. [Iglocska]

  - use lists designated as hostname lists (which can be domains too)
- Allow the new type "substring" to be used for warninglists. [Iglocska]

Changes
-------
- Version bump. [Iglocska]
- Updated warninglists. [Iglocska]
- Nicer screenshot view. [Iglocska]
- Click a screenshot to expand/collapse it. [Iglocska]
- Updated the warninglists. [Iglocska]
- Warninglists updated. [Iglocska]

Fix
---
- Fixed the hacky solution for hostname evaluation in warninglists.
  [Iglocska]
- Critical fix to an issue with event add fixed. [Andras Iklody]

  - a reuse of a pointer causes an invalid duplication of an attribute on entry, leading to the last attribute being dropped
- Fixed the org edit API. [Iglocska]

  - it only worked if all fields were set
  - switched to a different strategy where any changed field is updated
- Badges, badges and more badges! [Alexandre Dulaunoy]
- Badges more badges! [Alexandre Dulaunoy]
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- Organisation UI and API improvements. [Iglocska]

  - opened up the organisations controller to API actions
    - this includes index/add/edit/delete
    - uses the still new-ish standardised REST library
    - send GET requests to add/edit to view the parameters

  - reworked the org index to paginate 60 items instead of 20 and to have a view all button
- Fixed an issue that erroneously updated the date of an org creation on
  edit. [Iglocska]
- Just force utf8 encoding if it's not set. [Iglocska]
- Added a warning if utf8 encoding isn't set up in the database config.
  [Iglocska]

  - also, changed the default database config to enforce utf8
- Do the centering after the screenshot is shown. [Iglocska]

  - otherwise it returns 0 as the width
- Left off css changes. [Iglocska]
- Whois-registrant-email added as type when an email is detected in
  freetext. [Alexandre Dulaunoy]
- ACL updated for attribute level tagging. [Iglocska]
- Don't try to add the attribute tag field to proposals. [Iglocska]
- Andreas Ziegler significant contribution acknowledged in Copyright.
  [Alexandre Dulaunoy]
- Temporary fix for no relatedattributes producing an empty string
  instead of an empty array in the retrieved data. [Iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1857 from deralexxx/patch-6. [Alexandre Dulaunoy]

  Updating Authors to add Andreas
- Updating Authors to add Andreas. [Alexander J]

  and myself as well
  https://github.com/MISP/MISP/commit/ce5973f273420ef602a1c577f35927823014e17b
- Merge pull request #1856 from deralexxx/patch-5. [Andras Iklody]

  Small UI patch to make users aware to upload *.pem files
- Update add.ctp. [Alexander J]
- Update edit.ctp. [Alexander J]

  (*.pem) https://github.com/MISP/MISP/issues/1246
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- [misp-galaxy] - latest version included. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]

v2.4.60 (2017-01-17)
--------------------

New
---
- Request encryption of samples via the event REST api. [iglocska]

  - Add the encrypt flag to attributes to be added via the events/add or events/edit api
  - simply add "encrypt": true to the attributes that have a sample attached in the "data" field
  - make sure that the attribute value is the desired filename, the hashes will be added automagically
- Add a new api to check the supported PyMISP version. [iglocska]
- Index API for sightings added. [iglocska]
- Sightings API improvements :construction:. [iglocska]

  - reworked responses
  - started work on the new index
- Show attributetags on sync event preview. [Andreas Ziegler]
- Show attributetags on api calls for single attributes. [Andreas
  Ziegler]
- Show usage count of an attributetag in tag list. [Andreas Ziegler]
- Show usage count of an attributetag in taxonomies detail view.
  [Andreas Ziegler]
- Search for attributetag by clicking on one. [Andreas Ziegler]

  including major reorganisation of attributes search() method
- Add&remove attributetags on event view. [Andreas Ziegler]
- Add search&result for attributetags. [Andreas Ziegler]
- Add findAttributeIdsByAttributeTagNames() to Tag Model. [Andreas
  Ziegler]
- Show attributetags on event view. [Andreas Ziegler]
- Show attributetags on attribute index. [Andreas Ziegler]
- Add config options for attribute tagging. [Andreas Ziegler]
- Add AttributeTag. [Andreas Ziegler]
- Add table attribute_tags on updates to 2.4.53. [Andreas Ziegler]
- Add sql for attribute_tags (PostgreSQL) [Andreas Ziegler]
- Add sql for attribute_tags (MySQL) [Andreas Ziegler]

Changes
-------
- Use cakeresponse for JSON response in updateGraph instead of
  serialize. [Iglocska]
- Update of the JS filename. [Iglocska]
- Version bump. [Iglocska]
- Some UI love. [Iglocska]

  - back button fixed on tag selection popup
  - esc now closes popup forms / field edits
- Allow disabling/enabling publishing of events imported via the UI,
  fixes #1845. [Iglocska]
- Updated the taxonomies. [Iglocska]
- Description of session.timeout updated. [Iglocska]
- Added event ID to the attribute level tags. [iglocska]
- Made the attribute level tagging mandatory. [iglocska]

  - despite my earlier request to @rotanid, there is no need for this feature to be optional, it's one of the few cases where it should be universally enabled

Fix
---
- Fix a unicode issue with the correlation graphs. [Iglocska]
- Fix an issue with the graphs when no relations are found. [Iglocska]
- Clarification a selectable group is also an active group. [Alexandre
  Dulaunoy]

  or an active group is also selectable.
- Epic fail due to missing brackets. [Iglocska]

  - mimicing Apple's gotofail well.
- Some UI love. [Iglocska]
- Update the attribute timestamp on attaching/removing tags. [Iglocska]
- Unpublish event when adding/removing an attribute tag. [Iglocska]

  - also show the event being unpublished immediately
- Fixed some issues with the galaxies that got broken. [iglocska]
- Fixed some issues with the addTag/removeTag APIs. [iglocska]
- Fixed an issue that prevented tas to be added from attributes.
  [iglocska]

  - whenever the "all" taxonomy was chosen
- Further merge fixes. [iglocska]
- Merge issue fixed. [iglocska]
- Cleaner fix, testBool doesn't need to run testForEmpty. [Iglocska]
- Don't show value not set on boolean false values that are actually set
  in the server settings. [Iglocska]
- Disable_correlation not updated using the events/edit api. [Iglocska]
- Edit events by uuid instead of id, fixes #1842. [Iglocska]
- Only allow malware-samples to be created using the upload_sample api,
  fixes #1843. [Iglocska]

  - contrary to the documentation, setting the IDS flag decided the type of the resulting upload (malware-sample vs attachment)
  - attachments can easily be created without any black magic using the add attribute api anyway

  - also fixed a bug that prevented the timestamp of events receiving a sample via the upload_sample api from being re-timestamped
- [misp-taxonomies] updated to the latest version. [Alexandre Dulaunoy]
- [misp-warninglists] updated to the latest version. [Alexandre
  Dulaunoy]
- Cannot list users in own org - but button to do so is shown #1749.
  [iglocska]

  - normal users saw the option to see their own orgs' users but clicking the button resulted in an exception caused by the ACL
  - fixed a bug that caused the button to show up in the first place
- Fixed an issue with an empty SMIME field preventing users from being
  added, fixes #1821. [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- Debug alert removed. [iglocska]
- Copyright dates updated. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- Added sightings index to the ACL. [iglocska]
- Fixed some UI issues. [iglocska]
- Fixed an issue where the published field would disappear on the event
  view. [iglocska]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] Galaxy updated to the latest version. [Alexandre
  Dulaunoy]
- [misp-galaxy] New clusters exploit-kit and TDS added. [Alexandre
  Dulaunoy]
- Small UI issue fixed. [Iglocska]
- Fixed some UI issues with the correlation status on the event view.
  [Iglocska]
- Fix empty space issues with server settings. [Iglocska]

  - on input trim the string
  - on the not empty check, first trim the string to warn users about existing issues
- Show that an event is unpublished when you accept a proposal, fixes
  #1763. [iglocska]

  - we've had the system for a while for adding tags already anyway
- Fixed the editing of tags using the rest API. [iglocska]
- Merge issues fixed. [iglocska]
- Create attributetags during import of attributes. [Andreas Ziegler]
- Prepare attributetags in import data. [Andreas Ziegler]
- Export attributetags as Tag elements (like eventtags) [Andreas
  Ziegler]

Other
-----
- Merge branch 'feature/attribute-tagging' into 2.4. [Iglocska]
- Merge branch '2.4' into feature/attribute-tagging. [Iglocska]
- Merge branch '2.4' into feature/attribute-tagging. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1834 from mdtro/patch-1. [Andras Iklody]

  Fixed typo in dependency installs
- Fixed typo in dependency installs. [mdtro]

  rh-php56-bcmath should be rh-php56-php-bcmath
- Merge pull request #1833 from BenDrysdale/2.4. [Andras Iklody]

  Fixed typo in xINSTALL.centos7.txt
- Fixed typo in xINSTALL.centos7.txt. [Ben Drysdale]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1815 from Rafiot/travis. [Raphaël Vinot]

  Fixing travis
- Update pymisp. [Raphaël Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' into feature/attribute-tagging. [iglocska]

v2.4.59 (2017-01-01)
--------------------

New
---
- Added a new field for an exclude regex for the CSV / Freetext feeds.
  [iglocska]

  - just set a php compatible PCRE regex pattern to exclude values
- Added feed metadata download link. [iglocska]
- Various new feed features. [iglocska]

  - import feed descriptor json pastes to add a list of pre-defined feeds
  - improvements to the feed pull (a single non validating attribute shouldn't break the process)
  - altered the saving of the attributes to happen in chunks during a feed pull to avoid very large feeds from stalling the process
  - split the feeds into 3 tabs: default, custom, all
- Added caching and pagination to freetext/csv feeds. [iglocska]
- Added session settings to the server settings. [iglocska]

  - also, new method for writing the MISP config file

Changes
-------
- Version bump. [iglocska]
- Changed the feed cache locations. [iglocska]
- Added description for feed metadata download. [iglocska]
- Added colour fields to sql files. [iglocska]
- Colour field backticks removed. [iglocska]
- Added colour fields to taxonomies. [iglocska]
- View the feed index via the API (to easily extract / share the
  settings) [iglocska]

Fix
---
- Copy paste fail. [iglocska]
- Left off changes to the complextypetool. [iglocska]

  - oops
- Fixed a copy paste bug and the default feed index scope. [iglocska]

  - defaults to all feeds now
- Fix to several issues with the feeds: [iglocska]

  - settings (csv column number, delimiter) were ignored
  - skipped fields were still counted by the paginator showing some pages with fewer than the expected 60 values
- Setting naming consistency fail. [iglocska]

  - separator != delimiter
- Fixed some minor issues with the feed import. [iglocska]
- Updated the ACL. [iglocska]
- Added rest response to the importFeeds method. [iglocska]
- Fixed the colour settings for taxonomies. [iglocska]
- Updated to the latest version of the galaxy. [Alexandre Dulaunoy]
- Org field missing in log entry causing proposal sync to fail.
  [iglocska]

  - Added SYSTEM as the default value
- Allow users to fetch their PGP keys. [iglocska]
- Updated to the latest version of misp galaxy. [Alexandre Dulaunoy]
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- Show additional flags for non MISP feeds. [iglocska]
- Fixed a new issue introduced in ajax response handling. [iglocska]
- Invalid element load while browsing the galaxies, fixes #1752.
  [iglocska]

  - was hard to spot at first, but indeed the bug is as described in the issue and masked by an ajax load of the contents
- Only show related events in red if it's created by the same org, fixes
  #1528. [iglocska]

  - was using the local owner id instead of the creator id

Other
-----
- Merge branch '2.4.59' into 2.4. [iglocska]
- Merge branch '2.4' into 2.4.59. [iglocska]
- Merge branch 'feature/colour' into 2.4.59. [iglocska]
- Merge pull request #1786 from RichieB2B/ncsc-nl/fix-fuzzy. [Andras
  Iklody]

  Fix STIX exports for malware-sample attributes
- Fix STIX exports for malware-sample attributes. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1784 from SteveClement/patch-1. [Andras Iklody]

  Broken Image Typo
- Broken Image Typo. [Steve Clement]

  Remove bang (!) so it doesn't get interpreted as an image.

v2.4.58 (2016-12-22)
--------------------

New
---
- Disable correlation. [iglocska]

  - globally
  - on an event level
  - on an attribute level

Changes
-------
- Updated misp galaxies. [iglocska]

Fix
---
- Small fix on the attribute correlation popup's header. [iglocska]

  - F-A-I-L
- MISP galaxy update. [Alexandre Dulaunoy]
- Set event to locked = 1 when importing from a MISP export. [iglocska]
- Changed bro cached export to the .intel extension. [iglocska]
- Changed bro file extension to .intel. [Andras Iklody]
- Broken bro export. [Andras Iklody]

  - Sanitisation issues with linebreaks in comments breaking the export
- Cluster synonyms were shown twice on the event view, fixes #1777.
  [iglocska]
- Pull not respecting negated tag rules fixed, fixes #1775. [Andras
  Iklody]
- Don't show the attribute level correlation checkboxes if the event
  correlation is disabled. [iglocska]
- Invalid closing tag. [iglocska]

  - copy pasta fail supreme
- Added an alternative to bcmod if it doesn't exist. [iglocska]

  - simply threw an exception if the module wasn't loaded on the event view if it contained an IBAN number
- Added ACL changes. [iglocska]
- Some fixes with the automatic publish/unpublish feedback. [iglocska]

  - automatically set the event to unpublished in the view when adding/removing tags
  - officially the keep @RichieB2B happy patch ;)
- Unpublish events when tagging/removing tags. [iglocska]

  - same for galaxy clusters
  - also, new ajax way of showing/hiding published status
- Invalid lookup caused the same message to be displayed on correlation
  disabling and enabling for attributs. [iglocska]

Other
-----
- Merge branch 'feature/disable_correlation' into 2.4. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into
  feature/disable_correlation. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1779 from RichieB2B/nscs-nl/fuzzyhash. [Andras
  Iklody]

  Use Fuzzy_Hash_Value for ssdeep
- Use Fuzzy_Hash_Value for ssdeep. [Richard van den Berg]
- Merge pull request #1774 from enemarke/2.4. [Andras Iklody]

  Added support for creating users into different roles depending on ld…
- Added support for creating users into different roles depending on
  ldap group membership. [Emil Enemærke]

v2.4.57 (2016-12-19)
--------------------

New
---
- Added new option to the attribute level restsearch. [iglocska]

  - filter on attributes using timestamps newer than parameter
- Added the warninglist enforcement flag to the remaining exports.
  [iglocska]

  - still missing: Export modules
  - consider having the flag for misp JSON/XML and STIX perhaps?
- :construction:: Parameter to remove warning list hits from exports. [iglocska]
- Added a way to disable certain tags from the UI, fixes #1733.
  [iglocska]

  - also added a new setting to set the default posture when an event containing a tag is pushed (via the API/sync/etc)
    - new setting allows to automatically set new tags to hidden

  - the hidden setting only hides the tags from the tag selection when tagging an event
- First iteration of the new types. [iglocska]

Changes
-------
- Added documentation on the warninglist enforcement to the automation
  page. [iglocska]

  - also added a bunch of missing parameter descriptions
  - added missing code for some of the warninglist enforcement calls
- Added mobile-application-id to payload installation. [iglocska]
- Exposed the new warninglist override via APIs and moved the lookup
  method to the warninglist model. [iglocska]
- Added new attribute type: mobile applicaiton id. [iglocska]

  - Also some further changes to the warninglist enforcement
- Added twitter-id and mapped github-repo to external analysis.
  [iglocska]
- Rework of the galaxy UI, fixes #1738. [iglocska]

  - Reworked the UI elements to allow for more convenient pivoting between event index/event view/galaxy pages
  - Reworked the galaxy quick view on the event view
  - country flags added to the country fields
  - added authors to the clusters
  - tightened the access control to not show non-working buttons for users that don't have tagging rights
- Changed the event download as filename to misp.event.id.uuid.format,
  fixes #1515. [Iglocska]
- Added missing description field and ordered galaxy fields, fixes
  #1744. [iglocska]

Fix
---
- Failtypo fixed. [iglocska]
- Taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Added exception for site admins to be able to add galaxies to events
  of other users. [iglocska]
- Galaxy updated to the latest version. [Alexandre Dulaunoy]
- Added additional refanging patterns to the complex type tool, fixes
  #470. [iglocska]
- Better validation of links, fixes #1745. [iglocska]

  - move to the built in url validation instead of the regex we used before
- Fixed several issues with the template file uploads, fixes #1743.
  [iglocska]

  - Bug with uploading attachments as described in the issue
    - move from pass by reference for a loop was still lacking the correct selector to update the array element instead of the loop's copy
    - attachment uploader tried to base64 the file-name instead of the file-data and store it as the attachment

  - Fix to an unrelated bug that didn't encrypt malicious files when going through the template uploader
- MISP galaxy updated to the latest version. [Alexandre Dulaunoy]
- Issue with new installations not correctly setting the default
  password for the initial user. [iglocska]
- Fixed an invalid link used when pivoting from galaxies to clusters in
  the add cluster flow. [iglocska]
- Fixed an issue with the warninglist detection. [iglocska]
- On newer MySQL versions proposing a deletion to an attribute failed,
  fixes #1741. [iglocska]
- Fixed an issue with the freetext importer. [iglocska]

  - It looks like PHP does parse single quoted strings and replaces double backslashes with a single literal backslash
- Fixes the missing default for the descriptions of galaxy clusters.
  [iglocska]
- Fixes MySQL 5.7 group by issues. [iglocska]
- Python3 tests. [Raphaël Vinot]
- Pivot to the filtered event index from the event view using the
  selected cluster as a filter, affects #1731. [Iglocska]
- Galaxy permission issue fixes #1. [Iglocska]

  - affects #1731

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #1769 from RichieB2B/ncsc-nl/tl-in-subj. [Andras
  Iklody]

  Make threat level in E-mail subject optional
- Make threatlevel in E-mail subject optional. [Richard van den Berg]
- Merge branch '2.4.57' into 2.4. [iglocska]
- Some fixes and pre-validation modifications. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1767 from RichieB2B/ncsc-nl/backupdir. [Andras
  Iklody]

  Don't let misp-backup.sh fill up /tmp
- Use OutputDirName for temporary storage. [Richard van den Berg]
- Merge pull request #1766 from RichieB2B/ncsc-nl/speedup. [Andras
  Iklody]

  Speed up MISP by factor 10
- Add missing indexes. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1760 from moshekaplan/patch-2. [Andras Iklody]

  Update xINSTALL.centos7.txt
- Update xINSTALL.centos7.txt. [Moshe Kaplan]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1757 from RichieB2B/ncsc-nl/24h-sighting. [Andras
  Iklody]

  Use 24 hour clock
- Use 24 hour clock. [Richard van den Berg]
- Merge pull request #1755 from RichieB2B/ncsc-nl/fulltext. [Andras
  Iklody]

  Add fulltext indexes from AppModel.php to MYSQL.sql
- Add fulltext indexes from AppModel.php to MYSQL.sql. [Richard van den
  Berg]
- Merge pull request #1754 from moshekaplan/patch-1. [Andras Iklody]

  Update xINSTALL.centos7.txt
- Update xINSTALL.centos7.txt. [Moshe Kaplan]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1742 from RichieB2B/ncsc-nl/proposal_to_delete.
  [Andras Iklody]

  Set proposal_to_delete default to 0
- Set proposal_to_delete default to 0. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1728 from RichieB2B/ncsc-nl/backup. [Andras
  Iklody]

  Some adjustments to misp-backup.sh:
- Some adjustments to misp-backup.sh: - allow setting MISPPath in misp-
  backup.conf - use MySQL username/password from database.php by default
  - use machine sortable date for output file - do not store TmdDir name
  in tar - use tar non-verbosely. [Richard van den Berg]
- Merge pull request #1722 from MISP/travis. [Raphaël Vinot]

  up: Run tests in python3
- Merge branch '2.4' into travis. [Raphaël Vinot]
- Up: Run tests in python3. [Raphaël Vinot]
- Merge pull request #1727 from kirzaks/2.4. [Andras Iklody]

  Snort optimisation
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4. [Armins]
- Added fast_pattern. [Armins]

v2.4.56 (2016-12-07)
--------------------

New
---
- Tied the galaxies into the ACL. [Iglocska]
- First RC of MISP galaxies 1.0. [Iglocska]
- Added galaxy attach/detach functions. [Iglocska]
- First iteration of the galaxies (:construction:) [Iglocska]
- Added upgrade scripts. [Iglocska]
- Added galaxy tables. [Iglocska]
- Added the publish_timestamp and timestamp parameters to both
  restSearch functions, fixes #1703. [Iglocska]

  - TODO document it
  - new way of handling it, both accept lists with 2 values for ranges
- Added the published flag to restsearch. [Iglocska]

  - allows users to specify whether the events / attributes returned should come from published / unpublished events only. If the parameter is not set both are included

Changes
-------
- Some minor UI changes. [Iglocska]
- Update to gitignore. [Iglocska]
- Version bump. [Iglocska]
- More progress on the galaxies. [Iglocska]
- Some minor changes to the galaxy looks. [Iglocska]
- Add the possibility to specify a "type" instead of a list of "types"
  in the enrichment modules. [Iglocska]
- Add attribute ID to the context fields in the event view and enable
  pagination on it. [Iglocska]
- Added more information to the diagnostics download. [Iglocska]
- Allow JSON POSTing to set parameters for the CSV export. [Iglocska]

  - kill the url parameters with fire

Fix
---
- Removed a duplicate ACL entry. [Iglocska]
- Clusters added don't have the exportable field set on the tag and
  because of that they don't show up on the API. [Iglocska]
- Updated to the latest version of PyMISP. [Alexandre Dulaunoy]
- Moved requeue of pull scheduled job to the front. [Iglocska]
- Fixed missing publish flag in restsearch. [Iglocska]
- Galaxies are now loaded by default. [Iglocska]
- Updated event.json for travis tests. [Iglocska]
- Galaxy update. [Iglocska]
- Added galaxy submodule. [Iglocska]
- Index length fixed for several text fields. [Iglocska]
- Escape field names again. [Iglocska]

  - TODO, have a backtick replacement script for postgres
- Attempt at a fix for SQL woes. [Iglocska]
- Fixed an issue where a normal index was attempted to be created for a
  text field causing the installation to fail. [Iglocska]
- Fixed the detaching of galaxies. [Iglocska]
- Added missing dependencies for the index adder. [Iglocska]
- Removed copy paste junk. [Iglocska]
- Update PyMISP. [Raphaël Vinot]
- PyMISP updated. [Alexandre Dulaunoy]
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- MISP taxonomies updated. [Alexandre Dulaunoy]
- Warning lists updated. [Alexandre Dulaunoy]
- Do not allow empty values to be returned by the enrichment queries.
  [Iglocska]
- Use comment field from modules when using freetext attribute type
  detection. [Iglocska]
- Trim strings of brackets before running the freetext detection on
  them. [Iglocska]
- Temporary fix for a keyword mismatch between the import modules and
  the freetext import. [Iglocska]
- README updated with new features and export formats. [Alexandre
  Dulaunoy]
- Access attribute edit / editField via the UUID instead of the ID.
  [Iglocska]

  - also cleaned up some dumb crap in the attributes/edit function when POSTing JSONs
- Fixed an issue where the diagnostics complained about STIX not being
  installed if the stixtest.py was not readable. [Iglocska]
- Removed an accidentally added edit button. [Iglocska]
- Fixed an issue that incorrectly reported a feed update to have failed
  when not using delta-merge mode. [Iglocska]

  - the issue was that in the case of a feed update to a fixed event without delta merge, MISP tried to insert all parsed attributes, which correctly automatically blocked duplicates
  - however, since these attributes were blocked by the validator, the feed fetcher reported that the fetch didn't succeed as it contained validation errors

  - this fix simply runs non-delta merge mode updates through the comparisons to the existing event, removing duplicates in advance
- Fixed an issue that prevented the feeds from working in CSV mode if no
  value field was set. [Iglocska]
- Removed invalid entry in writeable file diagnostics. [Iglocska]

Other
-----
- Merge branch 'syntax' into 2.4. [Iglocska]
- [*] Corrected the bug with endless loops in while() [Birdy42]
- [*] Removed the double htmlentities check, minor text correction.
  [Birdy42]
- [+] #1711 added [CODE][/CODE] support for the discussion / posts.
  [Birdy42]
- [*] corrected a typo in add.ctp. [Rossier David]
- [+] #359 [Link] feature added to html tag supported for posts.
  [Rossier David]
- Merge pull request #1726 from liviuvalsan/bro_export_improvements.
  [Andras Iklody]

  Performance improvements, bug fixes and new features for the export to Bro
- - Performance improvements when exporting a large number of attributes
  into Bro format. - Fixed file header formatting for the export to Bro
  format (tabs used consistently). - Computing the time needed for
  generating the export to Bro format when done using a background job.
  - When generating the Bro export from the UI all the attributes are
  generated in one single text file similar to the CSV export instead of
  a zip file with different files inside. - Changed the file extension
  of Bro export files from ".intel" to ".txt". - Removed the allowNonIDS
  option from the Bro export as it doesn’t make sense to have it (Bro is
  an IDS). - Fixed some of the API endpoints which were not accepted
  (ACL issues). - Added support for a list of events that should be /
  should not be included in the export. - Added a new "meta.desc" column
  (added in Bro 2.5, see
  https://www.bro.org/sphinx/frameworks/intel.html) containing the
  description of the event and of the attribute. - Sanitized the
  exported data for Bro. - Fixed a number of value substitutions which
  were imported from Snort/Suricata and which were not working for Bro.
  Did instead substitutions needed for Bro. [Liviu Valsan]
- Merge branch 'feature/galaxy' into 2.4. [Iglocska]
- Updated PyMISP. [Iglocska]
- Merge branch '2.4' into feature/galaxy. [Iglocska]
- Merge pull request #1709 from Rafiot/travis. [Andras Iklody]

  Add php5-cli in the deps
- Add php-cli in the deps. [Raphaël Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]

v2.4.55 (2016-11-22)
--------------------

New
---
- Sightings enabled by default. [Iglocska]
- Added timestamps of shadow attributes wherever appropriate. [Iglocska]
- Added uuid as a restsearch parameter, fixes #1683. [Iglocska]

  - search for events/attributes by uuid
- Added checks for the loaded php extensions, fixes #1672. [Iglocska]

  - Diagnosing not loaded extensions was a nightmare
  - New system checks the loaded extensions via php and php-cli (could help with un****ing some RHEL/CentOS issues)
  - Version check for the php-cli php version added

  - only one extension is checked currently, to be updated at a later point in time (remember to also update the web and the cli extension list!)
- Show the date of the latest sighting / organisation on the event view.
  [Iglocska]
- Added multiselect for attributes on the event view. [Iglocska]

  - simply check the checkbox of an attribute/proposal then shift click the checkbox of another to select the full range
  - affects #1618

Changes
-------
- Version bump. [Iglocska]
- Changed the behaviour of the proposal index. [Iglocska]

  - choose between own events / all visible events
  - show timestamps on the proposal index and the creator org of the event
- Updated the NIDS exports. [Iglocska]

  - allow posting JSON/XML payloads with filter options
  - Added the type field to be able to restrict / attribute type

Fix
---
- Some additional changes to accomodate for the automatically enabled
  sightings. [Iglocska]
- Tell MISP to run the db update. [Iglocska]
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Fixed annoying issues with the tags not looking OK on a feed/server
  event preview. [Iglocska]
- Added sighting time to the event sighting summary. [Iglocska]
- Do not try to sort on fields that are not paginated. [Iglocska]
- Opened up attributes/editField to the API, fixes #1674. [Iglocska]
- Fixed an issue where adding an attribute to an empty temlate as a
  first element caused an error, fixes #1635. [Iglocska]
- Invalid error returned to the STIX/CyBox diagnostics if no version is
  installed, fixes #1661. [Iglocska]
- Revert to previous commit. [Alexandre Dulaunoy]
- Travis move to MySQL 5.6. [Alexandre Dulaunoy]
- Mysql requirements. [Alexandre Dulaunoy]
- Travis mysql requirement. [Alexandre Dulaunoy]
- Fixed an issue with editing MISP feeds, fixes #1664. [Iglocska]
- Fixed pagination issues with the taxonomy view, fixes #1660.
  [Iglocska]
- Tightened check for tag removals. [Iglocska]

  - users could remove tags via the api for other organisations
- Fixes an issue where the wrong set of tags were applied when
  populating an event from a template, fixes #1636. [Iglocska]
- Left off changes in attribute.php for the previous commit. [Iglocska]
- Added domain|ip to nids exports. [Iglocska]
- Tag API only returns a subset of the results, fixes #1656. [Iglocska]

  - pagination was used even for the API, changed it to a simple find
- Fixed annoyting column order in the statistics. [Iglocska]
- Some small fixes to the add user API, affects #1621. [Iglocska]

  - Do not force change_pw/termsaccepted default settings based on role when using the API
  - Some cleanup

Other
-----
- Merge branch '2.4.55' into 2.4. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1670 from Rafiot/travis. [Alexandre Dulaunoy]

  Fix mysql on travis
- Fix mysql on travis. [Raphaël Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Update to UPDATE.txt. [Andras Iklody]

  - indicate that a git pull is all that is normally needed.
- Merge branch '1641' into 2.4. [Iglocska]
- - search input for "select tag" is fixed and does not scroll up
  anymore - removed input end tag - added css classes to select tag and
  select tag source popups - so they can be easily changed via the local
  extra css. [cristian.bell@freenet.de]
- Merge branch '1652' into 2.4. [Iglocska]
- Replaced ip address with * for the virtualHost. [cristian bell]
- Merge branch '1651' into 2.4. [Iglocska]
- Block alert e-mails based on tag. [Richard van den Berg]
- Merge branch '1642' into 2.4. [Iglocska]
- Update UPDATE.txt. [Deventual]
- Merge branch '1653' into 2.4. [Iglocska]
- Sorts the "Attributes per organization" array by the total number of
  attr, highest on top. [cristian bell]

v2.4.54 (2016-11-04)
--------------------

New
---
- Added new statistics page, fixes #1648, fixes #1557. [Iglocska]

  - brought back the quick organisation overview as it's a much missed feature
  - added treemap for tags
  - brought attribute histogram into statistics page

  - more coming in the future
- Added a check and deletion tools for orphaned attributes to the
  diagnostics page. [Iglocska]
- Added two additional api filters to the event index (timestamp,
  publishtimestamp) [Iglocska]

  - Currently these are not exposed to the filter UI
  - Easy way to get metadata newer than timestamp/publish timestamp
- Enrichment queries now pass the base64 encoded data to the enrichment
  modules. [Iglocska]

  - first implementation, malware is sent as an encryptet zip base64 encoded
- Added admin user APIs. [Iglocska]

  - The following urls are now available via the API:
    - /admin/users/add
    - /admin/users/edit/id
    - /admin/users/view/id
    - /admin/users/index
    - /users/resetauthkey/id

  - For add and edit, sending a GET request will describe the APIs

  - New API response system's initial implementation, to be used for other APIs in the future
    - standardised responses
    - standardised error codes
    - convenience functions

  - TODO:
    - tie non admin functions into the APIs (maybe?)
    - reuse the new API system for other APIs
- First commit for the user API rework and the new response handler.
  [Iglocska]
- Show file sizes on the export page, fixes #1640. [Iglocska]
- Added new feature to block attributes from IDS sensitive exports based
  on proposals. [Iglocska]

  - Enabled via a new server setting (MISP.proposals_block_attributes)
  - Attributes are skipped from exports that require the to_ids flag if:
    - they have an active proposal that proposes to remove the to_ids flag
    - they have an active proposal that proposes to delete the attribute

  - Currently affected exports:
    - OpenIOC
    - All HIDS exports
    - All NIDS exports
    - All text exports
    - RPZ Zone file export

Changes
-------
- Further work on the user APIs. [Iglocska]
- Remove obsolete getEnrichmentSettings() [Andreas Ziegler]

  seems to have been replaced by Module.php getModuleSettings
- Remove obsolete variables. [Andreas Ziegler]
- Remove obsolete dropIndex() [Andreas Ziegler]

  not needed for reference, as there's a duplicate in AppModel.php (& in git)
- Use the TLD lists from the warninglists, fixes #1149. [Iglocska]

  - simply load any enable warninglist entries from the pre-defined TLD warninglists
  - Pass the resulting array to the complex type tool
  - during domain type heuristics, if the TLD list is not empty use the supplied list
  - alternatively generate a list based on the old TLD rules
  - does not alter any functionality otherwise

Fix
---
- PyMISP to the latest version. [Alexandre Dulaunoy]
- Fixed an issue with an incorrect condition on the admin index.
  [Iglocska]
- Increased space between taxonomy names in the treemap as some of them
  can be quite long. [Iglocska]
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- MISP name fixed. [Alexandre Dulaunoy]
- Fixed annoying capitalisation mess in the event index parameters.
  [Iglocska]

  - just throw everything to lowercase
- Fixed an invalid path for attribute downloads, fixes #1647. [Iglocska]
- Fixed some merge issues. [Iglocska]
- Fixes an invalid check allowing user profile modifications to target
  different users within the org. [Iglocska]

  - User edit had an incorrect check that allowed a normal user edit on a different account within the same org
  - Also removed the deprectated option for this function to be used by org/site admins to be used as an alternative to the admin edit

  - as reported by: Vytautas Paulikas and Robert Giruckas from SEC Consult.
- Attempted fix for an issue with large stix exports getting truncated.
  [Iglocska]
- Certificate typo fixed. [Alexandre Dulaunoy]
- Lowercasing in the tag search wasn't exactly great. [Iglocska]
- Removed test code. [Iglocska]
- Fixed an issue where pushing events worked even if the remote user
  wasn't a sync user. [Iglocska]
- Fixed an issue with the attribute search. [Iglocska]

  - a typo prevented the lookup based on event UUIDs
- Check if the taxonomy directory contains the machinetag.json file
  before trying to read it, fixes MISP/misp-taxonomies#45. [Iglocska]
- Fixed several issues with the import modules. [Iglocska]

  - config settings are not passed correctly to the import modules
  - not having any paste/file upload in an import module would fail
    - removed the requirement to have either filled, if a module doesn't use any of the two fields it will simple pass an empty data field
    - this could be handy for modules that create event data based on the userconfig fields
- Fixes an issue where attachments / malware samples were erroneously
  coloured white. [Iglocska]

  - placeholder hard-coded white class replaced with dynamic value
  - Can't check the referenced issue, shame on Norwegian.no for claiming to have wi-fi onboard...
- Invalid bro export generation due to invalid syntax on the intel
  field. [Iglocska]
- Made the UUID field in the event view optional. [Iglocska]

  - displaying the UUID field seemed to clutter the UI for some users
  - by default it is now disabled and a new control called show context is introduced
  - could be reused in the future for similar use-cases
- Fixed a UI issue with proposals and links, fixes #1624. [Iglocska]

  - fixed an issue where link type attribute values were not visible due to links being too similar of a colour to the blue background of attributes with indicators
- Better fix than the previous one. [Iglocska]
- Fixed a potential empty event_id field that blocked new CSV feeds from
  being added. [Iglocska]
- Removed double sanitisation of the resolved attributes. [Iglocska]

Other
-----
- Version bump. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Add: Screenshot updated. [Alexandre Dulaunoy]
- Add: Screenshot of an event - version 2.4.53. [Alexandre Dulaunoy]
- Merge branch 'features/userapi' into 2.4. [Iglocska]

  Conflicts:
  	app/Controller/UsersController.php
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Add: Hackathon drawing added. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1578 from rotanid/cleanup. [Andras Iklody]

  Cleanup
- Merge pull request #1637 from deralexxx/patch-3. [Andras Iklody]

  mention Roadmap in readme
- Mention Roadmap in readme. [Alexander J]

  .
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Removed Imported via the Freetext Import ... text. [Christophe
  Vandeplas]

v2.4.53 (2016-10-21)
--------------------

New
---
- Added a way to disable the default HTTP_ header namespace or to alter
  it to something else for the custom auth plugin. [Iglocska]
- Added quick search in tag selection popup. [Iglocska]
- CSV feeds and various fixes. [Iglocska]

  - Added the CSV feed format
    - users can specify which fields in the CSV should be parsed
    - comment lines are automatically omitted
    - new settings system added to feeds, currently only used for the value fields

  - Slight rework of the correlation lookup for the feeds
    - got the Speed Force treatment
    - correctly checks against value1 and value2 instead of value

  - Various freetext import fixes
- Added correlations to the freetext feed preview. [Iglocska]

Changes
-------
- Added the capability to search for attributes by uuid. [Iglocska]

  - ID field in the attribute search now accepts attribute UUIDs
  - Partially dealing with #1618
- Made the attribute search fields smaller and the form insta-submit on
  ctrl+enter. [Iglocska]

  - Deals with sme of the issues in #1618
- Rename CENTOS install files to get to the end of the list of install
  guides. [Iglocska]

  - people seem to think that we recommend CentOS for MISP which is absolutely not the case
- Added UUID to attribute list in event view. [Iglocska]
- Keep the event ID in the correlation graph's event nodes' name in
  addition to the info field. [Iglocska]
- Changed the event node names to (partial) event info fields for the
  correlation graph. [Iglocska]
- Validate the event_id as a numeric value. [Iglocska]
- Some changes to event defaults. [Iglocska]

  - Added default analysis value in case it is not set when adding a new event
  - Changed the threat level default to undefined if no default has been set
- MISP taxonomies updated to the latest version (OSINT + Manifest
  updated) [Alexandre Dulaunoy]

Fix
---
- Fixes an issue where adding a new user allowed an invalid role choice.
  [Iglocska]

  - as reported by: Vytautas Paulikas and Robert Giruckas from SEC Consult.
- Fixes an issue where an invalid role could be assigned to a user.
  [Iglocska]

  - As reported by: Vytautas Paulikas and Robert Giruckas from SEC Consult.
- Separate the GFI upload directory from the attachment directories.
  [Iglocska]

  - ensure that no one can't retrieve GFI export files
  - As reported by Vytautas Paulikas and Robert Giruckas from SEC Consult
- Don't correlate shadow attributes to attributes in the same event.
  [Iglocska]
- Fixed the titles of some columns on the event index. [Iglocska]
- Resolved an issue where the new uuid field didn't get coloured the
  same way as the remaining proposal fields. [Iglocska]
- Don't destroy the session on failed customauth login if customauth is
  not enforced. [Iglocska]
- If the custom auth is not required, throw the user to the usual login
  if the custom auth login failed. [Iglocska]
- Fixes a bug that returned the wrong user's email address on the event
  view, viewed by an org admin. [Iglocska]
- Added default values to some of the event fields when adding a new
  event. [Iglocska]

  - basically the only required field now is the info field, everything else uses sane defaults
- Fixed an inverse lookup. [Iglocska]
- Fixed an issue with editing feeds. [Iglocska]
- Pull icon visible even when pull is not enabled for an instance, fixes
  #1608. [Iglocska]
- Log name of remote server in event history, fixes #1607. [Iglocska]

  - currently only affects pull
  - it is becoming more and more crucial that we differentiate between a normal REST add and a push sync. This would allow us to log source servers also on pushes.
- Default setting change when browsing the preview index. [Iglocska]

  Automatically set a threat level based on the server config
- Changed the default value of the threat level ID to match the previous
  fix. [Iglocska]
- Fixed an issue where a validation fail would only semi-populate the
  feed add form fields. [Iglocska]
- Fixed an error on the automation page. [Iglocska]
- Fixed various minor issues and a potential more serious bug.
  [Iglocska]

  - various UI issues prevented the freetext/csv feed related fields from being hidden when adding a new MISP feed
  - issue that potentially prevented new feeds from being saved if no target event is set (cannot reproduce)
- Fixed an issue where adding an empty event would set the error key in
  the returned JSON. [Iglocska]
- Fixed an issue with the type restrictions, fixes #1603. [Iglocska]

  - fixes an issue where the type list in the attribute add/edit view wouldn't automatically restrict to the valid options
- Fixes an issue where the csv feed pull would be routed through the
  freetext code path. [Iglocska]

Other
-----
- Version bump. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1610 from RichieB2B/ncsc-nl/bcmath. [Andras
  Iklody]

  Add rh-php56-bcmath as a requirement for CentOS
- Add rh-php56-bcmath as a requirement for CentOS. [Richard van den
  Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]

v2.4.52 (2016-10-07)
--------------------

New
---
- First implementation of the freetext feed pull. [Iglocska]
- View proposal count on event index and filter events on whether they
  have proposals. [Iglocska]

  - only non deleted proposals are counted
  - allows users to quickly set up filters to view all events that have pending proposals
- Rework of the attribute/proposal views and popovers round 2.
  [Iglocska]

  - also fixes to a bunch of small UI bugs and code style issues
- First cut of the popover rework for form selects. [Iglocska]
- Add the sightings cont to the event index. [Iglocska]
- Add Tool for random string generation. [Andreas Ziegler]
- Add compatibility Lib for random_int. [Andreas Ziegler]
- Added the metadata flag to the event restsearch API. [Iglocska]

  - allows fetching metadata only without including attributes/proposals
- Db structure&data file for PostgreSQL support. [Andreas Ziegler]
- Add basic documentation on experimental PostgreSQL support. [Andreas
  Ziegler]
- Add basic experimental support for PostgreSQL. [Andreas Ziegler]

Changes
-------
- Updated to the latest MISP taxonomies. [Alexandre Dulaunoy]
- Cleanup of removed functionality. [Iglocska]
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Misp-warninglists updated to the latest version. [Alexandre Dulaunoy]
- External analysis/text attributes containing a uuid converted to a
  link to a MISP event. [Iglocska]
- Simpler handling of empty/temporary arrays. [Andreas Ziegler]
- Remove duplicate array key. [Andreas Ziegler]
- Remove obsolete files. [Andreas Ziegler]
- Update deb8/ubu1604 setup, composer to 1.2.1 (#1569) [Andreas Ziegler]
- Update cakephp to 2.8.9 (#1560) [Andreas Ziegler]
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Set var eventIDs only if necessary. [Andreas Ziegler]
- Html input text element should not have a separate closing elem.
  [Andreas Ziegler]
- Remove obsolete count variable. [Andreas Ziegler]
- Default roles all have API access. [Andreas Ziegler]

  - changed the default role set to have api access enabled
  - existing installations not affected
  - if a community wants to restrict API access for certain users they're free to do it

  (same as aa0383064345d24e1ceb32621457ec156c2cd809 but for postgres this time)
- Default roles all have API access. [Iglocska]

  - changed the default role set to have api access enabled
  - existing installations not affected
  - if a community wants to restrict API access for certain users they're free to do it
- Added sane defaults to the describeTypes api. [Iglocska]
- GeneratePassword now uses random passwords with a minimum length of 12
  characters. [iglocska]
- Allow the usage of posted JSON objects in the bro export. [Iglocska]
- Cleanup of removed Hids and Nids BroExport libraries that got merged
  into BroExport.php. [Iglocska]
- Refactor of the Bro export. [Iglocska]
- Reverted the changes to the NIDS export. [Iglocska]
- Correct some spelling issues. [Andreas Ziegler]
- Remove duplicate check for fullAddress. [Andreas Ziegler]

  got already checked a few lines above, can't be something else
- Remove redundant call to beforeFilter, just calling its parent.
  [Andreas Ziegler]
- Remove a variable that isnt used. [Andreas Ziegler]
- Remove obsolete code from TagsController. [Andreas Ziegler]
- Remove obsolete js function submitTagForm. [Andreas Ziegler]
- Remove obsolete file view.ctp. [Andreas Ziegler]
- Remove obsolete variables. [Andreas Ziegler]
- Remove redundant className attributes. [Andreas Ziegler]
- Remove some references to variables. [Andreas Ziegler]
- Use new Tool for random string generation. [Andreas Ziegler]
- Remove some obsolete code from View/Layouts. [Andreas Ziegler]
- Remove obsolete files succes.ctp. [Andreas Ziegler]
- Use correct closing tag in view element. [Andreas Ziegler]
- Creator e-mail in the event details, fixes #1252 (#1535) [Cristian
  Bell]

  * chg: creator e-mail in the event details, fixes #1252
- Cleanup of old acl system config files that hasn't been used in years.
  [Iglocska]
- Update cakephp to 2.8.7. [Andreas Ziegler]
- Use dependency instead of explicit deleteAll. [Andreas Ziegler]
- Made the new attribute marker in the notification e-mails a bit more
  obvious. [Iglocska]
- Replace 2 spaces after tab by double tab. [Andreas Ziegler]
- Replace 4 spaces after tab by double tab. [Andreas Ziegler]
- Replace spaces before tabs by tabs. [Andreas Ziegler]
- Replace spaces between tabs by tabs. [Andreas Ziegler]
- Text moved to the first choice for internal reference category
  attributes. [iglocska]
- Changed the response of the functionality in the PR to be in line with
  other ajax request responses in MISP. [Iglocska]
- Removed requirement for findAdminsResponsibleForUser for not site
  admin. [Iglocska]

  - Take own org's admins / siteadmins before looking for site admins from other orgs
- Chg: only show API/authkey to user with API key rights, fixes #1311 -
  code improvements as per @iglocska 's comments.  thanks. [Cristian
  Bell]
- Only show API/authkey to user with API key rights, fixes #1311 - adds
  some missing code parts from the initial commit. [Cristian Bell]
- Only show API/authkey to user with API key rights, fixes #1311.
  [Cristian Bell]
- Rename findTags() to findEventIdsByTagNames() [Andreas Ziegler]
- Remove some obsolete code. [Andreas Ziegler]
- Changed the default event table engine to InnoDB. [iglocska]
- Set "User" as the default role for new installations. [iglocska]

Fix
---
- Fixes to the ssdeep detection as it was way too loose. [Iglocska]
- Resolved several issues with error handling in the new feed system.
  [Iglocska]
- Removed already removed file that got reverted. [Iglocska]

  - As first committed by @rotanid
  - The file is not used any longer, however removing it causes issues unless we clean the model cache
  - upgrading to a new version will force the cleaning of the model cache, so it's a great time to finally remove it
- Various fixes to the feed system. [Iglocska]

  - allow users to override the IDS flags and keep all attributes pulled from a freetext feed IDS = off
  - UI changes
  - fix to a bug that caused already deleted attributes to be counted as existing ones
- Added missing initialisation of the synctool. [Iglocska]
- Added some missing entries to gitignore. [Iglocska]
- Added missing changes to the javascript file. [Iglocska]
- The JSON schema regarding the related event from Array -> Object.
  [Alexandre Dulaunoy]
- Left off the actual file affected for the last commit. [Iglocska]
- Fixed a bug with the event view. [Iglocska]

  - the fetcher was moving proposals within an attribute if the proposal was directed at the attribute (correctly)
  - this left the event proposal list in a non progressive array key format, which lead to a weird situation where the JSON format used string numeral keys in a dict as opposed to the desired list. Nobody in their right mind would ever want that.
  - fixed
- Fixed the incorrect column order on the event index. [Iglocska]
- Fixed the broken check that prevented the sightings count from
  displaying. [Iglocska]
- Really restrict the shown proposal count to non deleted proposals.
  [Iglocska]
- Added changes to JS. [Iglocska]
- Added the capability to merge attachments/samples. [Iglocska]
- Fixed the event index in various places (such as the user admin view)
  [Iglocska]

  - also added missing view files from previous patch
- Left off the changes to the js. [Iglocska]
- Various fixes to the user index, fixes #1597, fixes #1598. [Iglocska]

  - highlight deleted users
  - use the same index for the org user view (without the filter options)
  - fixes the pagination of the users when viewing it through the organisation view
- Added the git commit ID to the feed request. [Iglocska]
- Org id potentially not being set when capturing tags. [Iglocska]
- Fixed an issue that resulted in empty event tags showing up in the
  event index JSON. [Iglocska]
- Small fix to the worker start script. [Iglocska]
- Even dirtier hack to only replace the STIX_Package object with a
  Package object. [Iglocska]
- Several fixes to the STIX export. [Iglocska]

  - based on the findings of @RichieB2B
- Fixed an issue with the restsearch export potentially incorrectly
  loading all eligible events in one go into memory. [Iglocska]
- Fix an issue where duplicates of auth methods in Security.auth keep
  piling up. [Iglocska]

  - due to a bug, each change in the server settings with an auth plugin enabled would reappend the full list of enabled auth plugins to Security.auth
  - this lead to an exponential growth of the number of entries in the array in the config file
- Missing new TLDs in free text import, solves #1149 (#1574) [Cristian
  Bell]

  * fix: missing new TLDs in free text import, solves #1149
- Php warning on buildAlertEmailBody in Event.php. [Andreas Ziegler]

  if an attributes type was longer than $appendlen-2 a php warning was logged.
  str_repeat()'s 2nd parameter, an integer, must not be smaller than 0.
- Don't show the org restriction of a tag in the event view JSON.
  [Iglocska]
- Set the org_id field to 0 if it is not set. [Iglocska]
- Removed accidentally committed code. [Iglocska]
- Fixed an anchor in the documentation. [Iglocska]

  - as pointed out by @rotanid
- Removed functions needed for the delegation restored. [Iglocska]

  - as discovered by @RichieB2B
- Fixed an issue with the thread index that prevented your org only
  threads from ever being visible to users, as highlited in #1570.
  [Iglocska]
- Typo in comment. [Andreas Ziegler]
- The server add view incorrectly allowed the internal server settin to
  be set even if the default organisation picked wasn't the host
  organisation. [Iglocska]
- Hide the salt key in the UI unless it's the old default key, fixes
  #1566. [Iglocska]
- No tag set in the remote index leads to notice errors. [Iglocska]
- Sort server preview events by timestamp, fixes #1558. [Iglocska]
- Don't try to show sightings count if sightings aren't enabled.
  [Iglocska]
- Missing return keyword before a message-string. [Andreas Ziegler]
- PostgreSQL handling in __dropIndex() [Andreas Ziegler]
- DropIndex before adding indexes on tags/org_id &
  cake_sessions/expires. [Andreas Ziegler]

  to make sure they are created from scratch
- Restrict tag usage for restricted tags in a place where it was missed.
  [Iglocska]
- Don't load relations when running the password shell. [Iglocska]
- Removed left in debug line. [Iglocska]
- Append text to variable (as originally intended) [Andreas Ziegler]

  without this change, the text won't be used or display ever
- Add keyword 'new' to an exception throw. [Andreas Ziegler]
- Force order of the regex entries. [Iglocska]
- Fixes to the API request e-mail. [Iglocska]
- Fixes a bug introduced by f37963fde4ad91b625d3ee80eb52ebd048f3dc71
  where on API request the user itself receives an e-mail and not his
  org_admin or site_admin. [Cristian Bell]
- Added a fallback for no active flag being set on sharing group
  capture. [Iglocska]
- Issue resulting from references removal, #1501, 25e52a6 (#1544)
  [Andreas Ziegler]
- Fallback to insecure random for php 5.x if the random_compat submodule
  isn't loaded. [iglocska]
- Fixed the inversed namespacing in the STIX export, fixes #1543.
  [iglocska]
- Added missing changes needed for the new description of the bro
  export. [Iglocska]
- Updated the bro documentation. [Iglocska]
- Remove the temp directory after generating the bro cache. [Iglocska]
- Refactor of the bro export to always create a zip archive with
  separate files if "all" types are queried. [Iglocska]
- Some changes to the bro export. [Iglocska]

  - moved the whitelisting out of the plugin
  - source now contains the instance host org name (if applicable), the event UUID and the creator org name
- Removing some unused code. [Cristian Bell]
- Fix to an invalid parameter description on the automation page, fixes
  #1530. [Iglocska]
- Fixed an issue where non API users could not download events in
  JSON/XML format, fixes #1525. [Iglocska]
- Updated to the latest version. [Alexandre Dulaunoy]
- Fix the broken bruteforce protection. [Iglocska]

  - Moved the bruteforce protection directly to the login action
  - Fixed the datetime format used by the protection
  - Cleaned up the logging of failed attempts
- Removed deprecated path from functions that are allowed for API users.
  [Iglocska]
- Fixed the style of a page header. [Iglocska]
- Fixed an issue with internal sync failing on more than one added
  server. [Iglocska]
- Further fixes to the internal sync. [Iglocska]
- Internal sync fixed for pushes on your org only events. [Iglocska]
- Fixed various issue with the stix export, fixes #1505. [Iglocska]
- Typo recurisve/recursive in EventsController. [Andreas Ziegler]
- Fix to an invalid namespace in CIQ based elements in STIX. [Iglocska]
- Revert to the old functionality of the stix export where the data is
  passed back from the internal stix method, fixes #1509. [Iglocska]
- Notify the user requesting API key access if e-mailing is disabled on
  the instance. [Iglocska]
- Fixed an issue where fetching the PGP key without entering an e-mail
  address in the user creation form wasn't handled cleanly. [iglocska]
- Some clarification on the user creation/edit forms. [iglocska]
- Cleanup of the routes file. [iglocska]
- Removed unreachable line referencing a non-existing variable.
  [iglocska]
- Cleanup of missing whitespaces in PR. [Iglocska]
- Fixed a newly introduced bug that breaks the NIDS exports, as
  referenced in #1489. [iglocska]
- Added the default role selector to the ACLComponent. [iglocska]
- Removed filename check from the AppController. [iglocska]

  - rerouted all calls to the method to the Model equivalent
- Check whether e-mailing is enabled or not before publishing.
  [iglocska]

  - before the publishing process (wheter by a background worker or not) would be executed before checking whether e-mailing was even enabled
  - this lead to a lot of e-mail jobs that ended up doing nothing but creating a log entry
- Invalid indeces used for the MISP.host_org_id setting. [iglocska]
- Add key length to text field index. [iglocska]
- Removed incorrect index in the previous commit. [iglocska]
- Update version number to 2.4.51 in MYSQL.sql. [Andreas Ziegler]
- Removed unused lookup in EventsController::index(), fixes #1484.
  [iglocska]

  - old code became obsolete when the taxonomies were implemented
- Fixed a copy paste issue with the description comment of a method,
  fixes #1483. [iglocska]
- Added 2.4.51's database changes to MYSQL.sql. [iglocska]
- Added internal convenience method to check remote server version.
  [iglocska]
- Event index should respect pagination requests for API users.
  [iglocska]
- Inverse conditional for cleaning up the expired sessions. [iglocska]
- Moved the example API script using SSL client certificate. [iglocska]

Other
-----
- Merge branch '2.4.52' into 2.4. [Iglocska]
- Revert "fix: Removed already removed file that got reverted"
  [Iglocska]

  This reverts commit 832321a77c77bf325cc301772792e39a01cad198.
- Merge pull request #1600 from RichieB2B/ncsc-nl/update-tags. [Andras
  Iklody]

  Add missing tags from pushed events
- Add missing tags from pushed events. [Richard van den Berg]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch 'attribute_merge' into 2.4. [Iglocska]
- Allow merging for site admins. [Richard van den Berg]
- Allow merging of event attributes. [Richard van den Berg]
- Merge branch 'publishalert' into 2.4. [Iglocska]
- Fix indication of new attributes in E-mail alerts, fixes #1521.
  [Richard van den Berg]
- Merge branch 'taginfo' into 2.4. [Iglocska]
- Merge branch '2.4' into taginfo. [Iglocska]
- Merge pull request #1595 from RichieB2B/ncsc-nl/stix-fix. [Andras
  Iklody]

  Fix STIX XML and JSON exports
- Avoid duplicate key-sequence to satisfy STIX unique identity-
  constraint. [Richard van den Berg]
- Fix STIX XML and JSON exports. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Put tag info from event in E-mail subject, fixes #1107. [Richard van
  den Berg]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1591 from thomai/patch-2. [Andras Iklody]

  sudo is needed to create new ssl key.
- Sudo is needed to create new ssl key. [Thomas Maier]

  A normal user does not have permissions to the used folder /etc/ssl/private in Ubuntu 16.04/Mint 18 by default.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- MISP rfc repository added. [Alexandre Dulaunoy]
- Basic README added to explain the two JSON schemas. [Alexandre
  Dulaunoy]
- Merge pull request #1590 from Rafiot/upschema. [Alexandre Dulaunoy]

  Update JSON schema
- Add lax JSON schema for PyMISP. [Raphaël Vinot]
- Merge pull request #1589 from thomai/patch-1. [Alexandre Dulaunoy]

  Added python-setuptools for ubuntu install howto
- Added python-setuptools for ubuntu install howto. [Thomas Maier]

  You need to install the package python-setuptools on Ubuntu 16.04/Mint 18 to use the setup.py for the STIX installation.
- Merge pull request #1588 from RichieB2B/ncsc-nl/stix-fix. [Andras
  Iklody]

  Two small STIX fixes (again)
- Use consistent STIX/CyBOX IDs for domain|ip entries. [Richard van den
  Berg]
- Correct CIQ namespace. [Richard van den Berg]
- Merge pull request #1585 from RichieB2B/ncsc-nl/stix-fix. [Andras
  Iklody]

  Make STIX validate
- - correct namespace order - stix set_id_namespace calls cybox
  set_id_namespace. [Richard van den Berg]
- Revert "fix: missing new TLDs in free text import, solves #1149
  (#1574)" [Cristian Bell]

  This reverts commit e3bb9d3a4204ca00931e3f77afc318aaf292382e.
- Merge pull request #1571 from rotanid/bugfix-php-warning. [Andras
  Iklody]

  fix: php warning on buildAlertEmailBody in Event.php
- Merge pull request #1575 from RichieB2B/ncsc-nl/small-fixes. [Andras
  Iklody]

  Two small fixes
- Only show publish links for site admins. [Richard van den Berg]
- Log target org instead of requesting org. [Richard van den Berg]
- Separated a2enmod lines to prevent some confusion. [Andras Iklody]
- Merge pull request #1570 from rotanid/cleanup-obsolete. [Andras
  Iklody]

  cleanup
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1567 from ppanero/shibbsso. [Alexandre Dulaunoy]

  default org changed to id instead of name
- Default org changed to id instead of name. [ppanero]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1559 from rotanid/bugfixes. [Andras Iklody]

  Bugfixes
- Merge pull request #1382 from treyka/patch-2. [Alexandre Dulaunoy]

  Add install procedure for current version of ZeroMQ
- Add install procedure for current version of ZeroMQ. [Trey Darley]

  Debian 8 has an ancient version of ZeroMQ which is not compatible with the latest pyzmq on PyPI. Manually installing the current ZeroMQ release is a viable workaround.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1551 from rotanid/bugfixes. [Andras Iklody]

  Bugfixes & Cleanup
- Merge pull request #1550 from rotanid/mysql-postgresl-too. [Andras
  Iklody]

  chg: Default roles all have API access
- Merge pull request #1549 from ppanero/shibbsso. [Alexandre Dulaunoy]

  warining  due to session start fixed, warning due to org assigment wh…
- Warining  due to session start fixed, warning due to org assigment
  when possible null fixed, readme updated. [ppanero]
- Merge pull request #1547 from
  cristianbell/fix_request_API_wrong_user_emailed. [Andras Iklody]

  fix: fixes a bug introduced by f37963fde4ad91b625d3ee80eb52ebd048f3dc…
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '1541' into 2.4. [iglocska]
- Merge branch '2.4' into 1541. [iglocska]
- Merge branch '1457' into 2.4. [iglocska]
- Merge branch '2.4' into 1457. [iglocska]
- Merge branch '1501' into 2.4. [iglocska]
- Merge branch '2.4' into 1501. [iglocska]
- Merge branch '1503' into 2.4. [iglocska]
- Merge branch '2.4' into 1503. [iglocska]
- Merge branch '1511' into 2.4. [iglocska]
- Merge branch '2.4' into 1511. [iglocska]
- Merge branch 'feature/bro-export' into 2.4. [iglocska]
- Merge branch '2.4' into feature/bro-export. [iglocska]
- Merge branch '2.4' into feature/bro-export. [Iglocska]

  Conflicts:
  	app/Model/Event.php
- Model/Server.php modified so the settings remain the same after config
  change on the web UI. [ppanero]
- Bro export funtionality. [ppanero]
- Merge pull request #1538 from rotanid/small-cleanup. [Andreas Ziegler]

  Small cleanup
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1527 from rotanid/cakephp-update-287. [Andras
  Iklody]

  update cakephp to 2.8.7
- Merge pull request #1512 from rotanid/cleaner-delete. [Andras Iklody]

  Tag.php: use dependency instead of explicit deleteAll
- Merge pull request #1520 from ppanero/shibbsso. [Andras Iklody]

  stringer checks on email and nids_sid of user calculated from max
- Stringer checks on email and nids_sid of user calculated from max.
  [ppanero]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1504 from ppanero/shibbsso. [Alexandre Dulaunoy]

  shibboleth sso debug log capabilities added
- Deny by default instead of read-only. [ppanero]
- Typosfixed for PR. [ppanero]
- Shibboleth sso plugin index failure fixed. [ppanero]
- Shibboleth sso debug log capabilities added. [ppanero]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1510 from rotanid/bugfix. [Andreas Ziegler]

  fix: typo recurisve/recursive in EventsController
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1502 from rotanid/tabs-spaces. [Andreas Ziegler]

  Tabs vs. spaces indention
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1448 from TheDr1ver/2.4. [Andras Iklody]

  Add support to export an OpenIOC file via API
- Extra indent. [Nick Driver]
- Spaces to Tabs. [Nick Driver]
- Add support to export an OpenIOC file via API (Change spaces to tabs)
  [Nick Driver]
- Merge branch 'apirequest' into 2.4. [Iglocska]
- Merge branch '2.4' into apirequest. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch 'cristianbell-
  fix_1311_only_show_API/authkey_to_user_with_rights' into 2.4.
  [Cristian Bell]
- Merge branch 'fix_1311_only_show_API/authkey_to_user_with_rights' of
  https://github.com/cristianbell/MISP into cristianbell-
  fix_1311_only_show_API/authkey_to_user_with_rights. [Cristian Bell]
- Merge pull request #1497 from ppanero/centos_install. [Andras Iklody]

  Update INSTALL.centos7.txt
- Update INSTALL.centos7.txt. [Pablo Panero]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1493 from ppanero/centos_install. [Andras Iklody]

  change in SELtype, httpd_sys_content_rw_t does not exists
- Change in SELtype, httpd_sys_content_rw_t does not exists. [ppanero]
- Merge pull request #1485 from MISP/feature/postgresql. [Andras Iklody]

  support PostgreSQL database backend
- Merge pull request #1491 from rotanid/rename-findtags-function.
  [Andras Iklody]

  rename findTags() to findEventIdsByTagNames()
- Merge pull request #1492 from rotanid/small-cleanup. [Andras Iklody]

  chg: remove some obsolete code
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1486 from rotanid/update-version-nr-in-sql-file.
  [Andras Iklody]

  fix: update version number to 2.4.51 in MYSQL.sql

v2.4.51 (2016-08-29)
--------------------

New
---
- Add default role to the user creation, fixes #256. [iglocska]
- New piece by piece stix export allowing large datasets to be exported.
  [iglocska]
- Add e-mail in event history view, fixes #1389. [iglocska]

  - Only visible to site admins and org members
- Simple diagnostic tool for the modules added. [iglocska]
- Screenshot preview in the event view. [iglocska]
- Added a way to clear worker queues. [iglocska]
- Improved jobs overview. [iglocska]

  - Correctly interpreting job states
  - Show errored background jobs
  - Show jobs that cannot proceed because no active worker is monitoring the queue
  - Allow site admins to view the reason of the failure (up to 24h after the fact) including a stack trace

Changes
-------
- Enabled 2.4.51 db upgrade. [iglocska]
- Version bump. [iglocska]
- UI changes for the email field in the event history. [iglocska]
- New filename regex & separate functions. [Andreas Ziegler]
- Cleanup of the controllers and models. [iglocska]

  - removed incorrect, useless boiler plate comments
  - kept useful comments intact
  - added some missing line breaks to make the codebase a bit more uniform
  - removed some obviously obsolete TODO comments
- Internal reference category attributes should always default to your
  org only. [iglocska]
- Remove obsolete backups of config files. [Andreas Ziegler]
- Use central function for CIDR checks. [Andreas Ziegler]
- Add central function for CIDR check. [Andreas Ziegler]
- Cleanup TemplatesController.php. [Andreas Ziegler]
- Filename regex changes. [Andreas Ziegler]
- Fix indention of 4 files. [Andreas Ziegler]
- Better readability of config files. [Andreas Ziegler]
- Fix indention in some files. [Andreas Ziegler]
- Add space after keywords if/for/foreach/while/switch/catch. [Andreas
  Ziegler]
- Add spaces before opening curly brackets. [Andreas Ziegler]
- Remove whitespace at end of line. [Andreas Ziegler]
- Remove whitespace (space/tab) from empty lines. [Andreas Ziegler]
- Add newline character before EOF. [Andreas Ziegler]
- Cleanup Sighting.php. [Andreas Ziegler]
- Remove usage of App::import in favor of ::uses. [Andreas Ziegler]
- Remove not used old plugin file. [Andreas Ziegler]
- If the quickfilter on the event index only returns a single event,
  redirect to the event view directly, fixes #1430. [Iglocska]

  - the perfect last-minute-saturday-night patch
- Rename FileAccess to FileAccessTool. [Andreas Ziegler]

  every other tool classes name in the Lib/Tools/ folder also ends with "Tool"
- Change FileAccess from static to instantiable class. [Andreas Ziegler]
- Use 1/0 not true/false for conditions & other boolean sqlquery
  elements. [Andreas Ziegler]
- Org UUID visible on the organisations/view/ page #1445 - uuid field
  always visible even when value is empty. [Cristian Bell]
- Org UUID visible on the organisations/view/ page #1445. [Cristian
  Bell]
- Update cakephp to 2.8.6. [Andreas Ziegler]
- Dont depend on MySQL-result-format of select-count() [Andreas Ziegler]
- Remove obsolete upgrade stuff, unsupported. [Andreas Ziegler]
- Remove obsolete Schema stuff. [Andreas Ziegler]
- Add index for cake_sessions expires to MYSQL.sql. [Andreas Ziegler]
- Added missing new line at the end of file. [iglocska]
- Added the db changes needed for PR #1268. [iglocska]

  - Since 2.4.50 was released without any DB modifications and a current commit required it, it was a good opportunity to add this, as we can fast-track PR 1268 this way
- Replace a MySQL specific function by PHP code. [Andreas Ziegler]
- Remove obsolete backticks from sql queries. [Andreas Ziegler]

  backticks are only necessary to escape reserved keywords.
  as backticks are MySQL-specific, having them only where really necessary
   makes integrating support for other DBMS easier.
- Fix typo. [Andreas Ziegler]
- Added the tracking to all queued jobs. [iglocska]
- Removed incorrect comments. [iglocska]
- Made histogram.ctp a bit more readable. [iglocska]
- Attribute list on view event page sort by date issue #1355. [Cristian
  Bell]
- Attribute list on view event page sort by date issue #1355. [Cristian
  Bell]
- Attribute list on view event page sort by date issue #1355. [Cristian
  Bell]
- Redundant members list and organisations page - tab versus 4spaces.
  [Cristian Bell]
- Redundant members list and organisations page. [Cristian Bell]
- Redundant members list and organisations page #1013. [Cristian Bell]

Fix
---
- Pushing upgraded to respect the internal sync setting. [iglocska]

  - Allows the push of org only attributes
  - No downgrading of attributes/events
- Fixed an invalid log entry breaking the publishing process. [iglocska]
- Added missing job exception viewer view file. [iglocska]
- Fixes to the internal server setup. [iglocska]

  - Only allow enabling internal mode if the host organisation is set and it is chosen as the remote organisation when adding the server sync
  - This ensures that internal sync only happens when the same organisation owns both instances
- Some minor fixes to the client_certs for the sync to align it with the
  other upstream changes. [iglocska]
- Some exports (HIDS, NIDS) failing on certain MySQL versions due to an
  only_full_group_by policy violation in the attribute fetcher, fixes
  #1390. [iglocska]
- Updated the stix export files to support separate packaging.
  [iglocska]
- Update to the caching task. [iglocska]
- Refactoring of the STIX export. [iglocska]

  - Also adding it to the caching mechanism
  - still :construction:
- Differentiate queued and running jobs if no granular progress is
  returned. [iglocska]
- Version bump. [iglocska]
- Updated to the latest version of the MISP taxonomies. [Alexandre
  Dulaunoy]
- Update to latest version of PyMISP. [Alexandre Dulaunoy]
- Corrected attribute degradation on pull. [iglocska]

  - events were correctly degrading, however, attributes weren't on a pull
  - also removed some ancient compatibility code that was there for MISP 2.0 which is a version that hasn't been supported in ~3 years
- Cleaner way of handling no correlations in the correlation engine
  changes. [iglocska]
- Fixed a missing field in the correlation lookup causing travis to
  fail. [iglocska]
- Remove incorrect correlations on deleted attributes. [iglocska]
- Performance boost for the correlations. [iglocska]

  Going through insertMulti to insert correlations to get a massive speed boost
- Removed debug from previous commit. [iglocska]
- Resolved slow ingestion of warninglists. [iglocska]

  - switched to a more direct database access approach for the warninglist entry insertion
- Cleanup of some unused code. [iglocska]

  - based on @rotanid's findings
- Removed incorrect uses of pass by reference, fixes #1472. [iglocska]
- Remove substr() from value in CIDR part of restSearch. [Andreas
  Ziegler]
- Add missing $ to variable name in CIDR part of attribute search.
  [Andreas Ziegler]
- Fixed an invalid array_merge in the attribute fetcher. [iglocska]
- Raised the default timeout for modules. [iglocska]

  - possible fix for #1466
- Some exports (HIDS, NIDS) failing on certain MySQL versions due to an
  only_full_group_by policy violation in the attribute fetcher, fixes
  #1390. [iglocska]
- Missing ACL entries added. [Iglocska]
- Small fix to the Shibboleth authentication. [Iglocska]
- Minor code issues: - added brackets to the IF/ELSE statement.
  [Cristian Bell]
- Minor code issues: - redundant var initialisation - for the
  automatically created organization the "created_by" is 0, which
  produces a Notice error in /View/Organization/view.ctp. [Cristian
  Bell]
- Attribute delete should not return the full event via REST, instead a
  message saying that it was deleted similar to the event deletion is
  enough, fixes #1449. [iglocska]
- Added check for instances not using database sessions to skip the
  automatic session cleanup. [iglocska]

  - But... Use database sessions.
- Fixed an issue with the histogram on newer MySQL versions. [iglocska]
- Invalid response by the queryEnrichment() function if the module
  server is not reachable. [iglocska]
- Overwrite cached json exports, fixes #1439. [Richard van den Berg]
- Cleaner input for caching jobs. [iglocska]
- Fixed an issue with large samples from modules causing the import
  process to fail. [iglocska]
- Don't show the No worker active message in the jobs index if a job is
  already completed. [iglocska]
- Fixed the performance issues with the self cleaning by adding an index
  to the expired field. [iglocska]
- Some performance tuning for the auto-session-cleanup. [iglocska]
- Debug mode not set throws notices. [iglocska]
- Added automatic cleanup of expired sessions. [iglocska]

  - on page load for site admins
- View for the new jobs screen. [iglocska]
- Invalid permission check order leads to a notice. [iglocska]
- Show tag value in event history, fixes #1422. [iglocska]

  - also log removed tags
- Organisation index view fixes. [iglocska]

  - Changed the name of the User count field
  - Fixed an issue where the lookup of an invalid index not handled in the user count array occured when an organisation had no members (for example an external organisation, or a newly created local organisation)
- Moved lookup function from controller to model and fixed some other
  issues. [iglocska]

  - That function has no reason not to be in a model
  - Removed invalid contain
  - Simple lookup against the users table is more efficient
- Permissions for non-auth enabled users to use the API fixed.
  [iglocska]
- Hover not working correctly for users viewing the events of another
  organisation. [iglocska]

Other
-----
- Merge branch '2.4.51' into 2.4. [iglocska]
- Model/Server.php modified so the settings remain the same after config
  change on the web UI. [ppanero]
- Merge branch '2.4' into 2.4.51. [iglocska]
- Merge branch 'sslclientsync' into 2.4.51. [iglocska]
- Merge branch 'sslclientcert' into sslclientsync. [iglocska]
- Example API script using client cert. [Richard van den Berg]
- Merge branch '2.4' into sslclientsync. [iglocska]
- Add support for sync server SSL client certificates. [Richard van den
  Berg]
- Merge branch '2.4' into 2.4.51. [iglocska]
- First iteration of the internal sync rework. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #1482 from Rafiot/travis. [Raphaël Vinot]

  Fix travis
- Fix travis. [Raphaël Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1476 from rotanid/filename-regexes. [Andras
  Iklody]

  new filename regex & separate functions
- Merge pull request #1462 from rotanid/obsolete-files. [Andras Iklody]

  remove obsolete backups of config files
- Merge pull request #1469 from rotanid/centralize-cidr-check. [Andras
  Iklody]

  Centralize CIDR checks
- Merge pull request #1470 from rotanid/cleanup-tplctr. [Andras Iklody]

  cleanup TemplatesController.php
- Merge pull request #1471 from rotanid/filename-regexes. [Andras
  Iklody]

  filename regex changes
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1468 from rotanid/bugfixes. [Andreas Ziegler]

  Bugfixes
- Merge pull request #1464 from rotanid/indention-fixes. [Andreas
  Ziegler]

  fix indention of 4 files
- Merge pull request #1463 from rotanid/config-readability. [Andreas
  Ziegler]

  better readability of config files
- Revert "chg: remove not used old plugin file" [Iglocska]

  This reverts commit dd8ec54e2a6512a12c0214287db79a676a8dc968.
- Merge pull request #1461 from rotanid/cleanup. [Andreas Ziegler]

  Cleanup
- Merge pull request #1460 from rotanid/sightings-cleanup. [Andreas
  Ziegler]

  chg: cleanup Sighting.php
- Merge pull request #1459 from rotanid/uses-import. [Andras Iklody]

  remove several usages of App::import() in favor of App::uses()
- Merge pull request #1458 from rotanid/cleanup-old-plugin-orphans.
  [Andras Iklody]

  chg: remove not used old plugin file
- Merge pull request #1454 from ppanero/sso_integration_plugin. [Andras
  Iklody]

  Bug fixing on shibboleth auth. DB group loading and missing email bug…
- Bug fixing on shibboleth auth. DB group loading and missing email bugs
  fixed. [ppanero]
- Merge pull request #1456 from rotanid/fileaccess-overhaul. [Andras
  Iklody]

  FileAccess cleanup/consistency
- Merge pull request #1451 from cristianbell/fix_minor_code_fixes.
  [Andras Iklody]

  fix: minor code issues:
- Merge pull request #1443 from rotanid/boolean-datatype-handling.
  [Andras Iklody]

  change of boolean datatype handling #2
- Merge pull request #1446 from
  cristianbell/chg_1445_OrgUUID_visible_to_everyone. [Andras Iklody]

  chg: Org UUID visible on the organisations/view/ page #1445
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1447 from rotanid/cakephp-update-286. [Andras
  Iklody]

  update cakephp to 2.8.6
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1444 from Rafiot/bump_pymisp. [Raphaël Vinot]

  Bump PyMISP
- Bump PyMISP. [Raphaël Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1442 from rotanid/less-mysql-dependency. [Andreas
  Ziegler]

  chg: dont depend on MySQL-result-format of select-count()
- Merge pull request #1441 from rotanid/cleanup. [Andras Iklody]

  Cleanup
- Merge pull request #1440 from RichieB2B/ncsc-nl/cachejson-fix. [Andras
  Iklody]

  Overwrite cached json exports instead of appending
- Added placeholder for authkey on server edit. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Delete old and unused configuration file. [Alexandre Dulaunoy]

  Delete old and unused configuration file
- Merge pull request #1438 from rotanid/mysql-index-add-expires. [Andras
  Iklody]

  chg: add index for cake_sessions expires to MYSQL.sql
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge pull request #1437 from rotanid/less-mysql-dependency. [Andras
  Iklody]

  Less mysql dependency
- Merge pull request #1436 from rotanid/typofix. [Andreas Ziegler]

  chg: fix typo
- Merge branch 'memberslist' into 2.4. [iglocska]
- Merge branch '2.4' into memberslist. [iglocska]
- PyMISP updated to the latest version including the tests. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #1435 from cristianbell/fix_#1355. [Andras Iklody]

  chg: attribute list on view event page sort by date issue #1355
- Merge pull request #1429 from cristianbell/fix_misp2.49.50.js_#1428.
  [Andras Iklody]

  GET misp2.4.49.js - 404 Not Found #1428
- GET misp2.4.49.js - 404 Not Found #1428. [Cristian Bell]
- Update to the latest version of PyMISP. [Alexandre Dulaunoy]
- Version bump. [iglocska]

v2.4.50 (2016-08-10)
--------------------

New
---
- Added export module first iteration. [Iglocska]
- First revision of the new import system. [Iglocska]

Changes
-------
- Handle module results in one place. [Iglocska]
- Remove duplicate line from install doc. [Andreas Ziegler]
- Small cleanup of MYSQL.sql. [Andreas Ziegler]

  - integers instead of strings
  - spaces after commas, not before
  - add&remove spaces
- Updated to the latest version of MISP taxonomies. [Alexandre Dulaunoy]
- Added a warning for site admins for the export page to avoid site
  admins sharing a full export by accident. [Iglocska]
- PyMISP updated to the latest version. [Alexandre Dulaunoy]
- Viewing the public attributes of an event. [Iglocska]

  - new named parameter /public:1 for the event view to view the public information of an event
    - it will filter out all attributes that are not visible to all or inherit the event
    - if an event is not set to distribution all, the view will throw an exception if the parameter is passed
    - it can be used for data views by accessing /events/view/event_id/public:1.json or /events/view/event_id/public:1.xml

  - Also some fixes to the fetchEvent algorithm that ignored optional sharing group and distribution settings for site admins
- Small change to allow for categories to be passed through the
  enrichment modules. [Iglocska]
- Added sync user's org to the sharing group view. [Iglocska]

Fix
---
- Some cleanup. [Iglocska]
- Removed debug. [Iglocska]
- Further work on the modules. [Iglocska]
- More capitalisation. [Iglocska]
- Capitalisation > me. [Iglocska]
- More capitalisation issues. [Iglocska]
- I suck at capitalisation. [Iglocska]
- Lowercasetypo. [Iglocska]
- Fixed some issues with the module services not using the correct
  url/port settings. [Iglocska]
- Fixed checkbox types. [Iglocska]
- Fixed the import module. [Iglocska]

  - correctly populates the resolved attribute list
  - added validation by input type for fields
  - added error message from introspection config to the validation check
  - still needs plenty of refinement
- XSS vulnerability in a malicious feed provider. [iglocska]

  Thanks to Emanuele Gentili from tigersecurity.pro for reporting this vulnerability
- Small change, removal of unnecesary parameter. [iglocska]
- Fixed some issues with the misp export importer and added better
  logging. [iglocska]
- Taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Warning lists updated to the latest version. [Alexandre Dulaunoy]
- Removed the old administrative tools panel. [iglocska]
- Some cleanup in the freetext tool. [iglocska]
- Last pushed/pulled ID are not in the db anymore. [Raphaël Vinot]
- Clarification on menu. [KalyParker]

  Change menu 'Send Credentials' by 'Reset Password' on User's administration page.
  The functionality is to reset the password, not simply send credentials :speak_no_evil:
- Description of the JSON and XML was reversed. [Alexandre Dulaunoy]
- Warninglist warnings not shown if no relations are present. [Iglocska]
- Some fixes to the caching. [Iglocska]

  - invalid linebreaks used for the hids caching
  - added sha256 to the hids caches
- Added progress bar to JSON cache generation. [Iglocska]
- Various fixes to the cached exports. [Iglocska]

  - Tightened the rules for export generation when no valid published events exist
  - Corrected various issues with the progress bars
  - Added the missing JSON export to the caches
  - XML/JSON caches now correctly take into account the cached attachent inclusion setting
  - MISP will now show the users browsing the export page whether attachments will be cached with the current settings or not
  - Added correct progress bar to the HIDS export
- No categories set in a module causes the enrichment to fail.
  [Iglocska]
- If no attribute type change is possible in the resolved
  freetext/enrichment results then the correlation popover didn't fire.
  [Iglocska]
- Missing parameter in the OpenIOC export fixed, fixes #1393. [Iglocska]
- Fixed the white text on white background in proposal relation
  popovers. [Iglocska]
- Some proposal correlations lack the remove event date, for now only
  show it if it exists, fixes #1386. [Iglocska]
- If the types field passed back from the enrichment module is a string
  the import fails. [Iglocska]
- Aligned freetext import with the changes to the attribute resolution.
  [Iglocska]
- Fix to the 2.4.49 SG upgrade. [Iglocska]

  - was incorrectly changing the org_id of the synced sharing group instead of adding the org to the distribution list
- Remove list of instances for roaming sharing groups. [Iglocska]
- Allow distribution level 5 as an option for the upload_sample api,
  fixes #1377. [Iglocska]

Other
-----
- Merge branch 'feature/import-export-modules' into 2.4. [iglocska]
- Merge branch '2.4' into feature/import-export-modules. [iglocska]
- Merge branch '2.4' into feature/import-export-modules. [Iglocska]
- Merge branch '2.4.50' into 2.4. [iglocska]
- Merge branch '1426' into 2.4. [iglocska]
- Jobs creation for admin done under org_id = 0, before was taking the
  id of the group. [ppanero]
- Shibboleth authentication refined (Organization creation if the given
  one in the configuration does not exists). export process displaying
  as queued issue solved. Code changed in JobsController. [ppanero]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #1423 from MISP/elhoim-complete-sentence. [Andras
  Iklody]

  Complete sentence about confirmation of organisation merging
- Complete sentence about confirmation of organisation merging. [David
  André]
- Merge pull request #1403 from Rafiot/fix_dbchange. [Andras Iklody]

  fix: Last pushed/pulled ID are not in the db anymore
- Merge pull request #1417 from RichieB2B/ncsc-nl/fix-exports. [Andras
  Iklody]

  Fix export for non md5/sha1/sha256 types
- Fix export for non md5/sha1/sha256 types. [Richard van den Berg]
- Merge pull request #1413 from deloittem/feature/ansible. [Alexandre
  Dulaunoy]

  MISP ansible
- Init MISP ansible. [Mathieu Deloitte]
- Merge pull request #1410 from ppanero/sso_integration_plugin.
  [Alexandre Dulaunoy]

  SSO plugin (Shibboleth based). Instructions to enable and configure i…
- SSO plugin (Shibboleth based). Instructions to enable and configure it
  are present in the app/Plugin/ShibbAuth/README.md. [ppanero]
- Merge pull request #1411 from kalyparker/changemenu. [Andras Iklody]

  fix: clarification on menu
- Merge pull request #1408 from rotanid/install-doc-fix. [Andreas
  Ziegler]

  chg: remove duplicate line from install doc
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1398 from rotanid/mysql-cleaner. [Andreas Ziegler]

  chg: small cleanup of MYSQL.sql
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Update UPDATE.txt. [Alexandre Dulaunoy]

  Update the UPDATE process according to the development and release cycle.

  git fetch is required and not git pull.
- Merge pull request #1388 from 3c7/fix_categoriesarray. [Andras Iklody]

  Create categories array, if only one category given
- Create categories array, if only one category given. [nkuhnert]
- Merge pull request #1387 from 3c7/feature_customcomments. [Andras
  Iklody]

  Using custom comments for module return values/attributes
- Using custom comments for module return value. [nkuhnert]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]

v2.4.49 (2016-07-22)
--------------------

New
---
- Updates to the module system. [Iglocska]

  - hover modules now require a 0.5 second hover to fire off the query
  - Introduced a new timeout setting to avoid a long lasting query by the module system to stall MISP
- Added a php version check to teh diagnostics page. [Iglocska]
- Work on the refactoring of the module system. [Iglocska]
- Added a tag restriction to restrict the usage of a tag to a single
  organisation. [Iglocska]
- Installation instructions for MISP on Debian 8. [Andreas Ziegler]
- Installation instructions for MISP on Ubuntu 16.04. [Andreas Ziegler]

Changes
-------
- Taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Version bump. [Iglocska]
- Added the sharing group roaming setting to various parts of the
  application. [Iglocska]

  - sharing group add/edit
  - summary view
  - push rule checks
- Use CASE WHEN instead of IF in $virtualFields. [Andreas Ziegler]
- Use 1/0 not true/false for conditions & other boolean sqlquery
  elements. [Andreas Ziegler]
- Tags sharing input style checkbox forced. [Andreas Ziegler]
- Templates sharing input style checkbox forced. [Andreas Ziegler]
- Users autoalert/contactalert not empty & input style checkbox forced.
  [Andreas Ziegler]
- Another cleanup of MYSQL.sql. [Andreas Ziegler]
- Information Security Indicators from ETSI and Microsoft CARO added.
  [Alexandre Dulaunoy]
- Docs UPDATE/UPGRADE use latest tag/release instead of latest commit.
  [Andreas Ziegler]
- Update INSTALL docs to use latest tag/release instead of latest
  commit. [Andreas Ziegler]
- Add semicolon in sql queries. [Andreas Ziegler]
- Remove obsolete quotes from sql query. [Andreas Ziegler]
- Remove obsolete spaces from sql queries. [Andreas Ziegler]
- Add AFTER to sql ADD column statement. [Andreas Ziegler]
- Added additional DB changes required for PR #1334. [Iglocska]
- Added documentation on how to use the /index filters, fixes #1347.
  [Iglocska]

  - Still has to be moved to the MISP book
- Remove obsolete uuid() wrapper. [Andreas Ziegler]
- Remove duplicate array item. [Andreas Ziegler]
- Move tables to retain alphabetical order. [Andreas Ziegler]
- Taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Remove quotes from integers in MYSQL.sql. [Andreas Ziegler]
- KEY/INDEX are synonyms in MySQL, use INDEX only. [Andreas Ziegler]
- Coding conventions in FileAccess.php. [Andreas Ziegler]
- Remove obsolete upload function from ShadowAttribute. [Andreas
  Ziegler]
- Remove obsolete code. [Andreas Ziegler]
- Remove obsolete functions. [Andreas Ziegler]
- Remove quotes from integers in MYSQL.sql. [Andreas Ziegler]
- Use lowercase for int in whole MYSQL.sql. [Andreas Ziegler]
- Remove duplicate spaces from MYSQL.sql. [Andreas Ziegler]
- Added autoRegenerate to default.core.php. [Iglocska]

  - renews the session on activity
- Adding job duration to the "Job done." text. [Cristian Bell]
- Added pull diagram. [Iglocska]
- Allow multiple attributes to be added in one go via the API.
  [Iglocska]
- Updated warninglists. [Iglocska]
- Make script executable. [Iglocska]
- Added a check for the prio worker, added it to the worker tab.
  [Iglocska]
- Remove some obsolete FIXME notes. [Andreas Ziegler]

  the lines have been checked, only secure values are used as part of filenames and paths
- MISP stickers source added - PDF, SVG and PNG. [Alexandre Dulaunoy]
- Small fixes for ubuntu1604 install doc. [Andreas Ziegler]
- Make old debian install doc wheezy-specific. [Andreas Ziegler]
- New default logo on the login screen and some rearranging of the login
  interface elements. [Iglocska]

  - Users with OCD, rejoice!
- Compress IPv6 addresses on import. [Andreas Ziegler]
- Updated to the latest version of the MISP taxonomies. [Alexandre
  Dulaunoy]
- Remove useless empty comments at end of line. [Andreas Ziegler]
- Remove obsolete code. [Andreas Ziegler]
- Fix indention. [Andreas Ziegler]
- Use escapeshellarg() instead of addslashes() with exec() [Andreas
  Ziegler]
- Add fingerprint to pgp key select popover. [Iglocska]
- DescribeTypes broaden access to non-automation users too. [Alexandre
  Dulaunoy]
- Improve file access using new Lib. [Andreas Ziegler]

Fix
---
- Sharing group edit summary tab issues. [Iglocska]

  - if no external organisations were added it still showed the sentence listing them with the list being empty
- Added salt generation to UserInitShell. [Iglocska]
- Don't require users to accept the terms and conditions if they are not
  set, fixes #1381. [Iglocska]
- MySQL error on users.certif_public, fixes #1378. [Iglocska]
- Editing an event via the API should not require the distribution to be
  set in the pushed payload. [Iglocska]

  - The goal is to be able to issue quick edits to single fields instead of having to include any other fields
  - Permissions are checked before the internal _edit method anyway, this was only used to capture sharing groups
- Publish/Alert responses for API users added. [Iglocska]

  - publishing/alerting worked via the API, but it wasn't returning a response
- Small clarification in the diagnostics message for the PHP version.
  [Iglocska]
- Remove the default defined salt #625. [Cristian Bell]
- Removed a DB change that lead to an endless redirect to the news page.
  [Iglocska]
- Added the mitigation against httpoxy as described at httpoxy.org.
  [Iglocska]
- Allow correlations between a proposal and attributes in the same
  event. [Iglocska]
- Tag lookups are not string matches only, substring matches will not
  work. [Iglocska]
- Cherry picking and pulling updates should not require the pull flag to
  be set on an instance. [Iglocska]
- Removed the debug from the previous commit. [Iglocska]
- Fixed an issue with certificate uploades when adding an instance /
  editing an instance. [Iglocska]
- Fix virustotal detection for the freetext import tool, fixes #1373.
  [Iglocska]

  - regex currently looks for https://www.virustotal.com, but https://virustotal.com is also valid
- Roaming mode's functionality had to be reversed as it was still using
  the logic of limiting the server distribution. [Iglocska]
- Added roaming to sharing groups in  the mysql.sql. [Iglocska]
- Updated job_id to process_id for tasks in the leftover spots.
  [Iglocska]
- No need for default tasks in the MYSQL.sql file any longer. [Iglocska]

  - handled by the tasks automatically on view
- Added perm_delegate to the default roles in the MYSQL.sql file.
  [Iglocska]
- Fixed strings for tinyint(1) type fields in the MYSQL.sql file.
  [Iglocska]
- Fixed a typo in the sharing group model. [Iglocska]
- Added the new role permission for perm_delegate to the role model.
  [Iglocska]
- Fixes to the upgrade procedure for 2.4.49. [Iglocska]
- Save the process id of caching too. [Iglocska]
- Reverted version number in MYSQL.sql. [Iglocska]
- Changed field name from job_id -> process_id for tasks. [Iglocska]
- Use php5-redis package instead of pecl for deb7/ubu14. [Andreas
  Ziegler]
- Submodule updates: force overwrite. [Andreas Ziegler]
- Several fixes to the sharing group behavious. [Iglocska]

  - New setting roaming:
    - Until now, users could unselect "Limit instances to which data in this sharing group should be pushed to"
    - This lead to no servers added to the distribution list, and MISP would simply determine, based on the sync rules, whether the host organisation of the remote instance is eligible for the event
    - This works well in most cases, but in some cases, the local instance is not kept after a sync (aliases for the local instance baseurl vs remote instance's view of the url)
    - In these cases the sharing groups ended up being "unlimited", which was not the intent
    - Generally this shouldn't cause any issues as MISP still requires the sync link's organisation to be directly contained in an SG before it would push the event further
    - However, introducing the roaming setting this can be more clearly defined
    - By default, sharing groups are set to non roaming

  - Some further fixes to the sharing group update procedure for 2.4.49

  - Update the roaming status of existing sharing groups. Local sharing groups with no instances attached will become roaming by default, all others are assumed to be non-roaming
- Add own org of sync user to the Sharing group if the sync user is in
  no way contained in the sharing group. [Iglocska]

  - This situation should normally only occur during a pull when the remote end has a sharing group that allows access for all local orgs
- Progress on the sharing group fix for pulled server based sharing
  groups. [Iglocska]
- Cleanup of some messy function call parameters. [Iglocska]
- Fixed an issue where a MISP.org setting with non alphanumeric
  characters could lead to invalid STIX document generation. [Iglocska]
- Added taxonomies/delete to the ACL component. [Iglocska]
- Added functionality to remove taxonomies, fixes #1365. [Iglocska]
- Allow null values for taxonomies expanded column, fixes #1354.
  [Andreas Ziegler]
- Tightened lookups for the addTag / removeTag APIs. [Iglocska]

  - no longer a substring match, users have to specify the full tag name
- Add perm_delegate to MYSQL.sql. [Andreas Ziegler]
- Remove SET from sql ADD column statement. [Andreas Ziegler]
- Update mysql structure for 2.4.49 updates. [Andreas Ziegler]
- Specify correct&specific branches in .gitmodules. [Andreas Ziegler]
- Additional chars =~ in mail address regex. [Andreas Ziegler]
- Use different variable name in sub-loop. [Andreas Ziegler]
- Check for correct event uuid and id. [Andreas Ziegler]
- Fixed an issue where an event view by a malformed UUID would result in
  a lookup against the leading numerical value in the malformed UUID,
  fixes #1338. [Iglocska]
- Add warninglist tables to MYSQL.sql. [Andreas Ziegler]
- Use same default value as in AppModel update mechanism. [Andreas
  Ziegler]
- Tag keywords in attribute search filter has issues with an empty
  newline, fixes #1330. [Iglocska]
- Fixed leading/trailing white spaces from breaking the quick filter on
  the event index, fixes #1329. [Iglocska]
- Fixed an issue with an invalid offset in a comparison when adding
  events. [Iglocska]
- Removed duplicate of the same condition. [Iglocska]
- Filtering on attributes in the event view gives a no attributes
  warning if a tab doesn't contain attributes. [Iglocska]

  - Warning now only triggers if the event doesn't have any attributes in any tabs
- Throw exception for malformed xml file. [Andreas Ziegler]
- Set default value for realFileName. [Andreas Ziegler]
- Throw exception if necessary config cant be read. [Andreas Ziegler]
- Fixed two issues for API add event corner cases, fixes #1298.
  [Iglocska]

  - Correctly handle old style creator org fields ("orgc":orgc_string)
  - Correctly handle new tags with no colour set
- Follow up to the previous patch, same thing for log searches.
  [Iglocska]
- Move case statement and add break. [Andreas Ziegler]
- Fixed an issue with org admins having too much access via the logs.
  [Iglocska]
- Organisations updated with no changes cause erroneous log entries,
  fixes #1099. [Iglocska]
- Allow the export of an empty event in MISP JSON/XML format, fixes
  #1295. [Iglocska]
- Fixed an issue that caused MISP's capture org to disambiguate on the
  name instead of the UUID in some cases. [Iglocska]

  - Due to a fallback mechanism the disambiguation happened on the name if there was no UUID match during the saving of an event instead of creating a new organisation. This was an issue if a remote org changed UUID for example.
- Added domain|ip to the OpenIOC export. [Iglocska]

  - also, the new system should be much easier to extend with new mapping options and is generally a lot cleaner.
  - It would be more complete if Airbus wouldn't have skimped on power outlets on the A380s....
- Rework of the IOC export component, fixes #1292. [Iglocska]
- Ambiguous order field fixed, fixes REST sort of index. Fixes #1266.
  [Iglocska]

  - Fixes an issue where viewing the index of an instance remotely returns no events if sorted on a field.
  - This was caused by some ambiguous field names (such as ID)
  - Fixed by prepending the sorted field name by "Event."
- Fixed an issue with the attribute search incorrectly showing org
  admins the edit button for attributes they don't own, fixes #1278.
  [Iglocska]

  - Also added a way to propose directly from the attribute list / search results
- Empty comments may be added to events #1263. [Iglocska]

  - moved to plain jquery
  - check on back+frontend
  - better responses when adding events
  - fixed an issue with the org_id not being selected for posts
- Fixed a notice error with the attribute pagination. [Iglocska]
- Reverted previous change. [Iglocska]
- Secureauth removed from the config dump. [Iglocska]
- Old upgrade SQL script moved to legacy directory. [Alexandre Dulaunoy]
- Removal of unused file. [Alexandre Dulaunoy]
- Removed the field restrictions from the save() calls in the certauth
  plugin. [Iglocska]

  - apparently cakephp also removes those fields from the beforevalidation hook, meaning that a plugin can potentially escape any data consolidation methods. Not sure if this is intended behaviour by cakephp...
- Fix to an issue with default values not set by the beforeValidate of
  users. [Iglocska]
- Case-insensitive functions calls. [Andreas Ziegler]
- Removed some useless loops, fixes #1231. [Iglocska]
- Reverted the change from addslashes -> escapeshellargs. Will revisit
  the reason it was causing the uploads to fail at a later point in
  time. [Iglocska]
- Multiple values for the restsearch quickfilter added. [Iglocska]
- Proposals now have the correct page title. [Iglocska]

Other
-----
- Merge branch '2.4.49' into 2.4. [Iglocska]
- Merge branch '2.4' into 2.4.49. [Iglocska]

  Conflicts:
  	app/Controller/AppController.php
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #1380 from treyka/patch-1. [Andras Iklody]

  Small documentation clarification
- Small documentation clarification. [Trey Darley]
- Merge branch 'feature/modulerework' into 2.4. [Iglocska]
- Merge branch '2.4' into feature/modulerework. [Iglocska]

  Conflicts:
  	app/Model/Module.php
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1375 from cristianbell/fix_625_default_salt.
  [Andras Iklody]

  fix: Remove the default defined salt #625
- Merge branch '2.4' into feature/modulerework. [Iglocska]

  Conflicts:
  	app/Model/Module.php
  	app/Model/Server.php
- Merge branch '2.4' of https://github.com/MISP/MISP into
  feature/modulerework. [Iglocska]

  Conflicts:
  	app/Model/Server.php
- Merge branch '2.4' into 2.4.49. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch 'perm_delegate' into 2.4. [Iglocska]
- - Allow delegation when unpublishedprivate is set - Use perm_delegate
  instead of perm_publish for delegation. [Richard van den Berg]
- Update the Javascript package. [Iglocska]
- Fix Change the old job_id field to process_id in the tasks table.
  [Iglocska]
- Merge branch 'email' into 2.4. [Iglocska]

  Conflicts:
  	INSTALL/MYSQL.sql
- For upgrades. [Steve Fossen]
- Mysql for bug #1180. [Steve Fossen]
- Update initial install mysql too. [Steve Fossen]
- Email not being sent causing sync to fail. [Steve Fossen]

  main.ERROR: {"queue":"default","id":"a8bc18ea021640ebce6f9354c2573718","class":"ServerShell","args":[["pull","1","2","full","2770"]]} failed: SQLSTATE[HY000]: General error: 1364 Field 'email' doesn't have a default value {"type":"fail","log":"SQLSTATE[HY000]: General error: 1364 Field 'email' doesn't have a default value",
- Merge branch 'jobid' into 2.4. [Iglocska]
- Change job_id to varchar to resolve #1180. [I-am-Sherlocked]

  As mentioned in #1180, every spot that task->job_id is being set:

  app/Model/Task.php

  app/Controller/TasksController.php

  it's the returned value from CakeResque::enqueueAt which is the process_id (MD5).
  And I think renaming the field to process_id might be more representative of what it is?
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1367 from sfossen/patch-27. [Andras Iklody]

  log created is datetime not timestamp.
- Log created is datetime not timestamp. [Steve Fossen]
- Merge pull request #1366 from sfossen/patch-26. [Andras Iklody]

  rename to php variables match sql model
- Rename to php variables match sql model. [Steve Fossen]

  causing sync to fail, when new sharing groups are created.
- Merge pull request #1371 from rotanid/redis-doc-fix. [Andreas Ziegler]

  fix: doc: use php5-redis package instead of pecl for deb7/ubu14
- Merge pull request #1370 from rotanid/update-doc-fix. [Andreas
  Ziegler]

  fix: submodule updates: force overwrite
- Merge branch 'boolean' into 2.4. [Iglocska]
- Merge pull request #1362 from rotanid/taxonomy-expanded-null-value.
  [Andreas Ziegler]

  fix: allow null values for taxonomies expanded column, fixes #1354
- Merge pull request #1361 from rotanid/mysqlsql-clean. [Andreas
  Ziegler]

  chg: another cleanup of MYSQL.sql
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1353 from rotanid/install-update-doc-improvements.
  [Andras Iklody]

  Install/update doc improvements - releases instead of random commits
- Revert "Revert "chg: remove obsolete uuid() wrapper"" [Iglocska]

  This reverts commit bae6eadfe739a2d58b23dbe0d6263360500808f7.
- Merge pull request #1352 from rotanid/mysql-updates-cleanup. [Andras
  Iklody]

  Mysql updates cleanup
- Merge pull request #1351 from rotanid/sql-bugfix. [Andras Iklody]

  Sql bugfix & add to mysql.sql
- Merge pull request #1343 from rotanid/update-appmodel-mysql-update.
  [Andras Iklody]

  update mysql structure for 2.4.49 updates
- Merge pull request #1350 from rotanid/gitmodules-fix. [Andras Iklody]

  fix: specify correct&specific branches in .gitmodules
- Merge pull request #1349 from rotanid/mail-regex-change. [Andreas
  Ziegler]

  additional chars in mail address regex
- Revert "chg: remove obsolete uuid() wrapper" [Iglocska]

  This reverts commit 77ca0f8dd46222c2a0c7bc38608e0215988f33f3.
- Merge pull request #1342 from rotanid/variable-in-loop. [Andras
  Iklody]

  fix: use different variable name in sub-loop
- Merge pull request #1341 from rotanid/remove-uuid-wrapper. [Andras
  Iklody]

  remove obsolete uuid() wrapper
- Merge pull request #1340 from rotanid/small-cleanup. [Andreas Ziegler]

  chg: remove duplicate array item
- Revert "fix: Fixed an issue where an event view by a malformed UUID
  would result in a lookup against the leading numerical value in the
  malformed UUID, fixes #1338" [Iglocska]

  This reverts commit 1b064133755b814152f9c3b988ff0b93f68af326.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1339 from rotanid/bugfix-uuid-id-check. [Andras
  Iklody]

  fix: check for correct event uuid and id
- Merge pull request #1337 from CheYenBzh/2.4. [Andreas Ziegler]

  openIOC import issue / fileAccess class not found / Update EventsController.php
- Update EventsController.php. [CheYenBzh]
- Merge pull request #1332 from rotanid/mysql-sql-cleanup. [Andras
  Iklody]

  MYSQL.sql cleanup #3
- Update db_version in MYSQL.sql. [Andreas Ziegler]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1327 from rotanid/mysql-sql-cleanup. [Andras
  Iklody]

  MYSQL.sql cleanup #2
- Merge pull request #1326 from rotanid/fopen-handling-clean. [Andreas
  Ziegler]

  chg: coding conventions in FileAccess.php
- Merge pull request #1283 from RichieB2B/ncsc/fix-push-events. [Andras
  Iklody]

  Push events to server with push rules on non-exportable tags
- Push events to server with push rules on non-exportable tags. [Richard
  van den Berg]
- Merge pull request #1286 from rotanid/shadowattribute-
  uploadattachment-removal. [Andras Iklody]

  remove obsolete upload function from ShadowAttribute
- Merge pull request #1256 from rotanid/cleanup2. [Andras Iklody]

  misc cleanup round 3
- Merge branch 'cleanup3' into 2.4. [Iglocska]
- Merge branch 'write' into 2.4. [Iglocska]
- Merge branch '2.4' into write. [Iglocska]
- Merge pull request #1324 from rotanid/mysql-cleanup. [Andras Iklody]

  MYSQL.sql cleanup
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1319 from
  cristianbell/fix-939_graceful_maintenance_page. [Andras Iklody]

  issue 993: Graceful maintenance message.
- Issue 993: Graceful maintenance message. [Cristian Bell]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Updated MISP taxonomies. [Alexandre Dulaunoy]
- Merge pull request #1321 from
  cristianbell/chg_adding_job_duration_time. [Andras Iklody]

  chg: adding job duration to the "Job done." text.
- Merge pull request #1320 from Rafiot/update_tests. [Raphaël Vinot]

  Update testing
- Use more reasonable tests. [Raphaël Vinot]
- Update testing. [Raphaël Vinot]
- Merge pull request #1317 from cristianbell/fix-
  mail_jobs_date_modified. [Andras Iklody]

  Email jobs do not update the date modified once completed.
- Email jobs do not update the date modified once completed. [Cristian
  Bell]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1316 from deralexxx/patch-2. [Andras Iklody]

  Update UPDATE.txt
- Update UPDATE.txt. [Alexander J]
- Merge pull request #1315 from cristianbell/fix_issue_1289. [Andras
  Iklody]

  issue 1289 - Cache jobs do not update the date modified once completed.
- Issue 1289 - Cache jobs do not update the date modified once
  completed. I also added this to the contactemail(), publish(),
  postsemail() and alertemail(). But it's commented out as it's not part
  of the issue. I can commit it again w/ the lines uncommented.
  [Cristian Bell]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1309 from rotanid/gfi-exceptions. [Andras Iklody]

  exceptions in _readGfiXml()
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1288 from peasead/2.4. [Andras Iklody]

  updated CentOS 7 INSTALL guide
- Updated CentOS 7 INSTALL guide. [Andrew Pease]
- Merge pull request #1307 from rotanid/bugfix. [Andras Iklody]

  fix: move case statement and add break
- Merge branch 'test' into 2.4. [Iglocska]
- Add prio worker. [Richard van den Berg]
- Create new prio queue for publishing events. [Richard van den Berg]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Misp-warninglists updated. [Alexandre Dulaunoy]
- Merge pull request #1297 from cristianbell/fix-
  minor_CSS_HTML_bug_fixes. [Andras Iklody]

  fix minor css and html issues
- Fix minor css and html issues. [Cristian Bell]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1294 from cristianbell/chg-
  loader_update_interval_increase. [Andras Iklody]

  changing the loading bar update interval from 1000 to 3000 (as it is …
- Changing the loading bar update interval from 1000 to 3000 (as it is
  also in the jobs list); [Cristian Bell]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1282 from rotanid/fixme-cleanup. [Andreas Ziegler]

  remove some obsolete FIXME notes
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1277 from rotanid/install-doc. [Alexandre
  Dulaunoy]

  Install document updates
- Merge pull request #1276 from rotanid/doc-ubu. [Alexandre Dulaunoy]

  installation instructions for MISP on Ubuntu 16.04
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Fix #1272. [Alexandre Dulaunoy]
- Merge pull request #1271 from sfossen/patch-25. [Alexandre Dulaunoy]

  typo in alter
- Typo in alter. [Steve Fossen]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1264 from rotanid/ipv6-compress. [Andras Iklody]

  compress IPv6 addresses on import
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #1260 from sfossen/patch-24. [Andras Iklody]

  Organization UUID NULLable
- Fix for update script. [Steve Fossen]
- Organization UUID nullable. [Steve Fossen]

  1. For older MISP there isn't UUID
  2. UUID in out of order RelatedEvent processing compared to first Event from Organization
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Latest version of PyMISP included. [Alexandre Dulaunoy]
- Merge pull request #1255 from rotanid/bugfix. [Andreas Ziegler]

  fix: case-insensitive functions calls
- Merge pull request #1238 from rotanid/cleanup. [Andreas Ziegler]

  cleanup obsolete code
- Merge pull request #1254 from rotanid/escapeshellarg. [Andras Iklody]

  chg: use escapeshellarg() instead of addslashes() with exec()
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]

v2.4.48 (2016-06-08)
--------------------

New
---
- Enable/disable feed via API. [Iglocska]

  - simply POST to /feeds/enable/feed_id or /feeds/disable/feed_id to enable and disable a feed

Changes
-------
- Version bump. [Iglocska]
- Lowered the level of the custom css setting. [Iglocska]
- Added the option to load a custom css after the default css.
  [Iglocska]
- Update .gitignore to include .idea. [Andreas Ziegler]

  .idea contains settings of IDEs based on IDEA by IntelliJ
- Remove obsolete variables. [Andreas Ziegler]
- Remove obsolete files. [Andreas Ziegler]
- Use escapeshellarg() instead of addslashes() with exec() [Andreas
  Ziegler]
- Use consistent lowercase true/false. [Andreas Ziegler]
- Update jquery to 2.2.4 & jquery-ui to 1.11.4. [Andreas Ziegler]
- Add newline character before EOF to non-minified (text-)files.
  [Andreas Ziegler]
- Error handling after zip execution. [Andreas Ziegler]
- Remove comment: there is no exec wrapper in cakephp. [Andreas Ziegler]
- Remove handling of unsupported OS Windows. [Andreas Ziegler]
- Changed the naming convention of some scripts and updated them.
  [Iglocska]
- ValueIsUnique assumed the deleted flag to be set on attributes.
  [Iglocska]
- Events without attributes - warning for users and owner, fixes #1189.
  [Iglocska]
- Changed the default bootstrap to not append port 80 / port 443 in any
  case. [Iglocska]

  - it was causing issues for a user using a rather exotic configuration

Fix
---
- Fix to a bug that allowed adding server connections without an org.
  [Iglocska]
- Some small fixes. [Iglocska]

  - Lowered TLP string setting to low importance
  - auto set authkey if not set during user creation
- Add missing return statement. [Andreas Ziegler]
- Change to correct variable name. [Andreas Ziegler]
- Case-insensitive function calls. [Andreas Ziegler]
- Small fix to the top menu when debug mode is enabled. [Iglocska]
- Brace ordering. [Andreas Ziegler]
- Dont override type variable. [Andreas Ziegler]
- Case-sensitive functions calls. [Andreas Ziegler]
- Move unlink() to correct location. [Andreas Ziegler]
- Reverted two removals of dynamically accessed vars that shouldn't be
  removed. [Iglocska]
- Left off change in view_graph.ctp. [Iglocska]
- Can't add Elements to a newly created Template. fixes #1188.
  [iglocska]
- Fixed epel url for centos 7.x. [Iglocska]
- Minor cosmetic issue in distribution, fixes #1197. [Iglocska]
- Use of unset variable in Model/Event.php sendContactEmailRouter(),
  fixes #1210. [Iglocska]
- Fix to a duplicate parameter passed to fetchevent instead of passing
  the "to" parameter as expected. [Iglocska]
- Reverted a patch to allow organisations without uuids to be added.
  [Iglocska]
- Cannot delete users, fixes #1200. [Iglocska]
- Fixed an issue with the text export not returning anything if used via
  the API. [Iglocska]
- Default bootstrap fixed for http. [Iglocska]
- Fixed an issue with the default bootstrap.default.php. [Iglocska]
- Two small fixes. [Iglocska]

  - search by uuid on the event index via the quickfilters
  - view button on the disussion index added to make the UI a bit more consistent
  - This unimaginative patch would not have existed without an uncomfortable British Aerospace ATP
- Added the date field to the related attribute popover, fixes #1190.
  [Iglocska]
- Fix to a previous change of the bootstrap.php file to accomodate for
  some exotic setups. [Iglocska]
- Accidental invalid debug code left in the verifyGPG admin task
  breaking the script. [Iglocska]
- Fix to an error with MISP and MySQL 5.7+ caused by no order clause on
  a distinct select query, fixes #1188. [Iglocska]
- Cleanup of the password reset tool. [Iglocska]
- A removed user was giving some notice errors on the thread index.
  [Iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Add gitter webhook. [Raphaël Vinot]
- Merge pull request #1237 from rotanid/bugfix3. [Andras Iklody]

  fix: add missing return statement
- Merge pull request #1235 from rotanid/bugfix1. [Andras Iklody]

  fix: change to correct variable name
- Merge pull request #1236 from rotanid/bugfix2. [Andras Iklody]

  fix: case-insensitive function calls
- Merge pull request #1243 from SleuthKid/feature/nav-ng. [Andras
  Iklody]

  Small, non breaking changes to the MISP look and feel
- Small, non breaking changes to the MISP look and feel: - Removed old
  school glass stuff from navbars (bye bye) - Removed blue flame effect
  from MISP branding (srsly WHY?) - Minor ajustments to flush the
  changes globally. [Robert Haist]
- Merge pull request #1244 from FIRSTdotorg/2.4. [Andras Iklody]

  fixed compatibility issues between the CertificateAuth plugin and Apache
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Guilherme Capilé]
- Merge pull request #1242 from FIRSTdotorg/2.4. [Andras Iklody]

  create an Organisation if a string is provided (and not org_id)
- Merge pull request #1241 from gitter-badger/gitter-badge. [Andras
  Iklody]

  Add a Gitter chat badge to README.md
- Add Gitter badge. [The Gitter Badger]
- Apache compatibility adjustments. [Guilherme Capilé]
- Create an Organisation if a string is provided (and not org_id)
  [Guilherme Capilé]
- Merge pull request #1240 from cristianbell/issue-1107. [Andras Iklody]

  Issue 1107
- TLP:AMBER hardcoded in email subject #1107 - adding a default value.
  [Cristian Bell]
- TLP:AMBER hardcoded in email subject #1107. [Cristian Bell]
- Merge pull request #1239 from RichieB2B/ncsc-nl/fix-certauth. [Andras
  Iklody]

  Fix CertAuth plugin
- Add userDefaults explanation. [Richard van den Berg]
- Add missing Role, Organization, Server arrays to user. [Richard van
  den Berg]
- Fix spaces. [Richard van den Berg]
- Add CertAuth.userDefaults example. [Richard van den Berg]
- Fix parentheses. [Richard van den Berg]
- Merge pull request #1227 from rotanid/patch-1. [Andras Iklody]

  chg: update .gitignore to include .idea
- Merge pull request #1230 from rotanid/bugfix2. [Andras Iklody]

  fix: brace ordering
- Merge pull request #1233 from rotanid/cleanup-variables. [Andras
  Iklody]

  chg: remove obsolete variables
- Merge pull request #1229 from rotanid/bugfix1. [Andras Iklody]

  fix: dont override type variable
- Merge pull request #1232 from rotanid/cleanup-files. [Andras Iklody]

  chg: remove obsolete files
- Update bootstrap-timepicker to 0.3.0. [Raphaël Vinot]
- Rollback colorpicker to 2.0.0 ans update datepicker to 1.5.1. [Raphaël
  Vinot]
- Update bootstrap-colorpicker. [Raphaël Vinot]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Raphaël Vinot]
- Merge pull request #1228 from rotanid/case-sensitivity. [Andras
  Iklody]

  fix: case-sensitive functions calls
- Revert last change, using the version of the CSS/JS does not work.
  [Raphaël Vinot]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Raphaël Vinot]
- Merge pull request #1225 from rotanid/escapeshellarg. [Andras Iklody]

  chg: use escapeshellarg() instead of addslashes() with exec()
- Merge pull request #1224 from rotanid/true-false. [Andras Iklody]

  chg: use consistent lowercase true/false
- Merge pull request #1223 from rotanid/unlink. [Andras Iklody]

  fix: move unlink() to correct location
- Add css/js update script, update code accordingly. [Raphaël Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]

  Conflicts:
  	app/webroot/js/jquery-toc.js
- Merge pull request #1219 from rotanid/jquery-update. [Andras Iklody]

  chg: update jquery to 2.2.4 & jquery-ui to 1.11.4
- Merge pull request #1218 from rotanid/newlines. [Andras Iklody]

  chg: add newline character before EOF to non-minified (text-)files
- Merge pull request #1217 from rotanid/zip-exec-error-handling. [Andras
  Iklody]

  Zip exec error handling
- Merge pull request #1216 from rotanid/no-windows. [Andras Iklody]

  chg: remove handling of unsupported OS Windows
- Merge pull request #1214 from rotanid/fileaccesshandling. [Andras
  Iklody]
- EventsController: optimise file handling. [Andreas Ziegler]
- Merge pull request #1213 from rotanid/ModelEventCleanup2. [Andras
  Iklody]

  Model/Event.php cleanup 2
- Model/Event.php: remove unused functions. [Andreas Ziegler]
- Model/Event.php: remove unused variables. [Andreas Ziegler]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]

  Conflicts:
  	app/Model/Event.php
- Merge pull request #1212 from rotanid/ModelEventCleanup. [Andras
  Iklody]

  Model/Event.php cleanup
- Model/Event.php: use different key variable in sub-loop. [Andreas
  Ziegler]
- Model/Event.php: fix indention. [Andreas Ziegler]
- Model/Event.php: fix method invocation. [Andreas Ziegler]
- Model/Event.php: add variable defaults. [Andreas Ziegler]
- Model/Event.php: correct function naming. [Andreas Ziegler]
- Model/Event.php: remove duplicate array keys. [Andreas Ziegler]
- Merge pull request #1211 from rotanid/braces. [Andras Iklody]

  Braces
- Use consistent spacing around else if. [Andreas Ziegler]
- Use consistent spacing around else. [Andreas Ziegler]
- Remove space after unset before opening brace. [Andreas Ziegler]
- Add space after keywords if/for/foreach/while/switch/catch. [Andreas
  Ziegler]
- Add space before opening curly brackets. [Andreas Ziegler]
- Merge pull request #1209 from rotanid/removal. [Andras Iklody]

  WhitelistsController.php: remove obsolete variable
- WhitelistsController.php: remove obsolete variable. [Andreas Ziegler]
- Merge pull request #1207 from rotanid/semicolon. [Andras Iklody]

  remove obsolete semicolon after closing curly bracket
- Remove obsolete semicolon after closing curly bracket. [Andreas
  Ziegler]
- Merge pull request #1206 from rotanid/obsolete-spaces. [Andras Iklody]

  Removal of obsolete whitespace/spaces
- Remove single spaces after tabs. [Andreas Ziegler]
- Remove single spaces in front of tabs. [Andreas Ziegler]
- Remove whitespace at end of line. [Andreas Ziegler]
- Remove empty lines at end of files. [Andreas Ziegler]
- Remove whitespace (space/tab) from empty lines. [Andreas Ziegler]
- Merge pull request #1203 from sfossen/patch-23. [Andras Iklody]

  allow related events to send org uuid, since events send them already
- Allow related events to send org uuid, since events send them already.
  [Steve Fossen]

  There is the potential, that an org shows up in the RelatedEvent before it shows up in an Event and causes sync to fail. Already submitted a pull request to fix the crash, but potential for incomplete data.
- Merge pull request #1202 from sfossen/patch-22. [Andras Iklody]

  not local and no uuid, it's an invalid organisation
- Not local and no uuid, it's an invalid organisation. [Steve Fossen]

  sync fails with
  [2016-06-01 21:04:26] main.ERROR: {"queue":"default","id":"99b7d5ef61e24389ea2edf8c3f209856","class":"ServerShell","args":[["pull","1","1","full","2075"]]} failed: SQLSTATE[HY000]: General error: 1364 Field 'uuid' doesn't have a default value {"type":"fail","log":"SQLSTATE[HY000]: General error: 1364 Field 'uuid' doesn't have a default value","job_id":"99b7d5ef61e24389ea2edf8c3f209856","time":55606,"worker":"misp:14872"} []
- Merge pull request #1154 from sfossen/patch-12. [Andras Iklody]

  reduce warnings in debug log
- Reduce warnings in debug log. [Steve Fossen]

  - don't query if we don't have the key
  - set missing keys to null in foreach
- Merge remote-tracking branch 'origin/2.4' into 2.4. [Iglocska]
- Update PULL_REQUEST_TEMPLATE.md. [Raphaël Vinot]
- Update ISSUE_TEMPLATE.md. [Raphaël Vinot]
- Merge pull request #1193 from rotanid/defaults. [Andras Iklody]

  add some defaults
- Add some variable defaults. [Andreas Ziegler]
- Merge pull request #1192 from rotanid/removal. [Andras Iklody]

  Removal of obsolete code
- Remove/update obsolete code. [Andreas Ziegler]
- Remove unused functions. [Andreas Ziegler]
- Merge branch 'rotanid1' into 2.4. [Iglocska]
- Remove/update obsolete code. [Andreas Ziegler]
- Remove unused functions. [Andreas Ziegler]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1165 from rotanid/misc2. [Andras Iklody]

  misc cleanup round 2
- Explicit function call. [Andreas Ziegler]
- Remove obsolete space from: File ( [Andreas Ziegler]
- Explain regex and make it a bit simpler. [Andreas Ziegler]
- Fix upper/lowercase issues. [Andreas Ziegler]
- Remove commented out codelines. [Andreas Ziegler]
- Model/User.php: indention fixed. [Andreas Ziegler]
- Reformatting, indention, comment fixes. [Andreas Ziegler]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1199 from sfossen/patch-21. [Andras Iklody]

  remove continue at the bottom of loop
- Remove continue at the bottom of loop. [Steve Fossen]
- Merge pull request #1198 from Rafiot/composer. [Raphaël Vinot]

  Use composer to install cake resque
- Use composer to install cake resque, remove old dependencies. [Raphaël
  Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Update PULL_REQUEST_TEMPLATE.md. [Raphaël Vinot]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Raphaël Vinot]
- Add PR template. [Raphaël Vinot]
- Update ISSUE_TEMPLATE.md. [Raphaël Vinot]
- Fix english in template. [Raphaël Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4. [Raphaël
  Vinot]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1194 from rotanid/bugfix. [Andras Iklody]

  UsersController.php: remove duplicate array key
- UsersController.php: remove duplicate array key. [Andreas Ziegler]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1129 from I-am-Sherlocked/patch-4. [Andras Iklody]

  Casting the sharing_group_id to int value
- Throw exception for sharing group if unauthorised user. [I-am-
  Sherlocked]

  Instead of returning a false value for sharing_group_id, throw an exception if user is not authorised to save modifications to that sharing group.
- Fixing the error caused by a false sharing_group_id. [I-am-Sherlocked]

  If SharingGroup->captureSG returned false indicating it did not save the sharing group, then distribution should be set to 0, and the sharing_group_id to an integer 0.
- Casting the sharing_group_id to int value. [I-am-Sherlocked]

  Saving the sharing_group_id as it is returned by CaptureSG results in Error: [PDOException] SQLSTATE[HY000]: General error: 1366 Incorrect integer value: '' for column 'sharing_group_id' at row 1. Wrapping it in intval will insert the correct int value.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Warning lists updated to the latest version. [Alexandre Dulaunoy]
- Merge pull request #1182 from sfossen/patch-17. [Andras Iklody]

  Allow empty events in pull since they are pushed and importable
- Allow empty events in pull since they are pushed and importable.
  [Steve Fossen]

  Pulling events from a MISP instance didn't match the events imported from that same MISP instance export, nor did it match events published onto that MISP instance and viewable.

  Events without attributes:
      1) can be pushed
      2) imported
      3) exported

  This fix allows them to be pulled to allow consistency with all other actions.
- Merge pull request #1186 from sfossen/patch-20. [Andras Iklody]

  remove deprecation warning.
- Remove deprecation warning. [Steve Fossen]

  Deprecated (16384): Using key `action` is deprecated, use `url` directly instead. [APP/Lib/cakephp/lib/Cake/View/Helper/FormHelper.php, line 383]
- Merge pull request #1185 from sfossen/patch-19. [Andras Iklody]

  don't query every event for proposals, when you don't have permission…
- Don't query every event for proposals, when you don't have permission
  to get proposals. [Steve Fossen]

  A little hacky, but without correct permission, the returning null causes the else case ( Fallback for < 2.4.7 instances )  which then queries every event, for proposals which it doesn't have permission for, so wastes resources on both side.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1184 from sfossen/patch-18. [Andras Iklody]

  don't bother trimming if it's going to exit anyways.
- Don't bother trimming if it's going to exit anyways. [Steve Fossen]

  removes a warning on empty attribute.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1181 from sfossen/patch-16. [Andras Iklody]

  typo
- Typo. [Steve Fossen]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1168 from sfossen/patch-15. [Andras Iklody]

  remove default value from the call.
- Update Server.php. [Steve Fossen]
- Merge pull request #1169 from sfossen/patch-14. [Andras Iklody]

  change default to match check and downloadEventFromServer
- Change default to match check and downloadEventFromServer. [Steve
  Fossen]
- Merge pull request #1159 from Deventual/patch-1. [Andras Iklody]

  Update UPDATE.txt
- Update UPDATE.txt. [Deventual]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Add issue template. [Raphaël Vinot]

v2.4.47 (2016-05-24)
--------------------

Fix
---
- Wrong variable name in __ipv6InCidr() [Andreas Ziegler]
- Reverted a change that broke PyMISP's copy_list.py To be revisited for
  a better solution. [Iglocska]
- Removed duplicate array keys, fixes #1162. [Iglocska]
- Fixed a broken tag situation when the line wrap happened just between
  the tag and its delete button. [Iglocska]
- Tags were distorted when too many where in a single line due to a
  crappy table. [Iglocska]
- Left off a change. [Iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1166 from RichieB2B/ncsc-nl/fix-mod_proxy_fcgi-
  auth. [Andras Iklody]

  Fix for mod_proxy_fcgi + Apache 2.2 REST API authentication
- Pass Authorization HTTP header to php-fpm environment. [Richard van
  den Berg]
- Merge pull request #1164 from rotanid/bugfix. [Andras Iklody]

  fix: wrong variable name in __ipv6InCidr()

v2.4.46 (2016-05-23)
--------------------

New
---
- Added Statixtics for taxonomy and tag usage, fixes 1158. [Iglocska]

Changes
-------
- Tiny fix to an if statement. [Iglocska]
- Added sort by value or name option for tag statistics API. [Iglocska]

  - usage: mymisp/tags/tagStatistics/[percentage]/[name-sort]
    - both percentage and name-sort accept true/false
    - false is always the default setting
    - percentage set to true will show the tags by % instead of a count
    - name-sort set to true will sort the results by the namespace, alternatively by the count/percentage

Fix
---
- Fixed some wonky behaviour with the popover enrichment and the warning
  list popover. [Iglocska]
- Fixed an issue with the attribute search timing out. [Iglocska]
- Removed a superfluous line that broke lists of values from being
  passed to the restsearch API. [Iglocska]
- Bug causing the attribute search to truncate the search terms when a
  list of organisations is searched for, fixes #1156. [Iglocska]
- Added hard-delete for soft-deleted attributes, fixes #1144. [Iglocska]
- Added the option for users to see and undelete attributes if an event
  was created by their org, fixes #1144. [Iglocska]

  - Also some minor fixes to the ACL

Other
-----
- Merge pull request #1153 from sfossen/patch-13. [Andras Iklody]

  Handle error in getEventIdsFromServer better
- Handle error in getEventIdsFromServer better. [Steve Fossen]
- Merge pull request #1152 from rotanid/misc1. [Andras Iklody]

  misc cleanup round 1
- Misc cleanup. [Andreas Ziegler]
- Merge pull request #1155 from rotanid/bugfix. [Andras Iklody]

  IOCImportComponent.php: correct order of braces
- IOCImportComponent.php: correct order of braces. [Andreas Ziegler]
- Merge pull request #1151 from rotanid/filechecks. [Andras Iklody]

  small change to file checks
- Small change to file checks, use readable() instead of exists()
  [Andreas Ziegler]
- Merge pull request #1150 from rotanid/wording. [Andras Iklody]

  improve some text passages
- Improve some text passages. [Andreas Ziegler]

v2.4.45 (2016-05-20)
--------------------

New
---
- Added the news functionality back. [Iglocska]

  - admins can add/edit/delete news items
  - users get redirected if there is a newsitem that they haven't seen yet

Changes
-------
- Some additional cleanup after the merge of some obsolete stuff.
  [Iglocska]
- Some cleanup of old unused stuff. [Iglocska]
- Some more changes to the default bootstrap determination. [Iglocska]

  - updated bootstrap.default.php
- Added php5-json to ubuntu/debian installation guide. [Iglocska]

  - Added php5-json in case it is not installed by default thanks to the do no evil clause in the license (ノಠ益ಠ)ノ彡┻━┻
- Small fix to the logs index. [Iglocska]
- Small cosmetic change on the log index. [Iglocska]

Fix
---
- Fix to the redirect issues on logout. [Iglocska]
- Added the new db changes to the SQL files. [Iglocska]
- Some more cleanup on the redirects at login. [Iglocska]
- Removed redirect to the news page if no user is logged on. [Iglocska]
- Fixed an issue that would create blank server entries after a
  scheduled pull, fixes #1142. [Iglocska]
- Soft deleted attributes editable and they show up using attribute
  search, fixes #1144. [Iglocska]
- Wrong default setting in bootstrap.php fixed. [Iglocska]
- Fix to an issue causing the sync to fail due to an invalid version
  error for no reason. [Iglocska]
- Revert to relative paths only for requests coming via the command
  line. [Iglocska]

  - baseurl not auto-resolved if the $_SERVER['SERVER_ADDR'] isn't populated
  - solves issues with background workers executing requests on an instance where no baseurl is set
- Resolved commented out request type checks, fixes #1141. [Iglocska]
- Fixes to issues with MYSQL >= 5.7. [iglocska]
- Contact Users Form Email Issue fixed, fixes #1130. [Iglocska]

Other
-----
- Merge branch 'feature/news' into 2.4. [Iglocska]
- Added url detection to the news items. [Iglocska]
- Merge branch 'pr1148' into 2.4. [Iglocska]
- Simplify file readability check. [Andreas Ziegler]
- Remove unused code-lines. [Andreas Ziegler]
- Remove comment: there is no exec wrapper in cakephp. [Andreas Ziegler]
- Remove commented out code lines. [Andreas Ziegler]
- Remove duplicate sha256 case. [Andreas Ziegler]
- Remove duplicate code. [Andreas Ziegler]
- Fix an array declaration. [Andreas Ziegler]
- Attribute.php: update comments, indention, readability. [Andreas
  Ziegler]
- Merge branch 'pr1146' into 2.4. [Iglocska]

  Conflicts:
  	app/Controller/TemplatesController.php
  	app/Controller/UsersController.php
- Progressive removal of commented out if-statements. [Andreas Ziegler]
- AttributesController: remove obsolete commented code. [Andreas
  Ziegler]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1137 from rotanid/bugfix-pr-976-kerberos. [Andras
  Iklody]

  improve quality of PR#976 (kerberos auth)
- Improve quality of PR#976 (kerberos auth) [Andreas Ziegler]
- Merge pull request #1139 from rotanid/improvements. [Andras Iklody]

  improvements for comments & a regex
- Explain regex and make it a bit simpler. [Andreas Ziegler]
- AttributesController.php improvements. [Andreas Ziegler]
- Config.default.php: fix tiny typo. [Andreas Ziegler]
- Merge pull request #1138 from I-am-Sherlocked/patch-6. [Andras Iklody]

  Resolve only_full_group_by error in filterEventIndex
- Resolve only_full_group_by error in filterEventIndex. [I-am-
  Sherlocked]

  Event.id required in group by, to resolve

  >Error: [PDOException] SQLSTATE[42000]: Syntax error or access violation: 1055 Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'Event.id' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by

  in Request URL: /events/filterEventIndex
- Merge pull request #1136 from sfossen/patch-11. [Andras Iklody]

  remove warnings when importing event attributes without distribution set
- Remove warnings when importing event attributes without distribution
  set. [Steve Fossen]

  Warning (2): Illegal string offset 'distribution' [APP/Model/Event.php, line 1810]
  Notice (8): Uninitialized string offset: 0 [APP/Model/Event.php, line 1810]
  Warning (2): Illegal string offset 'distribution' [APP/Model/Event.php, line 1821]
  Notice (8): Uninitialized string offset: 0 [APP/Model/Event.php, line 1821]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Visualization of the database schema. [Alexandre Dulaunoy]
- Merge pull request #1131 from I-am-Sherlocked/patch-5. [Andras Iklody]

  Resolving the sql_mode=only_full_group_by error in Search Log
- Resolving the sql_mode=only_full_group_by error in Search Log. [I-am-
  Sherlocked]

  Similar to pull request #1121 and issue #749, the ID needs to be in group_by to solve this error in /admin/logs/search

  >Error: [PDOException] SQLSTATE[42000]: Syntax error or access violation: 1055 Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'Log.id' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
- Merge pull request #1128 from sfossen/patch-10. [Andras Iklody]

  fail gracefully if sharing group incomplete
- Fail gracefully if sharing group incomplete. [Steve Fossen]
- Quick filters for the logs. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]

v2.4.44 (2016-05-12)
--------------------

Fix
---
- Fixed an issue with the download as MISP XML/JSON failing for regular
  users due to a permission issue. [Iglocska]
- Fix to an issue with server urls having a trailing slash causing an
  invalid sharing group server detection. [Iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1125 from I-am-Sherlocked/patch-3. [Andras Iklody]

  Missing DEFAULT value in certif_public
- Missing DEFAULT value in certif_public. [I-am-Sherlocked]

v2.4.43 (2016-05-11)
--------------------

New
---
- Started work on the new attribute deletion. [Iglocska]

Changes
-------
- Prevent attribute edit on deleted attributes, prevent proposal
  correlation on deleted attributes. [Iglocska]
- Some small fixes to the soft-delete. [Iglocska]
- Further work on the soft deletes. [Iglocska]
- Soft-delete ready for testing. [Iglocska]
- Further progress on the attribute soft-deletes. [Iglocska]
- Further progress on the attribute soft delete. [Iglocska]
- Further work on the attribute soft delete. [Iglocska]
- DB changes for the attribute deletion. [Iglocska]

Fix
---
- Attribute search - download as CSV returns empty result set, fixes
  #1122. [Iglocska]
- Fixed an issue that would cause invalid empty events to be created
  when using the API to delete attributes. [Iglocska]
- Several issues with the soft delete resolved. [Iglocska]
- Fixed broken undelete button. [Iglocska]
- Left off a change. [Iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch 'feature/soft-delete' into 2.4. [Iglocska]
- Merge branch '2.4' into feature/soft-delete. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1120 from sfossen/patch-9. [Andras Iklody]

  patch for smime
- Patch for smime. [Steve Fossen]

  smime patch also needed in base mysql for new installs.
- Merge pull request #1121 from I-am-Sherlocked/patch-1. [Andras Iklody]

  Update UsersController.php
- Update UsersController.php. [I-am-Sherlocked]

  Grouping by Organization.name will throw a MySQL error
  "Syntax error or access violation: 1055 Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'misp.Organisation.id' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by"
  in "Request URL: /users/memberslist" , since Organization.name is not a unique field. Grouping by Organization.id instead will fix the issue.
- Fixed the logging of attribute deletes. [Iglocska]

v2.4.42 (2016-05-05)
--------------------

Changes
-------
- Filter event index for my own events. [Iglocska]

  - Part of the initiative for a happier Andrzej
- Attribute search download also offered as JSON, fixes #1035.
  [Iglocska]

  - also added some convenience functions for JSON/XML collections in the appropriate export tools
  - can start reusing them in other functionalities
- Added event ID to enrichment input, fixes #1091. [Iglocska]
- Small comment fix. [Iglocska]
- Fixed the flash messages when viewing remote instances. [Iglocska]
- Fixed invalid output of some fields in the remote instance views.
  [Iglocska]
- Removed the relation of users -> favourite tags. [Iglocska]

  - at the moment it is not used, but can cause issues
  - revisit this later
- Version bump. [Iglocska]
- Added options to inject the SCL php paths into the PATH when executing
  the worker shell scripts on RHEL/CentOS. [Iglocska]

Fix
---
- Problem with osint json/taxonomy, fixes #1119. [Iglocska]

  - Added a new validation for strings where "0" should be a valid value
- Comment from expansion lost after free-text import, fixes #1115.
  [Iglocska]
- Attachment upload of existing file, fixes #1024. [Iglocska]
- Fixed an ACL issue preventing normal users from viewing the instance
  version. [Iglocska]

  - this is required by the enrichment modules
- Fix to an issue for new installations. [Iglocska]

Other
-----
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]

v2.4.41 (2016-04-28)
--------------------

Changes
-------
- Updated the user edit view to match the user admin edit view's
  interpretation of the SMIME certificate field. [Iglocska]
- Renamed the JS used by MISP. [Iglocska]

Fix
---
- Fixed some issues with the favourite tags. [Iglocska]

v2.4.40 (2016-04-28)
--------------------

New
---
- Favourite tags. [Iglocska]

  - Add a tag to your favourites list
  - When tagging events there is a new setting: Favourite tags, which only contains the tags you've selected

Changes
-------
- Added encryption feature with PGP or S/MIME support. [Alexandre
  Dulaunoy]

Other
-----
- Airbus added as contributor. [Alexandre Dulaunoy]

v2.4.39 (2016-04-27)
--------------------

Changes
-------
- Small test with the embedded headers. [Iglocska]
- Reverted the previous change. [Iglocska]
- Small fix to the headers sent for SMIME. [Iglocska]

Fix
---
- Fixed an issue with handling SMIME encrypted messages on instances
  that don't have a signing key. [Iglocska]

Other
-----
- Merge branch 'feature/smime' into 2.4. [Iglocska]
- Updates to the SMIME setup instructions. [Iglocska]
- SMIME changes. [Iglocska]

  - tied into auto upgrade system
  - tied into server settings
  - some cleanup of overly verbose debug
  - Enforcing enable/disable everywhere
  - Changed temporary file structure
- Merge branch '2.4' into smime. [Iglocska]

  Conflicts:
  	app/Controller/AppController.php
- Merge pull request #1106 from koenigswinter/patch-1. [Andras Iklody]

  Update UPDATE.txt
- Update UPDATE.txt. [Heiko Siebel]

  Adopt CyBox Version: 2.1.0.12 (analogue to INSTALL documentation)
- Warning lists added, branches clarified and copyright dates updated.
  [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Updated warning list. [Alexandre Dulaunoy]
- Submodule update. [Iglocska]
- Add 'certif_public' in the fields. [devnull-]
- Unset 'certif_public' [devnull-]
- Add 'certif_public' in the searches. [devnull-]
- Missing ''domains.airbus@airbus.com': 'ai' [devnull-]
- Add the 'verify_certificate.ctp' view. [devnull-]
- Display the 'Certificate (x509) set' in the 'Ajax index' [devnull-]
- Add 'verifyCertificate' in 'Administration View' [devnull-]
- Update the config.default.php with the SMIME section. [devnull-]
- Add the field 'certif_public' in the view. [devnull-]
- Add the field 'certif_public' in Form. [devnull-]
- Add the field 'certif_public' in view. [devnull-]
- Add the field 'certif_public' in index. [devnull-]
- Add in form the field 'certif_public' [devnull-]
- Patch SMIME to sign and encrypt email. [devnull-]
- Update fields & add certificate as attachment to email. [devnull-]
- Add function verifyCertificate & update of fields. [devnull-]
- Update the flash messages displayed when no GPG key or certificate are
  set. [devnull-]
- Unset the user 'certif_public' [devnull-]
- Add certif_public in CakeSchema. [devnull-]
- Export the public certificate (for Encipherment) to the webroot.
  [devnull-]
- Instructions to install SMIME patch. [devnull-]
- Specific transport class to send SMIME with CakePHP (add SMIME
  headers) [devnull-]
- PATCH: Update the database schema (SMIME) [devnull-]

v2.4.38 (2016-04-23)
--------------------
- Merge branch 'feature/warninglists' into 2.4. [Iglocska]
- Removed link type from network attributes. [Iglocska]
- Added filter to only view attributes that generate a warning.
  [Iglocska]
- Polished the event level warnings. [Iglocska]

  - nice warning box on the right side
  - warninglists that cause a clash are now URLs
- Fixed an issue that caused warnings to be attached only after
  truncating the attributes for pagination. [Iglocska]
- Single transaction for saving all values of a warninglists from file.
  [Iglocska]
- Warning message removed if no warninglists are enabled. [Iglocska]
- Submodule changes. [Iglocska]
- Gitmodules update. [Iglocska]
- Merge branch '2.4' into feature/warninglists. [Iglocska]
- First version of the warnings finished. [Iglocska]
- Further progress. [Iglocska]
- Import, enabling, viewing, indexing of warninglists finished.
  [Iglocska]
- Warninglists :construction:. [Iglocska]
- Fix to an invalid check. [Iglocska]
- Small tune to the freetext import. [Iglocska]

  - url vs filename differentiation still being a headache
  - will need a more thorough look
- Keep formating of text type attributes. [Iglocska]
- Left off file. [Iglocska]
- Fix to the previous commit. [Iglocska]
- Fix to the PGP key being loaded into the session. [Iglocska]

  - it can lead to large PGP keys causing failed logins
- Fixed the IDS flag default setting for freetext-imported virus total
  links. [Iglocska]
- Fixed several invalid detections in the freetext import tool.
  [Iglocska]

  - Composite filename|hash types were incorrectly detected as hash types
- Freetext import tuning. [Iglocska]

  - refanging of various . notations
- Fix to the attribute quick edit field not being consistent with the
  attribute list. [Iglocska]

  - use short names for distributions
- Fix to a missing e-mail field on the discussion list for deleted
  users. [Iglocska]
- Added customisable main logo. [Iglocska]
- Org admins could not see the roles index. [Iglocska]
- Sighting feature added in the README. [Alexandre Dulaunoy]
- Merge pull request #1001 from deralexxx/2.4. [Andras Iklody]

  misp backup script
- Backup files as well. [Alexander J]
- Update misp-backup.sh. [Alexander J]
- Misp backup script. [deralexxx]
- Merge branch 'permissionfix' into 2.4. [Iglocska]
- Fix typos. [William Robinet]
- Fix permissions. [William Robinet]
- Removed an old unused field, fixes #1092. [Iglocska]

  - thanks to @steventgoossensB for finding the obsolete field
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #953 from MISP/elhoim-search-page-label. [Andras
  Iklody]

  Changed text Find valid IOCs in search page
- Changed text Find valid IOCs in search page. [David André]

  Using "Only find IOCs to use in IDS" instead since the IOCs where to_ids=0 are not invalid.
  It was confusing to some users.
- Added warning. [Iglocska]

  - to be removed once we do some testing
- Merge branch 'kerberos' into 2.4. [Iglocska]
- Add modification for erreur with ldap user modification for dc in conf
  file. [Tristan METAYER]
- Add kerberos Authentification fonction. [trucky dev]
- Fix to the URL generation. [Iglocska]

  - sometimes the URLs are inconsistent in links within MISP (/shadowAttributes vs shadow_attributes)
  - the URL generation now takes both cases into consideration
- Don't display menu items that the user has not right to access #1097.
  [Iglocska]

  - Removed feeds button for org admins
- Some ACL fixes. [Iglocska]
- 3 significant figures instead of 2 for the attribute type breakdown.
  [Iglocska]
- Change_pw was blocked for normal users. [Iglocska]
- Added percentages to the statistics API. [Iglocska]
- Didn't like the previous version of the statistics API. [Iglocska]

  - pretty printed JSONs to prevent eye-bleeds
- Added some statistics APIs for attribute types / categories.
  [Iglocska]
- Comment in attribute resolution now reflects the actual source of the
  attributes. [Iglocska]

  - instead of always saving it as the result of a freetext import
  - it now replaces the comment with the source enrichment module if applicable
- Fixed a capitalisation fail. [Iglocska]
- Filter events by creator e-mail address. [Iglocska]

  - for site admins only
- Naming consistency. [Iglocska]

  - changed event description to event info in some views
- Pretty print event JSONs. [Iglocska]
- Pretty printed queryACL's JSON response. [Iglocska]
- Some small changes. [Iglocska]
- Small fixes. [Iglocska]

v2.4.37 (2016-04-18)
--------------------
- Version bump. [Iglocska]
- Rework of the ACL. [Iglocska]
- Work on the new ACL system. [Iglocska]
- Add event date in alternate search results, fixes #1095. [Iglocska]
- Gitchangelog configuration added. [Alexandre Dulaunoy]
- Version bump. [Iglocska]

v2.4.36 (2016-04-15)
--------------------
- Fixed a check for the upload sample API to check if the target event
  actually exists. [Iglocska]
- Added comment field to upload sample API. [Iglocska]
- Changed the publish dating to number of days from fixed date.
  [Iglocska]

v2.4.35 (2016-04-15)
--------------------
- Added a way to block old publish alerts from going out. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1085 from rotanid/space-bugfix. [Andras Iklody]

  add margin between fileupload and submit button
- Add margin between fileupload and submit button. [Andreas Ziegler]
- Merge pull request #1078 from sfossen/patch-3. [Andras Iklody]

  defaults for events table.
- Revert the unsigned removal. [Steve Fossen]
- Defaults for events table. [Steve Fossen]
- Merge pull request #1076 from sfossen/patch-1. [Andras Iklody]

  default for roles perm_template
- Default for roles perm_template. [Steve Fossen]
- Merge pull request #1081 from sfossen/patch-6. [Andras Iklody]

  defaults for logs table.
- Defaults for logs table. [Steve Fossen]
- Merge pull request #1077 from sfossen/patch-2. [Andras Iklody]

  defaults for users tables.
- Defaults for users tables. [Steve Fossen]
- Merge pull request #1080 from sfossen/patch-5. [Andras Iklody]

  defaults for organisations table
- Defaults for organisations table. [Steve Fossen]
- Merge pull request #1079 from sfossen/patch-4. [Andras Iklody]

  defaults for jobs table
- Defaults for jobs table. [Steve Fossen]
- Merge pull request #1082 from sfossen/patch-7. [Andras Iklody]

  defaults for servers table.
- Defaults for servers table. [Steve Fossen]
- Merge pull request #1083 from sfossen/patch-8. [Andras Iklody]

  defaults for feeds table.
- Defaults for feeds table. [Steve Fossen]
- Merge pull request #1084 from rotanid/bugfix. [Andras Iklody]

  Model/Attribute.php: remove obsolete HTML-linebreak
- Model/Attribute.php: remove obsolete HTML-linebreak. [Andreas Ziegler]
- Sha-2 entries incorrect under Search Attributes GUI, fixes #1086.
  [Iglocska]
- Merge branch 'feature/sightings' into 2.4. [Iglocska]
- Update to the data model. [Iglocska]
- Merge branch '2.4' into feature/sightings. [Iglocska]

  Conflicts:
  	app/webroot/js/ajaxification.js
- Fix to an issue with the freetext import tool. [Iglocska]

  - Due to a typo 64 character long hashes could not be correctly added via the freetext import tool
  - Should be fixed now.
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1069 from RichieB2B/ncsc-nl/defang-hostnames.
  [Andras Iklody]

  Defang hostname attributes
- Also defang hostname attributes. [Richard van den Berg]
- Short name for tags, fixes #1075. [Iglocska]
- If a user gets removed, the organisation cannot be shown in his/her
  discussion thread posts and MISP throws notices. Show "Deactivated
  user" instead. [Iglocska]
- Fix to some deprecated action references in some forms throwing
  deprecated notices after upgrading to CakePHP 2.8. [Iglocska]
- [UI] Polulate using freetext in left Event Menu etc, fixes #1068.
  [Iglocska]
- JSON structure inconsistencies and bug, fixes #1065. [Iglocska]
- Second iteration of the sightings. [Iglocska]

  - Added STIX sighting support
  - better API add (via url parameter or POSTed object)
- Merge branch '2.4' into feature/sightings. [Iglocska]

  Conflicts:
  	app/Model/Event.php
  	app/Model/Server.php
  	app/View/Events/view.ctp
- Sightings column header disabled if sightings disabled. [Iglocska]
- Merge branch '2.4' into feature/sightings. [Iglocska]

  Conflicts:
  	app/Model/Attribute.php
- Merge branch '2.4' into feature/sightings. [iglocska]

  Conflicts:
  	app/Controller/SightingsController.php
  	app/Model/Sighting.php
- Fixed a bug with no sighting data in an event causing a notice.
  [iglocska]
- Cleaned up some leftover junk and some new additions. [iglocska]

  - clicking on a sighting count on the event view reveals contributor list
    - list of orgs and number of sightings
    - Orgs only shown (outside of own) if the policy to anonimise orgs is not enabled
    - works on an event and an attribute level
- First version of the sightings. [Iglocska]

  - add / delete sightings via REST
  - add sightings via the UI
  - View sightings info on an event and attribute level (event view only for now)
  - differentiate between own sightings and that of other orgs (additional information via popover still coming)

  - settings:
    - 1. enable / disable sightings server wide
    - 2. set sightings policy
      - a. Only Event owner can see sightings + everyone sees what they themeselves contribute
      - b. Anyone that contributes sightings to an event can see the sightings data
      - c. Everyone that can see the event can see the sightings
    - 3. Anonymisisation (in progress, data correctly retrieved in business logic)
      - a. if true, then only own org + "other" is shown
      - b. otherwise all orgs that submitted sightings are shown

  Further improvements needed for version 1 of sightings:
    - 1. Delete via the interface
    - 2. View detailed sightings information
    - 3. Graph the sightings data for the event
    - 4. Include the Sightings data in the XML/JSON views
    - 5. View sighting for attribute / event via the API

v2.4.34 (2016-04-08)
--------------------
- Version bump. [Iglocska]
- Submodule update. [Iglocska]
- CakePHP update. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #1063 from deralexxx/patch-1. [Andras Iklody]

  Update UPDATE.txt
- Update UPDATE.txt. [Alexander J]

  solved an issue I had with "This account is currently not available."

  Guess we can also change that in install guide
- Start the popover script on the event's attribute indexes page load.
  [Iglocska]
- Better sanitisation of the XML exports. [Iglocska]
- Fix to a bug with the enrichment system when using freetext type
  results. [Iglocska]
- Fixed the event edit redirect on REST add. [Iglocska]

  - sends a 302 instead of a 404
- Fixed a severe issue with the synchronisation causing edits to fail if
  the baseurl was not set on the remote. [Iglocska]
- Changed proposal response parsing from object to array. [Iglocska]
- Renaming an event description does not update the correlations event
  description, fixes #1058. [Iglocska]

  - Changing the event info / event date will update the correlations correctly
- Hover enrichment improvements. [Iglocska]

  - store fetched data in a variable, only fetch it once / view
  - better handling of arrays returned, can still use improvements
- Organisation filter field was case sensitive. Fixed. [Iglocska]
- Some cleanup for the sync. [Iglocska]

  - fixed some issues with the error detection on synced events
  - pre-filtering of events based on sync filters before pushing them should improve performance a great deal
- Changes to the logging to debug further. [Iglocska]
- Log the error code unless it is a 403. [Iglocska]
- Better error handling for pushes. [Iglocska]
- Fixed an invalid is_array call. [Iglocska]
- Typo fixed. [Iglocska]
- Fix to a copy-paste error as described in #935. [Iglocska]
- Typo fixed. [Iglocska]
- Added error handling for an edge case in the upload event to server
  mechanism, should help debugging #935. [Iglocska]
- Upload sample API will not create malware-samples if the to_ids flag
  is not set. [Iglocska]

  - mimicing the add attachment functionality
    - to_ids flag not set will create an attachment instead of a malware-sample
    - not setting the flag will not trigger the creation of any hashes
- Event filter window doesn't display correct information, fixes #994.
  [Iglocska]
- Fixed an issue with the event edit API. [Iglocska]

  - pushing more than one change per second would get blocked due to the event not being newer even if no timestamp was set
- Added a fix to enrichment modules with hover functionality not showing
  any results. [Iglocska]

  - When adding handling for modules returning arrays the default behaviour was overwritten. Fixed now.
- Initial feed loader tries to log an entry without initialising the log
  model. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Reference to the Twitter account added. [Alexandre Dulaunoy]
- Changes to the STIX export. [Iglocska]

  - added new hash types
  - added domain|ip type

  - some cleanup
- Rework of the correlation popovers. [Iglocska]
- Added the option to export in CSV format without any headers.
  [Iglocska]
- Execute cache cleaning on next page load. [Iglocska]
- Cache clearing improved and added a manual cache clearing for admins.
  [Iglocska]
- Error in the MYSQL.sql update. [Iglocska]
- MYSQL.sql updated. [Iglocska]
- Force all sessions to be deleted - also, temporarily removed the per
  user session destruction. [Iglocska]
- Fixed to an invalid path in the cache cleanup. [Iglocska]
- Cleaner cache cleanup. [Iglocska]
- Destroy sessions on next page load for all users if there was a db
  update. [Iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- MISP logo in a square. [Alexandre Dulaunoy]

v2.4.32 (2016-03-30)
--------------------
- Split the tagging permission into two. [Iglocska]

  - New permission flag: perm_tag_editor
    - taggers can tag events with existing tags
    - tag editors can create / edit / delete tags

  - Fixed several misleading UI elements for tagging
    - tagging users that don't own an event and aren't creators thereof cannot tag them
    - this was enforced before but the UI elements were present and threw errors

  - Migration is automatic
    - all existing tagger roles will automatically become tag editors
    - restricting current roles takes manual admin action, but the functionality should remain unchanged for those that just update
- Case insensitive tagname lookup for the addtag / removetag APIs.
  [Iglocska]
- Reworked the Tag add/remove APIs. [Iglocska]

  - new syntax
  - old syntax still accepted

  - new tool for rearranging request data to allow the APIs to automatically catch and correct typical rearrange errors

v2.4.31 (2016-03-30)
--------------------
- Fix to an issue with the password reset breaking the credentials.
  [Iglocska]

  - The password change forced on users by administrators couldn't save new passwords
  - instead it reset the password to a new random password

  - Resetting the password of such users via the admin interface should fix the issue
  - Alternatively manually setting the password also fixes it
- Re-enabled the missing poporvers on relations. [Iglocska]
- Fixed some issues with the hover enrichment modules. [Iglocska]
- Some refactoring of the freetext tool. [Iglocska]
- Handling of the "freetext" return format via the enrichment modules,
  and error handling fixed. [Iglocska]

  - freetext is now a valid return format, it will allow module developers to return an unparsed text blob which MISP will try to loop through the freetext import's detection mechanism
  - still a lot of improvements to be done for the detection mechanism

  - error handling for modules, instead of discarding errors they are now shown as a flash message on the freetext import result screen
- Unpublish event if the published flag is not set during an edit.
  [Iglocska]
- Fixed an issue where being redirected back to the edit page of the
  edit organisation action would leave the user with an unpopulated
  country list. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #1050 from SleuthKid/patch-1. [Andras Iklody]

  Small fix for main.css
- Small fix for main.css. [Robert Haist]

  There is a typo in main.css
- CIRCL logo added. [Alexandre Dulaunoy]
- Fix #1051. [Alexandre Dulaunoy]
- Fix to an invalid default password complexity validation, fixes #585.
  [Iglocska]
- Fixes to the plugin settings not working for any plugin beyond the
  first one. [Iglocska]
- Fixed a merge issue that removed the correlations from the freetext
  import view. [Iglocska]

  - also added the correlations to the enrichment view

v2.4.30 (2016-03-28)
--------------------
- Verision bump. [Iglocska]

v2.4.29 (2016-03-28)
--------------------
- Added the authkey to the admin user index, including filtering /
  searching for them. [Iglocska]
- Added org blacklisting to the global menu. [Iglocska]
- Added logging to the blacklist models. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Expansion modules added. [Alexandre Dulaunoy]
- Fix to an invalid log entry being created for a failed authentication,
  even on successful authentication attempts. [Iglocska]
- Version bump. [Iglocska]
- Merge branch '2.4' into feature/authentication. [Iglocska]

  Conflicts:
  	app/Config/bootstrap.default.php
  	app/Model/Server.php
  	app/webroot/js/ajaxification.js
- Appending the port when the baseurl is not set can now be disabled.
  [Iglocska]
- Organisation blacklisting added. [Iglocska]
- Don't loop through the available modules when viewing the server
  settings if no modules are available. [Iglocska]
- Added timestamp to the feed preview index, fixes #1044. [Iglocska]

  - looks a bit ugly, but since we don't have an event ID this makes sense. Altertnatively we can simply sort by timestamp by default and remove the field.
- Fix to an issue that causes the server certificate to be removed if a
  sync connection is edited. [Iglocska]
- Fix to some typos in the templates, fixes #1041. [Iglocska]
- List the Sharing groups via the API, fixes #1032. [Iglocska]
- Fixed Proposal naming, fixes #1034. [Iglocska]
- Add an API for getting a list of types, categories and category-type
  mappings supported by MISP, fixes #1031. [Iglocska]
- Further fixes. [Iglocska]
- Better logging of failed authentication attempts. [Iglocska]
- External auth error message changed. [Iglocska]
- Cleaner authentication issue messages. [Iglocska]
- Customise the home button. [Iglocska]
- Fix to the same issue. [Iglocska]
- Small change. [Iglocska]
- Small fix. [Iglocska]
- Added custom password reset / logout url. [Iglocska]
- Better automatic handling of the baseurl. [Iglocska]

  - Used to simply take the server address
  - Switched to a method that tries to use SERVER_NAME > HTTP_HOST > SERVER_ADDR
- Fix to an empty validation method call. [Iglocska]
- Optionally remove the log out button from externally authenticated
  users. [Iglocska]
- Merge branch '2.4' into feature/authentication. [Iglocska]
- Fix to the incoming address check. [Iglocska]
- First implementation of the new auth mechanism. [Iglocska]

v2.4.28 (2016-03-21)
--------------------
- Version bump. [Iglocska]
- Merge branch 'feature/enrichment' into 2.4. [Iglocska]
- Enrichment system first iteration ready. [Iglocska]
- Fix to the optional settings not being passed to the enrichment
  modules. [Iglocska]
- Further progress. [Iglocska]
- Better handling of no modules found / modules not reachable.
  [Iglocska]
- Limit available enrichment options based on modules enabled.
  [Iglocska]
- Dynamic settings retrieved from modules. [Iglocska]
- Updates to the enrichment system. [Iglocska]
- Merge branch '2.4' into feature/enrichment. [Iglocska]

  Conflicts:
  	app/Model/Event.php
- Fixed a typo in the feed adder, fixes #1022. [Iglocska]
- Default reverted to have the feeds disabled. [Iglocska]
- Fix to the previous commit. [Iglocska]

  - also enabling the test feed by default
- Update to the MYSQL.sql file for the feeds. [Iglocska]
- Releasable to field creates a popover on hover instead of click, fixes
  #1012. [Iglocska]
- Fixed an issue where a non sharing group editor saw the edit / delete
  buttons on the SG index, fixes #1012. [Iglocska]
- Attachment upload failing produces invalid flash message. [Iglocska]
- Allow the editing of the value in the freetext import results.
  [Iglocska]
- Event.php trying to unset causes fatal error, fixes #1019. [Iglocska]
- Fixed an issue where a proposal correlation would fail. [Iglocska]
- Fixed an invalid org comparison, blocking users that try to add events
  created by their own organisation on another instance from adding the
  event. [Iglocska]
- Merge branch '2.4' into feature/enrichment. [Iglocska]
- First implementation of the enrichment modularity. [Iglocska]
- Next stage in the enrichments. [Iglocska]
- Merge branch '2.4' into feature/enrichment. [Iglocska]
- Initial version of the enrichment. [Iglocska]

  - setup enrichment service settings via the admin settings
    - enable/disable
    - set url
    - set port

  - on the event view, attributes with enrichment options have a new action
    - depends on the choices resolved from /modules from the enrichment service
    - user can click enrichment and choose from the list of appropriate modules

  - when the user picks a module, MISP fetches the result of the query
    - currently it stores and shows the result in a debug message

  - next step: Tie it into the freetext import results
  - add additional fields to the python service

v2.4.27 (2016-03-11)
--------------------
- Re-added a feed. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Fix to a new bug introduced with the freetext import tool. [Iglocska]

  - reusing the same variable name for keys for a loop nested in another loop is not clever
- Popover didn't work if type change was active. [Iglocska]
- Cleaner escaping of the popover. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Freetext import results now show similar attributes. [Iglocska]
- Correctly detect e-mail addresses in the freetext import tool.
  [Iglocska]

v2.4.26 (2016-03-10)
--------------------
- Version bump. [Iglocska]
- Temporarily removed a feed. [Iglocska]

  - will readd it in an upcoming hotfix
- Merge branch 'feature/feeds' into 2.4. [Iglocska]
- Feed didn't respect the enabled flag. [Iglocska]

  - if a feed was disabled a site admin could still pull the contents
- First version of Feed system ready. [Iglocska]

  - tied into background processes
- Added default feeds. [Iglocska]
- Removed accidental junk. [Iglocska]
- Annoying non-clickable tags on event index fixed. [Iglocska]
- Correctly assign tag / sharing group to event fetched from feed.
  [Iglocska]
- New fields added. [Iglocska]

  - set the distribution and sharing group of a feed
    - will set all events received to the appropriate setting

  - set a tag that should be applied by default to the events received from the feed
- Fixed an issue with the filtering. [Iglocska]

  - needle, haystack or haystack, needle.
- Added downloading of an event from the index, better error handling.
  [Iglocska]
- Set attribute distribution to Inherit if it is not set. [Iglocska]
- Preview Event implemented. [Iglocska]
- Preview the index of a feed. [Iglocska]
- Merge branch '2.4' into feature/feeds. [Iglocska]

  Conflicts:
  	app/Model/Attribute.php
- Further progress. [Iglocska]
- Further progress on the feeds. [Iglocska]
- Work in progress on the feeds. [Iglocska]
- Return to the same event attribute pagination after accepting /
  discarding proposals. [Iglocska]
- List Organisation in alphabetical order for new users, fixes #989.
  [Iglocska]

  - Fixes an issue where organisations in both the admin add and admin edit user views were not sorted alphabetically
  - delays Przemek enrage timer
- Set proposal's deleted field to 0 if nothing is set before saving,
  fixes #988. [Iglocska]

v2.4.25 (2016-03-09)
--------------------
- Scheduled push incorrectly used the user e-mail address instead of a
  user object to initiate the sync, fixes #1000. [Iglocska]

v2.4.24 (2016-03-07)
--------------------
- Version bump. [Iglocska]
- Better feedback on the sync connection test. [Iglocska]

  - sync users that have not accepted the terms / have had a password reset initiated were redirected to the login page

  - fixes to the issue
    - if a user with automation/sync access uses the API and gets blocked because the terms weren't accepted or there is a pending password change they will be notified in a JSON/XML response
    - the sync test now takes this into consideration starting with this version and will report the cause of the failure

  - Both instances have to be 2.4.24+ for this to be reported correctly
- More flexibility when editing events via the REST API. [Iglocska]

  - Change the distribution / sharing group with a simple payload
  - no need to push any fields for the edit that are not required for the change

  - Example to change the distribution of an event via the API:
    - POST to /events/edit/event_id
    - payload {"Event":{"distribution": 4, "sharing_group_id":5}}
    - this will change the distribution to the sharing group with ID=5
    - Requirements: User has to have access to SG(5)
- Fixed an issue with empty event tags still kept in the json output of
  the event index. [Iglocska]
- Follow up fix to the previous patch. [Iglocska]
- Fixed a bug in the validation of two attribute types, fixes #1003.
  [Iglocska]
- Added logging to the connection test failing. [Iglocska]

  - the logging logs exceptions that pop up during the test
  - the idea is to be able to differentiate between no response, certificate issues, etc
- Follow up to the previous patch. [Iglocska]

  - pull / push mechanism would still alert on proposal exchanges
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- MISP taxonomies updated to the latest version. [Alexandre Dulaunoy]
- Fix to an issue with proposal notifications and tightening of the gpg
  diagnostics. [Iglocska]

  - Proposal alerts would be generated even if a deleted proposal got synced from a remote instance

  - One of the GPG diagnostic checks could run if a previous prerequisite has already failed
- Slightly better error reporting for GPG diagnostic issues. [Iglocska]
- All events quick filter added to event index, fixes #950. [Iglocska]
- Event Tag numbering fixed. [Iglocska]

  - When fetching events, non exportable tags are blocked at a tag level
  - this results in some empty eventTags, which were correctly unset
  - however, this resulted in an associative array instead of an indexed one in the exports

  - fixed by reindexing the eventTags
- If a user is disabled then he should not receive mass admin e-mails.
  [Iglocska]

  - however, if an admin specifically chooses to e-mail him/her it will still work
- Fixed an issue that blocked the editing of attributes in unpublished
  events if the MISP.unpublishedprivate setting was set. [Iglocska]
- Shameless small edit of the install documentation. [Iglocska]
- Update to the Debian install docs to reflect the changes made to the
  Ubuntu one. [Iglocska]
- Typo error with registrar fixed #984. [Alexandre Dulaunoy]
- Fixed an issue with the log search where the search terms would be
  discarded after pagination. [Iglocska]
- Pagination incorrectly sorts log entries after flipping the page,
  fixes #971. [Iglocska]
- Organisations sorted in the server add/edit views alphabetaically,
  fixes #974. [Iglocska]
- Added & to the allowed characters in the e-mail type validation, fixes
  #972. [Iglocska]
- Added quick filter tabs to the jobs index. [Iglocska]
- Better detection of the proxy settings not being set. [Iglocska]
- Fixed an issue that prevented the correct flash message to be shown
  when an event publishing was successful but not all e-mails could be
  sent out successfuly. [Iglocska]
- Fixed an issue where a proposal correlation would fail. [Iglocska]
- Fixed an invalid org comparison, blocking users that try to add events
  created by their own organisation on another instance from adding the
  event. [Iglocska]
- Version bump. [Iglocska]

v2.4.23 (2016-02-22)
--------------------
- Fixed a bug that caused the publish e-mails to not respect the sharing
  groups correctly. [Iglocska]

v2.4.22 (2016-02-21)
--------------------
- Added correlation as a quick filter on attributes in the event view.
  [Iglocska]
- Mass-accepting proposals did not work, fixes #959. [Iglocska]

  - fixed a legacy style org lookup
- Restore missing tasks if needed and some updates to the install
  script. [Iglocska]

  - If a task is missing then visiting the task index will automatically re-create it
  - MYSQL.sql brought up to date, the upgrade scripts in the application shouldn't have to run on first login
- Version bump. [Iglocska]

v2.4.21 (2016-02-19)
--------------------
- Fix to a critical vulnerability for the login authentication
  mechanism. [Iglocska]

  - The API key check was incorrectly logging in the wrong user when the API key started with a numeric value
- Fixed an issue with the link attributes in the attribute index/search.
  [Iglocska]
- Merge pull request #954 from MISP/elhoim-doc-clarification. [Andras
  Iklody]

  Clarify documentation for API calls
- Correct mistaken auto-replace of date. [David André]

  2015-02-15
- Clarify documentation for API call. [David André]

  Clarify which fields of events are used by **to**, **from** and **last** API calls parameters.
- Fix to an invalid org lookup when regenerating a user's authkey as an
  org admin. [Iglocska]
- Disabled the background workers for travis for now. [Iglocska]
- Fix to setting the job progress before initialising the model when
  correlating proposals. [Iglocska]
- Fixed a copy paste fail. [Iglocska]

v2.4.20 (2016-02-17)
--------------------
- Added correlations on a proposal level. [Iglocska]

  - tied into automatic datamodel updates
  - correlation is one way only (from proposal to attribute)
  - proposals don't correlate with one another

  - all distribution rules are adhered to
  - further improvements on the upgrade mechanism pipeline
- Changed the tag matching when capturing them case insensitive.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Updated misp-taxonomies. [Alexandre Dulaunoy]
- Fixed the reset button on the dashboard. [Iglocska]
- Fix to an invalid role check. [Iglocska]
- Added last login to org user index too. [Iglocska]
- Show last login for each user on the admin index. [Iglocska]
- Forgot to add save... [Iglocska]
- Some tuning to the previous commit. [Iglocska]
- Refresh auth on dashboard. [Iglocska]
- Several fixes to the add_misp_export tool, fixes #946. [Iglocska]

  - Fixed an issue where a user could take ownership of an event he added via this tool, even if the server setting to allow taking owenership was disabled
  - Fixed an issue that allowed a non publisher user to publish via this tool
- Check "Encode Attachments" box on default, fixes #947. [Iglocska]
- Version bump. [Iglocska]
- Reverted a version fix within the XML file. [Iglocska]

  - needs further fixes, sadly the version has always just showed the major and minor version in the exports
  - This masked an issue that would block the import of events that are even a hotfix away

  - As a temporary fix, I reverted the changes and the XML version field will now only show the major and minor version to restore compatibility (so 2.4.0 instead of 2.4.19)
- Fix to the issues with the proposals. [Iglocska]

  - proposals on REST edit could get added without an event_ID / attached to the incorrect event if certain conditions were met
  - removed proposal from event edit completely, as it goes against the intended functionality of out of bounds proposal management

  - also added an update script that removes the invalid proposals
    - these will automatically be rescyncronised on the next pull/push
- A recent CSS change broke the statistics page. [Iglocska]

  - Fixed
- Better log message for the previous commit. [Iglocska]
- Added cleaner error handling for events that could not be uploaded.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Delegation of sharing added in README. [Alexandre Dulaunoy]

  **delegating of sharing**: allows a simple pseudo-anonymous mechanism
  to delegate publication of event/indicators to another organization.
- Added new attribute type x509-fingerprint-sha1. [Iglocska]
- Version bump and footer version fix. [Iglocska]

v2.4.18 (2016-02-13)
--------------------
- Merge branch 'features/delegation' into 2.4. [Iglocska]
- Merge fixes. [Iglocska]
- Merge branch '2.4' into features/delegation. [Iglocska]

  Conflicts:
  	app/Controller/AppController.php
  	app/Model/AppModel.php
  	app/Model/Event.php
  	app/Model/Log.php
  	app/Model/Server.php
  	app/View/Elements/footer.ctp
  	app/webroot/css/main.css
- Removed an invalid version check. [Iglocska]
- First finished version. [Iglocska]
- First steps. [Iglocska]
- Hovering over an attribute correlations shows the correlated value.
  [Iglocska]

  - this helps with composite attributes where only one half of the attribute correlates

v2.4.17 (2016-02-11)
--------------------
- Version bump. [Iglocska]
- Merge branch 'feature/syncfix' into 2.4. [Iglocska]
- Fix to the tag import from XML if there is only a single tag.
  [Iglocska]

  - Single element XML import issue is back for the event tag
  - fixed
- Merge branch 'feature/syncfix' of https://github.com/MISP/MISP into
  feature/syncfix. [Iglocska]
- Hunting down the remaining issues. [Iglocska]

  - creating a random number for the name should only happen on new entries, not on edits
  - a sharing group edit can still contain new organisations, create them appropriately
- Remove modified from the fields to keep when updating a sharing group.
  [Iglocska]
- Other half of the fix to the UUID issue with sharing groups.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #931 from Rafiot/pick. [Alexandre Dulaunoy]

  Cherry-picked #930
- Add conditions for generateEmailAttachmentObject. [Richard van den
  Berg]
- Add conditions for resolveEmailObservable. [Richard van den Berg]
- Add conditions for generateFileObservable. [Richard van den Berg]
- Set conditions for simple observables. [Richard van den Berg]
- Use constant Exploit Target id. [Richard van den Berg]
- Remove leading backslashes. [Richard van den Berg]
- Fix typo. [Richard van den Berg]
- Add RegKey hives and conditions. [Richard van den Berg]
- Add ExploitTarget title. [Richard van den Berg]
- MISP taxonomies added. [Alexandre Dulaunoy]
- Merge pull request #926 from wllm-rbnt/2.4. [Alexandre Dulaunoy]

  Fix typos
- Fix typos. [William Robinet]
- First take at the fix to the UUID issue with sharing groups.
  [Iglocska]
- Fixes to the event downloads / APIs. [Iglocska]

  - download event as JSON now has the option to include attachments
  - switched to using the restsearch api instead of the deprecated /events/xml API

  - added attachment inclusion to both restsearch apis

  - fixed some bugs with the API
- Added option to download CSVs of non published events. [Iglocska]

  - automatically overrides IDS flag too
- Issue with filter taxonomies details, fixes #920. [Iglocska]

  The filter options are now added to the pagination
- Removing PEM from a server connection parameter, fixes #771.
  [Iglocska]

  - Added a way to remove the certificate file when editing the server connection
  - Also, it shows the currently selected certificate file as it caused some confusion before
- Order alphabetically organisations in list of organisations to add,
  fixes #918. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #919 from deralexxx/patch-1. [Andras Iklody]

  Update Whitelist.php
- Update Whitelist.php. [Alexander J]

  https://github.com/MISP/MISP/issues/681
- Taxonomies update. [Iglocska]
- Tag / taxonomy enabling made easy, fixes #914. [Iglocska]

  - Enable tags for a taxonomy in one go
  - Have an indicator of how many tags there are in the taxonomy and how many are enabled
- Default threat level setting for instance added. [Iglocska]
- Don't display options to users for which they don't have the rights to
  use, fixes #880. [Iglocska]
- Fixed the progress bars on the export view, fixes #902. [Iglocska]
- Template population menu fixes. [Iglocska]
- Fixed a display issue for the template choices when the name of a
  template is empty. [Iglocska]
- Removing template elements fixed, fixes #899. [Iglocska]
- Fixed adding / removing tags to a template, fixes #898. [Iglocska]
- Further fixes to the contact e-mail. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #904 from deralexxx/patch-5. [Andras Iklody]

  Comment a line that includes a comment
- Update INSTALL.ubuntu1404.txt. [Alexander J]
- Fix to the e-mail contents of the contact message. [Iglocska]

v2.4.16 (2016-02-02)
--------------------
- Version bump. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #903 from deralexxx/patch-4. [Andras Iklody]

  Create INSTALL.debian.txt
- Create INSTALL.debian.txt. [Alexander J]

  I know there is already an ubuntu document, but still I found value to have it being mentioned that debian is supported as well

  (There are also some minor changes to the ubuntu docu, would adjust the ubuntu doc as well)
- Fixes to several permission issues with the e-mailer. [Iglocska]

  - contact e-mail recipients were incorrectly set resulting in the e-mails landing at the wrong recipient
  - disabled users were not excluded from certain e-mails

v2.4.15 (2016-02-02)
--------------------
- Version bump. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #897 from koenigswinter/2.4. [Andras Iklody]

  Update INSTALL.ubuntu1404.txt
- Update INSTALL.ubuntu1404.txt. [Heiko Siebel]

  30: + gnupg-agent (apt-get install)
  178: - su www-data -c 'bash /var/www/MISP/app/Console/worker/start.sh', + sudo -u www-data bash /var/www/MISP/app/Console/worker/start.sh (default Ubuntu installation fails to start the workers after a reboot --> "www-data" has no shell in "/etc/passwd").
  220: + pip install redis
- Major speed boost to the correlation. [Iglocska]

  - it seems that for some reason some conditions in the correlation lookup massacred the performance of the correlation
  - doing that additional filter on a PHP level fixes it for now, but it would be interesting to investigate this further and potentially reuse the findings to improve other queries

  - also fixed an issue with the indexing script failing on some fulltext fields if it has to fall back to regular indeces.
- Reverted the automation change. [Iglocska]
- Merge branch 'update_script' into 2.4. [Iglocska]
- Merge pull request #1 from aaronkaplan/aaronkaplan-patch-1. [AaronK]

  Update UPDATE.txt
- Update UPDATE.txt. [AaronK]

  permissions: it's enough to chown -R www-data /var/www/MISP
- Merge branch 'master' of https://github.com/MISP/MISP. [aaronkaplan]
- Updated version check for cybox to be consistent with documentation.
  [David André]

  Related to installation documentation update recommending to use 2.1.0.12 as cybox version (a23027eee4ea9c09d92cf1d5b6f9e69fa9934057)
- Merge branch 'master' of https://github.com/MISP/MISP. [aaronkaplan]
- Merge pull request #727 from abulhol/master. [Andras Iklody]

  added composite domain|ip attribute
- Merge branch 'master' of https://github.com/MISP/MISP. [aaronkaplan]
- Fixed the documentation (automation) page. The JSON URL was wrong.
  [aaronkaplan]
- Left off a view for the org merge tool. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #894 from deralexxx/patch-3. [Alexandre Dulaunoy]

  Update INSTALL.ubuntu1404.txt
- Update INSTALL.ubuntu1404.txt. [Alexander J]

  change base url should be not optional but required for every installation to be changed
- Made the background workers baseline, should make the installation a
  bit easier. [Iglocska]
- Fix to the initial version of the correlation on the event index.
  [Iglocska]

  - also removed an expensive lookup of sharing group permissions required for event views utilising the pagination from being run on actions that do not make use of it
- Correlations on the event index, first implementation. [Iglocska]
- Display and Search for model ID in the audit logs, fixes #889.
  [Iglocska]

v2.4.14 (2016-01-29)
--------------------
- Version bump. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #893 from deralexxx/patch-2. [Alexandre Dulaunoy]

  mention install howto in Documentation part
- Mention install howto in Documentation part. [Alexander J]

  Spent some minutes to find the documentation how tot install MISP (and it is not mentioned in the PDF btw)
- Fix to the Proposal alerts not going out to users after one has
  failed. [Iglocska]
- Flash message if the current user can accept/discard proposals on the
  currently viewed event. [Iglocska]
- Fix to the download as... -> CSV export. [Iglocska]

  - incorrect parameter passed blocked CSVs from being exported when non IDS worthy attributes were meant to be included
- Reverted the header change, added note in app/Config/email on how to
  enable it. [Iglocska]

  - otherwise it might break custom e-mail configurations
- Fix for the previous header issue. [Iglocska]
- Attempt to fix the returnPath issue. [Iglocska]

  - it looks like PHP is overriding the setting
- Set the returnPath header in e-mails correctly. [Iglocska]
- Version bump. [Iglocska]

v2.4.13 (2016-01-28)
--------------------
- Added org merge tool. [Iglocska]

  - allows a site admin to merge all objects belonging to an organisation into another
    - this can be useful if duplicate organisations exist for example
    - the tool overrides the built in mechanism and should only be used if absolutely required
    - at the end of the process the original organisation is removed

  - the tool generates 2 files that are dropped in the log directory of MISP
    - 1 contains a JSON with all the changed fields and the IDs
    - 1 contains an SQL script that allows an admin to revert the changes
- URL fallback when adding users fails for the sync user dropdown.
  [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Fixed typos for organization. [Alexandre Dulaunoy]
- Fixed a bug that caused the "last" parameter in automation to fail.
  [Iglocska]
- Added the option to override attribute creation in the freetext import
  tool for site admins. [Iglocska]

  - site admins can now choose to create proposals instead of attributes via the freetext import tool via a checkbox
- Added a back button on the tag selection, fixes #845. [Iglocska]

  - User can now go back to the taxonomy selection when already in the tag select list
- Use freetext import tool for proposals, fixes #871. [Iglocska]

  - Added the ability to use the freetext import tool for proposals
- Show event owner in the alert e-mail, fixes #361. [Iglocska]
- Fixed an issue with the freetext import. [Iglocska]

  - url detection would detect any word with a trailing "." as a valid url
    - google. was detected as a url
  - this also caused training "."s to be included in valid urls
    - http://www.google.com.
- Copy pasta fail on the populate from template action. [Iglocska]

  - the lookup for valid event access was comparing the user's org name to the event's org id which always failed
- Cleanup of loading attachments into the data fields of event data
  views. [Iglocska]

  - was done inconsistently between attributes and proposals
  - adding it via the fetchEvent method instead of the controller action
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Fix to a translation of the orgs to IDs in the event index filters,
  fixes #868. [Iglocska]

  - it will now use the org name instead of the org ID
  - also, orgs are now sorted alphabetically instead of by ID
- Discussion notification e-mails linked to an invalid url. [Iglocska]
- Fix to a notice in the log search, fixes #872. [Iglocska]
- Fixed an invalid org lookup on the proposal download blocking users
  from downloading proposal attachments, fixes #874. [Iglocska]

v2.4.12 (2016-01-21)
--------------------
- Merge branch 'feature/proposalFix' into 2.4. [Iglocska]
- Entering a valid controller/action and an invalid one produced a
  different result pre-auth. [Iglocska]

  - not authenticated users now automatically get redirected to the login page, no matter what action they requested
  - This as a nice side effect also removed the bug that was caused by a site admin looking at an admin function before logging out / timing out and being incorrectly redirected to /admin/users/login
- Merge pull request #866 from MISP/cybox-version-check. [Andras Iklody]

  Updated version check for cybox to be consistent with documentation
- Updated version check for cybox to be consistent with documentation.
  [David André]

  Related to installation documentation update recommending to use 2.1.0.12 as cybox version (a23027e)
- Same SQL statement twice in a row for the cleanup script. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #865 from MISP/elhoim-patch-1. [Andras Iklody]

  Add php5-mysql in packages to install
- Add php5-mysql in packages to install. [David André]
- Update to the upgrade procedure. [Iglocska]

  - clearer instructions
  - removal script for obsolete columns

  - the removed columns can cause exceptions if not removed as described in #814

v2.4.11 (2016-01-20)
--------------------
- Fix to an invalid org lookup. [Iglocska]

  - prevents normal users from seeing the proposal index
  - still a left-over from 2.3

v2.4.10 (2016-01-20)
--------------------
- Version bump. [Iglocska]
- Fixed an issue with the visibility of proposals to attributes.
  [Iglocska]

  - proposals to attributes didn't adhere to the visibility of the attribute
  - users that were allowed to see an event but not a specific attribute could see proposals to the attribute
- Change to the previous commit. [Iglocska]
- Fix to the pagination of the orgs. [Iglocska]
- Added full text search to organisation index, fixes #803. [Iglocska]

  - also some fixes and enhancements in general for this

v2.4.9 (2016-01-19)
-------------------
- Fix to an issue with the XML cleanup method. [Iglocska]

  - lead to the XML REST add failing
- Attributes not included in the .json / .xml views of an event, leading
  to attachments not being synchronised, fixes #862. [Iglocska]

  - it looks like I've left off the attachment encoding for the REST event view
  - Should be fixed now
- Some changes to the default config file. [Iglocska]
- The new footer had two left feet. [Iglocska]
- Fix to an invalid permission lookup denying users from mass deleting
  attributes due to a copy pasta fail. [Iglocska]
- Removed lowercasing of parsed strings in the freetext import.
  [Iglocska]

  - case sensitive values also got lower-cased
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Pdb attribute - format is not checked. [Alexandre Dulaunoy]
- Pdb attributes added. [Alexandre Dulaunoy]

  pdb stands for Microsoft Program database (PDB) path information
- Whois-registrant-name attribute added. [Alexandre Dulaunoy]
- Adding URIs failed because of the missing validation entry. [Iglocska]
- Replaced the footer text. [Iglocska]

  - added link to the github page of MISP
  - made the text "Powered by MISP vversion_number" fixed
  - Replaced the surrounding text fields with two new fields (empty by default)
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge pull request #856 from rotanid/patch-1. [Raphaël Vinot]

  Update INSTALL.ubuntu1404.txt
- Update INSTALL.ubuntu1404.txt. [Andreas Ziegler]

  Debian 7 (Wheezy) is oldstable since April 2015
- Replaced encoded copyright sign with the sign itself to avoid the
  double encoding in the footer, fixes #853. [Iglocska]
- Reverted a change that leads to the pull failing. [Iglocska]
- Merge pull request #854 from RichieB2B/centos-docs. [Andras Iklody]

  Update CentOS documentation
- CentOS 7 needs chmod +x /etc/rc.local. [Richard van den Berg]
- Restart php-fpm after redis install. [Richard van den Berg]
- Updated MISP 2.4 INSTALL instructions for CentOS 6. [Richard van den
  Berg]
- Updated MISP 2.4 INSTALL instructions for CentOS 7. [Richard van den
  Berg]
- Fix to a bug allowing regular users of the owner organisation to
  edit/delete a synced event as discovered by @h122015. [Iglocska]

  - requirements for the actions changed from an org_id match to an orgc_id match
- Fix to a bug that caused taxonomies to create duplicates instead of
  updating an older version. [Iglocska]
- MISP taxonomies sub-module updated. [Alexandre Dulaunoy]
- Feature request via feathub added. [Alexandre Dulaunoy]
- Fix to an issue with the quickfilters not working, fixes comment by
  ztormhouse. [Iglocska]

  - invalid search on the org field, a remnant from 2.3
  - didn't cause exceptions on migrated issues as the field isn't removed post upgrade
  - throws an exception on fresh installations

  - fix now correctly looks up organisation names matching the entered string and uses the result set to filter the events
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #847 from Rafiot/add_csv_test. [Raphaël Vinot]

  Test CSV download
- Test CSV download. [Raphaël Vinot]
- MISP toolbar logo (CC-BY) [Alexandre Dulaunoy]
- Fix to an invalid data entry pre-validation call that broke prtn
  attribute entry with a leading + [Iglocska]

v2.4.7 (2016-01-14)
-------------------
- Version bump. [Iglocska]
- Merge branch 'feature/proposalFix' into 2.4. [Iglocska]
- Fixes to the proposal system. [Iglocska]

  - proposals were not synchronised during pulls due to a bug
    - affects both 2.3 and 2.4, the bug comes from the switch to json
    - missing JSON view for proposal interface
    - Also, 2.4->2.4 the organisation objects were incorrectly ommited from the sync
    - Fixes:
      - reverted back to XML for the old style proposal exchange
      - 2.3->2.4 is now fixed
      - 2.4->2.4 below 2.4.7 version will still not synchronise proposals on pull

  - Proposal pull reworked
    - requires 2.4.7 on both ends or higher
    - proposals are now synced in one go
    - massive increase in speed and reduction of log entries

  - Proposal e-mailing reworked
    - tied into the new 2.4 e-mailer, which was left out on 2.4's release by accident
    - triggers correctly now when a proposal is added (also on pull)
- Sort orgs alphabetically in user index filters. [Iglocska]
- Fixed missing validation for malware-type type attributes. [Iglocska]
- Order attributes by UUID for the CSV export, fixes #849. [Iglocska]
- Further fix to the previous commit affecting the log search.
  [Iglocska]

  - only show the subset of valid model options for the log search that would yield results based on the current dataset
- Fixed an issue with searching the logs by model where incorrect model
  entries would also show up as options. [Iglocska]
- Several changes to the logs. [Iglocska]

  - index now shows the model that the log entry concerns
  - added model to the search parameters
    - this allows for searches such as new users added (Model:User - action:add)

  - fixed a bug with the log search where going back to the first page of results would return you to the search form
- Added purpose of UPDATE.txt. [Iglocska]
- Small fix to the contact users form for org admins. [Iglocska]
- Fixed a double slashed path in the writeable dir diagnostics.
  [Iglocska]
- Fixed an issue where single event exports would fail. [Iglocska]

  - event id not stored in the events array from the passed parameters
- Check permissions on config files, fixes #837. [Iglocska]

  - red warning on the settings page if the config.php file is not writeable
  - failed changes in settings due to the config.php file not being writeable logged
- Some small changes to the diagnostics. [Iglocska]

  - made the PHP settings check look a bit more clear and changed it from failures to recommendations

  - added a file permission check for config.php (can add more in the future such as the background worker log files which can prevent the workers from starting)
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Make sure the perms are right after the upgrade. [Raphaël Vinot]
- Merge pull request #840 from Rafiot/2.4. [Raphaël Vinot]

  Merge PR #679, add more php version in the travis runs.
- Add php 5.5 and 7.0 in the travis tests. [Raphaël Vinot]
- Merge branch 'pr/679' into 2.4. [Raphaël Vinot]
- Update .travis.yml. [Steve Peak]
- Create .coveragerc. [Steve Peak]
- Debugging coverage. [Steve Peak]
- Add check for values on diagnostics page, fixes #839. [Iglocska]
- Updated an outdated upgrade procedure for cakephp in UPDATE.txt.
  [Iglocska]

  - as described in #833
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Changes to the organisations table in the upgrade script. [Iglocska]

  - matches the changes made to the MYSQL.sql
  - makes contextual fields nullable
- FIxed several issues. [Iglocska]

  - some performance tuning for the restSearch API
  - fixed an issue where overriding the contain parameters in the attribute fetcher would lead to an exception
  - fixed an issue where accepting a proposal would try to copy the sharing group of the event incorrectly (it now simply gets set to inherit event)
  - fixed an issue with the rest search API failing when some fields were not set
- Add org of proposal creator to the event view. [Iglocska]
- Added proposals to the event view attribute filters and fixed some
  descriptions, fixes #828, fixes #827, fixes #821. [Iglocska]
- Rework of the scheduled caching jobs. [Iglocska]

  - fixed a series of issues with the exports

v2.4.6 (2016-01-07)
-------------------
- Fix to a trailing slash in the baseurl breaking the upgrade script.
  [Iglocska]
- Fixed an issue where an event's sharing group ID would get set to the
  first available option even when a non sharing group distribution
  level is selected. [Iglocska]
- Reverted some contextual org fields to nullable. [Iglocska]
- Some cleanup. [Iglocska]
- Added tags to the CSV export, fixes #809. [Iglocska]
- Rework of the CSV export to include tags. [Iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Branch changed for Travis. [Alexandre Dulaunoy]
- Merge pull request #807 from Rafiot/clean_travis. [Raphaël Vinot]

  Update travis for 2.4, use Ubuntu Trusty
- Update travis for 2.4. [Raphaël Vinot]
- Updated upgrade.txt. [Iglocska]
- Quickfilter added for users. [Iglocska]
- Added malware sample to the file attribute filter. [Iglocska]

v2.4.5 (2016-01-04)
-------------------
- First version of the quick filters for the event view. [Iglocska]
- Payload delivery is now the default option for add attachment.
  [Iglocska]
- Multiple file upload added to the add attachment functionality.
  [Iglocska]
- Removed the test values for some attribute descriptions. [Iglocska]

  - still needs some work, few empty ones remain and a few descriptions could use clarification
- Merge branch 'portip' into 2.4. [Iglocska]

  Conflicts:
  	app/Model/Attribute.php
- Merge pull request #1 from abulhol/abulhol-patch-1. [Benjamin
  Gathmann]

  added domain|ip composite attribute
- Added domain|ip composite attribute. [Benjamin Gathmann]
- Typo fixed in whois-creation-date. [Alexandre Dulaunoy]
- Merge pull request #800 from FafnerKeyZee/2.4. [Alexandre Dulaunoy]

  Adding more information about Whois
- Update Attribute.php. [Fafner [_KeyZee_]]
- Merge pull request #1 from MISP/2.4. [Fafner [_KeyZee_]]

  Update from original)
- Fixes to the CSV export. [Iglocska]
- Invalid org capture method lead to orgs with empty UUIDs being matched
  with the first org with no uuid. [Iglocska]
- Add today's date as the event date field if not set. [Iglocska]
- Removal of PGP key generation for travis. [Iglocska]

v2.4.4 (2015-12-30)
-------------------
- Fixes to the first user initialisation. [Iglocska]

  - updated the UserInit command line tool
  - updated the built in user initialisation
- Fixed a typo in the logging that prevented users from being edited,
  fixes #586. [Iglocska]

  - A wrong variable lookup in the logging caused user edits to fail
- Fixes to some of the exports, fixes #798. [Iglocska]

  - Fixed a typo that prevented the event level parameters to be used in the CSV export
  - Fixed an issue where adding the contextual info in a CSV could lead to an invalid CSV if an event info field had a linebreak in it
  - Tuned the performance of time based filtering (until now it would lookup events that should have been excluded in the first place, only to throw them away after the lookup again)
- Initial JSON schema - MISP event (version 2.4) [Alexandre Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge pull request #797 from FafnerKeyZee/2.4. [Andras Iklody]

  Solving #786
- Solving #786. [Fafner [_KeyZee_]]
- Merge pull request #796 from FafnerKeyZee/2.4. [Andras Iklody]

  Fix for orgc_id into TemplatesController.php
- Update TemplatesController.php. [Fafner [_KeyZee_]]
- Updated to the latest version of PyMISP. [Alexandre Dulaunoy]
- Changed the attachment distribution settings to match the attribute
  distribution settings, fixes #777. [iglocska]

  - added inherit event as a distribution option for attachments
- Invalid orgc lookup in the template choice menu, fixes #795.
  [iglocska]
- Fixed some issues with the index length of the value fields in the
  MYSQL.sql file, fies #793. [iglocska]

  - Also some additional issues resolved
- Create cached export dirs if they don't exist, fixes #791. [iglocska]

  - until now it was assumed that the dirs are already created
  - just create them if they don't exist
- Invalid lookup of servers for the scheduled pull. [iglocska]

  - it was erroneously looking up servers that have push enabled instead of pull

v2.4.3 (2015-12-27)
-------------------
- Rework of the contributor field, some MYSQL.sql tweaks. [iglocska]

  - added indeces to the MYSQL.sql file
  - contributors now looks for shadow attributes instead of log entries (should make the event view much faster and resolve some timeout issues on sync when the log is massive)

v2.4.2 (2015-12-26)
-------------------
- Fixes a bug on invalid event IDs passed to the STIX export causing
  long execution times, fixes #747. [iglocska]

  - Running a stix export for a specific ID that doesn't exist results in a full STIX export for the user (events visible to the user)
  - This leads for an unnecesarily long export process when a quick export is expected

v2.4.1 (2015-12-26)
-------------------
- Several fixes to the exports, fixes #790. [iglocska]

  - New generic fetch attribute method was mistakenly using the order field as a condition, resulting in some exports only displaying a subset of the data
    - the fix to this fixes the issue described in #790 for text exports
  - Fix to the RPZ exports not working correctly
  - Fix to the horrible performance of RPZ exports
  - Fix to several background worker issues with exports
- Fixed some background worker issues. [iglocska]

  - scheduled pulls would fail because of invalid user object passed
  - invalid permissions checks / org checks would cause the RPZ export to fail when using background workers

v2.4.0 (2015-12-24)
-------------------
- Merge branch 'feature/fastupgrade' into 2.4. [iglocska]
- Index Correlation values. [iglocska]
- Added the reindexing of all tables to the upgrade procedures.
  [iglocska]
- Left off from previous commit. [iglocska]
- Fix to the templating being broken, fixes #787. [iglocska]
- Fast upgrade v1. [iglocska]
- Fix to several issues with the sync and and an issue preventing the
  editing of events, fixes #788, fixes #784. [iglocska]
- Removed obsolete news page from the side menu, fixes #780. [iglocska]
- CSV memory usage reduction on automation. [iglocska]

  - reduced the number of attributes at the cost of some additional processing time
  - this should reduce very slow processing of large data sets
- Fixed a serious issue with the snort/suricata export which would keep
  appending all eligible attributes over and over to the file instead of
  properly fetching them event by event resulting in a massive export
  file. [iglocska]
- More graceful handling of pgp errors in the emailer. [iglocska]

  - until now the encryption of emails happened in a try catch block
  - however, crypt_gpg throws a fatal error instead of an exception, killing the background worker

  - added an extra checking algorithm that will test the key for a valid encryption key (encryption enabled + not expired)
  - if it's not there, it will just log an error message and continue execution of the other e-mails
- Event tags correctly saved on rest add if they are set in the
  compressed format (event->tag instead of event->eventtag->tag)
  [iglocska]
- When adding/editing a sync user, the choice to limit a user by
  instance settings shows empty lines for instances without a name.
  [iglocska]

  - use the URL in those cases instead
- Editing an event via REST would not capture the tags. [iglocska]

  - if a user is a tagger the tag should be created (if not existing on the current instance) and added to the event
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Added the graphical interface. [Alexandre Dulaunoy]
- Updated to include new functionalities in available in 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of github.com:MISP/MISP into 2.4. [Alexandre
  Dulaunoy]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [Iglocska]
- Don't run the anti IE 8 check on requests that don't have a user agent
  set, fixes #775. [Iglocska]
- MISP screenshot panorama. [Alexandre Dulaunoy]
- Screenshots MISP 2.4 added. [Alexandre Dulaunoy]
- Editing an event with new attributes fails because a new id is not
  assigned correctly, fixes #773. [Iglocska]

  - the process of detecting and editing existing attributes did not account for a case where the uuid is not set for an attribute and therefore should be saved as a new attribute. Fixed
- Fix for an issue with event edits containing a new attribute and it
  not getting an ID as expected. [Iglocska]
- Taxonomies update. [Iglocska]
- Double comment field fixed. [Iglocska]
- Invalid fetchevent call fixed for proposal add attachment. [Iglocska]
- Fixed an issue where non-sharing group events would only send alert
  e-mails to site admins. [Iglocska]
- Typo fixed. [Iglocska]
- Removed crappy automatic CakePHP sorting from recorrelation.
  [Iglocska]

  - /facepalm
- Added indexing of the tables as an admin script. [Iglocska]
- Typo. [Iglocska]
- Missing subject added back. [Iglocska]
- Removed debug. [Iglocska]
- Fix to a previous merge issue with the e-mailer. [Iglocska]
- Fix to the email target on publish. [Iglocska]
- Update cakephp 2.7 to HEAD. [Raphaël Vinot]

  Fix #740
- Removed an accidental addition a while back. [iglocska]
- Fixed a menu and some cleanup. [iglocska]

  - Freetext import was loading the wrong menu
  - some leftover profiling code removed
- Slightly smarter correlation for generateCorrelations. [iglocska]
- Added default values to the log entry creation to avoid empty fields
  giving notices, fixes #769. [iglocska]
- Fix to the correlation peformance. [iglocska]
- More fixes to the background correlation generation. [iglocska]
- Merge branch '2.4' of https://github.com/MISP/MISP into 2.4.
  [iglocska]
- Fix mysql install script. [Raphaël Vinot]
- Changes to the generation recreation. [iglocska]
- Fixed an invalid link, fixes #761. [iglocska]
- Fixed issue with the headmmap, fixes #759 and fixes #760. [iglocska]
- Fixed an issue with discussions where a new thread would not have a
  default distribution and sharing group ID and would fail on creation,
  fixes #758. [iglocska]
- Various fixes. [iglocska]

  - resolved a missing variable issue on event views with no posts fixes #753
  - removed some obsolete code
  - sorted tags on the event view when assigning one to an event by name, fixes #416

  	modified:   app/Model/Taxonomy.php
- Fixed an issue with the upgrade script. [Iglocska]
- Disable e-mailing globally for an instance. [Iglocska]
- Default settings for roles altered. [Iglocska]
- Merge branch 'master' into 2.4-beta. [Iglocska]

  Conflicts:
  	VERSION.json
- Merge branch '2.4-beta' of https://github.com/MISP/MISP into 2.4-beta.
  [Iglocska]
- Fixed an issue with a certain condition combination failing during
  sync. [Iglocska]

  - pushing an event with a sharing group that doesn't exist on the remote and that has the sync user included as part of an all_org instance
  - the saving would generate a 405
- Added some fixes to corner cases. [Iglocska]

  - publishing an event when push is enabled to a 2.3 instance failed with an error instead of blocking
  - publishing an event wth the remote instance blocking it due to a sync user sharing group conflict resulted in an exception, handled gracefully now

  - Added mangle-sync towards 2.3
    - gracefully push non sharing group events in a 2.3 format
    - timestamps downgraded by 1 second - upgrading the 2.3 instance should automatically allow a resync of mangled events
- Merge branch '2.4-syncrework' into 2.4-beta. [Iglocska]

  Conflicts:
  	app/Model/Event.php
- Merge branch '2.4-syncrework' of https://github.com/MISP/MISP into
  2.4-syncrework. [Iglocska]

  Conflicts:
  	app/Controller/LogsController.php
- Event history now takes into account sharing groups. [Iglocska]
- Fix to the HIDS export. [Iglocska]
- Fixed the editing of sharing groups via event updates. [Iglocska]

  - if a sync user adds / edits an event with a newer version of a sharing group
  and the sync user is the local sync user of the SG or is an extender of the SG
  then the sharing group will be updated

  - valid changes:
    - Sharing group metadata changes
    - organisation detail changes (except uuid/name)
    - add / remove extend flag from orgs in the SG
    - add / remove all_orgs flag from servers in the SG
- Fix to the event filtering on organisation. [Iglocska]

  - org filters now accept org ID or org Name as parameter, fixing the sync filter

  - Also, fix to saving sharing group IDs on sync edits on an attribute level
- Merge branch '2.4-syncrework' of https://github.com/MISP/MISP into
  2.4-syncrework. [Iglocska]
- Extend field added to sharinggrouporg object on fetchevent. [Iglocska]
- Capture the sharing groups of attributes on event edit. [Iglocska]
- Merge branch '2.4-syncrework' of https://github.com/MISP/MISP into
  2.4-syncrework. [Iglocska]

  Conflicts:
  	app/Model/Event.php
- Merge branch '2.4-syncrework' of https://github.com/MISP/MISP into
  2.4-syncrework. [Iglocska]
- Correct conversion of the own server before sync. [Iglocska]

  - also a small fix to the event tags and unicode chars
- Further fixes to the sync. [Iglocska]

  - corrected the edit access rights for sync users with sharing groups
  - Various fixes to the organisation sync and how creation / modification dates are transmitted
  - Internal format differences compared to 2.3 causing mismatched field lookups fixed
- Merge branch '2.4-syncrework' of https://github.com/MISP/MISP into
  2.4-syncrework. [Iglocska]
- Further fixes on the sharing group sync. [Iglocska]
- Org and SG fixes for issues that are breaking the functionality.
  [Iglocska]
- Allow orgs to not have uuids. [Iglocska]

  - only in if they are external orgs
- More junk. [Iglocska]
- Only capture objects when adding an event via the API. [Iglocska]
- Removed junk. [Iglocska]
- Disable users. [Iglocska]

  - users can now be disabled by an admin
  - disabled users cannot login (via the UI or the API) and will be informed
  - login attempts by disabled users are logged

  - also added the expiration field for later use
- Merge branch '2.4-syncrework' of https://github.com/MISP/MISP into
  2.4-syncrework. [Iglocska]
- Further progress on the sync rework. [Iglocska]
- Fixed the locked field not being set on push. [Iglocska]
- Sharing group changes depend on modification time. [Iglocska]
- Fix to the Discussion boards. [Iglocska]
- Small fixes. [Iglocska]
- Merge branch 'master' into 2.4-syncrework. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/AttributesController.php
  	app/Controller/ShadowAttributesController.php
  	app/Lib/Tools/ComplexTypeTool.php
  	app/Model/Attribute.php
  	app/View/Pages/administration.ctp
- Visual fixes. [Iglocska]
- Further progress on the sync. [Iglocska]

  - also, added maintenance mode
  - various fixes
- Further progress. [Iglocska]
- Further work on the sync. [Iglocska]
- Merge artifact removed. [Iglocska]
- Fix to the download as failing due to an incorrect fetch to check if
  the event is visible to the user. [Iglocska]
- First stab at the push filters influencing the pull of a remote
  instance. [Iglocska]
- Further work on the discussions complete for now. [Iglocska]

  - adding a new post automatically scrolls to the new post
  - adding/editing/deleting posts persists the context (discussion thread vs event view)
- Finish of the new discussion post add. [Iglocska]

  - flips to the page where the post was added
  - scrolls to the last post
- Merge and rework of the thread pagination. [Iglocska]

  - not complete yet

  Merge branch 'master' into 2.4-beta

  Conflicts:
  	VERSION.json
  	app/Controller/EventsController.php
- Fixes to the logging. [Iglocska]

  - in some places MISP tried to save the org ID instead of the org name in the logs

  - fixed
- Added the possibility to enable debug for site admins. [Iglocska]

  - new option in server settings
  - enable debug (equal to normal debug level 1) for site admins only

  - regular users will be unaffected
- Also, enabled the filtering on pull. [Iglocska]

  Merge branch 'master' into 2.4-beta

  Conflicts:
  	VERSION.json
  	app/Controller/EventsController.php
  	app/Lib/Tools/XMLConverterTool.php
  	app/Model/Event.php
  	app/Model/Server.php
- Merge branch 'master' into 2.4-beta. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/EventsController.php
  	app/Controller/ShadowAttributesController.php
  	app/Model/Event.php
  	app/View/Elements/side_menu.ctp
- Some small taxonomy fixes. [Iglocska]
- Various fixes throughout the application. [Iglocska]

  - org field still used in some places other than the legitimate use-cases
- Rework of the taxonomies. [Iglocska]

  - users can now add taxonomy tags separately from normal tags on the event view
  - tag index now shows taxonomy
- Fix to logging causing certain functions to fail on migrated
  installations. [Iglocska]
- Blocked the colour update when the taxonomies are updated. [Iglocska]

  - better to not overwrite the local tag colours unless the tag is refreshed from the taxonomy view. A gree tlp:red looks silly.
- Temporarily re-added org field for jobs. [Iglocska]
- Further work on the taxonomies. [Iglocska]

  - colour coding
  - filters on the index
  - mass tag creation
- Updated taxonomies. [Iglocska]
- Update to the Taxonomies. [iglocska]
- First bash at Taxonomies. [iglocska]

  What works:
  - added submodules for taxonomies
  - added import tool for taxonomies
  - added models and convenience functions for taxonomies

  - site admins can update taxonomy libraries
  - list taxonomies / view indvidual ones (with all resolved tags)
  - create tags manually if a taxonomy is enabled
  - view related tags / events quickly from the Taxonomy view

  What doesn't work:
  - Users still cannot choose a tag from taxonomy lists (this will be the main functionality)
  - Feature cannot be disabled
- Update to the gitignore. [iglocska]
- Removed nested gitignores. [iglocska]
- Merge branch 'master' into 2.4-beta. [iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/Component/IOCImportComponent.php
- Added file as an option when a url like google.com is recognised.
  [iglocska]
- Memberslist now links to the organisations. [iglocska]
- Fix to a bug in the template attribute creation. [iglocska]
- New category lookup added to templates. [iglocska]
- Fix to the ZMQ call on publish incorrectly passing data to the event
  fetcher. [iglocska]
- Some bugs resolved. [iglocska]
- Empty server list causes the user creation to fail. [iglocska]

  - fixed
- Fixed a newly introduced bug in the IOC import component. [iglocska]
- Fixed too restrictive generateCorrelation attribute fields. [iglocska]
- Small fix to the upgrade script. [iglocska]
- Merge branch 'master' into 2.4-beta. [iglocska]

  Conflicts:
  	VERSION.json
- Fix to a bug in the financial tool's validation router. [iglocska]

  - it didn't use the validation type -> validation method array to call the validation function
  - resulted in CC validation not being called as expected
- Some left over merging issues among other things. [iglocska]
- Merge branch 'master' into 2.4-beta. [iglocska]

  Conflicts:
  	VERSION.json
  	app/View/Attributes/index.ctp
  	app/View/Elements/eventattribute.ctp
  	app/View/Elements/global_menu.ctp
  	app/View/Elements/side_menu.ctp
  	app/View/Events/automation.ctp
  	app/View/Events/index.ctp
  	app/View/Pages/administration.ctp
  	app/View/ShadowAttributes/index.ctp
  	app/View/Tags/index.ctp
- Added logo to organisation page. [iglocska]
- Merge branch 'master' into 2.4-beta. [iglocska]

  Conflicts:
  	VERSION.json
  	app/Lib/Tools/XMLConverterTool.php
  	app/Model/Event.php
  	app/Model/EventTag.php
  	app/Model/TemplateElementAttribute.php
  	app/Model/TemplateElementFile.php
  	app/Model/TemplateElementText.php
  	app/Model/ThreatLevel.php
  	app/View/Attributes/index.ctp
  	app/View/Elements/eventattribute.ctp
  	app/View/Elements/eventattributerow.ctp
  	app/View/Elements/global_menu.ctp
  	app/View/Elements/side_menu.ctp
  	app/View/Events/automation.ctp
  	app/View/Events/index.ctp
  	app/View/Pages/administration.ctp
  	app/View/ShadowAttributes/index.ctp
  	app/View/Tags/index.ctp
- Fixed an issue with the blacklists not saving the event org.
  [iglocska]
- Fix to an invalid json request detection leading to the JSON export
  failing. [iglocska]

  - It seems like relying on the Accept header can lead to the data type detection failing when accessing .json extension views
  - this issue seems to have gone unnoticed since until now the data passed to the json view was the same as that passed to the html view
  - this means that all the additional UI only features may have triggered in the background previously on .json views
- Permission checks. [iglocska]
- Merge branch 'master' into 2.4-beta. [iglocska]

  Conflicts:
  	VERSION.json
  	app/View/Elements/side_menu.ctp
  	app/View/Pages/administration.ctp
- Added the publisher role to the default role set. [iglocska]
- Tighter control over deleting organisations. [iglocska]
- Merge branch 'master' into 2.4-beta. [iglocska]

  Conflicts:
  	VERSION.json
- Merge branch 'master' into 2.4-beta. [iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/EventsController.php
- Merge branch 'master' into 2.4-beta. [iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/AttributesController.php
  	app/Controller/EventsController.php
  	app/Model/Event.php
- Fixed the proposal attachment upload. [iglocska]

  - was bugged before since the switch to the new format
  - comments were not enabled

  - fixed an issue where a proposed attribute could not be downloaded as it was pointing to a file in the attribute attachment directory
- Double click edit of attribute values wasn't working. [iglocska]

  - fixed
- Moved the logic for flagging an attribute for a validation issue to
  the model. [iglocska]
- Warning icon if a financial indicator fails the validation. [iglocska]
- Bin number added to validation. [iglocska]
- Comments now correctly save on attachments. [iglocska]
- Clarification of the malware checkbox on add attachment. [iglocska]
- Relaxed financial attribute validation. [iglocska]

  - also added 2 new types: bank-account-nr and aba-rtn
  - validation is completely relaxed
  - idea is to add a visual notification in the view for these attributes types if they are not valid (invalid financial indicators are still interesting)
- Some fixes to the api authentication. [iglocska]

  - Handle user not found gracefully
  - Log the failed authentication correctly
- Merge branch 'master' into 2.4-beta. [iglocska]

  Merge and upgrade of several new features

  Conflicts:
  	VERSION.json
  	app/Controller/ShadowAttributesController.php
  	app/Controller/TagsController.php
  	app/Model/AppModel.php
  	app/Model/Event.php
  	app/Plugin/SysLogLogable/Model/Behavior/SysLogLogableBehavior.php
- Merge branch 'master' into 2.4-beta. [Iglocska]

  Also, reworked a lot of remaining distribution checks not handled by the main fetch methods

  Conflicts:
  	VERSION.json
  	app/Controller/AttributesController.php
  	app/Controller/ShadowAttributesController.php
  	app/View/ShadowAttributes/add.ctp
  	app/View/ShadowAttributes/edit.ctp
- Merge branch 'feature/sg' into 2.4-beta. [iglocska]
- Merge branch 'feature/sg' of https://github.com/MISP/MISP into
  feature/sg. [iglocska]
- Small fix to the syslog. [iglocska]
- Merge branch 'master' into feature/sg. [iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/ShadowAttributesController.php
  	app/Lib/Tools/JSONConverterTool.php
  	app/Lib/Tools/XMLConverterTool.php
  	app/Model/User.php
  	app/View/Elements/eventattribute.ctp
- Fix to loading the correct logos in the graph view. [iglocska]
- Damn d3.js... Finally it doesn't bug out. [iglocska]
- Fixed an issue where orgs without a logo would not have the
  placeholder logo shown on graphs. [iglocska]
- Various bugfixes. [iglocska]
- Fix to the cc validator. [iglocska]
- Debug removed. [iglocska]
- Fix to the financial tool (incorrect CC validation) [iglocska]
- Updated the server preview to work between 2.4 instances. [iglocska]
- Fixed the index view to include the new objects in json view.
  [iglocska]
- Check if a tag is pushed with an event before trying to loop through
  the tags... [iglocska]
- Fixes to some validations issues using cakephp 2.7. [iglocska]
- Fix to the pubsub tool. [iglocska]
- Small fix thta resolves the inability to delete orgs. [iglocska]
- Further progress. [iglocska]

  - rework of the push mechanism
  - rework of the object capture on add
  - rework of the sync filter UI
- Further work on the filter UI. [iglocska]
- Fixed an issue with ajax forms. [Iglocska]
- New feature: Proposal to delete attribute, fixes #315. [Iglocska]

  - Users can now propose a deletion to an attribute
    - also tied into the mass accept mechanism
    - new UI elements to go along with this

  - Code refactoring for category list retrievals
    - Until now, several methods got the list of categories from the validation code
    - Was awkward with a fake empty element that had to be removed
    - altered the validation code to read the categoryDefinitions array instead
- Fixed a faulty replace that causes an infinite loop during the uuid
  generation. [Iglocska]
- Moved remaining UUID generation calls to the new uuid wrapper.
  [Iglocska]
- Fixed some more invalid org checks. [Iglocska]
- Fixes to the first time initialisation script. [Iglocska]
- Fixes to bugs with org usage from 2.3. [Iglocska]
- Removed debug. [Iglocska]
- Added the first version of the correlation graphing. [Iglocska]

  Conflicts:
  	VERSION.json
- Merge branch 'master' into feature/sg. [Iglocska]

  Merging all the new changes from master

  Conflicts:
  	VERSION.json
  	app/Console/Command/AdminShell.php
  	app/Controller/AttributesController.php
  	app/Controller/EventsController.php
  	app/Model/Attribute.php
  	app/Model/Event.php
  	app/Model/Log.php
  	app/Model/Server.php
  	app/Model/User.php
  	app/View/Elements/side_menu.ctp
  	app/View/Pages/administration.ctp
  	app/View/Users/admin_index.ctp
- Set of changes to the sync. [Iglocska]

  - finished preview feature
    - can now view events and attributes remotely
    - can copy over new event to local instance

  - new sync mode (update)
    - allows to only pull changes to events that exist locally already
    - works well with the manual pull of events, no need to pull events that we didn't manually confirm, but can still update all events that we pulled over

  - Fixed an issue with background tasks causing the logging to fail

  - reworked connection test showing version numbers of both instances
    - also telling the admin whether the sync is compatible or not

  - Further refactoring / tweaking of the vent view
- Progress on several features. [Iglocska]

  - implemented a custom pagination tool for data sets that are not directly taken from teh db
    - currently creates a pagination object that mocks CakePHP pagination
    - supports the CakePHP pagination view helper
    - supports: pagination, sorting, custom filters

  - implemented first step of the remote instance browser for admins
    - view an index of events on another instance
    - filter the events
    - uses the new pagination

  - still missing:
    - remote event view
    - fetch event from remote instance

  - reworked the event view
    - separated API and UI code path
      - major speedup for the API!
      - cleaner code as there was almost 0 overlap
    - discussions and attributes are now loaded separately from the event view
      - added after the event view loads via ajax
      - cleaner pagination
    - attribute pagination now finally allows for sorting
      - future improvement (coming soon): Show proposals only filter
      - filtering on the attributes in general
- 1st version of the upgrade documentation. [Iglocska]
- Progress on the sync. [iglocska]

  - pull from 2.3 -> 2.4 should work correctly now
- Added some fixes for XSS. [Iglocska]
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/EventsController.php
  	app/Controller/ServersController.php
  	app/Model/Attribute.php
  	app/View/Users/statistics.ctp
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Model/Tag.php
  	app/files/scripts/misp2stix.py
- First revision of the upgrade scripts. [Iglocska]

  - .sql file to add all the new fields / tables
  - admin tool to convert the old organisation fields to the new objects
  - still missing a cleanup method (to remove the old organisation fields once the conversion is done)
- Fix to an unescaped ID that could be used to inject XSS into the side
  menu on some views. [Iglocska]
- Flag incorrectly set for event edit's publishing right check.
  [Iglocska]
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/EventsController.php
- Contact details fixed in org add/edit. [Iglocska]
- Fix to the memberslist. [Iglocska]
- Cleanup and fixes to the memberslist. [Iglocska]
- Further progress. [Iglocska]
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/AttributesController.php
  	app/Controller/EventsController.php
  	app/Model/Attribute.php
  	app/Model/Event.php
  	app/Model/Server.php
- Relaxed visibility of org UUIDs and sharing groups (the latter for
  sync users) [Iglocska]
- Copy pasta fail. [Iglocska]
- Removed SG options if no SGs exist from attribute creation/edit.
  [Iglocska]
- Don't offer the SG option in the event add form if none exist.
  [Iglocska]
- Removed accidental inclusion. [Iglocska]
- Further work on the Sharing Groups. [Iglocska]
- Added the server filters to the server creation. [Iglocska]
- Duplicate field removed in MYSQL.sql. [Iglocska]
- Small fix to the js scripts involved in the sync rule creation.
  [Iglocska]
- UI for server filter rule editing finished. [Iglocska]
- Further work on the sync filters. [Iglocska]
- Slightly better looks. [Iglocska]
- Filters shown correctly when editing a server. [Iglocska]
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Model/Attribute.php
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Model/Attribute.php
  	app/Model/Event.php
- Updated MYSQL.sql. [Iglocska]
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
- Some work on the new types. [Iglocska]
- Merges. [Iglocska]
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Lib/Tools/XMLConverterTool.php
  	app/Model/Event.php
- Work on the new attribute types. [Iglocska]
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	VERSION.json
  	app/Controller/ServersController.php
  	app/Controller/ShadowAttributesController.php
  	app/Controller/UsersController.php
  	app/Model/Event.php
  	app/webroot/js/ajaxification.js
- Some merge issues removed. [Iglocska]
- Merge branch 'master' into feature/sg. [Iglocska]

  The merging is complete

  Conflicts:
  	VERSION.json
  	app/Console/Command/ServerShell.php
  	app/Controller/AppController.php
  	app/Controller/AttributesController.php
  	app/Controller/EventsController.php
  	app/Controller/PostsController.php
  	app/Controller/UsersController.php
  	app/Model/Attribute.php
  	app/Model/Event.php
  	app/Model/Log.php
  	app/Model/Server.php
  	app/Model/User.php
  	app/View/Elements/side_menu.ctp
  	app/View/Users/admin_index.ctp
  	app/webroot/js/ajaxification.js
- Progress on the sync. [Iglocska]

  - Creating objects whenever necessary during sync (sharing groups, organisations, etc)
  - it's still :construction:, but time to sleep
- More changes to the sync. [Iglocska]

  - pushes are now taking into account the push_rules and pull_rules fields
- Further work on the sync. [Iglocska]

  - sharing groups are now correctly checked in restfullEventToServer
  - The rules are very simple, the event has to:
    - be of distribution value 2 or 3
    - or 4 given that the attached sharing group meets the following requirements:
      - The sync user is in the sharing group's org list (otherwise he can't transfer it / become the owner)
      - Or the instance that is being synced to has to be set to "all_orgs"
      - The SG has to either not include any instances
      - Or include the instance that is being synced to
- Work on the sync. [Iglocska]

  - commit to update secondary test instance
- CheckVersionCompatibility tool finished. [Iglocska]

  - compares the local to the remote version
  - creates log entries for mismatches / connection issues
  - should be used for any server to server action
- Allow login via header for getVersion. [Iglocska]
- Version negotiation. [Iglocska]
- Futher fixes. [Iglocska]

  - organisations don't show any other tabs than events if they aren't local
  - some fixes with the SG generated text before creation
- Several changes. [Iglocska]

  - UI cleanup
  - separate view for active / passive sharing groups
  - deletion of SGs is blocked if there are still events / attributes / threads around that belong to the SG
- Finished the connection test tool. [Iglocska]
- Added connection test. [Iglocska]

  - also a fix to checkAuthUser
- Fixed the Org field on the user view. [Iglocska]
- New Server add / edit. [Iglocska]

  - add the remote organisation while adding a server
  - remote organisation can be chosen from the list of local or known remote organisations. Alternatively a new remote org can be created on the fly
  - Several UI changes
- Server moved to new org object. [Iglocska]

  - relation added
  - index updated
- Further progress. [Iglocska]

  - removed some junk
  - more work on the background workers
  - rewrote the correlation background job - should work correctly now and be a lot more memory efficient
- Some fixes to the background workers. [Iglocska]

  - also added date tracking on jobs
- Tags added to the e-mail. [Iglocska]
- Lots of progress. [Iglocska]

  - further work on implementing the SG changes everywhere
  - reworked the alert e-mails
  - reworked a lot of the logging
  - several convenience methods
- Fixed xml download of search results. [Iglocska]

  - was using an outdated local xml converter
  - it now correctly points to the XML conversion tool
- Several fixes. [Iglocska]

  - views updated
  - menues updated
  - fixed attribute search
- Further progress. [iglocska]
- Sharing groups correctly selectable in attributes. [Iglocska]

  - still needs work
- Further work on the new version. [Iglocska]

  - org checks fixed in a lot of places
  - fixed the searches to work with the new organisations
- Further work on the sharing groups. [Iglocska]
- Further work and some cleanup. [Iglocska]

  - decision to be revised: exports don't expose Sharing groups / org uuids to users unless they are admin (for the future: at least sync users have to be added for the new sync)
- Progress in moving all exports to the new distribution system.
  [Iglocska]
- Merge branch 'master' into feature/sg. [Iglocska]

  Conflicts:
  	app/Controller/EventsController.php
  	app/Controller/UsersController.php
  	app/Model/Event.php
- Further work on the sharing groups. [iglocska]

  - correlations should work fine now
  - users can only see events they should be allowed to see on the event index / event view / event history view
- Further work on the sharing groups: [iglocska]

  - changes to the data model
  - correlation engine updated
- User edit fixed. [iglocska]

  - choose organisation from a list as expected
  - fixed refreshauth
- Update to the roles and user filtering. [iglocska]

  - new role permission added for SG editors
  - roles reworked, permissions all looked up centrally from the role model instead of code replication across controllers and views
  - user filtering now correctly uses organisation objects instead of org strings
- Further work on the sharing groups. [iglocska]
- Further progress. [iglocska]
- Merge branch 'master' into feature/sg. [iglocska]

  Conflicts:
  	app/webroot/js/ajaxification.js
- Removed debug line. [iglocska]
- Initial commit. [iglocska]

v2.3.178 (2015-12-14)
---------------------
- Merge branch 'hotfix-2.3.178' [iglocska]
- Fixed an issue with the freetext importer where unsetting a duplicate
  value would not be reflected in the entry IDs. [iglocska]

  - this caused some attributes to be dropped from the end of the list
- Merge branch 'hotfix-2.3.177' [iglocska]
- Double quoting of quoted messages in discussion threads fixed.
  [iglocska]

v2.3.177 (2015-12-08)
---------------------
- Merge branch 'hotfix-2.3.177' [iglocska]
- Invalid message fixed when accepting several proposals at once.
  [iglocska]

v2.3.176 (2015-12-08)
---------------------
- Merge branch 'hotfix-2.3.176' [iglocska]
- Several fixes, among others fixes #748. [iglocska]

  - Double sanitisation when edditing an attribute/proposal comment removed
  - Fixed an issue where an ip/resource was recognised as a CIDR notation IP range instead of a url
  - Changed the flash message for publishing without e-mails to something less scary

v2.3.175 (2015-12-04)
---------------------
- Merge branch 'hotfix-2.3.175' [iglocska]
- Fix to a missing Log Model init causing an exception. [iglocska]
- Fix to the previous fix. [iglocska]

  - Flipped it the wrong way, fixed now
- Merge branch 'hotfix-2.3.174' [iglocska]
- Small fix to the previous commit. [iglocska]

  - Small fix to a copy-paste fail
- Merge branch 'hotfix-2.3.174' [iglocska]
- Further tweaks. [iglocska]

  - fixed some corner cases
  - added support for the same defanging to the freetext import tool
- Update to attribute validation and the freetext import tool, fixes
  #742. [iglocska]

  - defanged URL type attributes are refanged on input
  - admin script to do the same for all existing attributes

  - admin tool doesn't recognise a word followed by a . as a url

v2.3.174 (2015-12-04)
---------------------
- Merge branch 'hotfix-2.3.173' [iglocska]
- Junk left in the previous commit. [iglocska]

v2.3.173 (2015-12-02)
---------------------
- Merge branch 'hotfix-2.3.173' [iglocska]
- Filter and discussion changes. [iglocska]

  - event index filtering now accepts POST requests with a json object
    - format has to be filter syntax passed for each field. Example:
      - {"tags":"OSINT|TLP:WHITE|!PRIVINT", "published":"1"}
    - Fixed an issue with no tags being recognised leading to the index returning an unfiltered list
    - Required for filtered pulls from 2.4

  - Discussions
    - Event discussion thread initiated on first post instead of first view
- Merge branch 'hotfix-2.3.172' [iglocska]
- Fix to an incorrect call on sending out alert emails on edit.
  [iglocska]

v2.3.172 (2015-12-01)
---------------------
- Merge branch 'hotfix-2.3.172' [iglocska]
- Fix to a newly introduced bug that breaks updates of attributes via
  pulls. [iglocska]
- Merge branch 'hotfix-2.3.171' [iglocska]
- Rework of the event add/edit. [iglocska]

  - allows for saving an event even if an attribute fails
    - logs attributes that fail validation

  - same for edit

  - add_misp_export updated with the above in mind

v2.3.171 (2015-12-01)
---------------------
- Merge branch 'hotfix-2.3.170' [iglocska]
- Version bump. [iglocska]
- Reimplementation of the Add XML feature. [iglocska]

  - called Add MISP export now
  - can be an XML / JSON file
  - result browser with explanations of failures

  - REST XML/JSON add/edit of events returns errors instead of the partially succeeding event

v2.3.169 (2015-11-27)
---------------------
- Merge branch 'hotfix-2.3.169' [iglocska]
- Delete proposal attachment if the proposal was accepted / discarded.
  [iglocska]

  - there is no need to keep retransfering the actual attached file if all we want to convey is that the proposal is gone.

v2.3.168 (2015-11-27)
---------------------
- Merge branch 'hotfix-2.3.168' [iglocska]
- Fix to an issue where a proposal with an attachment could not be
  correctly accepted. [iglocska]

v2.3.167 (2015-11-26)
---------------------
- Merge branch 'hotfix-2.3.167' [iglocska]
- Updated CakePHP version to 2.7.7. [iglocska]
- Merge branch 'hotfix-2.3.166' into develop. [iglocska]
- Merge branch 'hotfix-2.3.165' into develop. [iglocska]
- Merge branch 'hotfix-2.3.166' [iglocska]
- Left off the view file from the previous commit. [iglocska]

v2.3.166 (2015-11-26)
---------------------
- Merge branch 'hotfix-2.3.166' [iglocska]
- Backport of a fix to 2.4 adding comments to proposed attachments.
  [iglocska]

v2.3.165 (2015-11-26)
---------------------
- Merge branch 'hotfix-2.3.165' [iglocska]
- Fix to an issue with the proposal uploader. [iglocska]

  - also a small fix to the baseurl auto detection
- Merge branch 'master' into develop. [iglocska]
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Initial JSON schema - MISP event (version 2.3) [Alexandre Dulaunoy]

v2.3.164 (2015-11-22)
---------------------
- Merge branch 'hotfix-2.3.164' [iglocska]
- Changes to the OpenIOC Import, fixes #725. [iglocska]

  - Removed the OpenIOC Indicator UUID persistence and moved it to a comment
    - this allows for the same OpenIOC report to be imported into separate events and won't result in a UUID collision

  - Reworked the composite indicator resolver
    - more generic, allows for 3 part composites (to allow for regkeypath/regkey/regvalue combinations)

  - Registry values now correctly recognised
- Merge branch 'hotfix-2.3.163' into develop. [iglocska]
- Merge branch 'master' into develop. [iglocska]
- Merge branch 'hotfix-2.3.161' into develop. [iglocska]

v2.3.163 (2015-11-19)
---------------------
- Merge branch 'hotfix-2.3.163' [iglocska]
- Version bump. [iglocska]
- Bugfix pack, fixes #724, fixes #721. [iglocska]

  - Fixed an issue with the new UUID generation method call in OpenIOC
  - Fixed an invalid validation check on the salt key

  - Added a note on the server page to make it more obvious that values can be changed by double clicking them

v2.3.162 (2015-11-17)
---------------------
- Merge branch 'hotfix-2.3.162' [iglocska]

  Conflicts:
  	app/View/Elements/side_menu.ctp
- Security fix fixing an XSS issue with the templates. [iglocska]

  - as discovered and reported by Rafael Pablos García of INCIBE

  - fixed a reflected XSS for template creator users when viewing a template
- Merge branch 'hotfix-2.3.160' into develop. [iglocska]
- Merge branch 'hotfix-2.3.159' into develop. [iglocska]
- Merge branch 'hotfix-2.3.158' into develop. [iglocska]
- Merge branch 'hotfix-2.3.157' into develop. [iglocska]
- Merge branch 'hotfix-2.3.156' into develop. [iglocska]
- Merge branch 'hotfix-2.3.155' into develop. [iglocska]
- Merge branch 'hotfix-2.3.154' into develop. [iglocska]
- Merge branch 'hotfix-2.3.153' into develop. [iglocska]
- Merge branch 'hotfix-2.3.152' into develop. [iglocska]
- Merge branch 'hotfix-2.3.161' [iglocska]
- Fix to a recent patch breaking the publish button. [iglocska]

v2.3.161 (2015-11-17)
---------------------
- Merge branch 'hotfix-2.3.160' [iglocska]
- Reverted the sanitisation of the baseurl variable on the view level.
  [iglocska]

  - sanitising it in appcontroller instead

v2.3.160 (2015-11-16)
---------------------
- Merge branch 'hotfix-2.3.160' [iglocska]
- Fixed some deprecated validations left over from the purge a few weeks
  ago. [iglocska]
- Merge branch 'basedir' into hotfix-2.3.160. [iglocska]

  Conflicts:
  	app/Controller/AppController.php
  	app/View/Pages/administration.ctp
- Updated an anchor that was missed previously. [pugilist]
- Patched termsaccepted and change_pw checks to redirect properly when a
  base directory is specified. [pugilist]
- Modified img tags to use baseurl. [pugilist]
- Modified many instances of html anchors and javascript
  document.location to use. [pugilist]
- Modified beforefilter to allow  to be accessed by all views.
  [pugilist]
- Removed a crappy solution to an issue with attributes being
  overwritten that was fixed a long time ago correctly on data entry.
  [iglocska]
- Fixed a security issue with the regular expressions. [iglocska]

  - as discovered and reported by Egidio Romano of Minded Security

  - Users with the perm_regex permissions could create a malicious regex that leads to RCE using the PHP /e modifier for preg_replace().
  - Regular expressions are now sanitised on edit / creation of the malicious modifier

  - also added an admin tool that lets admins clean their current set of regexes of the harmful modifier

v2.3.159 (2015-11-15)
---------------------
- Merge branch 'hotfix-2.3.159' [iglocska]
- Fixed an invalid detection of JSON requests when not passing the
  accept header. [iglocska]

  - some json actions worked by passing the .json extension in the url
  - these pages were correctly returning JSONs but were often internally running through the HTML code-path thanks to an invalid detection
  - the new correct detection should provide a major speed boost for certain json requests
- Added logging of auth key changes, fixes #715. [iglocska]

  - Changing the auth key now creates a log entry that inclues the user's ID, e-mail address old and new autkeys
  - Also removed the logging of the hashed password for newly created users
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- PyMISP submodule updated. [Alexandre Dulaunoy]
- PyMISP updated. [Alexandre Dulaunoy]

v2.3.158 (2015-11-13)
---------------------
- Merge branch 'hotfix-2.3.158' [iglocska]
- Version bump. [iglocska]
- Added an additional role to the default installation. [iglocska]

  - by default there was no publisher role
- Fixed a security issue with the CSRF protection being avoidable using
  some site admin functionality. [iglocska]

  - as discovered and reported by Egidio Romano of Minded Security

  - Lacking checks of HTTP methods in some functionality could lead to a site admin uploading and executing malicious scripts

  - Tightened HTTP method verification across the board for actions that modify data
  - Turned some administrative tasks to POST only actions
- Fixed a security issue with the site admin file uploader. [iglocska]

  - as discovered and reported by Egidio Romano of Minded Security

  - The site admin file upload tool allowed for unrestricted file upload that could lead to RCE
  - Fixed the file uploader to be much more restrictive
  - removed the interactive terms file upload
- Merge branch 'hotfix-2.3.157' [iglocska]
- Fixed an issue where PGP keys that are set to never expire show up as
  expired. [iglocska]

v2.3.157 (2015-11-12)
---------------------
- Merge branch 'hotfix-2.3.156' [iglocska]
- Better verification of PGP keys. [iglocska]

  - checks whether the key can be used to encrypt and whether it's expired

v2.3.156 (2015-11-11)
---------------------
- Merge branch 'hotfix-2.3.155' [iglocska]
- Merge branch 'hotfix-2.3.154' into hotfix-2.3.155. [iglocska]

  Conflicts:
  	VERSION.json
- Fix to a security issue. [iglocska]

  - as reported by RichieB2B
  - Trying to view an event that doesn't exist and one that the user has no access to resulted in different error messages
- Fix to a security issue in the PGP fetching tool. [iglocska]

  - reported by RichieB2B
  - The scraped URL for the PGP fetching tool was not sanitised before being echoed

v2.3.155 (2015-11-10)
---------------------
- Merge branch 'hotfix-2.3.155' [iglocska]
- Fix to 2 security issues as reported by RichieB2B. [iglocska]

  - The scraped URL for the PGP fetching tool was not sanitised before being echoed
  - Trying to view an event that doesn't exist and one that the user has no access to resulted in different error messages

v2.3.154 (2015-11-10)
---------------------
- Merge branch 'hotfix-2.3.154' [iglocska]
- Fixed an issue where a linebreak in an event info would break the CSV
  export, fixes #710. [iglocska]

  - also added comment field for attributes
  - until now multi line fields were both escaped and the line breaks removed
    - this was overkill, linebreaks are now kept intact

v2.3.153 (2015-11-09)
---------------------
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Updated PyMISP to the latest version. [Alexandre Dulaunoy]
- Merge branch 'hotfix-2.3.153' [iglocska]
- Fixed a bug with the attribute search API. [iglocska]

v2.3.152 (2015-11-08)
---------------------
- Merge branch 'hotfix-2.3.152' [iglocska]
- Fix to the CSV export, fixes #710. [iglocska]
- Improved logging, fixes #695. [iglocska]

  - Added logging of failed login attempts
  - Added (optional) logging of successful authentications
    - admin setting that has to be enabled
    - will log all API calls (both HTTP method and target url)

  - optional logging of user IP address for all logs
    - each log entry created while this setting is enabled will log the IP address of the client
    - disabling it also hides the IPs from the interface
    - added new IP field for the log search (only if enabled)

v2.3.151 (2015-11-03)
---------------------
- Merge branch 'develop' [iglocska]
- Merge branch 'hotfix-2.3.151' into develop. [iglocska]
- Removed obsolete gitignore files, fixes #704. [iglocska]
- Merge branch 'hotfix-2.3.150' into develop. [iglocska]
- Merge branch 'hotfix-2.3.149' into develop. [iglocska]
- Merge branch 'hotfix-2.3.148' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.147' into develop. [Iglocska]

v2.3.150 (2015-10-30)
---------------------
- Merge branch 'hotfix-2.3.150' [iglocska]
- Documentation changes. [iglocska]
- View all proposals via the API. [iglocska]

  - Proposals that can be accepted / discarded via the API
  - Can restrict the index to the proposals of a single event

v2.3.149 (2015-10-30)
---------------------
- Merge branch 'hotfix-2.3.149' [iglocska]
- Tagging added to the API. [iglocska]

  - Create / Edit / Remove / index / view tags via the API

v2.3.148 (2015-10-28)
---------------------
- Merge branch 'hotfix-2.3.148' [Iglocska]
- Added API for proposals. [Iglocska]

  - APIs for the following actions:
    - Add new proposed attribute to an event
    - Add proposed change to an attribute
    - View a proposal
    - Accept a proposal
    - Discard a proposal

  - new APIs described on the automation page
- Merge branch 'hotfix-2.3.147' [Iglocska]
- More details on the PGP validation tool. [Iglocska]

v2.3.147 (2015-10-27)
---------------------
- Merge branch 'hotfix-2.3.147' [Iglocska]
- Small fix to the pgp key validation tool. [Iglocska]

  - doesn't break on completely invalid keys anymore
- Merge branch 'hotfix-2.3.146' into develop. [iglocska]
- Merge branch 'hotfix-2.3.145' into develop. [iglocska]
- Merge branch 'hotfix-2.3.144' into develop. [iglocska]
- Merge branch 'hotfix-2.3.143' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.142' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.141' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.140' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.139' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.138' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.136' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.135' into develop. [Iglocska]

v2.3.146 (2015-10-27)
---------------------
- Merge branch 'hotfix-2.3.146' [iglocska]
- Version bump. [iglocska]
- Fix to a vulnerability found in attributescontroller. [iglocska]

  - vulnerability reported by Airbus Group CERT

  - Deprecated ajax attribute view had inverse access control logic
  - removed ajax path
  - added XML/JSON view

v2.3.145 (2015-10-22)
---------------------
- Merge branch 'hotfix-2.3.145' [iglocska]
- Reverted change in proposal file storage path that wasn't needed.
  [iglocska]

v2.3.144 (2015-10-21)
---------------------
- Merge branch 'hotfix-2.3.144' [iglocska]
- Version bump. [iglocska]
- Removed junk. [iglocska]
- Fixes to several issues, fixes #693. [iglocska]

  - Fixed a critical bug in the XML export
    - As of recently XML exports include relations as they were missing before
    - the sanitisation of the event info field in related attributes was incorrectly sanitized of unicode characters
    - this can lead to the XML export breaking and also for affected events to be blocked from synchronisation

  - Proposal fixes
    - fixed an invalid uuid generation that lead to an exception
    - fixed the attachments for proposals still using the old attachment system that disallows most filenames
    - added the automatic creation of hashes for attachment proposals
- Merge branch 'hotfix-2.3.143' [Iglocska]
- Removed junk. [Iglocska]
- Merge branch 'hotfix-2.3.143' [Iglocska]
- Added the attribute relations to the XML / JSON output, fixes #687.
  [Iglocska]

v2.3.143 (2015-10-15)
---------------------
- Copyright notices as a list. [Alexandre Dulaunoy]
- Update following recommendation #686. [Alexandre Dulaunoy]
- Merge branch 'master' of github.com:MISP/MISP. [Alexandre Dulaunoy]
- Merge branch 'master' of https://github.com/MISP/MISP. [Iglocska]
- Updates following recommendation #686. [Alexandre Dulaunoy]
- Merge branch 'master' of github.com:MISP/MISP. [Alexandre Dulaunoy]
- Licensed updated to AGPL 3.0 - #686. [Alexandre Dulaunoy]

v2.3.142 (2015-10-14)
---------------------
- Merge branch 'hotfix-2.3.142' [Iglocska]
- Fixed the current user check while removing dead workers, fixes #685.
  [Iglocska]

  - as pointed out by RichieB2B

v2.3.141 (2015-10-13)
---------------------
- Merge branch 'hotfix-2.3.141' [Iglocska]
- Replaced get_current_user for the process owner identification, fixes
  #685. [Iglocska]

  - As RichieB2B noted, get_current_user() gets the owner of the script in CentOS / RHEL not the user executing the script (as in Ubuntu)

  - Current solution uses posix_getpwuid and posix_geteuid if the php-posix package is installed
  - if not, it uses whoami
- Merge branch 'master' of https://github.com/MISP/MISP. [Iglocska]
- Documentation location updated (misp-book) [Alexandre Dulaunoy]

v2.3.140 (2015-10-12)
---------------------
- Merge branch 'hotfix-2.3.140' [Iglocska]
- Issue fixed with open_basedir preventing the worker diagnostics from
  working, fixes #685. [Iglocska]

  - for some users the workers appeared to be dead even though the worker processes were functional and started by the correct user
  - this was due to access to /proc being blocked by open_basedir directive settings
  - added a check and the corresponding view changes to this being the case

v2.3.139 (2015-10-09)
---------------------
- Merge branch 'hotfix-2.3.139' [Iglocska]
- Fix to a previous invalid check on the cakephp version. [Iglocska]
- Merge branch 'hotfix-2.3.138' [Iglocska]
- Fixed the worker diagnostics showing incorrect data under Red Hat /
  CentOS, fixes #685. [Iglocska]

  - Under these distros, php is blocked from seeing concurrently running php processes even under the same user
  - instead of running ps, the diagnostic now checks the existance of the pid file in /proc/

v2.3.138 (2015-10-09)
---------------------
- Merge branch 'hotfix-2.3.136' [Iglocska]
- Further fixes that caused issues with old PHP versions. [Iglocska]

v2.3.137 (2015-10-09)
---------------------
- Merge branch 'hotfix-2.3.136' [Iglocska]
- Version bump. [Iglocska]
- Fixed a possible issue with the previous commit on certain php
  versions. [Iglocska]

v2.3.136 (2015-10-09)
---------------------
- Merge branch 'hotfix-2.3.136' [Iglocska]
- Upgrade to CakePHP 2.7, fixes #684. [Iglocska]

  - cakephp submodule updated to 2.7
  - make sure that you update your instance!

  - not updating will not break compatibility
- Merge branch 'hotfix-2.3.135' [Iglocska]
- Left off view file. [Iglocska]

v2.3.135 (2015-10-08)
---------------------
- Merge branch 'hotfix-2.3.135' [Iglocska]
- Version bump. [Iglocska]
- Fix to an issue with the calendar and added view to help with gitbook
  page generation. [Iglocska]

  - datepicker seems to bug out as of recently
    - misplaced popup that overlaps with the top bar
    - fixed by updating to a newer version of datepicker

  - added a new view that generates a markdown version of the categories and types view, for easier gitbook generation
- Merge branch 'hotfix-2.3.134' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.133' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.132' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.131' into develop. [iglocska]
- Merge branch 'hotfix-2.3.130' into develop. [iglocska]
- Merge branch 'hotfix-2.3.129' into develop. [iglocska]
- Merge branch 'hotfix-2.3.128' into develop. [iglocska]
- Merge branch 'hotfix-2.3.127' into develop. [iglocska]
- Merge branch 'hotfix-2.3.126' into develop. [iglocska]
- Merge branch 'hotfix-2.3.123' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.122' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.121' into develop. [Iglocska]

v2.3.134 (2015-09-24)
---------------------
- Merge branch 'hotfix-2.3.134' [Iglocska]
- Fix to an issue that blocked event blacklist entries from being added
  manually, fixes #676. [Iglocska]
- Merge branch 'hotfix-2.3.133' [Iglocska]
- Fixed an issue where the recorrelation of all events would run into
  memory issues. [Iglocska]

  - before the recorrelation admin tool would load all attributes into memory in one go
  - now it loads them in chunks of 1k attributes at a time

v2.3.133 (2015-09-24)
---------------------
- Merge branch 'hotfix-2.3.132' [Iglocska]
- Fix to the previous commit. [Iglocska]

v2.3.132 (2015-09-23)
---------------------
- Merge branch 'hotfix-2.3.132' [Iglocska]
- Fixed an issue with old upgraded instances that didn't use the db
  session handler. [Iglocska]

  - diagnostic tool would throw exceptions because the db session tables are still missing in some older instances
  - if a different session handler is used, the test is skipped
- Changed behaviour where REST delete returns the index on success,
  fixes #673. [Iglocska]

  - REST delete of events lacked an API specific response
  - simply redirected to the index

  - it now returns eitehr "Event deleted" or "Event was not deleted" depending on the outcome
- Merge pull request #673 from Rafiot/travis. [Raphaël Vinot]

  Add some submodules to the travis run
- Update default version for cakephp, make sure PyMISP follows master.
  [Raphaël Vinot]
- Add codecov. [Raphaël Vinot]
- Add pymisp as a submodule. [Raphaël Vinot]
- Add coveralls. [Raphaël Vinot]
- Merge pull request #672 from Rafiot/travis. [Raphaël Vinot]

  Move test cases to PyMISP
- Move test cases to PyMISP. [Raphaël Vinot]

v2.3.131 (2015-09-21)
---------------------
- Merge branch 'hotfix-2.3.131' [iglocska]
- Fix to the text export ignoring the rule to exclude unpublished and
  non-IDS flagged data, fixes #646. [iglocska]
- Fixes to the user index, fixes #556. [iglocska]

  - index can now be sorted case insensitive
  - removed a notice error during sorting (sorting parameters should not be displayed as a filter)
- Started admin FAQ section, added info on resetting a password using
  the command line, fixes #624. [iglocska]
- Merge branch 'hotfix-2.3.130' [iglocska]
- Version bump. [iglocska]

v2.3.130 (2015-09-17)
---------------------
- Merge branch 'hotfix-2.3.130' [iglocska]
- Fix to an issue introduced in 2.3.128 that incorrectly causes MISP to
  not sync due to a version mismatch. [iglocska]

v2.3.129 (2015-09-16)
---------------------
- Added an API to quickly check the current MISP version, fixes #664.
  [iglocska]
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Merge pull request #663 from MISP/Rafiot-patch-1. [Andras Iklody]

  Fix #654
- Fix #654. [Raphaël Vinot]

  At least, I think so, please review :)

v2.3.128 (2015-09-16)
---------------------
- Merge branch 'hotfix-2.3.128' [iglocska]
- Added a diagnostic to check and purge overgrown session tables.
  [iglocska]

v2.3.127 (2015-09-16)
---------------------
- Merge branch 'hotfix-2.3.127' [iglocska]
- Fix to a new bug introduced with the correlation engine. [iglocska]

  - an attribute could correlate with another attribut of the same event
- Added ID in the response of the upload sample API. [iglocska]

  - it now also returns the ID of the created/updated event
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Merge pull request #658 from Rafiot/master. [Raphaël Vinot]

  Fix pull request
- Added gcc in dependencies (related to
  https://github.com/MISP/MISP/issues/302) [David André]
- Added gcc in dependencies (related to #302) [David André]

v2.3.126 (2015-09-16)
---------------------
- Merge branch 'hotfix-2.3.126' [iglocska]
- Removed redirect to the news page. [iglocska]
- Removed junk file. [iglocska]
- Collection of changes / fixes. [iglocska]

  - Event blacklist functionality extended
      - Several context fields added
      - edit existing entries to change the context fields

  - removed the deprecated news page

  - hash attribute types get validated against empty values

  - fixed an excepion on REST add of attributes when the validation stops an attribute from being entered

  - fixed the parameters in some exports being ignored after a recent patch

  - added an admin tool to prune orphaned attributes

  - cleanup and move of the database update methods - they are now accessible from any model

  - Footer now shows MISP version including sub version
- Event blacklist context completed. [iglocska]
- Further progress on several issues. [iglocska]
- Progress on several issues. [Iglocska]

  - switching workstations, this is all :construction:
- Merge pull request #653 from Rafiot/master. [Raphaël Vinot]

  [Travis] Fix DB
- [Travis] Fix DB. [Raphaël Vinot]
- Merge pull request #652 from Rafiot/travis2. [Raphaël Vinot]

  [Travis] Big update, Almost ready to run tests.
- Big update, Almost ready to run tests. [Raphaël Vinot]
- Fix to a display bug on the event index when short tags are used.
  [Iglocska]

v2.3.125 (2015-09-09)
---------------------
- Merge branch 'hotfix-2.3.125' [Iglocska]
- Left off shell script. [Iglocska]
- Initialise first user via the command line. [Iglocska]

  usage:

  /var/www/MISP/app/Console/cake userInit -q

  returns the created auth key or an error message if users already exist

  The created account is an admin user, with the login being admin@admin.test / admin
- Fixed XSS in several views. [Iglocska]

  - reported by Roberto Suggi Liverani from NCIA
- Added comment in text export paragraph that. [David André]

  non IDS flagged attributes are also exported by default.
- Fix travis message in README. [Raphaël Vinot]

v2.3.124 (2015-09-07)
---------------------
- Merge branch 'hotfix-2.3.124' [Iglocska]
- Several issues resolved. [Iglocska]

  - fixed an issue where pushing a single event would fail

  - both event and attribute edits via the API work without providing a timestamp. The current timestamp is instead attached

  - both event and attribute edits fill the required fields from the data in the database if not supplied (as long as the uuid is found)
- Typo, fixes #632. [Iglocska]
- Fix to a serious bug with adding attributes via the API and
  performance fixes. [Iglocska]

  - due to a bug, setting an attribute ID in the /attributes/add API call can lead to overwriting an existing attribute

  performance improvements:

  - massive improvements to the correlation performance
  - improvements to the attribute validation process
- Merge pull request #639 from Rafiot/travis. [Raphaël Vinot]

  Add partial travis support
- Add partial travis support. [Raphaël Vinot]

v2.3.123 (2015-09-03)
---------------------
- Merge branch 'hotfix-2.3.123' [Iglocska]
- Enhancements to the reportValidationIssuesAttributes action.
  [Iglocska]

  - now also shows issues not related to the value field
  - takes an optional parameter to validate a single event's attributes

v2.3.122 (2015-09-02)
---------------------
- Merge branch 'hotfix-2.3.122' [Iglocska]
- Version bump. [Iglocska]
- Fixed XSS in the footer. [Iglocska]

  - reported by Roberto Suggi Liverani from NCIA

v2.3.121 (2015-09-02)
---------------------
- Merge branch 'master' of https://github.com/MISP/MISP. [Iglocska]
- Merge pull request #629 from RichieB2B/ncsc-nl/stix-tags. [Alexandre
  Dulaunoy]

  Export MISP tags as STIX journal entries
- Export MISP tags as STIX journal entries. [Richard van den Berg]
- Corrected typo in word-wrapping for description in event display.
  [David André]
- Merge pull request #626 from MISP/wrap-description. [Alexandre
  Dulaunoy]

  Word-wrap for event description
- Word-wrap for event description. [David André]
- Merge branch 'hotfix-2.3.121' [Iglocska]
- Version bump. [Iglocska]
- Addition to the previous commit. [Iglocska]
- Fix to a reflected XSS in the event choice. [Iglocska]
- Merge branch 'hotfix-2.3.120' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.118' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.117' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.116' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.115' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.120' [Iglocska]
- Cleanup of some mistakes. [Iglocska]

v2.3.120 (2015-08-27)
---------------------
- Merge branch 'hotfix-2.3.118' [Iglocska]
- Add / Remove tags from events via a new API. [Iglocska]

v2.3.118 (2015-08-27)
---------------------
- Merge branch 'master' of https://github.com/MISP/MISP. [Iglocska]
- Merge pull request #618 from nullprobe/patch-1. [Alexandre Dulaunoy]

  Update MYSQL.sql
- Update MYSQL.sql. [nullprobe]

  Unnecessary comma makes the import fail.
- Merge pull request #577 from bemre/patch-1. [Raphaël Vinot]

  Update INSTALL.ubuntu1404.txt
- Update INSTALL.ubuntu1404.txt. [Bâkır Emre]

  it must be core.php instead of Core.php

v2.3.117 (2015-08-27)
---------------------
- Merge branch 'hotfix-2.3.117' [Iglocska]
- Collection of fixes. [Iglocska]

  - CSV export ignored the tag parameters
  - tagging events didn't work as expected in some cases
  - timing out and clicking on an admin action results in being redirected to a non-existing admin login page
  - distribution setting ignored when uploading attachments

v2.3.116 (2015-08-25)
---------------------
- Merge branch 'hotfix-2.3.116' [Iglocska]
- Fix to the previous hotfix. [Iglocska]

  - indexes were not created if they already existed
  - this was an issue if a non unique index was present

  - also made the process more verbose and added a generic method that deals with index removal
- Merge branch 'master' of https://github.com/MISP/MISP. [Iglocska]
- Removed git pull (x2) since we are already doing checkout. [David
  André]
- Merge branch 'hotfix-2.3.115' [Iglocska]
- Resolved an issue that can lead to duplicate events showing up in
  MISP. [Iglocska]

  - UUID uniqueness was previously not enforced
  - changed the MYSQL.sql file to reflect the changes
  - Added upgrade admin tool to remove duplicate events and make the database changes required
  - Tweaked the tool for the attribute uuid fix so that it cannot created duplicate keys

  - some minor fixes, such as automatically removing eventTag objects on event deletion
- Merge branch 'hotfix-2.3.114' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.113' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.112' into develop. [Iglocska]

v2.3.114 (2015-08-24)
---------------------
- Merge branch 'hotfix-2.3.114' [Iglocska]
- Version bump. [Iglocska]
- Fixed a bug with downloadSample that returns all accessible samples
  instead of the requested one, fixes #610. [Iglocska]

  - fixed incorrect branch order causing this issue
- Merge branch 'hotfix-2.3.113' [Iglocska]
- Various fixes to the OpenIOC import and the password reset, fixes
  #600, fixes #599, fixes #565. [Iglocska]

  - OpenIOC import now correctly sets IDS flags based on type
  - OpenIOC import specifies the source file in the comments

  - Fixed a blackhole issue with the password reset popups

v2.3.112 (2015-08-18)
---------------------
- Merge branch 'hotfix-2.3.112' [Iglocska]
- Added event ID field to restSearch APIs, to assist #456. [Iglocska]

  - eventid a new parameter for both event and attribute restsearch
  - these APIs now accept arrays in both json and xml format (you can send "eventid": ["15", "16"] instead of "eventid": "15&&16" in addition to the old functionality
- Merge branch 'hotfix-2.3.111' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.111' [Iglocska]
- Some fixes to the OpenIOC import tool. [Iglocska]

  - added support for SHA types
  - fixed an issue that caused the import to fail with duplicate attributes (the list gets pruned now)
  - fixed an issue where no supplied contextual fields would lead to empty attributes being created
  - removed the requirement for the files to have the .ioc extension
- Merge branch 'hotfix-2.3.110' into develop. [Iglocska]

v2.3.110 (2015-08-18)
---------------------
- Merge branch 'hotfix-2.3.110' [Iglocska]
- Fix to a new bug introduced with the blacklisting that can prevent new
  events from being added via the UI. [Iglocska]
- Merge branch 'hotfix-2.3.109' into develop. [Iglocska]

v2.3.109 (2015-08-18)
---------------------
- Merge branch 'hotfix-2.3.109' [Iglocska]
- Version bump. [Iglocska]
- Added event ID/UUID to the event filters and attribute search.
  [Iglocska]

  - enter a UUID in the event ID field of the attribute search to find attributes belonging to a certain event
  - use event IDs / UUIDs to filter events on the event index
- Merge branch 'hotfix-2.3.108' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.107' into develop. [iglocska]
- Merge branch 'hotfix-2.3.106' into develop. [Iglocska]

v2.3.108 (2015-08-18)
---------------------
- Merge branch 'hotfix-2.3.108' [Iglocska]
- Database update admin-actions are now logged and if they fail the
  errors are logged. [Iglocska]

v2.3.107 (2015-08-17)
---------------------
- Merge branch 'hotfix-2.3.107' [iglocska]
- Several bigger changes. [iglocska]

  - new functionality: Event blacklisting by UUID
    - site admins cna enable this feature in the server settings
    - enabling the feature will make the required db changes
    - any deleted event will automatically get blacklisted
    - this prevents deleted events from flowing back from a synced instance
    - site admins can manually add UUIDs to the list and remove entries

  - fix to UUID duplication issues for attributes
    - simply run the admin script and it will regenerate the UUID of attributes that are duplicates, if any such exist
    - timestamps/event published status will not be affected

  - config.core.php now includes a change that prevents from 404 exceptions being logged
    - the sync uses 404s to signal that an event with a given uuid does not exist when negotiating proposal synchronisation
    - this causes a dangerously high amount of noise in the logs

v2.3.106 (2015-08-07)
---------------------
- Merge branch 'hotfix-2.3.106' [Iglocska]
- Download all samples for an event ID via the API. [Iglocska]

  - as explained on the automation page
  - also, better error handling

  - all API calls that fail during authentication will now return a JSON/XML error message instead of redirecting to the login page
- Merge branch 'hotfix-2.3.105' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.104' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.103' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.102' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.101' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.100' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.99' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.98' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.97' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.96' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.95' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.94' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.93' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.92' into develop. [Iglocska]

v2.3.105 (2015-08-07)
---------------------
- Merge branch 'hotfix-2.3.105' [Iglocska]
- New functionality: API to download sample by hash. [Iglocska]

  - simply pass an MD5 hash along and receive a sample if available zipped and base64 encoded in a response object
  - pass any hash along with a flag set and receive any samples from events that have the passed hash

  - Also, fix for an issue with the freetext import not using semi-colons as separators

v2.3.104 (2015-08-04)
---------------------
- Merge branch 'hotfix-2.3.104' [Iglocska]
- Some fixes to the upload malware API. [Iglocska]

  - Threat level ID options correctly set
  - Threat level ID validation tightened to reject anything but the existing threat levels
  - The upload malware API now logs validation issues during the failed creation of attributes / events
- Merge branch 'master' of https://github.com/MISP/MISP. [Iglocska]
- Update dependencies. [Raphaël Vinot]

  * the real name of libxslt-dev is libxslt1-dev
  * curl is required later in the installation and may not be present on the system

v2.3.103 (2015-08-04)
---------------------
- Merge branch 'hotfix-2.3.103' [Iglocska]
- Additional parameters for the upload sample API. [Iglocska]
- A list of changes to the way attachments are uploaded, fixes #559,
  fixes #482. [Iglocska]

  - new API for uploading malware samples
    - allows the upload of several files
    - can be used to populate a pre-existing event, or create a new event
    - expects a JSON or an XML object with the samples base64 encoded
  - new way of storing malware samples
    - original filename not used any longer
    - samples are renamed to their md5 hashes
    - original filename preserved in a secondary txt file
  - removed filename validation as it is no longer used for the command line execution
    - this allows unicode name files to be uploaded!
    - changed the UI attachment upload to reflect these changes
    - code more centralised and extendible

v2.3.102 (2015-07-27)
---------------------
- Merge branch 'hotfix-2.3.102' [Iglocska]
- Added the same functionality to the regex edit. [Iglocska]
- Added error message if regex is added without choosing a type, fixes
  #575. [Iglocska]

  - user will be taken back to the form if no type selected
- Merge branch 'hotfix-2.3.101' [Iglocska]
- Mass IDS toggle for freetext import, fixes #576. [Iglocska]

  - added a toggle for the IDS fields in the freetext import to quickly set all found attributes to being IDS worthy

v2.3.100 (2015-07-22)
---------------------
- Merge branch 'hotfix-2.3.100' [Iglocska]
- Fixed an issue with the NIDS export not correctly working for single
  events. [Iglocska]
- Merge branch 'hotfix-2.3.99' [Iglocska]
- Incremental export generation for HIDS and NIDS exports. [Iglocska]

  - Instead of fetching all events at once for the export, events are fetched one by one
  - Greatly reduces memory footprint (It mostly depends on the event with the most eligible attributes now, instead of the combined list of all events)
  - Because of the lower memory usage, the time taken for the export is also slashed to a fragment of what it was before

v2.3.99 (2015-07-20)
--------------------
- Merge branch 'hotfix-2.3.98' [Iglocska]

v2.3.98 (2015-07-17)
--------------------
- Merge branch '570' into hotfix-2.3.98. [Iglocska]
- Convert tab to spaces. [Richard van den Berg]
- Remove unused relatedTTP. [Richard van den Berg]
- Add timezone +00:00 to timestamp. [Richard van den Berg]
- Change incident description to title. [Richard van den Berg]
- Add Indicated_TTP. [Richard van den Berg]
- Add Valid_Time_Position. [Richard van den Berg]
- Add indicator types. [Richard van den Berg]
- Add condition attributes. [Richard van den Berg]
- Some changes to the workers. [Iglocska]

  - some fixes with the previous iteration of the background workers
  - PID now checked using ps -p instead of looking for it in /proc
- Changes to the hids exports. [Iglocska]

  - fixed some issues with unset variables (from, to, last) when triggered by the background workers
  - reduced memory usage of the hids exports (removed storing the hashes twice in memory, drastically removed the data retrieved from the db when preparing the export)

v2.3.97 (2015-07-13)
--------------------
- Merge branch 'hotfix-2.3.97' [Iglocska]
- Version bump. [Iglocska]
- Merge branch 'pr567' into hotfix-2.3.97. [Iglocska]
- Use setupHttpSocket for fetchPGPKey. [Richard van den Berg]
- Merge branch 'pr564' into hotfix-2.3.97. [Iglocska]
- Edited comment for RPZ_Policy. [David André]

  Removed copy/pasta and added a correct comment for RPZ_Policy
- Merge pull request #1 from MISP/master. [David André]

  Update to latest MISP master
- Merge branch 'pr546' into hotfix-2.3.97. [Iglocska]
- Use innodb engine for cake sessions table. [David André]

v2.3.96 (2015-07-12)
--------------------
- Merge branch 'hotfix-2.3.96' [Iglocska]
- Rework of the diagnostics for background workers. [Iglocska]

  - shows dead background workers
  - allows site admins to add workers to any queue on the fly
  - allows site admins to kill workers on the fly

v2.3.95 (2015-07-09)
--------------------
- Merge branch 'hotfix-2.3.95' [Iglocska]
- Some tuning to the hostname / url type recognition in the freetext
  import tool, fixes #562. [Iglocska]

v2.3.94 (2015-07-08)
--------------------
- Merge branch 'hotfix-2.3.94' [Iglocska]
- Fix to an error with very large strings in an array causing a failure
  in the XML conversion of simpleXML, fixes #500. [Iglocska]

  Moved the XML conversion in restfullEventToServer() to MISP's own xml conversion tool

v2.3.93 (2015-07-07)
--------------------
- Merge branch 'hotfix-2.3.93' [Iglocska]
- Fixes to the RPZ export based on the testing of elhoim. [Iglocska]

  - some errors in the format (wrong comment character used, rpz-ip not appended to IP addresses, missing semi-colon)
  - removed hostnames that are on domains blocked by the rules based on domain attributes

v2.3.92 (2015-07-01)
--------------------
- Merge branch 'hotfix-2.3.92' [Iglocska]
- Fix to an incorrect validation of temporary filenames. [Iglocska]
- Merge branch 'hotfix-2.3.91' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.90' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.89' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.91' [Iglocska]
- File management fixed in server settings. [Iglocska]

  - a previous patch removed the contents of the page

v2.3.91 (2015-07-01)
--------------------
- Merge branch 'hotfix-2.3.90' [Iglocska]
- GnuPG.binary demoted to optional setting as it should be. [Iglocska]

v2.3.90 (2015-07-01)
--------------------
- Merge branch 'hotfix-2.3.90' [Iglocska]
- Version bump. [Iglocska]
- Fix to XSS in the template creation process. [Iglocska]
- Security fix: Fix to a possible PHP Object injection. [Iglocska]

  - unserialized user input replaced with json_decode
- Merge branch 'hotfix-2.3.89' [Iglocska]
- Version bump and debug code removed. [Iglocska]
- Fix for disabled fields causing issues with the security component
  fixes #555. [Iglocska]

  - the disabled fields are no longer created via the form helper
- Merge branch 'hotfix-2.3.88' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.87' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.86' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.84' into develop. [iglocska]

v2.3.88 (2015-06-29)
--------------------
- Merge branch 'hotfix-2.3.88' [Iglocska]
- Complete rework of the ZeroMQ implementation. [Iglocska]

  - python server running in the background doing the publishing
  - MISP -> python script communication via redis
  - configurable / controllable via the admin UI
- Merge branch 'hotfix-2.3.87' [Iglocska]
- Removed debug code. [Iglocska]
- Merge branch 'hotfix-2.3.87' [Iglocska]
- Version bump. [Iglocska]
- Several fixes. [Iglocska]

  - added multi edit to freetext import comments
  - added a missing file from hotfix-2.3.87 (pgp key import view)
  - updated gitignore to ignore some items that are outside of the scope of the git package
- Proposal mass accept/discard, fixes #466. [Iglocska]

v2.3.87 (2015-06-25)
--------------------
- Merge branch 'hotfix-2.3.86' [Iglocska]
- Merge branch 'fix-stix-date-ranges' into hotfix-2.3.86. [Iglocska]

  Conflicts:
  	app/View/Events/automation.ctp
- Move example to bottom of h3. [Richard van den Berg]
- Fix bold and spacing. [Richard van den Berg]
- Add/move missing tags examples. [Richard van den Berg]
- Clarify the use of empty parameters in URL. [Richard van den Berg]
- Clarify more date formats. [Richard van den Berg]
- Clarify date format. [Richard van den Berg]
- Add $from and $to to Event->stix() [Richard van den Berg]
- DateFieldCheck actually expects YYYY-MM-DD. [Richard van den Berg]
- Added pub/sub feature using ZeroMQ, fixes #540 and fixes #526.
  [Iglocska]

  - by installing the requirements described in the update and the install instructions (ubuntu only for now, centos/red-hat versions to be tested and described), administrators can enable the pub/sub feature
  - assign a port to the service via the interface
  - each time an event is published, MISP will use ZMQ's PUB feature to push out a MISP JSON package using the "misp_json" prefix
- Some merge issues resolved. [Iglocska]
- Merge branch 'feature/rpz' into hotfix-2.3.86. [Iglocska]

  Conflicts:
  	app/Console/Command/EventShell.php
  	app/Model/Server.php
- Opened up the rpz API for automation. [iglocska]
- Merge branch 'master' into feature/rpz. [iglocska]
- Small fixes. [iglocska]

  - filename fix
  - per event download fixed
- Added the missing ways to exploit the rpz functionality. [iglocska]

  - rpz added to exports, both old-style and with background workers
  - per event rpz functionality added
- First revision of the RPZ export complete. [iglocska]

  - documented in automation view
  - right now it follows the simple rule of user > admin settings > default values when generating the export
  - Parameters can be passed via url / JSON object / XML object
  - filters include filter on event ID, date range, tags

  TODO:
  - buttons for a per event download via the UI
  - introduce new export option for normal users (via background workers and the old style export)
- Further progress, still rough around the edges. [iglocska]

  - server settings and validation work
  - configurable template via settings
  - configurable via API as well

  - Also trying to define the structure for future Plugin settings
  - The idea is to have them in a separate tab all prepended with the plugin name
  - since this is not yet part of the future flexible plugin system, it is still kept in the main codebase, but the idea is to get the naming conventions ready for the future version
- First version of the RPZ export. [iglocska]

  - still undocumented
  - very naive policy settings
  - limit per event / tags / date range
- Removed some junk. [Iglocska]
- PGP key selection on fetch, fixes #554. [Iglocska]

  - MISP will now fetch a list of all keys matching the e-mail address from the MIT server from the user edit view
  - A popup will present all the matching keys (with the creation date, key ID, email addresses associated - and the fingerprint when hovering over them)
  - Once the admin clicks on one, it will fetch the desired key

  - future enhancement possibility: move the second stage (the actual key fetch) to the server side instead of a direct ajax query from the user's browser

v2.3.85 (2015-06-22)
--------------------
- Merge branch 'hotfix-2.3.85' [Iglocska]
- Tuning of the complex type tool. [Iglocska]

v2.3.84 (2015-06-18)
--------------------
- Merge branch 'hotfix-2.3.84' [iglocska]
- Various changes and bug fixes. [iglocska]

  - contact reporter first tries to contact orgc users on the instance, if they don't exist, it will contact the owner (instead of going straight to the owner)
  - hostname / domain name validation change broke validation of hostnames/domain names / email addresses with a "-"
  - Some documentation changes for the REST API (more coming)
  - some tuning of the freetext import
- Merge branch 'hotfix-2.3.83' into develop. [iglocska]
- Merge branch 'hotfix-2.3.82' into develop. [iglocska]
- Merge branch 'hotfix-2.3.81' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.80' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.79' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.78' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.77' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.76' into develop. [Iglocska]
- Install instruction change under ubuntu: No more reference to removed
  INSTALL.SH file, fixes #520. Also, removed BUGS.txt, fixes #519.
  [Iglocska]
- Merge branch 'hotfix-2.3.75' into develop. [Iglocska]

v2.3.83 (2015-06-17)
--------------------
- Merge branch 'hotfix-2.3.83' [iglocska]
- Small tweak to the email/domain/hostname validation, affects #551.
  [iglocska]

v2.3.82 (2015-06-16)
--------------------
- Merge branch 'hotfix-2.3.82' [iglocska]
- Relaxed validation of tlds in domain/hostname/email-src/email-dst
  attributes to allow for longer custom tlds. [iglocska]
- Merge branch 'hotfix-2.3.81' [Iglocska]
- Removed some junk. [Iglocska]

v2.3.81 (2015-06-10)
--------------------
- Merge branch 'hotfix-2.3.81' [Iglocska]
- Version bump. [Iglocska]
- Some further cleanup / refactoring. [Iglocska]
- Updated the documentation to reflect the correct STIX / CyBox versions
  required. [Iglocska]

  - Updated the admin tool to check the STIX / Cybox versions
- Fixes to the e-mailer and the HIDS export. [Iglocska]

  - HIDS exports did not include filename|hash types
  - Sending a password reset / welcome message picked the opposite subject line
  - line breaks were sent as literals.

v2.3.80 (2015-06-09)
--------------------
- Merge branch 'hotfix-2.3.80' [Iglocska]
- Version bump. [Iglocska]
- Added the option to use an alternat executable for gpg, fixes #498.
  [Iglocska]

  - users can specify an alternate gnupg executable
  - Since GnuPG2 is not compatible with the last stable CryptGPG version, there are 3 options for CentOS / Red Hat users:
    1. Don't use a passphrase for the server's PGP key
    2. Install the beta version of CryptGPG (1.4.0b4)
    3. Install GnuPG classic and point MISP to the executable

  - This patch enables option 3, administrators can point MISP to the alternate executable in the server settings
- Server setting changes logged, fixes #531. [Iglocska]

v2.3.79 (2015-06-06)
--------------------
- Merge branch 'hotfix-2.3.79' [Iglocska]
- Added documentation changes to avoid a non-compatible cybox
  installation, fixes #529. [Iglocska]

  - STIX exports were failing when using the master branch of the Cybox Python libraries
  - installation guide now forces users to use the last compatible release
- Documentation for the new export option added. [Iglocska]
- Added a new API parameter that allows to restrict events to the most
  recently published ones, #527. [Iglocska]

  - added the new flag "last" to the list of parameters
  - exports affected: XML, CSV, NIDS, HIDS, STIX, Text, RestSearch
  - Valid values: number + format where format can be d, m, h for day, minute, hour (examples: 5d or 12h or 30m)
- Merge branch 'hotfix-2.3.78' [Iglocska]
- Version bump, also, hotfix fixes #521. [Iglocska]
- Tags sorted by name not ID, fixes #522. [Iglocska]

  - Affected views: Tag index, event view tag attach dropdown
- Fixed an issue with log entries being truncated (Requires
  administrator action!) [Iglocska]

  - added a new entry to the admin tools (Administartion -> Administrative tools)
  - converts title and change columns in the logs table to text from varchar(255)

v2.3.77 (2015-06-05)
--------------------
- Merge branch 'hotfix-2.3.77' [Iglocska]
- Fix to non publish users being able to get around the restriction.
  [Iglocska]

  - fixed an incorrect privilege check on the publish pop-up

v2.3.76 (2015-06-04)
--------------------
- Merge branch 'hotfix-2.3.76' [Iglocska]
- Auth users should only be able to create events for their org.
  [Iglocska]

  - Sync users should be able to create an event for another orgc, but auth users should not
  - Fixed
- Install instruction change under ubuntu: No more reference to removed
  INSTALL.SH file, fixes #520. Also, removed BUGS.txt, fixes #519.
  [Iglocska]
- Merge branch 'hotfix-2.3.75' [Iglocska]
- Freetext import tool now prunes duplicate values, fixes #517.
  [Iglocska]
- Oversanitisation breaks links in attribute values, fixes #371.
  [Iglocska]
- Merge branch 'mbstring' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.74' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.73' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.72' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.71' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.70' into develop. [iglocska]
- Merge branch 'mbstring' [Iglocska]
- CakePHP 2.6.7 requires the php mbstring extension. [Richard van den
  Berg]

  - on CentOS this is a separate package php-mbstring
  - on Ubuntu this is part of libapache2-mod-php5

v2.3.74 (2015-06-03)
--------------------
- Merge branch 'hotfix-2.3.74' [Iglocska]
- Timing for rescheduling of tasks changed slightly. [Iglocska]

  - The rescheduling now happens before the task is executed - this way a failed job will not prevent the rescheduling of the next execution time

v2.3.73 (2015-06-03)
--------------------
- Merge branch 'hotfix-2.3.73' [Iglocska]
- AJAX attribute creation would block a follow-up publish request, fixes
  #514. [Iglocska]

  - Popover_form purged after the form has been submitted
  - a duplicate hidden div was created for confirmation popups within the attribute creation popup and clicking publish populated the wrong div
- Fixes issue with firefox not pasting the fetched PGP key, fixes #514.
  [Iglocska]
- Merge branch 'hotfix-2.3.72' [Iglocska]
- Some fixes to the documentation. [Iglocska]

  - workers potentially started as root in the documentation, fixed
- Fixed the max width of the attribute value field, fixes #512.
  [Iglocska]
- Updated bootstrap datepicker, fixes #507. [Iglocska]
- NIDS filename changes, fixes #509. [Iglocska]

  - instead of misp.rules the filename becomes misp.format.eventid.rules where eventid is only set if a single event is exported
- Disablerestalert setting clarified and default set to true, fixes 511.
  [Iglocska]
- Free text import tool tuning, fixes #510. [Iglocska]

  - comma separated values now correctly parsed
  - Ports in IP/url/link/domain/hostname now added as a comment
  - virustotal now automatically recognised as external analysis / link

v2.3.71 (2015-06-01)
--------------------
- Merge branch 'hotfix-2.3.71' [Iglocska]
- Events without attributes are now blocked from pull/push, fixes #476.
  [Iglocska]

  - Events published / pushed will now refuse to sync if the situation arises where no attributes would be eligible to be synced
  - Events pulled that contain no attributes will be thrown away
- Merge branch 'hotfix-2.3.70' [iglocska]
- Version bump. [iglocska]
- Merge branch 'certat' into hotfix-2.3.70. [iglocska]
- Merge branch 'master' of https://github.com/MISP/MISP. [Aaron Kaplan]
- Update INSTALL.ubuntu1404.txt. [AaronK]

  Add a note on Debian Wheezy installation instructions
- Merge branch 'master' of https://github.com/MISP/MISP. [Aaron Kaplan]
- Merge branch 'master' of https://github.com/aaronkaplan/MISP. [Aaron
  Kaplan]
- Merge branch 'master' of https://github.com/MISP/MISP. [Aaron Kaplan]
- Should read if (defined(...)) [Aaron Kaplan]
- Merge branch 'master' of https://github.com/aaronkaplan/MISP. [Aaron
  Kaplan]
- Merge https://github.com/MISP/MISP. [Aaron Kaplan]
- Move CERT.at logo file. [L. Aaron Kaplan]
- Merge https://github.com/MISP/MISP. [Aaron Kaplan]
- Added CERT.at org file Also testing pull requests upstream. [Aaron
  Kaplan]
- Merge branch 'hotfix-2.3.69' into develop. [iglocska]

v2.3.69 (2015-05-27)
--------------------
- Merge branch 'hotfix-2.3.69' [iglocska]
- Left of tuning of complex type tool in previous commit. [iglocska]

  - also, appcontroller now loads the security component, so that the blackhole override doesn't produce errors
- Finished the e-mailing rework branch, fixes #505, fixes #504, fixes
  #502, fixes #499. [iglocska]

  - this commit is mostly here to capture what was changed in hotfix 2.3.69

  - e-mailing completely reworked, all e-mails now flow through the same method
  - that method will handle all encryption and the decisions whether to send e-mails unencrypted to users without an encryption key, whether to keep the body of the e-mail untruncated, etc
  - all e-mails are now also logged here (including the reason of a potential failure)

  - new server settings for default template messages for password resets / new user welcome messages

  - admin e-mail interface reworked and org admins now also have access to the features

  - password resets / new user for site and org admins (where applicable) - quickly reset the password of a user and alert them using the pre-defined reset template

  =====

  - Tuned the freetext import to really accept free-text. Let me know if you have any tips for tuning the detection further!

  - it now breaks the passed string on whitespace and line-break and tries to resolve the rest. Filename resolution tightened to exclude anthing that starts or ends with a .
- Blackhole message due to csrf replaced with something more obvious,
  fixes #504. [iglocska]

  - user will get an explanation of the csrf error and that going back and refreshing the form will fix it
  - also, there is a link that will take the user to the baseurl (which will redirect to the login page if the csrf issue occured on the login page)
- New emailer finished. [iglocska]
- Further progress. [iglocska]
- Rework of the e-mailing, part 1. [iglocska]

  - Reworking the way e-mails are sent - all of it goes through a centralised e-mail method
  - just pass the recipient, recipient encryption key collection, body, alternate body if the message cannot be encrypted, subject, reply to address and pgp key for reply to along and the method will do the rest

  - encrypt if possible, check if sending without encryption is allowed, signing, adding attachment for reply to encryption key, using alternate sanitised body if it is enforced for accounts that cannot use encryption is all done in one place

  - easy to maintain and expand with future changes (such as the S/MIME pull request on github)
- Merge branch 'unencrypted' into hotfix-2.3.69. [iglocska]
- Removed extraneous dash. [Richard van den Berg]
- Fixed typo. [Richard van den Berg]
- Also respect GnuPG.bodyonlyencrypted for posts alerts. [Richard van
  den Berg]
- Merge branch 'ncsc-nl/posts-alerts' into ncsc-
  nl/email_body_only_encrypted. [Richard van den Berg]
- Do not send details of events unencrypted. [Richard van den Berg]
- Merge branch 'email-notifications' into hotfix-2.3.69. [iglocska]
- Use correct CakeResque queue. [Richard van den Berg]
- Fix whitespaces. [Richard van den Berg]
- Fix posts alerts. [Richard van den Berg]
- Send E-mail notifications for new posts in discussion and event
  threads. [Richard van den Berg]
- Freetext import tool now splits the input by line break and
  whitespace, fixes #502. [iglocska]
- Merge branch 'hotfix-2.3.68' into develop. [iglocska]
- Merge branch 'hotfix-2.3.67' into develop. [iglocska]
- Merge branch 'hotfix-2.3.66' into develop. [iglocska]
- Merge branch 'hotfix-2.3.65' into develop. [iglocska]

v2.3.68 (2015-05-21)
--------------------
- Merge branch 'hotfix-2.3.68' [iglocska]
- Date set to today's date by default, fixes #495. [iglocska]

v2.3.67 (2015-05-20)
--------------------
- Merge branch 'hotfix-2.3.67' [iglocska]
- Ignoring non MISP AUTHORIZATION headers, fixes #478. [iglocska]

  - Users being logged on would not be able to use the actions that are also used for automation
  - Those actions trigger a check of the authorization header, which in certain use cases can be set with values that is outside of the scope of MISP

  - MISP will now try to only detect MISP auth keys in the headers and if it detects something else it ignores it

v2.3.66 (2015-05-15)
--------------------
- Merge branch 'hotfix-2.3.66' [iglocska]
- Fix to copy pasta issue breaking from/to filters in exports, fixes
  #494. [iglocska]

v2.3.65 (2015-05-15)
--------------------
- Merge branch 'hotfix-2.3.65' [iglocska]
- Fixed issue with proxy settings attempted to be added in synctool,
  even if not set. [iglocska]
- Merge branch 'hotfix-2.3.64' into develop. [iglocska]
- Merge branch 'password_script' into develop. [iglocska]
- Merge branch 'hotfix-2.3.63' into develop. [iglocska]
- Corrected typo. [Christophe Vandeplas]
- Links to website. [Christophe Vandeplas]
- MISP diagrams in SVG licensed under CC-BY-SA added. [Alexandre
  Dulaunoy]
- Merge branch 'hotfix-2.3.62' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.61' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.60' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.59' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.58' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.57' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.64' [iglocska]
- Merge branch 'certauth' into hotfix-2.3.64. [iglocska]
- Minor typo in the unset -- should be ['User']['gpgkey'] [Guilherme
  Capilé]
- Removed session handling from plugin and moved to AppController.
  [Guilherme Capilé]
- Merge remote-tracking branch 'upstream/master' [Guilherme Capilé]
- Merge branch 'master' of github.com:FIRSTdotorg/MISP. [Guilherme
  Capilé]
- Added user defaults to plugin. [Guilherme Capilé]
- Added client SSL certificate authentication as a CakePHP plugin.
  [Guilherme Capilé]
- Added client SSL certificate authentication as a CakePHP plugin.
  [Guilherme Capilé]
- Added user defaults to plugin. [Guilherme Capilé]
- Added client SSL certificate authentication as a CakePHP plugin.
  [Guilherme Capilé]
- Added client SSL certificate authentication as a CakePHP plugin.
  [Guilherme Capilé]
- Merge branch 'cakephppath' into hotfix-2.3.64. [iglocska]
- Update UPDATE.txt. [remg427]

  app missing in path for cakephp
- Merge branch 'saltlength' into hotfix-2.3.64. [iglocska]
- Calrify salt length in INSTALL.md. [Gábor Molnár]
- Note salt key length requirement to INSTALL.md. [Gábor Molnár]
- Merge branch 'rsakey' into hotfix-2.3.64. [iglocska]
- Removed the RSA key recommendation from INSTALL.ubuntu1404.txt. [David
  André]
- Removed the RSA key recommendation from INSTALL.centos7.txt. [David
  André]
- Removed the RSA key recommendation from INSTALL.centos6.txt. [David
  André]
- Left off a file. [iglocska]
- PGP key lookup for lazy MISP instance admins, fixes #492. [iglocska]

  - Added a button for the add user / edit user views that fetches the entered e-mail addresses pgp key from pgp.mit.edu
- Implemented correct from / to api parameter checks. [iglocska]

  - based on stevengoossensB's pull request

v2.3.64 (2015-05-13)
--------------------
- Merge branch 'password_script' [iglocska]
- Password reset fix. [iglocska]
- Added link to GNU AGLP License v3 text. [David André]

v2.3.63 (2015-05-04)
--------------------
- Merge branch 'hotfix-2.3.63' [iglocska]
- Removed debug. [iglocska]
- Parse authorization headers for a valid MISP auth key, fixes #478.
  [iglocska]

  - Keeps parsing until a valid auth key is found
- Merge branch 'master' into hotfix-2.3.63. [iglocska]
- Corrected typo. [Christophe Vandeplas]
- Links to website. [Christophe Vandeplas]
- MISP diagrams in SVG licensed under CC-BY-SA added. [Alexandre
  Dulaunoy]
- Merge pull request #468 from elhoim/patch-6. [Andras Iklody]

  Fix for #467
- Fix for #467. [David André]

  Fix for issue #467
  Changed the label of IDS checkbox for proposals

v2.3.62 (2015-04-16)
--------------------
- Merge branch 'hotfix-2.3.62' [Iglocska]
- Small fix to editing an event via the api. [Iglocska]

  - adding attributes without a uuid will cause the edit to fail
  - attributes without a uuid will now be added as a new attribute
- Merge branch 'hotfix-2.3.61' [Iglocska]
- Fixed various issues with the attribute REST api. [Iglocska]

  - also updated the sample curl scripts

v2.3.60 (2015-04-13)
--------------------
- Merge branch 'hotfix-2.3.60' [Iglocska]
- Background job for pull incorrectly checks the push flag on the
  server, fixes #457. [Iglocska]

  - Issue fixed: When background jobs are enabled the wrong flag is checked when attemptying to enqueue a pull

v2.3.59 (2015-04-08)
--------------------
- Merge branch 'hotfix-2.3.59' [Iglocska]
- Fix to an issue with the caching. [Iglocska]

  - CSV caching was saving to file on each attribute, creating extremely high amounts of I/O
  - reduced it to saving to file / event

  - fixed incorrect pathing
- Merge branch 'triple-dots' into hotfix-2.3.59. [Iglocska]
- Only truncate string if adding ... will make it shorter. [Richard van
  den Berg]
- Merge branch 'cakeresque-update' into hotfix-2.3.59. [Iglocska]
- Include composer.phar self-update. [Richard van den Berg]
- Use cake-resque:4.1.2. [Richard van den Berg]

  - Remove --no-update for cake-resque
   - Added UPDATE.txt for keeping up2date between major releases
- Merge branch 'cakephp-update' into hotfix-2.3.59. [Iglocska]
- Remove gitlink for app/Plugin/CakeResque. [Richard van den Berg]

  CakeResque is installed with composer.phar

  Removing the gitlink gets rid of this annoying error message:
  No submodule mapping found in .gitmodules for path 'app/Plugin/CakeResque'
- Update cakephp to latest 2.6 branch. [Richard van den Berg]
- Merge branch 'cakeresque-queues' into hotfix-2.3.59. [Iglocska]
- Use correct CakeResque queues. [Richard van den Berg]
- Merge branch 'proxy' into hotfix-2.3.59. [Iglocska]
- Use isOK() for version check. [Richard van den Berg]
- Catch HTTP error codes. [Richard van den Berg]
- Catch invalid proxy configuration. [Richard van den Berg]
- Allow SyncTool with empty $server. [Richard van den Berg]
- Allow SyncTool to be used for generic HTTP(S) connections. [Richard
  van den Berg]
- Use SyncTool for diagnostics. [Richard van den Berg]
- Fix typo. [Richard van den Berg]
- Add proxy section to server diagnostics. [Richard van den Berg]
- ConfigProxy() checks for empty arguments, no need to do it twice.
  [Richard van den Berg]
- Add proxy support to SyncTool. [Richard van den Berg]
- Merge branch 'ids_example' into hotfix-2.3.59. [Iglocska]
- Removed .swp file ; updated .gitignore. [Koen Van Impe]
- Example file on how to get the exported IDS data from MISP. [Koen Van
  Impe]
- Merge pull request #1 from MISP/master. [Koen Van Impe]

  Update from original
- Merge branch 'password' into hotfix-2.3.59. [Iglocska]
- Update to install howto. [Alexander J]

  remove of -p password in order to avoid having the password in your bash history and the install command for postfix
- Merge branch 'gitignore' into hotfix-2.3.59. [Iglocska]
- Fix cakephp path in .gitignore. [Richard van den Berg]
- Merge branch 'stix_no_random_ids' into hotfix-2.3.59. [Iglocska]
- Consistent timestamps for STIX objects. [Richard van den Berg]
- Consistent id's for malware-sample artifacts. [Richard van den Berg]
- Consistent id's for observable compositions. [Richard van den Berg]
- Use property class name in object ID. [Richard van den Berg]
- Use attribute uuid for cybox id's. [Richard van den Berg]
- Merge branch 'stix-info' into hotfix-2.3.59. [Iglocska]
- Use org name and baseurl in XML namespace for STIX. [Richard van den
  Berg]
- More informative CIQ titles. [Richard van den Berg]
- More informative STIX titles. [Richard van den Berg]
- Merge branch 'install-centos' into hotfix-2.3.59. [Iglocska]
- Fix line breaks. [Richard van den Berg]
- Php-xml is needed for DOMDocument class. [Richard van den Berg]
- Merge branch 'master' of github.com:MISP/MISP into ncsc-nl/install-
  centos. [Richard van den Berg]
- Documentation changes. [Richard van den Berg]

  - Added changes from 9378837f39a52e246fb1c11aac18343c8c8992a0 for CentOS
  - Fixed some typos
- Merge branch 'disallow_unpublished_events' into hotfix-2.3.59.
  [Iglocska]
- Fixed missing parentheses‎ [Richard van den Berg]
- Make unpublished events private if MISP.unpublishedprivate == true.
  [Richard van den Berg]
- Merge remote-tracking branch 'upstream/master' [Richard van den Berg]
- Disallow unpublished events. [Richard van den Berg]

v2.3.58 (2015-04-01)
--------------------
- Merge branch 'hotfix-2.3.58' [Iglocska]
- Sync update issue fixed. [Iglocska]

  - attributes were not correctly updated during a manual push due to an incorrect conditional
  - re-publishing was unaffected

v2.3.57 (2015-03-16)
--------------------
- Merge branch 'hotfix-2.3.57' [Iglocska]
- Organization field in Servers too short to fit valid organisation
  identifiers, fixes #436. [Iglocska]

  - updated the MYSQL.sql file for future MISP installations
  - added admin script to do the update from the web interface
- Merge branch 'hotfix-2.3.56' into develop. [Iglocska]
- Merge branch 'hotfix-2.3.55' into develop. [iglocska]
- Merge branch 'hotfix-2.3.53' into develop. [iglocska]
- Merge branch 'hotfix-2.3.52' into develop. [iglocska]
- Merge branch 'hotfix-2.3.51' into develop. [iglocska]
- Merge branch 'hotfix-2.3.50' into develop. [iglocska]
- Merge branch 'hotfix-2.3.49' into develop. [iglocska]
- Merge branch 'hotfix-2.3.48' into develop. [iglocska]
- Merge branch 'hotfix-2.3.47' into develop. [iglocska]
- Merge branch 'hotfix-2.3.46' into develop. [iglocska]
- Merge branch 'hotfix-2.3.45' into develop. [iglocska]
- Merge branch 'hotfix-2.3.44' into develop. [iglocska]
- Merge branch 'hotfix-2.3.43' into develop. [iglocska]
- Merge branch 'hotfix-2.3.42' into develop. [iglocska]
- Merge branch 'hotfix-2.3.41' into develop. [iglocska]

v2.3.56 (2015-03-14)
--------------------
- Merge branch 'hotfix-2.3.56' [Iglocska]
- Site admins can now create proposals, fixes #417. [Iglocska]

  - site admins can now create proposals to an event / attribute as long as the event does not belong to their organisation
  - new icon for proposals to differentiate them from edits
- Version bump. [Iglocska]
- Sync users should default to termsaccepted and no password change
  required, fixes #432. [Iglocska]
- Search in logs fixed, fixes #434. [Iglocska]

  - The log search incorrectly set the search terms for empty fields, meaning that any log entries that had unfilled columns, such as it is the case with admin_email would never return results

v2.3.55 (2015-03-10)
--------------------
- Merge branch 'hotfix-2.3.55' [iglocska]
- Security fix. [iglocska]

  - filenames are now enclosed by quotes instead of double quotes while executing the zip command via exec

v2.3.54 (2015-02-24)
--------------------
- Merge branch 'hotfix-2.3.54' [iglocska]
- Version bump. [iglocska]
- Json view fixed, fixes #411. [iglocska]

v2.3.53 (2015-02-23)
--------------------
- Merge branch 'hotfix-2.3.53' [iglocska]
- Version bump. [iglocska]
- Disabled the animation in the MISP logo. [iglocska]

  - it was quite heavy on CPU usage and it was too subtle to notice anyway
- Org admins editing privileged users demotes the privileged user to a
  lower permission level, fixes #408. [iglocska]

  - an org admin now correctly can select the previously assigned privileged role for a user that he/she is editing
- Merge branch 'hotfix-2.3.52' [iglocska]
- Version bump. [iglocska]
- API search incorrectly generating JSON with several events, fixes
  #407. [iglocska]

  - also fixed the edit button on the index

v2.3.52 (2015-02-18)
--------------------
- Merge branch 'hotfix-2.3.51' [iglocska]
- Version bump. [iglocska]
- Further work on the exports. [iglocska]

  - Performance improvements for the event search exports
  - JSON view code moved to Lib
  - Fixed an issue that didn't restrict the dates correctly with the from / to parameters

v2.3.51 (2015-02-16)
--------------------
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Fix pull #400. [Alexandre Dulaunoy]
- MISP logo added. [Alexandre Dulaunoy]
- MISP logos added (SVG, PDF and PNG) [Alexandre Dulaunoy]

v2.3.50 (2015-02-16)
--------------------
- Merge branch 'hotfix-2.3.50' [iglocska]
- Added more contextual info for the CSV exports, fixes #391. [iglocska]
- Correlation disabled for http-method, fixes #406. [iglocska]
- Missing json view file added. [iglocska]

  - return attributes fails when requesting the results in JSON
  - added missing view file

v2.3.49 (2015-02-16)
--------------------
- Merge branch 'hotfix-2.3.49' [iglocska]
- Relaxed the auth key requirement for nids exports. [iglocska]

  - incorrect check on the nids exports blocked logged in users from downloading the snort/suricata rules of an event
  - check removed

v2.3.48 (2015-02-10)
--------------------
- Merge branch 'hotfix-2.3.48' [iglocska]
- Version bump. [iglocska]
- Fixed an issue with the free-text import failing on more than ~100
  parsed values, fixes #389. [iglocska]

  - Caused by a 1k variable / form limit imposed by php since 5.3.9
  - Form data now collected by JS and passed as a single JSON in the POST request
  - Allows massive IOC lists to be imported
  - improved performance

v2.3.47 (2015-02-09)
--------------------
- Merge branch 'hotfix-2.3.47' [iglocska]
- Documentation changes. [iglocska]
- Merge branch 'hotfix-2.3.46' [iglocska]
- Patch fixing json download, fixes #387. [iglocska]

  - World's smallest patch

v2.3.46 (2015-02-05)
--------------------
- Merge branch 'hotfix-2.3.45' [iglocska]
- New documentation left off. [iglocska]

v2.3.45 (2015-02-05)
--------------------
- Merge branch 'hotfix-2.3.45' [iglocska]
- Version incremented. [iglocska]
- Removed the old documentation, fixes #378  and some small fixes.
  [iglocska]

  - resolved an issue of warnings being generated when an event without attributes / relations gets XML exported.
  - added new dump of the documentation

v2.3.44 (2015-02-04)
--------------------
- Merge branch 'hotfix-2.3.44' [iglocska]
- Version incremented. [iglocska]
- Left off file in previous hotfix added. [iglocska]

  - added a file that was not pushed during the last hotfix
  - some improvements to the XML export to lower memory usage

v2.3.43 (2015-02-03)
--------------------
- Merge branch 'hotfix-2.3.43' [iglocska]
- Documentation fail fixes #384. [iglocska]

v2.3.42 (2015-02-03)
--------------------
- Merge branch 'hotfix-2.3.42' [iglocska]
- Small change to the XML export. [iglocska]

  - won't write to file after all, simply keeps adding to a string in memory. Should still resolve the XML conversion taking up high amounts of memory issue.
- Various improvements to the exports. [iglocska]

  - Unified the way exports accept negated parameters
  - Fixed the documentation
  - Most exports are now restrictable by the event date (From/To parameters)
  - none cached XML export now writes to file after converting each event, clearing the memory and resolving any potential memory issues

v2.3.41 (2015-02-02)
--------------------
- Merge branch 'hotfix-2.3.41' [iglocska]
- Merging several pull requests and a few other changes. [iglocska]

  - Pull request by RichieB2B: CentOS 6 & 7 installation instructions
  - Pull request by RichieB2B: STIX exports now include comments for indicators
  - Pull request by RichieB2B: Issue fixed with md5 type attributes not generating observables correctly during a STIX export
  - Password policy change-able by a site admin via a regex and a min char requirement. Old functionality assumed if not set.
  - bug fixed with incorrect jobs being created appearing during a scheduled pull (designates a push)
  - slight changes to the installation instructions
  - database.default.php now uses localhost instead of 127.0.0.1 and the default MySQL port
- Merge branch 'RichieB2B-ncsc-nl/install-centos' into hotfix-2.3.41.
  [iglocska]
- Added INSTALL files for CentOS. [Richard van den Berg]
- Merge branch 'RichieB2B-ncsc-nl/stix_indicator_comments' into
  hotfix-2.3.41. [iglocska]
- Pretify some comments. [Richard van den Berg]
- Fixed typo. [Richard van den Berg]
- Fix string assignments to StructuredText. [Richard van den Berg]
- Map most MISP attribute comments into STIX. [Richard van den Berg]
- Preserve indicator comments in STIX export. [Richard van den Berg]
- Merge branch 'RichieB2B-ncsc-nl/stix_md5_hash' into hotfix-2.3.41.
  [iglocska]
- Export md5 hashes without file name in STIX. [Richard van den Berg]
- Fixed a bug with the way scheduled syncs are logged. [iglocska]
- Password complexity definable by admin. [iglocska]

  - administrators can use a regex and a length setting to define password requirements
  - old behavior used if left untouched
- Merge branch 'hotfix-2.3.40' into develop. [iglocska]

v2.3.40 (2015-01-15)
--------------------
- Merge branch 'hotfix-2.3.40' [iglocska]
- Fix to the new sync issues since 2.3.39, fixing #365. [iglocska]

  Incorrectly trying to look up authenticated user in the model fixed
- Merge branch 'hotfix-2.3.39' into develop. [iglocska]

v2.3.39 (2015-01-12)
--------------------
- Merge branch 'hotfix-2.3.39' [iglocska]
- Fixes to the scheduled tasks and some documentation issues. [iglocska]

  - Scheduled pulls should work correctly now
  - Scheduled pushes and pulls correctly display in the logs
  - Scheduled caching correctly sets the next date of execution
- Merge branch 'hotfix-2.3.38' into develop. [iglocska]
- Merge branch 'hotfix-2.3.38' [iglocska]
- Copy pasta fail. [iglocska]
- Merge branch 'hotfix-2.3.38' [iglocska]
- Added missing view. [iglocska]
- Merge branch 'hotfix-2.3.38' [iglocska]
- Remote attribute deletion removed. [iglocska]

  - Deleting attributes on connected MISP instances can cause serious performance issues on multiple interconnected instnaces, temporarily removed
  - Version number incremented
- Update to the automation page. [iglocska]

  - new parameters for the text export explained
- New way to download a single event. [iglocska]

  - The event export buttons have been unified into a single download as... button
  - clicking it loads a popup with all of the export formats
  - added snort, suricata, text dump to the export options
  - added the option for an extra setting for some exports (such as including non IDS flagged attributes, encoding attachments)
  - easily extendable system

  - moved the hidden popup divs into the general layout, can be easily reused anywhere

  - removed the auth refresh option that was re-enabled recently as it seems to sometimes cause issues

  - text exports now allow "all" to be specified as type, which will dump all attribute values that the user can see
  - text exports now allow restricting the results based on event id
- Merge branch 'hotfix-2.3.37' into develop. [iglocska]

v2.3.37 (2014-12-12)
--------------------
- Merge branch 'hotfix-2.3.37' [iglocska]
- Logging of admin emails and auth refresh. [iglocska]

  - admin emails now generate log entries
  - authentication is refreshed on activity
- Merge branch 'hotfix-2.3.36' into develop. [iglocska]
- Merge branch 'hotfix-2.3.36' [iglocska]
- Fix to some event altering actions not updating the timestamp.
  [iglocska]
- Merge branch 'hotfix-2.3.35' into develop. [iglocska]

v2.3.36 (2014-12-10)
--------------------
- Merge branch 'hotfix-2.3.35' [iglocska]
- Small fix. [iglocska]

v2.3.35 (2014-12-10)
--------------------
- Merge branch 'hotfix-2.3.35' [iglocska]
- Freetext import tool enhancement. [iglocska]

  - mass edit types where applicable
  - ip-src/ip-dst type will create two attributes, one for each
- Merge branch 'hotfix-2.3.34' into develop. [iglocska]
- Merge branch 'hotfix-2.3.33' into develop. [iglocska]
- Elhoim and Prz care-package. [iglocska]

  Merge branch 'hotfix-2.3.34'
- Version number incremented. [iglocska]
- Changed the annoying click to view feature on each row on certain
  index pages to double clicks. [iglocska]
- Admin contact user menu moved next to new/list user buttons, recipient
  e-mails are now sorted alphabetically. [iglocska]
- Empty filter options were not that obvious to some users in the
  event/user index filter popup. [iglocska]
- Long filename overlapping with malware button on attachment upload,
  fixes #357. [iglocska]
- Attribute search now correctly searches attribute comments too for
  contained expressions, fixes #342. [iglocska]
- Added tooltip for event ID in attribute search results, fixes #351.
  [iglocska]
- Changed wording of warning message when entering a targeting type
  attribute, fixes #355. [iglocska]

v2.3.34 (2014-12-05)
--------------------
- Merge branch 'hotfix-2.3.33' [iglocska]
- STIX export now correctly uses a custom namespace instead of the
  default "example", fixes #301. [iglocska]
- Merge branch 'hotfix-2.3.32' into develop. [iglocska]
- Merge branch 'hotfix-2.3.31' into develop. [iglocska]

v2.3.33 (2014-12-03)
--------------------
- Merge branch 'hotfix-2.3.32' [iglocska]
- Fix to an issue with the markings in the STIX export. [iglocska]

  - xpath describing the current node and descendants is incorrect

v2.3.31 (2014-11-27)
--------------------
- Merge branch 'hotfix-2.3.31' [iglocska]
- Version number incremented. [iglocska]
- Merge branch 'hotfix-2.3.31' [iglocska]
- Several issues fixed. [iglocska]

  - MYSQL.sql file now correctly includes the task entries
  - GenerateCorrelation admin task is now a background job
  - Organisation of events pulled now get the org in the server object as the owner instead of the one who initiates the pull
  - Small fix to wrapping text in the pivot graph
- Merge branch 'hotfix-2.3.30' into develop. [iglocska]

v2.3.30 (2014-11-27)
--------------------
- Merge branch 'hotfix-2.3.30' [iglocska]
- Some freetext import tweaks, fixes #330, fixes #334. [iglocska]

  - freetext import now optionally allows setting the comment field
  - removing rows in the freetext import result redirects to the event view if all rows are gone
- Incorrect flash message on successfu freetext import fixed, fixes
  #322. [iglocska]
- Confidence mapping changed to boolean in stix export, fixes #326.
  [iglocska]
- Alternate event org display. [iglocska]

  - shows both orgc and org to normal users
  - naming convention changed (orgc => source org, org => member org)
  - this should allow users to see if an event was generated on their instance or not.

v2.3.29 (2014-11-20)
--------------------
- Merge branch 'hotfix-2.3.29' [iglocska]
- Improvements to the attribute search. [iglocska]

  - case insensitivity
  - tag searches

  also, generatecorrelation is now a background job
- Merge branch 'hotfix-2.3.28' into develop. [iglocska]
- Merge branch 'hotfix-2.3.27' into develop. [iglocska]

v2.3.28 (2014-11-19)
--------------------
- Merge branch 'hotfix-2.3.28' [iglocska]
- Fix to the CSRF protection blocking a proposal add. [iglocska]

v2.3.27 (2014-11-14)
--------------------
- Merge branch 'hotfix-2.3.27' [iglocska]
- Diagnostics check fails on PGP check if the server's key is a sign
  only key. [iglocska]
- Merge branch 'hotfix-2.3.25' into develop. [iglocska]
- Merge branch 'hotfix-2.3.25' [iglocska]
- Further corner case fixed (shadow attribute to attribute, not event)
  [iglocska]

v2.3.26 (2014-11-14)
--------------------
- Merge branch 'hotfix-2.3.25' [iglocska]
- Comments also sanitized. [iglocska]
- Merge branch 'hotfix-2.3.25' [iglocska]
- Related events not correctly sanitized in the xml export. [iglocska]
- Merge branch 'hotfix-2.3.25' [iglocska]
- Added to the caching mechanism. [iglocska]

v2.3.25 (2014-11-14)
--------------------
- Merge branch 'hotfix-2.3.25' [iglocska]
- Stronger escaping of special characters in the XML exports. [iglocska]
- Merge branch 'hotfix-2.3.24' into develop. [iglocska]
- Merge branch 'hotfix-2.3.23' into develop. [iglocska]
- Merge branch 'hotfix-2.3.24' [iglocska]

v2.3.24 (2014-11-12)
--------------------
- Fix to an issue with the CSV export. [iglocska]

  - missing linebreak after header row added
  - fixed an issue with quotes in the value field not being escaped properly

v2.3.23 (2014-11-05)
--------------------
- Merge branch 'hotfix-2.3.23' [iglocska]
- Fixes issue with file attachments not being downloadable for users of
  another org. [iglocska]
- Merge branch 'hotfix-2.3.22' into develop. [iglocska]
- Merge branch 'hotfix-2.3.22' [iglocska]
- Document referencing deprecated way of passing authkey in url.
  [iglocska]

v2.3.22 (2014-11-03)
--------------------
- Merge branch 'hotfix-2.3.22' [iglocska]
- Added flag to mimic the quickfilter of the event view to the API.
  [iglocska]

  - search on any sub-string match in the event info, orgc, attribute value, attribute comment via the API
- Merge branch 'hotfix-2.3.21' into develop. [iglocska]

v2.3.21 (2014-10-31)
--------------------
- Merge branch 'hotfix-2.3.21' [iglocska]
- Fix to the missing accept terms button. [iglocska]
- Merge branch 'hotfix-2.3.20' into develop. [iglocska]

v2.3.20 (2014-10-31)
--------------------
- Merge branch 'hotfix-2.3.20' [iglocska]
- Version pushed. [iglocska]
- Quick filter tool, some further tweaks to the filters. [iglocska]

  - quick filter on the event index
  - finds events with a sub-string match on event info, orgc, attribute value, attribute comment
- Added new functionality to the filters. [iglocska]

  - users can now search on attributes
  - attribute search returns any event that has a a sub-string match on the entered attribute
  - can also be used to negate (e.g: don't show me any events that have a sub-string match on any of its attributes)
- Merge branch 'hotfix-2.3.19' into develop. [iglocska]
- Merge branch 'hotfix-2.3.19' [iglocska]
- Left off from previous commit. [iglocska]
- Merge branch 'hotfix-2.3.19' [iglocska]
- Font change caused some misalignment. [iglocska]

v2.3.19 (2014-10-30)
--------------------
- Merge branch 'hotfix-2.3.19' [iglocska]
- Version updated. [iglocska]
- Merge branch 'hotfix-2.3.19' [iglocska]
- Fix to the STIX export fixes #311 and a temporary fix to an OpenIOC
  import issue. [iglocska]

  - STIX export had 2 issues as pointed out by RichieB2B:
      - Incorrect name assigned to incidents due to copy-pasta fail
      - Historyitems incorrectly handled

  - For the OpenIOC import:
      - Mapping DnsEntryItem/Host to hostname
      - Mapping of hostnames to Network activity failed due to incorrect capitalistion
      - Temporarily removed the ignore function on certain indicators. Ignoring an element in an AND-ed branch happens without a pruning of the element IDs
- Merge branch 'hotfix-2.3.18' into develop. [iglocska]
- Merge branch 'hotfix-2.3.18' [iglocska]
- Small visual fix. [iglocska]

v2.3.18 (2014-10-29)
--------------------
- Merge branch 'hotfix-2.3.18' [iglocska]
- File management added and various small changes. [iglocska]

  - Important! Logo images have now moved to a different location! Make sure that you update your settings!
  - Site admins can now manage the uploaded image files and the terms of use file via the server settings interface
  - add, link, delete files directly from the interface
- Merge branch 'hotfix-2.3.17' into develop. [iglocska]

v2.3.17 (2014-10-28)
--------------------
- Merge branch 'hotfix-2.3.17' [iglocska]
- Update to the terms and conditions. [iglocska]

  - use terms file as before if nothing else specified
  - specify a file in the app/files/terms directory via the server settings tool
  - specify whether to show it inline or create a download link for users instead
  - by default everything is the same as before, except that the MISP installation path is no longer exposed by a non-existing terms file
- Merge branch 'hotfix-2.3.16' into develop. [iglocska]
- Merge branch 'hotfix-2.3.14' into develop. [iglocska]
- Merge branch 'hotfix-2.3.16' [iglocska]
- Version number fixed. [iglocska]

v2.3.16 (2014-10-27)
--------------------
- Merge branch 'hotfix-2.3.16' [iglocska]
- Made the version check exclusive to the diagnostics tab. [iglocska]

v2.3.15 (2014-10-27)
--------------------
- Merge branch 'hotfix-2.3.15' [iglocska]
- Event attribute pagination is persistent through edits / deletes.
  [iglocska]

v2.3.14 (2014-10-27)
--------------------
- Merge branch 'hotfix-2.3.14' [iglocska]
- Version check tool added. [iglocska]

  - check the latest tag on github and compare it to the local version
  - from here on all hotfix, minor, major releases should be tagged apropriately.
- Merge branch 'hotfix-2.3.13' into develop. [iglocska]
- Merge branch 'hotfix-2.3.13' [iglocska]
- Changing an attribute's field on the fly now requires a double click.
  [iglocska]
- Merge branch 'hotfix-2.3.12' into develop. [iglocska]
- Merge branch 'hotfix-2.3.11' into develop. [iglocska]
- Merge branch 'hotfix-2.3.10' into develop. [iglocska]
- Merge branch 'hotfix-2.3.12' [iglocska]
- Fix to the capitalisation in the user index filter and fix to the
  scripts tmp folder not being created on git clone. [iglocska]
- Merge branch 'hotfix-2.3.11' [iglocska]
- Added missing empty file. [iglocska]
- Merge branch 'hotfix-2.3.11' [iglocska]
- Further work on the manual, fix to the user filter. [iglocska]
- Work on the documentation and font change. [iglocska]

  - Adding all the new features to the documentation
  - removed Robotolight from css to fix issues with chrome/firefox on Windows
- Merge branch 'hotfix-2.3.10' [iglocska]
- Fix to the GFI upload. [iglocska]
- Merge branch 'hotfix-2.3.10' [iglocska]
- Merge branch 'hotfix-2.3.9' into develop. [iglocska]
- Merge branch 'hotfix-2.3.9' [iglocska]
- Fix to the filters. [iglocska]
- Merge branch 'hotfix-2.3.9' [iglocska]
- Fix to the filters. [iglocska]
- Merge branch 'hotfix-2.3.9' [iglocska]
- Fix to the filter. [iglocska]
- Merge branch 'hotfix-2.3.9' [iglocska]
- Merge branch 'hotfix-2.3.8' into develop. [iglocska]
- Merge branch 'hotfix-2.3.8' [iglocska]
- Changes to the installation. [iglocska]
- Merge branch 'hotfix-2.3.7' into develop. [iglocska]
- Merge branch 'hotfix-2.3.7' [iglocska]
- Added missing comment about enabling the scheduler worker fixes #295.
  [iglocska]
- Merge branch 'hotfix-2.3.6' into develop. [iglocska]
- Merge branch 'hotfix-2.3.6' [iglocska]
- Fixes to the proposal ajax mechanism for newer cakephp versions.
  [iglocska]
- Merge branch 'hotfix-2.3.6' [iglocska]
- Copy pasta fail breaking the proposal accept button fixed, fixes #293.
  [iglocska]
- Merge branch 'hotfix-2.3.5' into develop. [iglocska]
- Merge branch 'hotfix-2.3.5' [iglocska]
- Reverted switch to InnoDB for the events table for now, fixes #292.
  [iglocska]

  - fulltext indexes are not supported on mysql < 5.6 for innodb, and the default version for the current ubuntu distribution seems to be 5.5 still

  Might revisit this in the future
- Merge branch 'hotfix-2.3.4' into develop. [iglocska]
- Merge branch 'hotfix-2.3.3' into develop. [iglocska]
- Merge branch 'hotfix-2.3.2' into develop. [iglocska]
- Merge branch 'hotfix-2.3.4' [iglocska]
- Further improvements to the freetext regex to remove unprintable
  chars. [iglocska]
- Merge branch 'hotfix-2.3.4' [iglocska]
- Remove non printable characters from free text import. [iglocska]
- Merge branch 'hotfix-2.3.4' [iglocska]
- Better split on linebreaks for the freetext import. [iglocska]
- Merge branch 'hotfix-2.3.4' [iglocska]
- Fix to the previous patch. [iglocska]
- Merge branch 'hotfix-2.3.4' [iglocska]
- Fixes issues with the event filters. [iglocska]

  - tags not filtered correctly
  - status bar showing current filters now shows actual strings for tags / analysis / distribution / threat level instead of the IDs
- Merge branch 'hotfix-2.3.3' [iglocska]
- Upgrade to the upgrade documentation to remove the old cache data.
  [iglocska]
- Merge branch 'hotfix-2.3.2' [iglocska]
- CIDR now recognised by freetext import. [iglocska]
- Typo fail fixed. [iglocska]

v2.3.0 (2014-10-07)
-------------------
- Documentation changes. [iglocska]

  - also added the default templates
- Updates to the documentation. [iglocska]
- Incorrect script tmp directory checked in the health tool. [iglocska]
- Another change to the baseurl check. [iglocska]
- Update to the baseurl check in the health tool. [iglocska]

  - https was checked incorrectly before
- Small fix for the statistics. [iglocska]
- Update to the documentation. [iglocska]
- Change db engine to InnoDB. [iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Updated documentation for new release. [Christophe Vandeplas]
- Removed unused column in the health tool. [iglocska]
- Performance improvements. [iglocska]

  - faster load time of the event view by not using Cake's Js generation
- Cleanup of the worker health tool. [iglocska]
- Moved the eventattributerow element back directly into eventattribute.
  [iglocska]

  - Removed serious performance issue on large events
- Update to the event view, attribute rows still had parts of the old
  forms in them hurting performance. [iglocska]
- UI redesign of the template and worker health. [iglocska]

  - UI of templates a bit clearer
  - Worker health tool added to the server settings tool
- Error fixed in the url generation for the filter event index popover.
  [iglocska]
- Incorrect naming fixed. [iglocska]
- Added the option to take ownership of an event uploaded via the Add
  MISP XML button. [iglocska]

  - server setting has to be enabled to allow for this
  - can cause issues if the event gets synchronised with an instance that has a different creator organisation for the same event
  - it is recommended not to use this, but in some cases it can be very helpful - the setting for it in the configuration is called MISP.take_ownership_xml_import
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Merge branch 'hotfix-2.2.40' into develop. [iglocska]
- Copy pasta fail. [iglocska]
- Changes to CakeResque installation fixes #287. [iglocska]

  - CakeResque's installation instructions changed
- Merge branch 'hotfix-2.2.39' [iglocska]
- Merge branch 'hotfix-2.2.38' [iglocska]
- Updated .gitignore. [iglocska]
- Issue with the new csrf protection with the new ajax fields.
  [iglocska]
- Some missing tests added. [iglocska]
- Merge branch 'feature/health' into develop. [iglocska]
- First small changes to the INSTALL.txt, more to follow before 2.3.0 is
  ready. [iglocska]
- No feedback from the failed numeric test for incorrect server
  settings. [iglocska]
- Download of the settings/diagnostics results implemented. [iglocska]

  - Should help with trouble shooting, administrators can now download a json file containing all the settings and issues shown by the tool.
- Added the new server settings to the menues. [iglocska]
- Several changes for the diagnostic tool. [iglocska]

  - Added extra diagnostic tools
- Default config.php added. [iglocska]
- Reworked the server settings for boolean settings and settings that
  have a few options as values. [iglocska]

  - Toggles instead of free-text
- Cleanup, MISP health tool. [iglocska]

  - cleanup of a lot of deprecated settings
  - tool to help assess and alter issues with the instance settings
  - new mechanism to store settings
- Merge branch 'hotfix-2.2.39' into develop. [iglocska]
- Small fix to avoid repeated incorrect invalid messages after the first
  failed check. [iglocska]
- Merge branch 'hotfix-2.2.39' into develop. [iglocska]
- Fix to the PGP key validation tool, fixes #284. [iglocska]
- Debug left in code. [iglocska]
- Changes to the exports, fixes #285. [iglocska]

  - XML export was slow, replaced SimpleXML with a simple script that outputs XML for massive performance gains
  - New option in bootstrap to allow the cached XML export to also include the attachments
  - CSV caching slightly rearranged, it's much more memory efficient now
  - Some fixes to relatedevent orgs being shown even if showorg is disabled
  - Added a new site admin action to generate several 3k events for load testing (slow)
- Pagination controls truncated for events with lots of attributes.
  [iglocska]
- Slightly better looks for the tags on the index. [iglocska]
- Some minor changes to the event index. [iglocska]

  - Tags are now fully shown on the event index
  - can be enabled via bootstrap (the Configure::write setting is in the bootstrap.default.php file)
  - shorthand distribution names
  - narrowed some of the fields down
- Several fixes including compatibility with the STIX to_xml()
  performance fix. [iglocska]

  - STIX export performance greatly improved thanks to 84ce8d8be6376797053668d68e1b863713f008dd
  - some junk removed
  - fixed some minor pagination issues on the event view
  - site admin dummy event creator now has target-* type attributes
- Merge branch 'hotfix-2.2.38' into develop. [iglocska]
- Fixed authored date format, closes #283. [iglocska]
- Merge branch 'hotfix-2.2.37' [iglocska]
- Import from OpenIOC now includes the original file as an attachment,
  fixes #157. [iglocska]
- Added event distribution to alert e-mail, fixes #127. [iglocska]
- Publishing now immediately sets the event to published. A failed push
  will keep the event published, but it will note that it failed in the
  jobs / flash message. [iglocska]
- Merge branch 'hotfix-2.2.37' into develop. [iglocska]
- Fixed an incorrect check for the no PGP key warning condition
  partially responsible for #271. [iglocska]
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Merge branch 'hotfix-2.2.35' [iglocska]
- Merge branch 'hotfix-2.2.36' [iglocska]
- Added the confirmation box div to all the pages that can have the
  publish popup. [iglocska]
- Annoying css bug causing the menues that overlap with the filters not
  to work. [iglocska]
- Added CVE to the freetext tool. [iglocska]
- CakePHP update. [iglocska]
- Show the number of events for each tag in the tag index. [iglocska]
- Small permission change. [iglocska]
- Index filtering made more generic, added to users. [iglocska]
- Added the option to export the event info field with each attribute in
  the csv exports. [iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Merge branch 'hotfix-2.2.36' into develop. [iglocska]

  Conflicts:
  	app/Controller/AppController.php
- Fixes authentication issues for some exports. [iglocska]

  - some exports did not allow users to authenticate via passing the auth key through the header
- Merge branch 'feature/proposalfix' into develop. [iglocska]
- Typo causing the pushed proposals to have an incorrect "old_id" field.
  [iglocska]
- Publish button now loads a popover similar to the attribute delete
  buttons. [iglocska]
- Failed e-mails don't break the proposal creation any longer.
  [iglocska]
- Small tweak to the contributor field. [iglocska]

  - no need for a LIKE in the comparison, should make it slightly faster
- Fix to the push failing. [iglocska]
- MYSQL file left off. [iglocska]
- SQL scripts, some UI chnages. [iglocska]

  MYSQL.sql and upgrade_2.3.sql updated
  Fixed incorrect proposal counts showing up due to attributes that are flagged for deletion also being counted
  Added some extra fields to the view proposal view to make it more useful
- Same as the previous commit, only for the freetext import tool.
  [iglocska]
- Various improvements with the way events are unpublished after
  changes. [iglocska]

  - UI improvements, events appear unpublished after ajax queries that alter attributes
  - Events get unpublished by the attribute replace tool and template population as they should
- Further work on the sync. [iglocska]

  - changed the pull implementation for proposals
- Merge branch 'hotfix-2.2.35' into feature/proposalfix. [iglocska]
- Publishing now also pushes proposals. [iglocska]

  This is especially important to push deleted proposals once a proposal has been accepted
- Merge branch 'feature/proposalfix' of https://github.com/MISP/MISP
  into feature/proposalfix. [iglocska]
- Proposal package now correctly saved on the far end. [iglocska]
- Work on the proposal sync for push - from the sender's side.
  [iglocska]
- More work on the sync fix. [iglocska]
- Further work on the sync fixes. [iglocska]
- Push now also only does a differential push. [iglocska]

  - send uuids of events to be pushed together with timestamps to the other instance
  - other instance removes events that are already up to date or locally created from the array
  - sends the remaining uuids back
  - first instance initiates the push of events that were not filtered out
- Futher work on the proposal sync. [iglocska]
- Further changes. [iglocska]
- First round of fixes. [iglocska]
- Merge branch 'hotfix-2.2.35' into develop. [iglocska]
- Further work on the previous patch. [iglocska]
- Merge branch 'hotfix-2.2.35' into develop. [iglocska]
- Fix to the previous commit. [iglocska]
- Proposal validation now calls the Attribute validation method instead
  of using the (incorrect) duplication in ShadowAttribute. [iglocska]
- Missing validation for http-method in Shadow-Attributes. [iglocska]
- Merge branch 'hotfix-2.2.34' [iglocska]
- Permission fix to the event filters. [iglocska]

  Users could only choose their own organisation in the org filter due to an overly restrictive filtering of the available options. Relaxed to all organisations that have an event that is visible to the user.
- Small fix to the proposal accept button and cakephp 2.4.8+ (related to
  3da49c9) [iglocska]
- View left off from previous commit. [iglocska]
- Reworking of the event filtering. [iglocska]
- Made thread title clickable in event discussions fixes #270.
  [iglocska]
- Fixed an ajax issue with event discussions. [iglocska]

  - could not add posts via the event view
  - related to 3da49c964bcb274049f94c130e93ad0bfef004ba
- Merge branch 'hotfix-2.2.34' into develop. [iglocska]
- Commas in CSV now escaped properly fixes #281. [iglocska]
- Update INSTALL.txt. [Alexandre Dulaunoy]

  Fix #252
- Merge branch 'hotfix/export_suricata' [Christophe Vandeplas]
- Performance. [iglocska]
- Small performance improvement. [iglocska]

  The contributor field in the event view is evaluated based on proposal log entries from the log table affecting the current event. In order to improve performance, the LIKE check for the event ID is moved to the last argument in order to avoid parsing rows that could be ignored by the other arguments quicker.
- Updated cakephp. [iglocska]
- Fixed broken AJAX queries in MISP as a result to changes in cakephp
  2.4.8+ [iglocska]

  A change in cakephp version 2.4.8+ has resulted in ajax form submitions breaking. Reason for this was a change in the SecurityComponent taking the url specified in the form into account when generating the CSRF tokens.

  This is now fixed by embedding the correct url in the ajax forms.
- More missing <?php tags. [iglocska]
- Missing <?php tag in a view file. [iglocska]
- Missing view file added. [iglocska]
- Updates to the STIX export. [iglocska]
- Fix to the previous commit. [iglocska]

  - previous commit broke the flash message alignment when debug was enabled
- Fixed the annoying collapsing top bar. [iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Merge branch 'hotfix/export_suricata' into develop. [Christophe
  Vandeplas]
- Regex bugfix in the ids export + suricata export using dns keyword.
  [Christophe Vandeplas]
- Merge branch 'hotfix-2.2.33' [iglocska]
- Merge branch 'feature/stix_export' into develop. [iglocska]
- Some cleanup. [iglocska]
- Download stix xml / json result. [iglocska]
- Removed old junk version of the export. [iglocska]
- First version of the STIX export implementation. [iglocska]

  - currently to_xml() has performance issues, if it's not resolved fast, it would be a good idea to move the export to the background workers

  - some UI changes
- Python scripts to handle the conversion from a MISP JSON event to
  stix/cybox. [iglocska]
- Start of the stix export tool. [iglocska]
- Merge branch 'feature/templates' into develop. [iglocska]
- Same org / site admin restriction on freetext importer added.
  [iglocska]
- Truncated the event info fragment shown in the pivot bubbles by one
  extra character. [iglocska]
- Merge branch 'feature/templates' into develop. [iglocska]

  Conflicts:
  	app/Model/Event.php
- Update to the main MYSQL.sql file. [iglocska]
- Update for the MYSQL scripts for the new features. [iglocska]
- Several features finished. [iglocska]

  - first version of templating system complete
  - first version of freetext importer complete
  - first version of mass attribute replace tool complete

  - some UI changes
- Freetext import tool. [iglocska]

  Added freetext import tool
- Some fixes to the templating. [iglocska]

  - resolved bugs with permissions
  - fixed the broken mass delete tool
  - Fixed an issue with the type not being chosen correctly for file type attributes when created through the templating tool
- First version of the templating feature complete. [iglocska]

  - still needs some refinement, but it's feature-complete
- Further work on the templates. [iglocska]
- More work on the templates. [iglocska]

  - Templates can now be created and populated
  - Users can populate an event using a template (still needs work)
  - File type elements are not yet implemented
- Further work on the templating system. [iglocska]
- Work on the templating system. [iglocska]

  - create a basic template
  - add text elements to the template
  - rearrange elements
- Merge branch 'hotfix-2.2.33' into develop. [iglocska]
- 2 Background worker issues fixed. [iglocska]

  - Start-up script could only be started from the script's location

  - Division by zero in e-mail alerts when calculating the progress of the background job
- Merge branch 'hotfix-2.2.32' [iglocska]
- Merge branch 'hotfix-2.2.32' into develop. [iglocska]
- Removed junk left in the previous commit. [iglocska]
- Update to the way xml files are cached. [iglocska]
- Merge branch 'hotfix-2.2.31' [iglocska]
- Merge branch 'hotfix-2.2.31' into develop. [iglocska]
- Fix to an incorrect check for privileges in the event deletion.
  [iglocska]
- Merge branch 'hotfix-2.2.30' [iglocska]
- Fixes to several ajax related issues. [iglocska]

  - malware samples / attachments couldn't be downloaded
  - links weren't actually links

  - deleting an attribute / shadowattribute now opens a custom confirmation dialogue. This is also where the CSRF tokens are generated for the post request to execute the delete, resulting in a faster event view load
- Fix to several permission issues. [iglocska]
- Merge branch 'hotfix-2.2.30' into develop. [iglocska]
- Attributes not edited correctly when pushing an edit through REST api
  if the event came from a manual export. [iglocska]

  - fixed
- Merge branch 'hotfix-2.2.29' [iglocska]
- Merge branch 'hotfix-2.2.29' fixes #259. [iglocska]
- Merge branch 'hotfix-2.2.29' into develop. [iglocska]
- Fixed a copy paste fail in the previos commit. [iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Nicer way of resizing activated fields. [iglocska]
- Merge branch 'hotfix-2.2.29' into develop. [iglocska]
- Better feedback from edits to events failing via REST api. [iglocska]

  - also, site admins can edit events regardless of who the orgc is via the REST api.
- Merge branch 'hotfix-2.2.28' [iglocska]
- Merge branch 'hotfix-2.2.28' into develop. [iglocska]
- Update to the installation instructions (fixes #257) and the 2.2
  upgrade script. [iglocska]

  - fixed 2 incorrect entries in the installation.txt file

  - fixed an incorrect variable name in the 2.2 event upgrade script
- Merge branch 'hotfix-2.2.27' [iglocska]
- Merge branch 'hotfix-2.2.27' into develop. [iglocska]
- Events directly exported from MISP and imported to another instance
  failed on edit, fixes #259. [iglocska]

  - Events exported were enclosed in a <response> tag, which the sync automatically filters out, but a manual export and import would fail on edits

  - added a conditional that removes the <response> tag if an event is encapsulated in a request to the edit method
- Merge branch 'hotfix-2.2.26' [iglocska]
- Merge branch 'hotfix-2.2.26' into develop. [iglocska]
- Update to the installation instructions, fixes #257. [iglocska]
- Merge branch 'hotfix-2.2.25' [iglocska]
- Merge branch 'hotfix-2.2.25' into develop. [iglocska]
- Fixed an issue with an incorrect timestamp comparison for attributes,
  allowing the update of an attribute with an older version. [iglocska]
- Merge branch 'hotfix-2.2.24' [iglocska]
- Merge branch 'features/ajaxification' into develop. [iglocska]
- Another small permission fix. [iglocska]
- Merge branch 'features/ajaxification' into develop. [iglocska]
- Nicer fix for the previous issue. [iglocska]

  - since checkboxes weren't working for site admins
- Merge branch 'features/ajaxification' into develop. [iglocska]
- Fix to site admins not being allowed to edit attributes. [iglocska]
- Merge branch 'features/ajaxification' into develop. [iglocska]
- Merge branch 'develop' into features/ajaxification. [iglocska]

  Conflicts:
  	app/View/Elements/img.ctp
- Merge branch 'hotfix-2.2.24' into develop. [iglocska]
- CSV export now includes date for each attribute, fixes #255.
  [iglocska]
- Merge branch 'hotfix-2.2.23' [iglocska]
- Merge branch 'hotfix-2.2.23' into develop. [iglocska]
- Incorrect default timeout value fixed in core.php. [iglocska]
- Merge branch 'hotfix-2.2.22' [iglocska]
- Merge branch 'hotfix-2.2.22' into develop. [iglocska]
- Automation authentication via header fixes #254. [iglocska]

  - Authentication via headers was only allowed if _isRest() returned true
  - this only happened for pages returning JSON or XML content

  - a new check, _isAutomation() was added that allows authentication via headers for certain methods used by the automation system
- Merge branch 'hotfix-2.2.21' [iglocska]
- Merge branch 'hotfix-2.2.21' into develop. [iglocska]

  Conflicts:
  	app/Controller/AttributesController.php
- Several fixes. Fixes #246 and fixes #248. [iglocska]

  - Exporting a JSON object erroneously included related objects which prevented the exported event from being added back to MISP via the API

  - Downloading search results as XML / CSV now correctly includes all of the search results instead of just the 60 visible ones on the UI (cut off by the pagination)

  - The tags parameter in the exports now correctly accepts null as a valid value even if it is the last parameter
- Merge branch 'hotfix-2.2.20' [iglocska]
- Merge branch 'hotfix-2.2.20' into develop. [iglocska]
- Missing parantheses. [iglocska]

  - fixed.
- Merge branch 'hotfix-2.2.20' into develop. [iglocska]
- GPGKey not showing up for admin/users/view. [iglocska]

  - incorrect conditional fixed
- Very large PGP keys would prevent users from logging in - fixes #142.
  [iglocska]

  - removed the PGP key from the Auth user

  - PGP key of currently logged in user is looked up on demand and not stored in the session
- Fix to event REST add. [iglocska]

  - upgrade script broke adding events via the rest interface if they had an xml_version included

  - fixed, also, add now more flexible with directly adding events from an export encapsulated in a response tag
- Merge branch 'hotfix-2.2.19' [iglocska]
- Merge branch 'hotfix-2.2.19' into develop. [iglocska]
- Fixed an issue with IE9 not rendering the contributor image as a small
  icon. [iglocska]
- Small changes to the UI to help with low resolutions. [iglocska]

  - side menu now becomes fixed if the resolution is too low to fit all menu elements
  - fix to the logo resize script causing errors when on the login screen - due to it never being rendered.
- Fix to the csv export in the automation not allowing a full export
  ignoring ids flags. [iglocska]
- Merge branch 'hotfix-2.2.18' into develop. [iglocska]
- Fix to the csv export's issue with exporting all events ignoring the
  ids flag. [iglocska]
- Merge branch 'hotfix-2.2.18' into develop. [iglocska]
- Merge branch 'hotfix-2.2.17' [iglocska]
- Merge branch 'hotfix-2.2.17' into develop. [iglocska]
- Fix to the export issue with md5 / sha1 fixes #237. [iglocska]
- Merge branch 'feature/paramToPost' into develop. [iglocska]
- API improvements fixes #234. [iglocska]

  - events/restSearch, attributes/restSearch, events/xml, attributes/returnAttributes

  - users can now POST a search array in XML / json instead of sending the parameters in the url
- Cakephp update. [iglocska]
- Merge branch 'hotfix-2.2.16' [iglocska]
- Update to cakephp. [iglocska]
- Merge branch 'hotfix-2.2.16' into develop. [iglocska]
- RestSearch can now return a json (both attribute and event) fixes
  #233. [iglocska]

  - also a whitelisting issue fixed
  - tag search field not set now correctly returns all events regardless of tags
- Merge branch 'hotfix-2.2.15' [iglocska]
- Merge branch 'hotfix-2.2.15' into develop. [iglocska]
- Fixed text attribute exports not working with the auth key in the url.
  [iglocska]

  - legacy attribute export was broken due to the text action in the attributescontroller not being allowed globally
- Merge branch 'hotfix-2.2.14' [iglocska]
- Merge branch 'hotfix-2.2.14' into develop. [iglocska]
- Event description in alert e-mail subject made optional, fixes #231.
  [iglocska]
- Merge branch 'hotfix-2.2.13' [iglocska]
- Clearer disctinction between proposals that belong to an attribute and
  proposals to an event. [iglocska]
- Ajaxification of the event page done also, replaced histogram in
  memberslist. [iglocska]

  - AJAX requests now also respond with a small message at the bottom of the page, notifying the user of the result
  - The following actions work now on the event page via ajax:

  1. Add / remove tags
  2. quick edit any attribute field if eligible
  3. quickly create a proposal of any attribute field if not eligible to edit
  4. popover attribute creation (also works with batch add)
  5. popover proposal creation (also works with batch add)
  6. delete attributes
  7. accept/discard proposals
  8. mass edit / delete attributes

  Also, replaced the old memberslist, with a small lightweight css/js based one.
- Further work on the ajaxification. [iglocska]

  - mass deletes / mass edits

  - tagging now done via ajax

  - also, several small unrelated issues fixed
- Rework of the way the ajax editing works. [iglocska]

  - forms are now dynamically pulled onclick
  - performance greatly enhanced
  - solves the issues with the CSRF protection kicking in if the user edits a field after using the back button
- Next step in the ajaxification. [iglocska]

  - multiselect / multidelete
  - some additional UI changes for the event view
- Next step in the ajaxification of the event view. [iglocska]

  - users can now edit all fields in an attribute whilst on the event page

  - issues left to fix:
  	- tag changes after an attribute change run into CSRF protection
  	- batch add not handled gracefully yet
  	- going back to the event view and editing a field gives users an error message over the CSRF protection - instead, silently check if the page is loaded in a dirty way and refresh the ajax fields silently
  	- quickadd of attributes still missing
- Next step in the ajaxification. [iglocska]
- Two missing view-elements from the previous commit added. [iglocska]
- First commit of the event view ajaxification. [iglocska]

  - pagination of the attribute index within the event view
  - add attributes in a pop-up window
  - instantly refresh attributes
- Merge branch 'hotfix-2.2.13' into develop. [iglocska]
- Missing user guide images added. [iglocska]
- Merge branch 'feature/alternate_search' into develop. [iglocska]
- Alternate search results. [iglocska]

  - Users can now elect to receive their attribute search results in the new alternative view

  - instead of receiving a list of attributes matching the search options, users are presented with a list of events that contain matching attributes

  - number of matches and a percentage of those matches being marked as indicators for IDSes are shown

  - the events are ordered by the percentage of IDS worthy attribute
- Merge branch 'hotfix-2.2.13' into develop. [iglocska]
- CSV exports have a new column: to_ids. [iglocska]

  - event level exports from the event view now export all attributes regardless of to_ids value

  - to_ids value now has its own column in the csv exports
- Distribution field in event view shortened. [iglocska]

  - now only shows the distribution level name
  - the description is in the title of the field, hovering over it will show it
- Fix to comments not being synced. [iglocska]

  - attribute comments will now be correctly synced
- Merge branch 'hotfix-2.2.12' [iglocska]
- Small change to the new alert e-mail titles. [iglocska]

  - the event description in the subject shortened to 55 characters maximum.
- Merge branch 'patch-8' of https://github.com/Xen0ph0n/MISP into
  hotfix-2.2.12. [iglocska]
- Remove Missing GPG flash if Unencrypted Email is enabled. [Chris
  Clark]

  Adds a check for a true value in GnuPG.onlyencrypted and will only display the "No GPG Key Set in your Profile" message to the user if it is missing AND MISP is set to send only encrypted email. This way orgs not using GPG will not see the banner on every index view.
- Merge branch 'patch-7' of https://github.com/Xen0ph0n/MISP into
  hotfix-2.2.12. [iglocska]
- Tweaks To Email Output. [Chris Clark]

  Small tweaks to email formatting to sync up with UI Changes.. also added event title to Subject (questionable if this is something desired globally as it would not be encrypted).
- Update to include starting the BG Workers. [Chris Clark]

  This is present in the upgrade.txt but not the install.txt. I'm not sure if this is the right location for noting this, but in the current version publishing events will not function w/out starting the BG workers.
- Merge branch 'hotfix-2.2.11' [iglocska]
- Added CSV to pages allowed to be visited without being logged in for
  automation. [iglocska]

  - same as the other export formats
- Merge branch 'hotfix-2.2.11' [iglocska]
- CSV export changes. [iglocska]

  - It is now possible to restrict the CSV automation export by type / category

  - updated the automation page to describe how the syntax works

  - fixed an issue with line breaks not being sanitized for the CSV export
- Merge branch 'hotfix-2.2.10' [iglocska]
- Some cleanup. [iglocska]
- Merge branch 'hotfix-2.2.10' [iglocska]
- Updated cakephp. [iglocska]

  - includes the HttpSocket fix to CakePHP by cvandeplas
- Merge branch 'hotfix-2.2.9' [iglocska]
- Some UI changes and other minor changes. [iglocska]

  - images updated in user manual

  - fixed validation issues with named pipe (at the moment it's very loose)

  - Fixed an issue with shadow attriubutes not showing for events that have no attributes

  - some minor UI changes to make MISP a bit prettier
- Merge branch 'hotfix-2.2.9' [iglocska]
- Small animation for the MISP logo. [iglocska]
- User guide and UI changes. [iglocska]

  - first set of changes to the user guide, still missing updated images

  - some UI changes to make the looks a bit more appealing
- Merge branch 'hotfix-2.2.8' [iglocska]
- SHA256 based shadowattribute validation added. [iglocska]

  - it was missing before
- Merge branch 'hotfix-2.2.7' [iglocska]
- The list of contributors no longer show the logo of an org that hasn't
  made a proposal. [iglocska]

  - Until now, organisations that have made any change to an event in the past (even including an admin running scripts that update the event) would flag an event as having an extra contributor

  - From now on, the Contributors field only shows orgs that have created proposals
- Merge branch 'hotfix-2.2.7' [iglocska]
- Fix to the xml automation export and various other changes. [iglocska]

  - xml export now correctly exports all attachments if specified as parameter

  - print view fixes

  - disclaimer for old IE versions (< 10) and compatibility mode users when viewing the statistics (The heatmap calendar requires 10+)
- Merge branch 'hotfix-2.2.7' [iglocska]
- Print view fixed for event view. [iglocska]
- Merge branch 'hotfix-2.2.6' [iglocska]
- Previous commit was incorrect, fixed. [iglocska]
- Merge branch 'hotfix-2.2.6' [iglocska]
- Fixed a bug that allowed read-only users to create an event.
  [iglocska]
- Merge branch 'hotfix-2.2.6' [iglocska]
- Anonymising the e-mail addresses in discussions. [iglocska]

  - The email addresses were shown on the event view even if the post was made by a user of another org
  - fixed
- Merge branch 'hotfix-2.2.6' [iglocska]
- Restricting the event log to show only proposals when selecting the
  contributions of an org. [iglocska]

  - the event changes that a proposal creation creates are also logged (such as disarming the proposal email lock) -> this should not be shown in this log view.
- Merge branch 'hotfix-2.2.5' [iglocska]
- Incorrect method call. [iglocska]

  - updateXML was moved to the event model, but some calls still tried to call it within the EventsController
- Merge branch 'hotfix-2.2.4' fixes #220 and fixes #221. [iglocska]
- Incorrect check in the API when using the authkey in the URL.
  [iglocska]

  - check lead to the user incorrectly being passed on after authentication, not returning any private data of their own organisation.

  - Also, publishing an event with the background jobs enabled now correctly shows that the job was added to the queue instead of telling the user that the event has been published.
- Incorrect branching code closing bracket. [iglocska]
- Xen0ph0n's patch updated according to his recommendation. [iglocska]

  - replace '.' in domain names, ip-src and ip-dst with '[.]' instead of '-'
- Merge pull request #217 from Xen0ph0n/patch-5. [iglocska]

  Code to defang URLs/Emails/Domains/IPs in Alerts
- Code to defang URLs/Emails/Domains/IPs in Alerts. [Chris Clark]
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Merge branch 'hotfix/2.2.2' [Christophe Vandeplas]
- Correct unneeded $(echo $var) [Christophe Vandeplas]
- Merge branch 'hotfix-2.2.3' [iglocska]
- Fixes with the synchronisation. [iglocska]

  - background pulls fixed
  - now correctly logs changes
  - now correctly updates attributes
- Incremental pull and fixes to pulling shadow attributes. [iglocska]

  - during the event id pull, the local server already checks the timestamps, removing the ids of events that are not newer than the local version
  - this results in only the event metadata being pulled for all events, and the attributes of only those events that need to be updated are pulled resulting in much quicker pulls

  - Fixed an issue with proposals that got pulled not finding the attribute that they are proposals to (for proposals that belong to an attribute)
- Merge branch 'hotfix-2.2.1' [iglocska]
- Changes to the tagging. [iglocska]

  - tags can now be set correctly for all events
  - some UI changes to the tags
  - moved the deletion of all event_tags when a tag gets deleted to beforefilter
- Merge branch 'hotfix-2.2.1' [iglocska]
- Deleting tags fixed. [iglocska]

  - now it correctly deletes tags
  - also deletes all EventTags
- Merge branch 'hotfix-2.2.1' [iglocska]
- Update to the tag automation tag searches. [iglocska]

  - A colon in the tag search tag will render the tag search invalid. Since colons are commonly used in tag names, this poses an issue - users should use a semi-colon instead, which gets automatically converted to a colon.
- Fixing newlines in script. [Christophe Vandeplas]
- Merge branch 'develop' [iglocska]
- Minor corrections in the UPGRADE docu. [Christophe Vandeplas]
- Clean cache at upgrade. [Christophe Vandeplas]
- Merge branch 'develop' [iglocska]

v2.2.1 (2014-02-19)
-------------------
- Merge branch 'feature/sharing_groups' into develop. [Alexandru
  Ciobanu]
- Save sharing group in EventsController::_add() [skip ci]     - changed
  JSON Sharing Group format to match other models. [Alexandru Ciobanu]
- Set user org based on new organisation field. Ensures backware
  compatibility. [Alexandru Ciobanu]
- Add org back in views, but hidden. [Alexandru Ciobanu]
- Unique organisations and sharing groups  - remove old org field from
  views, still present in controllers since it'll    break everything if
  removed  - show sharing groups in event view. [Alexandru Ciobanu]
- Sharing groups fixes [skip ci]  - exports obey sharing group  -
  Organisation HABTM SharingGroup  - event alerts and publishing
  consider sharing group  - users can download attachments only if in
  correct sharing group  - MISP bake template, to be used for new
  scaffolds. [Alexandru Ciobanu]
- Adds share to specific server option [skip ci] [Alexandru Ciobanu]
- Enforce access limitations baased on sharing group. [Alexandru
  Ciobanu]
- Adds Organisation and Sharing group CRUD [skip CI]  - updates message
  flashing with better color coding:     red == error, yellow ==
  warning, green == success  - updates schema to include organisation
  and sharing_groups tables;  - adds baked fixtures and test cases for
  newly added models; [Alexandru Ciobanu]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [Alexandru Ciobanu]
- Adds initial sharing group structures [skip ci] [Alexandru Ciobanu]
- Fixing newlines in script. [Christophe Vandeplas]
- Minor corrections in the UPGRADE docu. [Christophe Vandeplas]
- Clean cache at upgrade. [Christophe Vandeplas]
- Added OpenIOC mapping for DnsEntryItem/RecordName fixes #210.
  [iglocska]
- UI now correctly shows if self-signed certificates are allowed for a
  link. [iglocska]
- Changes to uploading a ca file for a server link. [iglocska]

  - create folder if it doesn't exist
  - correctly save file if edited
- Bug fixes. [iglocska]

  - issues with the way users were passed to the related event finder during a publish
- Update to the threatconnect import. [iglocska]

  - Threatconnect import now allows any valid threatconnect csv file to be imported as long as type, value, confidence, description and source are included
- Deprecated flag used to check it sync is enabled. [iglocska]

  - fixed, now correctly looking for MISP.sync
- Thread count now correctly displayed in the statistics. [iglocska]

  - Viewing an event without a discussion thread creates an empty thread in preparation of future posts - these empty threads should not count as active threads though.
- Fix to scrolling the heatmaps. [iglocska]

  - Scrolling would reset the organisation data -> fixed
- Small change in the installation description. [iglocska]

  - clearer description of the mysql import process
- Fixed some incorrect values in the MYSQL.sql file. [iglocska]
- Statistics changes. [iglocska]

  - remove actions such as login, logout, changepw
  - fixed range so that a addinga a massive event doesn't make every other day seem less active
- Fix to the statistics page. [iglocska]

  - heatmap now fed the correct data
- Updated message for old browsers. [iglocska]
- Bug with the text export. [iglocska]
- Removal of obsolete stuff. [iglocska]

  - taking out the trash
- Some fixes to the automation and an updated manual. [iglocska]

  - made it easier to provide null values if the user would want to specify the n+1th parameter whilst leaving the nth on null
- Xml export now takes null in the eventid parameter as null. [iglocska]

  - also a debug method removed
- Changes to the installation instructions. [iglocska]

  - some changes also to the scripts
  - replaced old scripts with newer versions (jquery, d3)
  - Some updates to the manual (still needs more work)
- Updated link in gitmodules to cake-resque. [iglocska]
- Check if column exists in mysql upgrade script. [iglocska]

  - if a column already exists, don't try to add it
  - if the key of a value exists, don't insert it
- Fixed various things. [iglocska]

  - logging of event publishing enabled for background jobs
  - disabled a gpg debug mode that was enabled by accident
  - better feedback for publishing
- Merge branch 'feature/test' of https://github.com/MISP/MISP into
  feature/test. [iglocska]
- Small fix to the upgrade script. [iglocska]

  - location of the upgrade sql script fixed
- Various changes. [iglocska]

  - regexp structural changes added to the upgrade script (type)
  - Added publish / alert to the background jobs
  - fixed a misalignment with the statistics
- Fix to issues with the install script. [iglocska]

  - no more relative jumps in the script
  - moved the cakephp include directory to fix background worker issues
- Engrish. [iglocska]
- Further work on the install script. [iglocska]
- Updated paths for the console and test. [iglocska]
- Left off line that executes mysql query from the script. [iglocska]
- Cosmetic change to the upgrade script. [iglocska]
- Database update added to upgrade script. [iglocska]
- More fine tuning to the scripts. [iglocska]
- Removed deleted plugin references from default bootstrap file.
  [iglocska]
- Changed previous commit. [iglocska]
- More work on the scripts. [iglocska]
- Fix to the upgrade scripts. [iglocska]
- Upgrade shell scripts. [iglocska]
- Integration of plugins / cake core into MISP as submodules. [iglocska]

  - easier installation script
  - the goal is to reduce the procedure to a few steps
- Further work on the upgrade scripts / description. [iglocska]
- Bug with the exports. [iglocska]

  - only events that could be seen were checked when calculating whether the user's org needs to recache the exports. This meant that the information was incorrect if another org has a visible event that was newer.
- Typo fixed. [iglocska]
- Added structure for export folders. [iglocska]

  - previously not added because git ignores empty directories
- Update to gitignore. [iglocska]
- Merge branch 'feature/test' of https://github.com/MISP/MISP into
  feature/test. [iglocska]
- Added threat level id-s for the event table to the upgrade script.
  [iglocska]
- Small fixes. [iglocska]
- CakeResque inclusion. [iglocska]
- Update to the default bootstrap file for 2.2. [iglocska]
- Updated the schema file. [iglocska]
- Removed unused Model file from an old version of the pivots.
  [iglocska]
- New upgrade scripts and more. [iglocska]

  - MYSQL.sql updated
  - upgrade_2.2.sql updated

  - List of active proposals for you and your organisation now shows the org logos of the contributing organisations
- Changed name of Populate from IOC to OpenIOC fixes #154. [iglocska]
- Visual changes to the attribute list / search Fixes #162. [iglocska]

  - org shown for each attribute
  - performance improvement (only necessary fields loaded for the event)
- Mass replace replace of the old CyDefSig name to MISP - fixes #82.
  [iglocska]
- Bruteforce logging. [iglocska]

  - if a user becomes blacklisted, the system will log it. Fixes #206
- Various changes. [iglocska]

  - contributors shown on the event view (list of the organisation logos of users that have contributed through proposals)
  - these link to the event history containing only entries from their organisation

  - changes to the activity heatmap
  - heatmap now dynamically changes the range on the graph based on the obtained values
  - performance improved
  - buttons to move back or forward in time on the calendar

  - Attributes:
  - warning for the user if he/she has selected the attribute category "targeting-data" or "attribution" as these could contain classified information
  - UI improvements across most attribute and shadowattribute input views

  - Updated cal-heatmap to the newest version
- CSV added to tag searches. [iglocska]

  - also, fixed an issue where an incorrect tag search would return all possible IDs that are visible to the user
- Several changes in one (xml version, tag filters for exports)
  [iglocska]

  - xml version now included in the xml exports
  - MISP will now check the xml version on all imports related to sync / add MISP XML and try to update the incoming info if it detects an older version

  - exports now take tag names as a parameter (affected exports: XML, text, HIDS, NIDS)

  - eventtags now correctly get removed when an event is deleted
- Changes to the logging and scheduling. [iglocska]

  - Scheduled tasks for pull / push now working as intended
  - Rescheduling of all tasks fixed
  - protection against the rescheduled task ending up in the past

  - further event history fixes
  - fixed lots of erroneous logging
  - performance improvement with logging (no longer loading controllers for no reason)
  - logging extra actions that weren't logged before (proposal accept / discard, server pull / push)
- Changes to the log system. [iglocska]

  - View Event history now shows the logo of the org whose action triggered the log entry
  - View Event History now shows different fields than before
  - Proposals now logged
  - Accepting / Discarding a proposal now doesn't create junk edit / delete entries as before.
  - Creators of an event can now see all of the log entries altering an event in the event history log. This includes deleted events.
- Incorrect argument passed to cache generation. [iglocska]
- Org admins should be able to delete / edit their own server links.
  [iglocska]
- Permission issue with delete servers. [iglocska]

  - fixed a bug that prevented the deletion of sync links
- Fixes to the tagging. [iglocska]

  - made menu options invisible for non tagging permission users that requires the permission
  - colour picker added to edit (was only enabled on add)
- Tagging system. [iglocska]

  - new special role for tagging
  - can create tags with a name + colour combination (using a colour picker plugin)
  - users can assign tags to events
  - can filter events by tags on the index
- New permission. [iglocska]

  - tagger: a user that can create / edit / delete the list of tags that is usable for events
- Changes to the sync action pages. [iglocska]

  - fixed access control
  - any admin can now encode new servers. Org admins can pull/push for their own instances.

  - Upload certificates during an edit
- Threat level changes. [iglocska]

  - upgrade script that populates threat level from the old risk field for every event that doesn't have a threat level set.
  - threat levels in an event (from a sync for example) that are unknown to the local instance now show the numeric value of the threat level
- Changes to the admin methods. [iglocska]

  - cleaned up the methods, they all now return results without debug mode enabled
  - Added a verification method for all user GPG keys (as an expired key for example would send out empty messages)
- Changes to the misc admin functions. [iglocska]

  - cleaned them up a bit, views for results
  - removed query() and replaced it with CakePHP find()
- Changes to the automation. [iglocska]

  - authorization key should be sent through headers.
  - passing it in the url is deprecated
  - updated automation page to reflect the changes

  - csv export now has headers
- Roles correctly visible to users. [iglocska]

  - users can now check what each role group grants in terms of permissions
  - users cannot see a non-working add user / list users button
- Accepting / Discarding Proposals changed to POST only. [iglocska]

  - it is not possible to discard / accept a proposal with a GET request anymore
- SSL certificate changes. [iglocska]

  - you can now upload a certificate file and allow a server link to use a provided self signed certificate. This should solve the issues that some organisations are having when trying to connect their instances
- Small change to CVE notation fixes #186. [iglocska]
- Cosmetic changes. [iglocska]

  - Valid renamed to Published on the event index
  - Attributes that are flagged as IDS signatures are now shown with a (IDS) notation at the end of the line in the alert e-mail
- Merge branch 'feature/test_attribute_date' into feature/test.
  [iglocska]
- Some minor changes and fix to a vulnerability. [iglocska]

  - fix to the creator of a proposal being able to also accept it
  - new attributes are now shown in the e-mail denoted by a * when an event is republished
  - the date of an attribute's creation is shown
- Changes to the attributes. [iglocska]

  - attributes in the event view now show the date when they were added / modified

  - the alert e-mail now shows which attributes are new since the last commit
- Small fix to the date filter. [iglocska]

  - fixed the datefilter to be inclusive of the border values. Entering all events from the 13th of january should include events that were created on that day, not just the 14th and newer.
- Some changes from master branch. [iglocska]

  - regexp default list
  - GFI improvements (removed a lot of junk imports, distribution taken from the event)
- File left off from previous commit. [iglocska]
- Proposal changes. [iglocska]

  - anyone can see proposals that can see an event
  - fixed a vulnerability where a user could add a proposal to an event blindly that he couldn't see
- Some security fixes. [iglocska]
- Some minor changes. [iglocska]

  - Statistics page has gotten a lot of extra information
  - Removed some old junk files
  - Made the size of the graph in the memberslist larger to fit all the new attribute types
- Left off files added. [iglocska]

  -Missing view file for statistics
  -Added includes needed for the heatmaps (using http://kamisama.github.io/cal-heatmap)
- Error When Exporting as IOC if not Site Admin. [Chris Clark]

  This was comparing the wrong value to the event org to determine org membership and thus $isMyEvent value for privileges for export of IOCs if not a site admin.
- Tweak to allow IOC Export of events you don't own but are shared
  Conflicts:     app/Controller/Component/IOCExportComponent.php. [Chris
  Clark]
- Added Attribute Category and Types to Track Targeting Data. [Chris
  Clark]
- First version of the new statistics page. [iglocska]

  - shows a heatmap of user activity based on the logs
  - can show it for all users or for users of a specific org
- Bug fixes. [iglocska]

  - Fix to some of the exports not working in legacy (non background-job) mode
  - Issue also occured while using automation
- Fixed vulnerability. [iglocska]

  - Persistent XSS through the thread title fixed
- Serious bug with the discussion boards. [iglocska]

  - A malformed [Thread][/Thread] tag can lead to an infinite loop on the event / thread view. Fixed.
- Some small fixes. [iglocska]

  - Corrected some weak notifications on background jobs
  - Changed the view slightly to view background jobs
  - fixed an issue where editing a sync server setting would cause an error due to the id not being passed to the logging plugin
- Fix of a new pagination rule overwriting the rest allowing users to
  see more than they should. [iglocska]
- Merge branch 'feature/CakeResque' into feature/test. [iglocska]
- Several features. [iglocska]

  - Sync for background jobs (pull + push)
  - more e-mailing delegated to background jobs
  - A bunch of bug fixes and minor changes
- Work on the background job and the proposals. [iglocska]

  - Proposals now get synced on pull
  - several bug fixes
  - new startup script for the background workers
- Small change to the tasks index. [iglocska]

  - removed script that after changes was basically a copy of another one
- More work on the background jobs. [iglocska]

  - added scheduler to the export caching
  - site admins can set up the intervals of the automated caches, and the exact times at which they should be executed.
- Further work on the background jobs. [iglocska]

  - started work on scheduling
  - view to add scheduled tasks (still needs work)
  - moved cache job bulk-code to the job model from the controller
  - bootstrap timepicker
- Further work on the scheduled tasks. [iglocska]

  - Also some changes left off from the previous commit
- Preparing for the scheduled tasks. [iglocska]

  - incorporated cidr from develop
  - some other improvements to the background jobs
- Proposal changes Fixes #192. [iglocska]

  - Contextual comments for proposals
  - shows proposal count in the top bar
  - new view showing all of the events of the user's organisation with an active proposal
- Further work on the background jobs. [iglocska]

  - contact reporter now moved to the model
  - backround job not implemented for it yet
- Merge branch 'develop' into feature/CakeResque. [iglocska]

  Also, more work on the background jobs
  - started work on publishing
  - started making the background jobs an optional setting in bootstrap

  Conflicts:
  	app/Controller/AppController.php
  	app/Controller/EventsController.php
- Next version of exports done. [iglocska]
- Further work on the exports. [iglocska]
- Most of the export caching done. [iglocska]

  - also a fair bit of refactoring of the code, fatter models, thinner controllers, component moved to Lib
- More work on the background jobs. [iglocska]

  - Started work on the exports
- Removed debugkit. [iglocska]
- Merge branch 'develop' into feature/CakeResque. [iglocska]

  - develop and the first CakeResque implementation merged

  Conflicts:
  	app/View/Layouts/default.ctp
- :q. [iglocska]
- Revert "Merge branch 'master' into develop" [iglocska]

  This reverts commit fbe2eddc7ac1cc6038196d4b1c497fe84eee532e, reversing
  changes made to b59965b971aa8216b3fa65e9dd8881be74a4a0a5.
- Merge branch 'master' into develop. [iglocska]

  Conflicts:
  	INSTALL/MYSQL.sql
  	app/Controller/EventsController.php
  	app/Model/Attribute.php
- Merge pull request #199 from Xen0ph0n/patch-3. [iglocska]

  Issue Exporting Events as IOC's when not SiteAdmin
- Tweak to allow IOC Export of events you don't own but are shared.
  [Chris Clark]
- Merge pull request #1 from Xen0ph0n/patch-2. [Chris Clark]

  Error When Exporting as IOC if not Site Admin
- Error When Exporting as IOC if not Site Admin. [Chris Clark]

  Fixed Syntax error if not site admin.. also fix in event component which was comparing wrong values to establish ownership of event
- Error When Exporting as IOC if not Site Admin. [Chris Clark]

  This was comparing the wrong value to the event org to determine org membership and thus $isMyEvent value for privileges for export of IOCs if not a site admin.
- Merge branch 'hotfix-2.1.33' [iglocska]
- Few minor tweaks. [iglocska]
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Merge pull request #197 from Xen0ph0n/master. [iglocska]

  Update to allow clean entry of Whitelist Items
- Update to allow clean entry of Whitelist Items. [Chris Clark]

  Updated this along with whitelist.php to allow for simple entry of names in the whitelist, this file will allow proper application of those blocked names to exported NIDS sigs.
- Update to allow clean entry of Whitelist Items. [Chris Clark]

  Added non alpha delimiters hardcoded so no preg_match errors and entries in whitelist can be human redable w/out extra leading and trailing chars.
- Merge branch 'hotfix-2.1.33' [iglocska]
- Update to the GFI import. [iglocska]

  - fixed an issue where a blacklisted value added through uloadattachments would break the import

  - fixed the distribution level of attributes created by the GFI import always being your org only

  - removed registry attributes that do not contain a malware sample or a dropped file in the value

  - fixed a set of regular expressions dealing with the sanitisation of user names that would fail on user names consisting of more than one word

  - added a few regular expressions
- Merge branch 'hotfix-2.1.32' [iglocska]
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Merge pull request #195 from Xen0ph0n/patch-1. [iglocska]

  Capitalized Home in global menu... it was killing my OCD.
- Capitalized Home ... it was killing my OCD. [Chris Clark]
- Merge branch 'hotfix-2.1.32' [iglocska]
- Merge branch 'hotfix-2.1.31' [iglocska]
- Added explanation for CIDR searches to the automation page. [iglocska]
- Merge branch 'hotfix-2.1.32' into develop. [iglocska]

  - Also, added CIDR to rest searches. Make sure you use the following format:

  a.b.c.d|e

  Conflicts:
  	app/Controller/AttributesController.php
- Fix for incorrect values returned through CIDR search. [iglocska]
- CIDR searches fixes #190. [iglocska]

  - possible to use CIDR when searching attributes
- Call the TAXII client if it's enabled in configuration. [Alexandru
  Ciobanu]
- Fixed validation on Event::_add() Try atomic save for events Add
  threat level to JSON sample. [Alexandru Ciobanu]
- Replace Risk with ThreatLevel [skip ci]     - Event.risk has been
  replaced by Event.threat_level_id.       all functionality remains the
  same and users should not see       any difference.       ENUM() used
  for Event.risk is vendor specific and requires       too many hacks to
  play nicely with bake.     - Added default schema file, SQL dumps
  should be avoided since       they make updating/upgrading a pain.
  - Removed old unused schemas. [Alexandru Ciobanu]
- Basic JSON API CRUD [ci skip]     - adds JSON example to shell scripts
  - adds sample JSON event     - ??? for some redundant Attribute model
  conditions     - updates travis with CakePHP installation. [Alexandru
  Ciobanu]
- Display footer notice of missing PGP/GPG key. [Alexandru Ciobanu]
- PHP 5.4 E_STRICT fix. [Alexandru Ciobanu]
- Initial JSON REST. [Alexandru Ciobanu]

  Some small travins changes too.
  FYI there's an automated travis build available at
  https://travis-ci.org/MISP/MISP
  We don't have unit testing and travis setup is subpar so everything will fail
  for now.
- Merge branch 'hotfix-2.1.31' into develop. [iglocska]
- Fix to users with auth key access not being able to reset their
  authkey. [iglocska]
- Merge branch 'hotfix-2.1.30' [iglocska]
- First kick at Travis. [Alexandru Ciobanu]
- Post merge changes. [iglocska]

  - some changes to remove strict messages caused by an update to cakephp

  - added missing changes to the sql files - all changes from the merge are reflected in ROLECHANGE.sql, import that to upgrade your instance!
- Merge branch 'feature/discussion' into develop. [iglocska]
- Update to the discussions. [iglocska]

  - Moved the menues out of the views to the common menu element
- Some minor changes. [iglocska]

  - Contextual comments added to all imports (GFI, ThreatConnect, OpenIOC)

  - Some minor fixes to OpenIOC exports and linebreaks in attributes
- Contextual comments. [iglocska]

  - Attributes now have a comment field
- Renamed the .sql file used to upgrade. [iglocska]
- Merge remote-tracking branch 'origin/feature/XML_and_UI' into
  feature/discussion. [iglocska]

  - Also some improvements to the shadow attributes

  - some minor UI changes

  Conflicts:
  	app/Controller/EventsController.php
  	app/View/Elements/global_menu.ctp
  	app/View/Layouts/default.ctp
- Small changes after merging the two feature branches. [iglocska]

  - Update to the representation of the new permission flags

  - some small issues with the merge resolved
- Files left off added. [iglocska]
- Merge branch 'feature/roleChanges' into feature/XML_and_UI. [iglocska]

  Conflicts:
  	app/Controller/UsersController.php
  	app/View/Regexp/admin_add.ctp
  	app/View/Regexp/admin_edit.ctp
  	app/View/Regexp/admin_index.ctp
  	app/View/Roles/admin_add.ctp
  	app/View/Servers/add.ctp
  	app/View/Servers/edit.ctp
  	app/View/Servers/index.ctp
  	app/View/Servers/pull.ctp
  	app/View/Servers/push.ctp
- First rework of the siteadmin role. [iglocska]

  - ADMIN org removed.

  - Siteadmins are now identified by the perm_site_admin flag

  - Siteadmins can now be of any organisation

  - editing the regexp / whitelist rules can now be done by a special user with the perm_regexp_access in his/her role

  - Executing a mass replace of attribute values based on the regexp rules cannot be initiated by a regexp/whitelist user, only by a site admin

  - If the login page is reached without any users / roles defined they are automatically created (perviously it was only the user that was created)

  - Org admins are restricted from assigning perm_site_admin, perm_sync and perm_regexp_access roles to users. This can only be done by a site admin.
- Few more changes. [iglocska]

  - some views didn't have the menu element yet
- Further work on the UI. [iglocska]

  - reworked almost all of the side menues to be centralised

  - Some fixes for the IOC export not handling two new-ish types correctly

  - Some changes to the menues (including a few options that didn't exist before)

  - rework of the popovers in some forms
- Merge branch 'develop' into feature/XML_and_UI. [iglocska]
- First revision of the unified menu and XML upload. [iglocska]

  - centalising the side menu for easier maintainability

  - XML upload of event(s) from the interactive interface
- More changes to the discussion boards. [iglocska]

  - quote / event tags

  - anonymised e-mail addresses
- Merge branch 'develop' into feature/discussion. [iglocska]

  - Pivots, attributes, discussions hideable

  Conflicts:
  	app/Controller/EventsController.php
  	app/webroot/css/main.css
- SQL template changes. [iglocska]
- Thread creation if it doesn't exist for an event. [iglocska]
- AJAX upgrade to the discussion board. [iglocska]

  - Quickpost without reloading the page with AJAX

  - for page changes / adding posts show an animated spinner

  - spinner div / styles available from every page (the div is located in the default layout and is hidden unless manually shown)
- Discussions. [iglocska]

  - fully working version
  - some improvements still possible (hiding discussion on demand, add/edit with ajax)
- Discussion boards. [iglocska]

  - First fully working version
  - Create threads or create a thread attached to an event
  - Add posts to threads / edit them / delete them
- First version of the event discussion UI. [iglocska]
- Merge branch 'hotfix-2.1.30' into develop. [iglocska]
- Fix to an issue that prevented attachments being uploaded with invalid
  category choices when the malware checkbox was ticked. [iglocska]

  - re-introduced the removed check for valid category / type combinations based on the checkbox and the chosen category
- Merge branch 'hotfix-2.1.29' [iglocska]
- Merge branch 'hotfix-2.1.29' into develop. [iglocska]
- Loosened the filename validation on attachments. [iglocska]

  - filenames without extensions were blocked for example
- Merge branch 'hotfix-2.1.28' [iglocska]
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Merge branch 'hotfix/docu' [Christophe Vandeplas]
- Merge branch 'hotfix-2.1.28' [iglocska]
- Merge branch 'hotfix-2.1.28' into develop. [iglocska]
- Linebreaks shown in list attributes. [iglocska]
- Merge branch 'hotfix-2.1.28' into develop. [iglocska]
- Line breaks not shown in attribute values. [iglocska]
- Merge branch 'hotfix/docu' into develop. [Christophe Vandeplas]
- Quickstart in docu. [Christophe Vandeplas]
- Merge branch 'hotfix-2.1.27' [iglocska]
- Merge branch 'hotfix-2.1.27' into develop. [iglocska]
- Small cosmetic fix. [iglocska]

  - fixed a cosmetic issue with 3+ digit ID numbers, an event info with wide characters can cause the pivot element to flow over into a second row.
- Merge branch 'hotfix-2.1.26' [iglocska]
- Quick fix for the export changes. [iglocska]

  - pass by references on method calls removed
- Merge branch 'feature/IDSsuri' into develop. [Christophe Vandeplas]
- Snort export, updated urls, new url is backwards compatible.
  [Christophe Vandeplas]
- NIDS - fixes issue from last commit. [Christophe Vandeplas]
- NIDS - substitute illegal chars, improved some rules. [Christophe
  Vandeplas]
- Performance improvements in email and dns. rule for user agent.
  [Christophe Vandeplas]
- Improvements in the email NIDS rules. [Christophe Vandeplas]
- Improved smtp rules. [Christophe Vandeplas]
- Start of different structure for multiple rule-formats. [Christophe
  Vandeplas]
- Merge branch 'hotfix-2.1.26' into develop. [iglocska]

  Conflicts:
  	app/Controller/AttributesController.php
- UI fixes. [iglocska]

  - popover effect in IE/Chrome not as annoying anymore
  - only the active select will have a popover, clicking away destroys it

  - Added popovers to the add attachments instead of the old info fields
- Merge branch 'hotfix-2.1.25' [iglocska]
- Small fix to the layout. [iglocska]

  - left menu would move along horizontally when forced to scroll left and right on lower resolution screens / smaller windows

  - small script that keeps the left menu at the left edge of the page as opposed to the left edge of the window
- Merge branch 'hotfix-2.1.24' [iglocska]
- Change to the attribute download method. [iglocska]

  - Permissions weren't checked correctly when downloading attachments
- Merge branch 'hotfix-2.1.23' [iglocska]
- Merge branch 'feature/searchapi' into develop. [iglocska]
- Some permission issues with restSearch of an event. [iglocska]

  - __fetchEvent used, which checked the currently logged in user

  - instead now, __fetchEvent has a new optional parameter that automation methods can use to pass the org along that was read from the provided auth key
- Merge branch 'feature/searchapi' into develop. [iglocska]
- Fix to the conditions when doing a restsearch. [iglocska]

  - Was always searching for 'value' due to a bug. Fixed.
- Merge branch 'feature/searchapi' into develop. [iglocska]
- Update to the automation description. [iglocska]

  - Syntax description for the new features
- Merge branch 'feature/searchapi' into develop. [iglocska]
- First release of the new API features. [iglocska]
- Security fix and new download attachment feature. [iglocska]

  - users can now download attachments using the APIkey

  - security issue fixed where a user could download attachments that he/she can't even see by navigating to attributes/download/<attribute_id>
- First round of implementations for the new API searches. [iglocska]

  - users can search RESTfully for attributes based on various filtering mechanisms and get either an event that includes the located attribute(s) or just an array of attributes returned.

  - users can also request all attributes of a (or several) types and get them returned as an XML
- First version of the api search. [iglocska]

  - requires the auth key of a user and the user has to have auth key permission

  - user can specify what should be returned (event / attribute) - currently only event is implemented

  - user can specify 4 filters (value, type, category, org)

  - all these fields can have several values separated by &&

  - Values can be negated by putting "!" infront of them
- Merge branch 'hotfix-2.1.23' into develop. [iglocska]
- Fix to the download of attribute search results as XML. [iglocska]

  - now uses the unified __fetchEvent method to retrieve the events

  - __fetchEvent has a new optional parameter "idList" which restricts the results to an array of event IDs.
- Merge branch 'hotfix-2.1.22' [iglocska]
- Merge branch 'hotfix-2.1.22' into develop. [iglocska]
- Fix to the exports not working since the new pivoting. [iglocska]

  - Helper echoed a blank line, breaking the xml export

  - Helper will now only be called during view when it's not a rest request.
- Merge branch 'hotfix-2.1.21' [iglocska]
- Merge branch 'hotfix-2.1.21' into develop. [iglocska]
- Accidental debug removed. [iglocska]
- Merge branch 'hotfix-2.1.21' into develop. [iglocska]
- Change to the proposal list. [iglocska]

  - removed own proposals from the list
  - allowing site admin to see all proposals of any org
- Merge branch 'hotfix-2.1.19' [iglocska]
- Merge branch 'hotfix-2.1.20' [iglocska]
- Merge branch 'hotfix-2.1.19' into develop. [iglocska]
- Debug info removed. [iglocska]
- Merge branch 'hotfix-2.1.19' into develop. [iglocska]
- Previous commit fixed. [iglocska]
- Merge branch 'hotfix-2.1.20' into hotfix-2.1.19. [iglocska]
- Merge branch 'hotfix-2.1.19' into develop. [iglocska]
- Fixed a case that could cause overlapping pivot elements to appear.
  [iglocska]

  - The height calculation did not take into account gaps between child elements caused by them having several children. This caused a newly added sibling's children to overlap. Fixed by compensating for the vertical displacement between children when returning the height data.
- Merge branch 'hotfix-2.1.20' into develop. [iglocska]
- Fix to the related attributes. [iglocska]

  - related atributes were flowing into the next field if there were too many to fit the 5% width

  - hovering over a related attribute caused a misaligned tooltip to appear and block the link itself on IE
- Merge branch 'hotfix-2.1.19' [iglocska]
- Merge branch 'hotfix-2.1.19' into develop. [iglocska]
- Delete button gone from pivot elements that should not be deleted.
  [iglocska]

  - When looking at an event, a user should not be able to delete the pivot path that he/she took to get to that particular event.

  - Deleting the root pivot item is an exception, this will simply reset the pivoting.
- Merge branch 'hotfix-2.1.19' into develop. [iglocska]
- Height adjustment was not cummulative. [iglocska]

  - inserting a branch to a previous sibling only pushed the next sibling down a line, not the following one. Fixed.
- Merge branch 'hotfix-2.1.19' into develop. [iglocska]
- Fix to removing the root element causing issues with pivoting.
  [iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Typo fixed (missing comma) between 2 attributes. [Alexandre Dulaunoy]
- New attributes added to the shadow attributes. [Alexandre Dulaunoy]

  sha256, http-method, named-pipe and mutex added to the
  shadow attributes. Fixing #170

  This is not solving the core issue of having duplicate
  attributes declaration in MISP but this is fixing the
  consistency issue between attributes and shadow attributes.
- Merge branch 'hotfix-2.1.19' into develop. [iglocska]
- Finished the first version of the new pivoting. [iglocska]

  - Users can go back to a previous event and branch the pivoting by choosing a new relation

  - users can remove individual pivoted branches
- Further work on the pivoting. [iglocska]

  - still has some issues with arranging the height for some branching
- Heights / depths calculated for rearranging the pivot thread in view.
  [iglocska]

  - The idea is to draw a horizontal path instead of a vertical one
- First refactoring of the pivoting. [iglocska]
- Merge branch 'hotfix-2.1.18' [iglocska]
- Merge branch 'hotfix/2.1.18' [Christophe Vandeplas]
- Merge branch 'hotfix-2.1.18' into develop. [iglocska]
- Deleting attributes deletes associated shadow attributes. [iglocska]

  There was a bug causing "zombie" shadowattributes to stay in events if the attribute has been deleted
- Merge branch 'hotfix-2.1.18' into develop. [iglocska]
- Menu change. [iglocska]

  - added link to view the proposals
- Merge branch 'hotfix-2.1.18' into develop. [iglocska]
- Two files left off. [iglocska]
- Merge branch 'hotfix-2.1.18' into develop. [iglocska]
- Fixes to the Shadow attribute e-mailing. [iglocska]

  - E-mail locks are now correctly reset by discarding / accepting a proposal

  - Also, new index page to see the list of proposals that a user can accept
- Merge branch 'hotfix/2.1.18' into develop. [Christophe Vandeplas]
- Fix bug in pull updated events, improved performance. [Christophe
  Vandeplas]
- Merge branch 'hotfix-2.1.17' [iglocska]
- Merge branch 'hotfix-2.1.17' into develop. [iglocska]
- Left-over line removed. [iglocska]
- Merge branch 'hotfix-2.1.17' into develop. [iglocska]
- Small cleanup. [iglocska]
- Attachments correctly exported with events/view/1.xml now. [iglocska]

  - bug that broke transfer of attachments on pull fixed

  - data only exported on view() not mass xml exports
- Merge branch 'hotfix-2.1.15' [iglocska]
- Merge branch 'hotfix-2.1.15' into develop. [iglocska]
- Export fixes. [iglocska]

  - conversion of the array in the XML export to be compatible with the XML parser (some invalid characters could break it)

  - New separate CSV export that includes all visible unpublished and non IDS signature attributes on request
- A fix to the csv export. [iglocska]
- Merge branch 'hotfix-2.1.15' into develop. [iglocska]
- Fix to a typo causing exports to fail. [iglocska]
- Merge branch 'hotfix-2.1.14' [iglocska]
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Fix version number master. [Christophe Vandeplas]
- Merge branch 'hotfix-2.1.14' [iglocska]
- Merge branch 'hotfix-2.1.14' into develop. [iglocska]
- Removed a left-over junk line from the shadow attribute controller.
  [iglocska]
- Merge branch 'hotfix-2.1.14' into develop. [iglocska]
- Fix to sync users being able to edit events that don't belong to them
  interactively. [iglocska]
- Merge branch 'hotfix-2.1.13' [iglocska]
- Merge branch 'hotfix-2.1.13' into develop. [iglocska]
- Removed vulnerability and comment from correlation. [iglocska]
- Merge branch 'hotfix-2.1.12' [iglocska]
- Merge branch 'hotfix-2.1.12' into develop. [iglocska]
- Final change to the placement of the logos on the login page.
  [iglocska]
- Merge branch 'hotfix-2.1.12' into develop. [iglocska]
- Small alignment fix again. [iglocska]
- Merge branch 'hotfix-2.1.12' into develop. [iglocska]
- Small alignment change. [iglocska]
- Merge branch 'hotfix-2.1.12' into develop. [iglocska]
- Added second logo to the left of the login screen. [iglocska]
- Merge branch 'hotfix-2.1.8' [iglocska]
- Merge branch 'hotfix-2.1.11' [iglocska]
- Merge branch 'hotfix-2.1.8' into develop. [iglocska]
- A previous change reverted by accident in the previous commit.
  [iglocska]
- Merge branch 'hotfix-2.1.8' into develop. [iglocska]
- Upgrade script for 2.1.8. [iglocska]

  - we have introduced the "locked" flag for events to protect events of the original creator from being edited by a sync user

  - IMPORTANT: before running the script below, make sure to create the locked field for the event table (see INSTALL/LOCKED.sql)

  - This script (generateLocked found in the Administrative tools menu) will attempt to set the locked value for existing events to ease the transition

  - The default value for locked is 0, and all events created on the instance should be set to this value

  - events that were synced from another instance should have their locked value set to 1

  - this script checks for local organisations and sets the locked field to 1 for all events not created by them

  - a local organisation, as defined for the scope of this scrips is: an organisation with at least 2 members or an organisation with a single member that is not a sync user.

  - The script is only accessible by site admins and will return a notification about the number of events altered.
- Merge branch 'hotfix-2.1.11' into hotfix-2.1.8. [iglocska]
- Update to the MYSQL.sql file to reflect the 'locked' changed.
  [iglocska]
- Introduced a typo in the previous commit. [iglocska]
- Further updates to the sync. [iglocska]
- Merge branch 'hotfix-2.1.11' into develop. [iglocska]
- Fix to the e-mailing. [iglocska]
- Merge branch 'hotfix-2.1.11' into develop. [iglocska]
- Small fix to the previous commit. [iglocska]
- Merge branch 'hotfix-2.1.11' into develop. [iglocska]
- Changes to the shadow attribute controller. [iglocska]

  - users that weren't publishers couldn't accept / discard proposals

  - emails were blocked by an incorrect debug mode for the e-mailer
- Some smaller fixes. [iglocska]

  - PGP key of the user shown in the profile instead of always showing N/A

  - Contact e-mails now include the instance's owning org in the subject

  - Users can now enable/disable contact e-mail subscriptions
- Merge branch 'hotfix-2.1.10' [iglocska]
- Merge branch 'hotfix-2.1.10' into develop. [iglocska]
- Users weren't able to change the contactalert field. [iglocska]
- Merge branch 'hotfix-2.1.9' [iglocska]
- Merge branch 'hotfix-2.1.9' into develop. [iglocska]
- Fix to not being able to accept shadowAttributes. [iglocska]

  - recursive -1 used for loading attribute, then referencing the event
- Merge branch 'hotfix-2.1.7' [iglocska]
- Vulnerability url is now configurable (Fix #153). [Alexandre Dulaunoy]

  A global configuration CyDefSig.cveurl added to specify the URL
  where to reference a CVE/NVD number. CyDefSig.cveurl is optional
  and if not existing fallbacks to the original google.com URL.
- Attribute http-method added - issue #161 fixed. [Alexandre Dulaunoy]

  The attribute HTTP method added. By default, the values
  must match the known HTTP method from RFC2616, RFC2518,
  RFC3253, RFC3648, RFC3744, RFC5789, RFC5323. The method
  is case sensitive.
- Terms and conditions separated from the template. [Alexandre Dulaunoy]

  If a file terms exists in app/View/Users, the terms are included.
  If not, the default message is included to inform the admin. This
  avoids to overwrite local terms when updating MISP code.
- Merge branch 'hotfix-2.1.7' into develop. [iglocska]
- Fix to the distribution changes breaking threatconnect imports.
  [iglocska]
- Merge branch 'hotfix-2.1.6' [iglocska]
- Merge branch 'hotfix-2.1.5' [iglocska]
- Merge branch 'hotfix-2.1.6' into develop. [iglocska]
- Changes to the initial distribution settings. [iglocska]

  - The initial attribute distribution level now allows the option for 'event', inheriting the event's distribution level
- Merge branch 'hotfix-2.1.5' into develop. [iglocska]
- Attributes won't show two links to the same event anymore on the event
  view. [iglocska]
- Merge branch 'hotfix-2.1.4' [iglocska]
- Merge branch 'hotfix-2.1.4' into develop. [iglocska]
- Fix to incorrect distribution setting in the openIOC importer.
  [iglocska]
- Merge branch 'master' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Merge branch 'hotfix-2.1.3' [iglocska]
- Typographic errors fixed in automation page. [Alexandre Dulaunoy]
- Trailing ":" removed from title page template. [Alexandre Dulaunoy]
- Merge branch 'hotfix-2.1.3' into develop. [iglocska]
- Default distribution level flags in bootstrap.php. [iglocska]

  - Each instance can now have its own default event and attribute distribution level set
- Merge branch 'hotfix-2.1.2' [iglocska]
- Merge branch 'hotfix-2.1.2' into develop. [iglocska]
- Set the default value of the flag disabling rest alert messages to
  false. [iglocska]
- Merge branch 'hotfix-2.1.1' [iglocska]
- Merge branch 'hotfix-2.1.1' into develop. [iglocska]
- Notification on rest add of published events. Fixes #138. [iglocska]
- Merge branch 'develop' into 'master' for v2.1. [Christophe Vandeplas]
- Pivot thread changed slightly. [iglocska]

  - There is a reset button in the first arrow

  - adding an event that exists already in the list should not create a new pivot point
- Jumping between pivot thread points changed. [iglocska]

  - no longer adds the event to the thread
- Fixed the CSS issues with the pivot thread. [iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [Christophe Vandeplas]
- Incorrect mutex validation fixed. [iglocska]
- Pivot threads and other changes. [iglocska]

  - Users can now see the path they took while jumping from related event to related event

  - Removed the breadcrumbs

  - Some UI changes (user menues were not showing the active page, etc)
- Updated README.md. [Christophe Vandeplas]
- Crumbs not shown on error messages. [iglocska]
- Change to the routing the login to remove the admin tag. [iglocska]
- Removed the breadcrumbs from the login page. [iglocska]
- Accidental change to gitignore reversed. [iglocska]
- File left off from previous commit. [iglocska]
- Breadcrumbs for the views. [iglocska]

  - makes navigating the site easier
  - some new css changes to support this
- Fixes to the openIOC import tool. [iglocska]

  - should handle nested OR branches better now
  - domain now mapped to Network/DNS
- Fixes #144, the edit page losing the previous setting. [iglocska]
- Change to the confusing invalid event message. [iglocska]
- Changes to the filename validation. [iglocska]

  - . allowed in filenames to allow for names such as test-1.0.ext
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Version 1.0 of MISP XML Document Type Definition. [Alexandre Dulaunoy]

  The first version of the XML format is loosely based on the current XML
  format used by MISP in commit 84b552fb7441bf2beb0c711acde3b0af336afba8.

  The purpose is to track down the changes in the format and especially
  to ensure a consistent definition of the XML format for external tools
  and software using the MISP XML format.
- IOC file import filename regex fix. [iglocska]

  - Didn't account for several words separated by '.'-s (file.name.ext)
- Migration script updated with the regexp changes. [iglocska]
- Fixes an issue with the upload of malware samples not generating an
  md5 hash if the file is too large. [iglocska]
- Removed password creation for new users through the contact users
  menu. [iglocska]
- Discard shadowattribute changed to Postlink. [iglocska]

  - Prevents deletion through XSRF
- Fixed an issue with siteadmin contact e-mails resetting passwords of
  non existing users. [iglocska]

  - a site admin could issue a password reset to a non-existing user
- Fixed a newly created bug in memberslist. [Christophe Vandeplas]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Memberslist based on orgc, is more logic to reflect the contributions.
  [Christophe Vandeplas]
- Minor NIDS export performance improvement. [Christophe Vandeplas]
- Some bugs fixed. [iglocska]

  - Resetting the auth key for a user that doesn't exist created an empty
  user

  - change_pw showed an admin menu on the side

  - rerouting after an incorrect auth request fixed (users/index doesn't
  exist)

  - temporarily disabled the redirect after login
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Fixes XSS vulnerability in filters. [iglocska]
- Fixes in server push. [Christophe Vandeplas]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [Christophe Vandeplas]
- Server push lower memory footprint solving OoM problem. Enabled per-id
  push like pull. [Christophe Vandeplas]
- More logging with PGP errors. [Christophe Vandeplas]
- Initial refactoring of the event view / xml exports. [iglocska]

  - event view and xml exports all use __fetchEvent now

  - unified the permission checks

  - same output for event/id.xml and the xml exports
- Minor change with shadowattributes. [iglocska]

  - short was still used on the shadow attribute value field, if the
  shadow attribute was a proposal to the event itself and not to an
  attribute
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Reverted commit of url validation that didn't validate parts of urls.
  [Christophe Vandeplas]
- Fixing problems in pull with distribution data validation. [Christophe
  Vandeplas]
- Removed TODO. [Christophe Vandeplas]
- Some css changes broke the shadow attributes. [iglocska]

  - should be fixed
- Change of domain type in IOC Export fixes #134. [iglocska]
- OpenIOC issue. [iglocska]

  - Attribute type domain exported into the wrong ioc term.
- Security issue fixed with UsersController. [iglocska]

  - users could view other user profiles

  - users could view other user profiles through edit user
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Leftovers from communitie/cluster/... [Christophe Vandeplas]
- Removed quotation marks from csv export. [iglocska]

  - Not needed, linebreaks are removed anyway
- Import ThreatConnect attributes into event, see issue #119.
  [Christophe Vandeplas]
- Fixes in data validation. [Christophe Vandeplas]
- Revert "fix bug in removing remote attributes if push is not enabled"
  [Christophe Vandeplas]

  This reverts commit c4d5344153a7f183372f3acbc703e6bfcb57e23e.
- Fix bug in removing remote attributes if push is not enabled.
  [Christophe Vandeplas]
- Cleanup: hidden functions to _function and removed unnecessary
  function. [Christophe Vandeplas]
- Minor admin tools improvements. [Christophe Vandeplas]
- Huge performance increase in generateCount. [Christophe Vandeplas]
- Fixes bug introduced in commit
  2334599f3d460c4371597dc336749bebded459de. [Christophe Vandeplas]
- Minor UI glitch in IOC/IDS naming. [Christophe Vandeplas]
- Do not change 'info' field upon pull (was: Imported from $url)
  [Christophe Vandeplas]
- Fixes #133. [Christophe Vandeplas]
- Redirects to filtered events page upon delete. [Christophe Vandeplas]
- UI improvement on private event/attribute. [Christophe Vandeplas]
- Removal of some references to the old private flag. [iglocska]
- Re-enabled route from /admin/users/login to /users/login. [iglocska]

  - when an admin user got logged out the system threw an error instead of
  returning him/her to the login screen
- Slight colour change for the private background colouring. [iglocska]
- Some UI changes and reattached the regexp for the admin validation
  tool. [iglocska]

  - org only events have a redish background in the event index

  - org only events and attributes have their distribution level marked in
  red
- Must be sleepy...holliday effect? [Christophe Vandeplas]
- Fixes bug in previous commit. [Christophe Vandeplas]
- Improved password generation algorithm in reset password. [Christophe
  Vandeplas]
- Corrections in the documentatino. [Christophe Vandeplas]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- 'type' same size in regexp than in attribute. [Christophe Vandeplas]
- Minor change in reportValidationIssueAttributes() [Christophe
  Vandeplas]
- First refactoring of the regexp. [iglocska]
- Some cleanup. [iglocska]

  - removal of references to the old blacklist
- MYSQL.sql change left off from regexp changes. [iglocska]
- Change to the GFI import and the attachment downloads. [iglocska]

  - GFI import issue fixed with attribute ID 1 not existing causing the
  import to fail for several attributes

  - GFI import change: registry keys with binary value are now artifacts
  dropped instead of persistance mechanism

  - GFI import change: files with size of 0 will be omitted

  - file attachment download change: moved away from the deprecated media
  view in favour of cakeresponse->file()
- Some UI fixes related to the debug/nondebug alignment. [iglocska]
- Regexp type changes also for non ADMIN users. [iglocska]

  - left the view for them off in the previous commit
- Continued rework of the regexp. [iglocska]

  - Regular expressions are now only checked for attributes

  - Regular expressions are now defined and checked on a type by type
  basis, with the setting "ALL" affecting all attributes

  - creation / deletion of several attributes in one edit to accommodate
  for several checked type options

  - perform on all admin option now only saves attributes that actually
  get changed by the regexp, making the function usable again for larger
  databases

  - Some feedback on what got changed during a perform on all

  - UI changes in the index / regexp add / edit views to reflect the type
  sensitivity changes
- Removal of the blacklist. [iglocska]

  - Since regexp can be used to blacklist things, there's no need to have
  two separate features that accomplish the same thing

  - Add a regexp named /1.1.1.1/ with nothing as replacement and it will
  behave the same as adding a blacklist for 1.1.1.1 in the old system.
- Bug in a previous commit. [iglocska]

  - left in some debug used to escape php encryption during testing
- Attribute index UI bug fixed. [iglocska]
- Regexp changes, UI changes. [iglocska]

  - first cleanup of regexp

  - some changes left off from the UI changes that were not in the views
  themselves
- UI changes applied to the actions menu. [iglocska]

  - The side menu is now fixed / relatively positioned based on the debug
  mode, like the header and the footer.
- Some changes to the UI. [iglocska]

  - The previous UI changes fixed the top and the bottom bar to the
  viewport

  - It was great for the UI with the debug disabled, but it obstructed the
  debug info with it on

  - now, turning debug off fixes the top bar and the bottom bar, turning
  it on returns it to the top and bottom of the page, as it was in earlier
  versions
- Footer download GPG Z-index changes. [iglocska]

  - GPG key download was behind the layer for the center footer,
  preventing the user from clicking the download link. Fixed.
- Some more HTML fixes. [iglocska]
- HTML error fix. [iglocska]

  - div id starting with a digit (the id wasn't needed anyway so removed
  it)
- HTML error fixed. [iglocska]

  incorrect span in ul
- Some small UI changes. [iglocska]
- Cosmetic relocation of the auth errors on the login screen. [iglocska]
- Small change to the flash messages. [iglocska]

  - fixing it to the same position
- Footer.ctp left off of the previous commit. [iglocska]
- Changes to the UI. [iglocska]

  - login screen looks a bit fancier and is more customisable
  - admins can add a Logo next to the login fields, there's a MISP logo
  ontop with a line of text above and below it, editable via bootstrap.php
  - Footer re-added, has the PGP key download and the center footer text
  from MISP 1.1
  - A logo on the right side of the footer, optionally added by
  bootstrap.php

  - Header, Footer, menu are now fixed and not affected by scrolling the
  screen
- Change to the login screen. [iglocska]

  - Places an optional logo to the left
  - MISP logo above the login fields, with an optional pre and post text

  - define them in the bootstrap as indicated in bootsrap.default.php
- Hard coded urls for the event index. [iglocska]

  - Should provide a tiny performance boost
- Several fixes. [iglocska]

  - Fixed the search pagination beyond the first page

  - Hard coded routing of the menues in the global actions area
- Several copy paste failures fixed in the previous commit. [iglocska]

  - /facepalm
- ACL checks changed. [iglocska]

  - until now checkAction was used to check permissions of a user

  - but since all of the role permissions are checked beforefilter in
  appcontroller and saved into a public array, doing a lookup of the
  array saves an SQL call for each permission check.
- Closes #131. [iglocska]

  - Seems like a change removed this functionality since 2.0, fixed
- Fix to users not being able to edit attributes. [iglocska]
- IOC -> IDS name change for attribute index. [iglocska]

  - also for attribute add and edit
- Small change to the xml search download. [iglocska]
- Search result downloads (CSV format) [iglocska]

  - added the button for the CSV download
  - fixed a bug with the csv search result downloader blocking non IOC
  results even if the search terms did not specify IOCs only.
- Some cleanup on the views. [iglocska]
- Some UI changes. [iglocska]

  - Signature / IDS Signature changed to IOC
- Bugfix for the creation of several attributes with the same UUID.
  [iglocska]

  - SHA256 and SHA1 hash attributes that get auto-generated on malware
  sample upload had the same hash as the filename|md5. Fixed.
- Views updated to include CSV in the menues. [iglocska]

  - CSV and also IOC downloads on events are now hidden if the event is
  not published
- Update to the exports. [iglocska]

  - export page updated to include the CSV export

  - some changes to the CSV export and incorrect handling of data for
  admins
- More changes to the whitelists, exports. [iglocska]
- To_ids turned off on attribute creation by default. [iglocska]
- Firther work on the exports. [iglocska]

  - Some refactoring of the whitelist checks
  - tighter rules for published / to_ids on certain exports
  - attribute search now has the IOC checkbox
- Changes to export validation, CSV export, Whitelist redesign.
  [iglocska]

  - CSV export for individual events, all events, search results
  - Whitelists are now preg_matches instead of simple string matches
  - whitelist checks are to be applied on almost all exports
  (implementation in progress)
  - the exception will be the search result exports, if the (to be
  implemented) to_ids only checkbox isn't checked
- Width + height, should be fixed (event index images) [iglocska]
- Small part left off from the previous commit.. [iglocska]
- Overriding the css that's blocking the size change. [iglocska]

  - on the event index
- Typo fixed. [iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Solves memory exhaustion upon generateCorrelation. [Christophe
  Vandeplas]
- Some UI changes. [iglocska]

  - removed the e-mail for non site admins from the event index (they can
  still see it in the event view if the event was created by the same org)

  - added a text MISP logo

  - smaller icons for the event index
- Merge branch 'feature/sync/timestamp' into develop. [Christophe
  Vandeplas]
- A. [Christophe Vandeplas]
- Minor changes. [Christophe Vandeplas]
- Page for admin with some links. [Christophe Vandeplas]
- Grouped documentation. [Christophe Vandeplas]
- Removed warning message. [Christophe Vandeplas]
- Update to the attribute search. [iglocska]

  - Use ! to exclude terms in the value/id/org fields

  - org search works the same way as value / id now, you can enter several
  terms separated by a newline. Also, adding ! infront of a term will
  exclude the organisation from the results

  - sub string search for organisations
- Consistency in MYSQL database file. [Christophe Vandeplas]
- Unify db schema. [Christophe Vandeplas]
- Filter logic reworked. [iglocska]

  - Affects org and info field

  - terms have to be saparated by pipe (|)

  - terms can be terms that will be OR-d or excluded terms that will be
  AND-ed

  - to exclude a term use !

  - A valid filter search for info would be: 'term1|term2|!term3'
  -> this would result in all events with the info field containing term1
  or term2 but not term3
- NOT filter for orgs on the event index. [iglocska]

  - entering for example '!futuremark' would exclude all events created by
  the organisation 'futuremark'
- Email addresses of event creators visible to users if same org.
  [iglocska]

  - On the event index, users can view the e-mail address of the event
  creator, if the event belongs to their own organisation
- Some fixes to the filters event index. [iglocska]

  - siteadmins can now search the creator org instead of the owner org
  (like normal users would)

  - Changed the org search to be a partial match instead of an exact match
- Two small changes. [Iglocska]

  - email of the user creating an event shown if current user's org ==
    event's orgc

  - on export, the check for to_ids will happen outside of the if branch
    that sets extra restrictions of non site admins. Otherwise site-admins
    would accidentally include attributes that aren't iocs.
- Fix to the filters on IE. [Iglocska]

  - old versions of IE didn't handle an incorrect form creation as gracefully as the other browsers

  - forms should not be created within a table unless it's within a <td> (it was
    on <tr> level before). The normal solution would be to encapsulate the
    entire table in a form, but since we have formlinks for the deletes /
    publishes this would get flagged as form tampering by the security
    components.

  - As a fix, filter forms are created separately for the 4 search fields within their <td> now with hidden fields that keep the persistence of the previously
    entered filter terms
- Incorrect line removed from migration. [iglocska]
- Update to the migration. [iglocska]
- First update to the SQL scripts. [iglocska]
- Wrong file included in previous commit. [iglocska]
- ShadowAttribute notifications, and some minor fixes. [iglocska]

  - New field for events, locking an event from sending out a contact
  e-mail when a proposal is made to it
  - Default setting for the new field is 0, if a shadow attribute is
  added an e-mail is sent to all subscribing members of the orgc and the
  new field is set to 1
  - Accepting a change resets the field to 0
- Extra access control restriction for reportValidationIssues.
  [iglocska]
- Merge branch 'feature/sync/timestamp' of https://github.com/MISP/MISP
  into feature/sync/timestamp. [iglocska]
- Micro cleanup of servers index. [Christophe Vandeplas]
- ReportValidationIssues function. [Christophe Vandeplas]
- Fix UI issue of top bar. [Christophe Vandeplas]
- First start of report functions. see issue #122. [Christophe
  Vandeplas]
- Little bit more details about sync errors. [Christophe Vandeplas]
- Shows spaces in attribute value. fixes #19. [Christophe Vandeplas]
- Sanitisation of the data when generating .ioc file. [iglocska]
- Login url won't include /admin/ anymore. [iglocska]

  - routing issue fixed
- Addition of the Event History. [iglocska]

  - uses the logs to generate a list of actions affecting the selected
  event and all of its attributes

  - view is very minimalistic, not to show anything restricted
- Sync pull backwards compatibility with MISPv2. [Christophe Vandeplas]
- (workaround) better error message when HTTP problem with Server Pull.
  [Christophe Vandeplas]
- UI consistency. [iglocska]
- Several smaller changes. [iglocska]

  - Fix to the proposed attribute edit that got broken in a previous
  commit

  - Fix to the org filters for non admin users

  - Some changes to the documentation
- More updates to the manual. [iglocska]
- Some UI changes and partial update to the manual. [iglocska]
- Added 2 new type of attributes. [iglocska]

  - sha256 / filename|sha256
  - uploading a malware sample now automatically creates a filename|sha1
  and a filename|sha256 in addition to the sample|md5
- Fix incorrect order of checking user info (with REST authkey)
  [Christophe Vandeplas]
- Fix MYSQL missing ; [Christophe Vandeplas]
- Merge branch 'feature/sync/timestamp' of https://github.com/MISP/MISP
  into feature/sync/timestamp. [Christophe Vandeplas]
- Reference to maxDist removed in the attribute edit view. [iglocska]

  - obsolete
- Removed some obsolete code. [iglocska]

  - canEditDist is obsolete, removed some more references to it
- Bug fixed with event creation. [iglocska]

  - Previous commit unsetting new attribute IDs breaks if no attributes
  present -> fixed
- Fix bug in iocexport. [Christophe Vandeplas]
- Merge branch 'feature/sync/timestamp' of https://github.com/MISP/MISP
  into feature/sync/timestamp. [Christophe Vandeplas]
- Protection against lost attributes with saveAssociated. [iglocska]

  - attributes that are added have to have their id unset before being
  added in order to avoid overwriting existing attributes
- Fix file download missing extension. [Christophe Vandeplas]
- Merge branch 'feature/sync/timestamp' of https://github.com/MISP/MISP
  into feature/sync/timestamp. [iglocska]
- Merge branch 'feature/sync/timestamp' of https://github.com/MISP/MISP
  into feature/sync/timestamp. [Christophe Vandeplas]
- Micro improvement. [Christophe Vandeplas]
- Change to the routes. [iglocska]

  - disabling the routes to indeces with pagination throws an error when
  switching to another page
- Shadow attribute change. [iglocska]

  - fixed incorrect link to edit shadow attributes and the distribution
  checks
- Update to the publish. [iglocska]

  - _publish doesn't attempt to upload events that have a distribution of
  0 or 1 (private and community) but instead just set to published and
  return true
- Update to the IOCImprt/Export. [iglocska]

  - bringing the two components up to date with the distribution changes
- Typo in UsersController fixed. [iglocska]
- Routing and some UI changes to the users admin_index. [iglocska]
- UI changes and more work on the sync. [Iglocska]

  - updated the side menu
- Merge branch 'feature/sync/timestamp' of https://github.com/MISP/MISP
  into feature/sync/timestamp. [Iglocska]
- Minor improvements in documentation. [Christophe Vandeplas]
- Merge branch 'feature/sync/timestamp' of https://github.com/MISP/MISP
  into feature/sync/timestamp. [Christophe Vandeplas]
- Bugfix in UI. [Christophe Vandeplas]
- Pull can not edit events / attributes. [Iglocska]

  - added the _edit method in EventsController
- Merge branch 'feature/sync/timestamp' of https://github.com/MISP/MISP
  into feature/sync/timestamp. [Iglocska]
- Fix to the attribute list when not logged in. [Iglocska]

  - incorrect syntax fixed
- Small bug with view() fixed. [Iglocska]
- Some more fixes to the sync. [Iglocska]
- Merge branch 'feature/sync/timestamp' of https://github.com/MISP/MISP
  into feature/sync/timestamp. [Iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into
  feature/sync/timestamp. [Christophe Vandeplas]

  Conflicts:
  	app/View/Attributes/index.ctp
  	app/View/Events/add.ctp
  	app/View/Events/edit.ctp
- Merge branch 'feature/gui' into develop. [Christophe Vandeplas]

  Conflicts:
  	app/View/Users/memberslist.ctp
- Performance - caching of CakeRouting and url generation. [Christophe
  Vandeplas]
- UI filter of event view (forgot this file) [Christophe Vandeplas]
- Unified links. [Christophe Vandeplas]
- Improve UI of event index filtering. [Christophe Vandeplas]
- Fix documentation link. [Christophe Vandeplas]
- Performance improvement with static urls. [Christophe Vandeplas]
- Fix bug no tooltip with Chrome/IE on attributes. [Christophe
  Vandeplas]
- Fix no tooltip bug on Chrome and probably IE. [Christophe Vandeplas]
- Removed not necessary sort results in huge performance improvement.
  [Christophe Vandeplas]
- Peformance. [Christophe Vandeplas]
- UI tooltip love. [Christophe Vandeplas]
- Logos shown in memberslist. [iglocska]
- Named pipes and mutex. [iglocska]

  - added the 2 types under the artifacts dropped category
- Further changes to the degradation of the distribution. [Iglocska]
- Further work on the distribution. [Iglocska]
- Further changes to the distribution. [Iglocska]

  - changed to use the new int field
- Few changes. [Iglocska]
- New sql changes. [iglocska]
- Change to new distribution. [iglocska]

  - first stage
- Removed incorrect validation. [iglocska]
- Accidental inclusion of some debug in the previous commit. [iglocska]

  - removed
- Small bug with the highlighthelper. [iglocska]

  - ending the input with a break line will cause the highlter to fail
  - fixed
- Small change to the timestamp. [iglocska]

  - Moved the timestamp generation for attributes and events that are
  being saved and don't have one to Model->beforeValidate()
- First cleanup of AttributesController and EventsController after the
  move to timestamps. [iglocska]
- Small mistake in the previous commit. [Iglocska]
- Update to the sync. [Iglocska]

  - timestamp now correctly compared, events that have an older timestamp
    will be discarded, same with attributes

  - right now the response is the same as a successful edit though, should
    be handled more gracefully

  - pull is not yet tested

  - attachments and shadow attributes not yet implemented

  - backflow is nicely blocked by the timestamp as intended

  - needs cleanup (from, dist_change)
- Saving over night, something still blocks the timestamp from being
  saved after a push... [iglocska]
- More work on the timestamps. [iglocska]

  - Event correctly changes timestamp when attribute edited in the UI
  - Attribute correctly changes timestamp when edited in the UI

  - Still very much work in progress, several parts are not supposed to
  work yet
- First (still non-working) version of the timestamp + uuid sync.
  [iglocska]

  - timestamp field added to events and attributes (int length 11 called
  timestamp, default value 0)
  - timestamps created on add / edit when apprioriate
  - during an add, if an event/attribute is not being pushed through a
  sync with an existing timestamp, create a timestamp
  - on edit, check whether the timestamp is newer than the old one and
  only add the attribute or event then
- Bug with adding an event and the org being set incorrectly. [iglocska]
- Changes to the event filtering. [iglocska]

  - there was a bug that pushed the data entered into the "published"
  filter field to the date fields -> fixed

  - Also a bug in the serverscontroller, pulling threw an undefined
  warning from the log controller because a single saveField was used and
  the logController couldn't save the url data for the action
- Merge branch 'feature/gui' of https://github.com/MISP/MISP into
  feature/gui. [iglocska]

  Conflicts:
  	app/Controller/EventsController.php
- Fix incorrect location of loadModel for Attribute. [Christophe
  Vandeplas]
- Filters updated and some changes for the sync. [iglocska]

  - visual changes
  - date from/until fields
  - published field
  - a reset form button

  - the org of an event added by a sync user will be that of the host
  instance's own organisation identifier
- Merge branch 'feature/gui' of https://github.com/MISP/MISP into
  feature/gui. [iglocska]
- Force passwd change for admin user on creation. [Christophe Vandeplas]
- Create default admin user automatically. [Christophe Vandeplas]
- First version of the new filters on event index. [iglocska]
- Small UI change to the exports screen. [iglocska]
- Small fix to event view attribute access permissions. [iglocska]

  - Server only attributes not visible to members of another organisation
  - fixed
- Tiny cosmetic change. [iglocska]
- Merge branch 'feature/gui' of https://github.com/MISP/MISP into
  feature/gui. [iglocska]
- UI hide top links when not logged in. [Christophe Vandeplas]
- Changes to the event view. [iglocska]

  - reworked the way events are loaded and reloaded to check for
  privileges
- Slight change to the event xml output. [iglocska]

  - now includes both shadowattributes related to attributes and events
- Merge branch 'feature/gui' of https://github.com/MISP/MISP into
  feature/gui. [iglocska]

  Conflicts:
  	app/View/Events/view.ctp
- UI fix login screen. [Christophe Vandeplas]
- Merge branch 'feature/gui' of https://github.com/MISP/MISP into
  feature/gui. [Christophe Vandeplas]
- Alignment of action buttons. [Christophe Vandeplas]
- Update to the shadow attributes. [iglocska]

  - UI changes
  - changed the relationship between shadowattributes and events to be
  hasMany
- Small mistake in the previous commit. [iglocska]
- Attribute edit US change. [iglocska]
- Removed pointer change on hover for the message css class. [iglocska]
- Display related events in multiple columns. fixes #113. [Christophe
  Vandeplas]
- Merge branch 'feature/gui' of https://github.com/MISP/MISP into
  feature/gui. [iglocska]
- Sort arrows. [Christophe Vandeplas]
- More UI changes. [iglocska]
- CSS change for the flash messages. [iglocska]
- Update to the import IOC ui. [iglocska]

  - new css class for the graph
- More UI changes. [iglocska]
- Attribute type pipe and mutex. [iglocska]

  - 2 new attribute types
  - Same change as on develop
- Update to the event index view. [iglocska]
- Slight changes to the role creation and edit views. [Iglocska]
- UI changes. [Andras]
- More UI changes. [Andras]
- UI changes to event add/edit and change to events controller. [Andras]

  - updated the UI for the event add and edit views

  - change to the privileges when editing events - siteadmins could not edit
    events of other orgs.
- New forminfo tooltip and update to search attribute. [Andras]

  - added tooltip to css

  - small update to search attribute
- UI event fixes. [Christophe Vandeplas]
- UI events partial improvements. [Christophe Vandeplas]
- UI rules and users improvements. [Christophe Vandeplas]
- Merge branch 'feature/gui' of https://github.com/MISP/MISP into
  feature/gui. [Christophe Vandeplas]

  Conflicts:
  	app/View/Logs/admin_index.ctp
  	app/View/Logs/admin_search.ctp
  	app/View/Users/memberslist.ctp
- GUI changes for the user views. [iglocska]
- Merge branch 'feature/gui' of https://github.com/MISP/MISP into
  feature/gui. [iglocska]
- UI changes to the logs. [iglocska]
- UI Logs, documentation, memberslist and fixed bug in highlight.
  [Christophe Vandeplas]
- UI servers. [Christophe Vandeplas]
- UI blacklist whitelist regexp. [Christophe Vandeplas]
- UI export and automation. [Christophe Vandeplas]
- Attribute search and list. [Christophe Vandeplas]
- Hilight row. [Christophe Vandeplas]
- Minor improvements. [Christophe Vandeplas]
- Mirated first parts of nice GUI proposed by Alexandru of CERT-EU.
  [Christophe Vandeplas]
- Update to the IOC import tool. [iglocska]

  - Tries to resolve some branching to increase the number of successful
    imports

  - Moved to the event view and the import only adds attributes without
    changing the event's data itself

  - Visualisation of the original IOC, showing the successes and failures
- Fixing some REST API and XML issues. [Christophe Vandeplas]
- Quick fix for strict warning over an incorrect argument. [iglocska]

  - in adminCrudComponent
- Minor cleanup. [Christophe Vandeplas]
- Further cleanup of the REST XML output. [Christophe Vandeplas]
- Fixes information leakage vulnerability on REST XML outputs.
  [Christophe Vandeplas]
- Removed useless hop_count. [Christophe Vandeplas]
- Date issue when adding a user. [Iglocska]

  - the date for a new user was not set and defaulted to 0000-00-00 - this
  caused an issue when the user was edited and the admin was either
  prompted to change the date manually or the date was set to 2033.

  - date for newsread is now initially set to 2000-01-01
- Disabled HTML5 validation for Users/admin_add. [Iglocska]

  - the new cakephp HTML5 validation forced users to enter a GPG key under
  all circumstances. Removed.
- Strict messages fixes #99 and user edit requiring to change password
  fixes #67. [Iglocska]

  - Plugins and the user model were throwing strict messages in php 5.4+
  or with E_STRICT on php 5.3 and lower. Should be fixed.

  - New cakePHP added automatic HTML5 validation to form fields, which
  breaks fields that can alternatively be left empty to not be edited
  (such as the password field in user edits) - removed the html5 form
  validation from user edits.
- Update to the mysql.sql file. [Iglocska]

  - aros setup from earlier versions was still included. Removed.
- Further progress on the OpenIOC import. [Iglocska]

  - works fine now, but a lot of data still gets discarded
- Further work on the IOCImport. [Iglocska]

  - Also, major performance fix for the event view
- OpenIOC Importer. [Iglocska]

  - Import from .ioc
  - map to MISP attributes and insert them
  - try to resolve AND logical operators where possible, otherwise discard
- Missing images added closes #92. [iglocska]
- Fixes #88. [Iglocska]

  - events searchable by uuid
  	-> /events/view/<uuid>
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Moved fragmented massagedata to Model::beforeValidate() [Christophe
  Vandeplas]
- Added the component from the previous commit. [iglocska]
- Moved the ioc export to a component. [Iglocska]

  - Less clutter
- Further changes to the export features. [Iglocska]

  - fixed issues with some download exports not being downloaded
  - eliminated some code repetition
- Issue with event publish logs failing. [Iglocska]

  - info was not set with saveField. Fixed.
- Changes to the export conditions. [Iglocska]

  - attributes with to_ids == 0 won't be exported unless it's an XML
  export
  - Fix to a typo in the IOC export
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]

  Conflicts:
  	app/Controller/EventsController.php
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [Christophe Vandeplas]
- First minor cleanup of export #78. [Christophe Vandeplas]
- Typo with several _isSiteAdmin() calls fixed. [Iglocska]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Fix rest authentication and further auth clean up. [Christophe
  Vandeplas]
- Update to the installation instructions. [Andras Iklody]

  - to reflect the removal of the old ACL
- Removal of more remnants of the old ACL and tightening of the filename
  checks. [Andras Iklody]

  - actAs acl removed from role and user models together with some extra
  code related to the ACL

  - Fix of the filename regex as pointed out by cvandeplas.
- Further changes to the authorisation. [Andras Iklody]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [iglocska]
- Db changes for the integrated ownership. [Andras Iklody]

  - updated the MYSQL.sql file,
  	- tables aros, acos, aros_acos removed and shadow_attributes added
- Removal of the remains of the old authorization / adding new ones
  where needed. [Andras Iklody]
- Reference to a now gone method fixed. [Andras Iklody]
- Small errors with the merge corrected. [Andras Iklody]

  - some errors managed to slip through during the merge, should be fixed
- Integrated ownership, ACL and minor fixes. [Andras Iklody]

  - Orgs can propose new attributes or changes to existing attributes for
    events that they do not own

  - publishing users of the owner organisation can see, accept or discard
    them

  - Reworked the access control

  - minor fixes
- Merge branch 'feature/cleansanitize' into develop Fixes #96.
  [Christophe Vandeplas]
- Fix sanitization in AppController #96. [Christophe Vandeplas]
- Fix sanitization in AdminCrudComponent #96. [Christophe Vandeplas]
- Fix sanitization in Events #96. [Christophe Vandeplas]
- Fix sanitization in Regexp #96. [Christophe Vandeplas]
- Fix sanitization in Roles #96. [Christophe Vandeplas]
- Fix sanitization in Attributes #96. [Christophe Vandeplas]
- Fix sanitization in Users #96. [Christophe Vandeplas]
- Fix sanitization in Blacklists #96. [Christophe Vandeplas]
- Fix sanitization in Servers #96. [Christophe Vandeplas]
- Fix sanitization in Whitelist. [Christophe Vandeplas]
- Fix sanitization in Logs. [Christophe Vandeplas]
- Merge branch 'develop' of https://github.com/MISP/MISP into develop.
  [Christophe Vandeplas]
- Performance tweak. [Andras Iklody]

  - User/Role not looked up recursively anymore for authorisation checks -
    improves performance significantly. Also, checking perm_add and
    perm_modify instead of doing a lookup in the ACL tables
- Merge branch 'feature/correlation' into develop. [Christophe
  Vandeplas]
- Cleanup crappy sanitization. [Christophe Vandeplas]
- Rewrote fetching of the related events. [Christophe Vandeplas]
- Remove unused function. [Christophe Vandeplas]
- New logic to generate correlation, relates to issue #95 . Updated DB
  schema ! [Christophe Vandeplas]
- Fixes #141. [Christophe Vandeplas]
- Merge branch 'master' of https://github.com/MISP/MISP. [iglocska]
- Tightened the export rules. [Iglocska]

  - text, xml, ioc exports of attributes with to_ids == 0 are now
    blocked.
- Bug with attribute edits. [iglocska]

  - users without publishing rights couldn't edit attributes. Fixed
- Sanitization of the data when creating .ioc files. [iglocska]
- Fix to the highlight issue. [iglocska]

  - new line at the end of the search list would break the highlighter and
    throw a warning
    - fixed
- Show the org logo in the memberslist. [iglocska]
- Merge branch 'namedpipes_mutex' [iglocska]
- Named pipes and mutex. [iglocska]

  - added the 2 types under the artifacts dropped category
- Fix for the search. [iglocska]

  - Due to the sanitization being fixed, the search results broke

  - This is a quick copy of the fix implemented on develop by cvandeplas
- Quick fix to the sanitization. [iglocska]

  - the double sanitization needed a quick fix until the development branch
    gets merged in the future
- Fix to the bulk search when logged in as a non admin. [iglocska]

  The search filter was broken and didn't return the expected result. Should
  be fixed.
- Updated README. [Christophe Vandeplas]
- Update README. [Christophe Vandeplas]
- Issue with Correlations going missing. [Andras Iklody]

  - Update to the delete in afterSaveCorrelation
- Removed some obsolete code. [Andras Iklody]

  - getName functions removed

  - Fixed a reference to it in the logable behaviour
- Some fixes to indeces not set. [Andras Iklody]

  - Affecting Event creation, attribute deletion remotely and logging of
    event deletion
- Merge branch 'removeprivate' into develop. [Andras Iklody]
- Removal of deprecated code. [Andras Iklody]

  - The flag private is deprecated, removed together with the code that was
    affected by it
- Merge branch 'master' into develop. [Andras Iklody]

  Conflicts:
  	app/Config/bootstrap.default.php
- Merge branch 'master' of https://github.com/MISP/MISP.git. [Christophe
  Vandeplas]
- Fixed a sanitization issue with encrypted emails. [Andras Iklody]
- Updated gitignore. [Christophe Vandeplas]
- Fix merge issue. [Christophe Vandeplas]
- Merge branch 'master' of https://github.com/MISP/MISP.git. [Christophe
  Vandeplas]
- Merge branch 'master' of https://github.com/MISP/MISP. [Andras Iklody]

  Conflicts:
  	app/Config/bootstrap.default.php
- Small fix. [Andras Iklody]
- Small changes. [Andras Iklody]

  - added an optional field to the bootstrap default (used by the e-mail
    notification system)

  - Clarification about the isAdmin and isSiteAdmin (comment)
- Removes multiple correlation engines Fixes #83 but after testing issue
  #95 comes to light. [Christophe Vandeplas]
- Removed unused CyDefSIG.showowner field. Closes issue #93. [Christophe
  Vandeplas]
- Merge branch 'develop' [Andras Iklody]
- Updated github url. [Christophe Vandeplas]
- Merge branch 'master' of https://github.com/BeDefCERT/MISP. [iglocska]
- Updated INSTALL docu and apache templates. [Christophe Vandeplas]
- Small fixes. [Andras Iklody]

  - Comments about isAdmin vs isSiteAdmin

  - Extra config line added to bootstrap.default.php for the built in e-mail
    system
- Wrong version of adminCrudComponent. [Andras Iklody]

  - Can cause issues when saving roles, replaced with the newer version.
- Removed leftover debug code. [Andras Iklody]

  - forced exception to test debug output left in - removed
- Small edit fixes #75. [iglocska]

  - Event was not deleted when another non site-admin org user tried to
    delete an event due to the event not being read before its organisation
    was compared to that of the logged in user -> fixed.
- Bug with pull. [iglocska]

  - Pulling all from the server list view would cause all new events to be
    pulled as intended, but attachments would not be pulled with their
    respective attributes

  - the few lines of code responsible for loading the file and base64
    encrypting it for the transfer were misplaced within a correlation check

  - fixed.
- Small bug with sorting events by validation. [iglocska]

  - didn't work properly, fixed.
- Updates to the manual. [iglocska]

  - new export features

  - contact user features
- Missing view for IOC export. [iglocska]
- First version of an IOC export feature. [iglocska]

  - Builds basic .ioc file of an event, OR-ing all eligible attributes

  - mass export via a zip file to be implemented later
- Small error. [iglocska]
- Small bug. [iglocska]

  - Messages left empty for all but the first user in a mass custom e-mail
  - fixed.
- Small message notifying the admin that the e-mail was sent. [iglocska]

  - flash message after e-mail sent
- Debug exception left in. [iglocska]

  - removed
- E-mailing system for site-admins. [iglocska]

  - site admins able to contact users by e-mail from within the system
  - PGP encrypted where available
  - Password reset with automatic temporary key generation
  - all of the above options have a mass-email version where every user is
    contacted at once
  - Potential new users can be contacted too (GPG key can be supplied)
- Fix to a validation error. [iglocska]

  - regkey|value's validation was inversed only accepting incorrect entries
- Double sanitization fixed. [iglocska]
- Extensions of filenames now validate if a number is included.
  [iglocska]
- Update to the validation of file names to allow _ in the extension.
  [iglocska]
- Search for attributes by organisation. [iglocska]

  - New search functionality on request - restrict attributes by
    organisation

  - Also, attributes in the list attributes and search attributes result
    pages, that belong to the user's organisation will have a red event ID
- Related events. [iglocska]

  - Implemented on request: related events created by the same organisation are now coloured red
- Validation of vulnerability to CVE number, Fixes #35. [iglocska]
- Change to the location of the add attribute/attachment buttons. Fixes
  #49. [iglocska]
- Moved the batch import checkbox, Fixes #50. [iglocska]
- Update to the default config files. [iglocska]

  - Some minor changes to the default config files
- Slight change to the xml export of search results. [iglocska]

  - Disabled the feature for "List Attributes".
- New export feature. [iglocska]

  - To restrict the authentication key from being used by interactive users,
  implemented a new export page that uses the uses cake's user
  authentication

  - the old export features still exist for users with perm_auth enabled
    accounts - renamed to automation

  - Exporting the events that found attributes belong to in a search
    attributes result page

  - exporting of individual events to file by clicking a link in event view
- Temporary fix for an issue with the ACL. [iglocska]
- Updates to the manual. [iglocska]
- Update to the targets of contact emails and more. [iglocska]

  - The original creator of an event will also get contacted by contact org
    if he/she has the contactalerts turned off.

  - error in the SQL permissions of normal users and org admins - they
    weren't able to modify/delete events of their own organisation that they
    themselves didn't create
- Bug fixes. [iglocska]

  - issues of admin orgs not being able to edit/delete org events

  - owner org removed for org admins

  - email only visible from own org to org admins
- Upgrades to the installation and upgrade process. [iglocska]

  - Instructions updated

  - SQL scripts tidied up of incorrect junk (from export)

  - upgrade scripts finish gracefully
- Small change to the migration. [iglocska]
- Change to the migration script fixing an error. [iglocska]

  During the structure export of the ACL tables the current increment count
  from the test environment got left in, caused errors when creating a new
  role.
- Instructions for the upgrade. [iglocska]

  - 1st version
- Update to generateCount. [iglocska]

  - generateCount used to just run through all attributes and save them, to
    generate the count. It led to VERY long execution times on larger
    databases (25k+ attributes). With the extra processing that each save()
    does for attributes, this was horribly slow.

  - new generateCount just saves the events based on the number of
    associated attributes, only having to save the events (of which there
    are considerably less).
- More updates to the migration. [iglocska]
- Slight change to generating the ArosAcos. [iglocska]

  - permission field is not set when roles are read during the ArosAcos
    generation script - needed for generateACL. Fixed.
- Shell scripts updated to populate the ACL. [iglocska]
- Some changes to the migration script. [iglocska]
- Merge branch 'develop' of https://github.com/BeDefCERT/MISP into
  develop. [iglocska]
- Quick fix of the git url. [Christophe Vandeplas]
- Highlighting in log searches. [iglocska]

  - new helper that can be used for highlighting

  - highlighting of the search terms in the log search result - index view.
- Removed the js title bubble for related events. [Andras Iklody]

  - Removed javascripts based title bubble showing the event info in related
    events / attributes and in the search attribute view.

  - Replaced it with values provided by extra cake queries as the delay for
    fetching the info field through a js rest request was annoyingly slow

  - some coding standards
- Attribute and event access. [Andras Iklody]

  - Updated the check for authorisation to view an event and attribute as
    the system hid some valid combinations (such as a server only attribute
    in a higher distribution level event).
- Regexp validation. [Andras Iklody]

  - an invalid regexp entry could block any event/attribute from being
    entered. Introduced a check on regexp entry to block faulty patterns.
- Changes to logs and some minor changes. [Andras Iklody]

  - Regexp, blacklist, roles, whitelists now logged

  - adminCRUD now sets ID (for the logging) on edit

  - some minor UI changes (removal of empty action menues on the left menu
    bar)
- Previous edit was an error. [Andras Iklody]
- Error in a previous commit. [Andras Iklody]
- Enabled filename whitelisting for GFI sandbox uploads. [Andras Iklody]

  - filename wasn't validated before exec() to unzip before
- Subscription to alerts from contact reporter. [Andras Iklody]

  - Users can now choose to subscribe to receive e-mails from the "Contact
    Reporter" feature.
- Changed email alert. [Andras Iklody]

  - It didn't respect private events and alerted everyone. Fixed.
- Removed sanitization of emails. [Andras Iklody]

  - caused linebreaks to be sanitized, it's a plain text e-mail so
    sanitization isn't needed.
- Tighter checks so users can't edit events of other orgs. [Andras
  Iklody]
- Update to the admin privileges. [Andras Iklody]

  - Changed the requirement for a lot of functions to be site admin as
    opposed to admin.
- Cleanup of some duplicate junk. [Andras Iklody]
- New regular expressions default values. [Andras Iklody]

  - List of new values for the regexp table

  - if the user_id for an event is not set, set it to that of the user with
    the e-mail address of 'cisprotection@ncirc.nato.int'.
- Colouring of search terms works in links. [Andras Iklody]

  - links now have proper colouring to make the found terms more visible
- Some changes to the search. [Andras Iklody]

  - changes to the validation of the results

  - fixes an issue where the escaping of slashes showed up with a //

  - made the found results more visible and case insensitive
- Slight update to the filename regex. [Andras Iklody]

  - accept extensions from 2 to 4 characters in length
- Fixed some regex issues and file name validation. [Andras Iklody]

  - Fixed an issue that caused attribute values to be converted to 1 on
    save in case of an empty regexp table

  - Filename validation now happens via whitelisting instead of filename
    sanitization
- Checkbox / radio misalignment. [Andras Iklody]

  - Fixed an issue with IE interpretting an unset padding value for
    checkboxes / radio selects as a good reason to give it some high value.
- Previous edit was incorrect, fixed. [Andras Iklody]
- Tiny Migration and UI edit. [Andras Iklody]

  - updates to the migration SQL script

  - small change in the new/edit roles UI to solve a misalignment
- Typo... [Andras Iklody]
- Case-sensitivity. [Andras Iklody]
- SQL update. [Andras Iklody]
- Merge branch 'develop' of /home/git/cydefsig into develop. [deresz]
- Export distribution. [Andras Iklody]

  - Export didn't take into account distribution rules, should be fixed

  - Fixed a bug with editing attributes
- Still issues with the attribute search. [Andras Iklody]

  - should be ok now
- Fix to the updated search attributes. [Andras Iklody]

  - issue on the live server with the search field left empty, fixed
- Several things (search, migration) [Andras Iklody]

  - Changes to the default setting for non private events after migration

  - search attribute update to be able to exclude events
- Updated the migration script (SQL) [Andras Iklody]

  - Script updated based on the issues during testing

  - Changed the file upload/downoad mechanism.
- Composite type change. [Andras Iklody]

  - composite type's value not exploded if value1 already set (to hopefully
    fix issues with the migration tool)
- Missing migration sql updates. [Andras Iklody]
- Regexp fixed. [Andras Iklody]

  - Regexp replacement didn't actually change the data in the object. Fixed.
- Update sql script to go from 1.0 -> 2.0. [Andras Iklody]

  - First version of an SQL upgrade script
- Fixed a minor error. [Andras Iklody]

  - comma at the end of line missing in SQL file
- Changes to the distribution handling of attributes. [Andras Iklody]

  - Only the creating org of the event can change the distribution of
    attributes

  - Attribute distribution setting are only pushed on edits if they were
    manually changed (so that the distribution level of events on the
    creating server doesn't get degraded by an edit and push of the event at
    a synced server when using connected community settings).

  - slight change to the batch attribute search, the search terms are only
    echoed up to 9 terms to prevent the mass echoing of a long list
- Some updates to the migration script. [Andras Iklody]

  - Getting it up to date
- Attribute edit fixed. [Andras Iklody]

  - Editing attributes caused an error because the uuid was not passed back
    from the form (and it is used to find the attribute locally for rest)

  - UUID is now used from the read attribute for non rest users. In the long
    run it would be cleaner to not allow non rest users to reach that part
    of the code.
- Minor changes. [Andras Iklody]

  - some changes to the access control

  - re-renabled regexp and blacklists, will need a closer look though

  - editing a role should update ACL

  - some other minor things
- Previous commit was slightly off. [Andras Iklody]

  Changed the placing of the unset, as it broke the push of attachments.
  Should be fine now.
- Major bug with attributes disappearing during sync. [Andras Iklody]

  Found a bug where an instance that has a lower attribute count pushing to
  another would cause the attributes with equal attribute ID to get
  overwritten with the pushed ones. Unsetting the attribute ID before the
  push fixes this.
- Update to the menu. [Andras Iklody]

  - minor cosmetic change
- Reworked the sync / release control. [Andras Iklody]

  - Fixed issues with the sync
  	- Secondary publishes on remote servers failed
  	- Introduced new fields in events to stop backward traverse of
  	  edit information that lead to low performance and eroneous
  	  distribution information updates when more than 2 servers were
  	  linked
  	- Deletion of an attribute now deletes on remote servers

  - Changes to the event ownership
  	- Original creator org now noted in the event itself
  	- Only original creator org can change distribution
  	- Events will show up with the original creator org for users
  	  (admins can see both that and the owner of the event on the
  	  local instance)
  	- Server.organization now used in junction with the connecting
  	  user's org and the instance's org (from the bootstrap) to
  	  determine distribution flow control and access rights

  - Lots of minor changes
- Coding standards. [Noud de Brouwer]

  this is to the new php53-pear-CakePHP_CodeSniffer-0.1.11.
- Updated structure of the documentation. [Christophe Vandeplas]
- Further cleanup. [Christophe Vandeplas]
- Updated LICENSE from copyright to AGPL and first cleanup of files.
  [Christophe Vandeplas]
- Minor change to the validation. [Andras Iklody]

  - Some types didn't have any validation info, defaulting in an incorrect
  input - fixed

  - re-enabled the sanitization of file names
- Minor changes to the validation. [Andras Iklody]
- Changes to link validation and minor fixes. [Andras Iklody]

  - Links get validated now to filter malicios code

  - removed a double edit button in the case of an admin editing himself

  - fixed an error with adding new attributes
- Updates to security. [Andras Iklody]

  - perm_auth new toggle, can disable auth key usage for a role

  - prevents sync / rest with a perm_auth == false key

  - some changes to sync to provide better feedback on why it failed

  - rewording of distribution options
- Redirect for ServersController. [Andras Iklody]

  Added redirect for index in case of non sync users
- Reworked aros_acos creation. [Andras Iklody]

  - moved and fixed the aros_acos creation on the new role creation

  - new method in appController that sets all the aros_acos from scratch
    (for example for a new instance, or a changed acos / aros table)

  - some minor changes, redirects to the terms page on invalid events
    removed, etc.
- Missing file from the last commit. [Andras Iklody]

  Missed a file from the package
- Fixes to access rights, some sanitization, etc. [Andras Iklody]

  - Admins cannot manually change anyone's authkey, they need to generate a
    new one via the reset link

  - Some pages could be accessed by changing the url - fixed (though needs
    further testing)

  - Edited a change in the manual that may have been confusing

  - Some changes to the way ACL is set up - still needs more work
- Temporary fix for file-uploads under windows. [Andras Iklody]

  Added an alternate file-upload/download path creation for PHP_OS ==
  'WINNT'

  Also removed autofill for the login field
- Corrected a typo preventing the sync from working. [Andras Iklody]
- Changes to the admin org access and sanitization. [Andras Iklody]

  1. Some errors fixed in the way redirects worked for org admins

  2. fixed some double sanitization resulting in incorrect characters
  displayed in certain fields
- Added hover over event IDs in search attributes view. [Andras Iklody]

  Hovering over the event IDs now shows the event info in the list generated
  by the search attributes page
- Security for UsersController. [Andras Iklody]

  org admins could edit users of other orgs by accessing the edit page
  through the URL. Fixed.
- Further changes to org admins. [Andras Iklody]

  org admins can manage their own server connections
  org admins cannot see other orgs' users in the users list
- Issue with uploading attachments fixed. [Andras Iklody]

  Uploading an attachment would fail while trying to set the event to
  unpublished. Fixed.
- Small update to the regular import regexp view. [Andras Iklody]

  An empty table cell caused a cosmetic misalignment of the cell border.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Org admin privileges. [Andras Iklody]

  Added restrictions for org admins and regular users to be able to see
  regexp/whitelist/blacklist information without being able to edit them.
  Org admins can also see the roles but not edit them.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Fix for the synchronisation. [Andras]

  An error in the pull fix broke the push/publish feature. Fixed.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Attribute distributions. [Andras Iklody]

  Added feature to block distribution levels that would get overruled by the
  event distribution. The distribution of the event will be the currently
  selected distribution when creating an attribute.
- Merge branch 'develop' of ssh://172.29.79.164/home/git/cydefsig into
  develop. [Andras Iklody]
- Distribution. [Noud de Brouwer]

  attributes inherit distribution from event.
- Fix for the org admin privileges. [Andras Iklody]

  Editing / creating users and the organisation permissions for org admins
- Org admin can only see org logs. [Andras Iklody]

  Added check for the above
- RBAC. [Noud de Brouwer]

  only create users within own organisation.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Pull fixed. [Andras Iklody]

  Fixed the issues with pull, should work fine now
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Fixed push/publish. [Andras Iklody]

  Fixed a few issues that caused push/publish not to work
- RBAC. [Noud de Brouwer]

  org admin and RBAC admin.
- Better fix to Sanitize::clean() problem. [deresz]

  'escape' option was removed.
- Sanitize. [Noud de Brouwer]

  Sanitize can not be used in PGP key.
- GPG. [Noud de Brouwer]

  start of check/correct.
- DB. [Noud de Brouwer]

  in conversion create Blacklist table as well.
- PGP. [Noud de Brouwer]

  clean key remark.
- PGP. [Noud de Brouwer]

  direction-like-out-commented try.
- RBAC. [Noud de Brouwer]

  so role is editable.
  (i will not commit/push during after hours ;) )
- Merge branch 'develop' of ssh://misp.ncirc.nato.int/home/git/cydefsig
  into develop. [Noud de Brouwer]
- Roles controller Jquery helper added. [deresz]

  For some reason I needed it
- RBAC. [Noud de Brouwer]

  role editable on user page (by admin).
- RBAC. [Noud de Brouwer]

  roles/view/<id>.
- RBAC. [Noud de Brouwer]

  ampesant in html.
- RBAC. [Noud de Brouwer]

  admin must be able to edit role, where-ever.
- Distribution level explanation. [Andras Iklody]

  The description of the distribution levels has been updated
- Slight change to distribution description. [Andras Iklody]

  Changed the explanation for each distribution level on event creation
- Sync. [Noud de Brouwer]

  curl test update using a generic named xml.
- Merge branch 'develop' of ssh://misp.ncirc.nato.int/home/git/cydefsig
  into develop. [Noud de Brouwer]
- Small change to batch searches. [Andras Iklody]

  An empty new line caused every attribute to be displayed. Fixed.
- Batch search for attributes. [Andras Iklody]

  Implementation of request to be able to do batch attribute searches
- Sql blacklist. [Noud de Brouwer]

  somehow all _working_ code for blacklist got committed and pushed
  but not the sql db change, find this here-in.
- Error. [Noud de Brouwer]

  behavior error or just plain wrong on our side.
- Error. [Noud de Brouwer]

  behavior error or just plain wrong on our side.
- Error. [Noud de Brouwer]

  behavior error or just plain wrong on our side.
- PHP practice. [Noud de Brouwer]

  array-content.
- CakePHP. [Noud de Brouwer]

  odity, if i add "tes\ntestt\ntes", blacklist the testt,
  i get "tes\ntestt" as content. (other behaviors?)
- Blacklist. [Noud de Brouwer]

  Blacklist gets activated on Event.info and Attribute.value.
- Behavior. [Noud de Brouwer]

  Use settings, par-example, name a field to Import Blacklist.
- Blacklist. [Noud de Brouwer]

  AdminCrud looking for Blacklist Flash message
  and Import Blacklist menu button.
- Blacklist. [Noud de Brouwer]

  A list of stringparts not to be able to enter.
- AdminCrud and coding standard. [Noud de Brouwer]

  more AdminCrud and coding standard clean up.
- AdminCrud. [Noud de Brouwer]

  use of the AdminCrud component.
- App syntax. [Noud de Brouwer]

  Controller/Component to share AdminCrud.
- Git. [Noud de Brouwer]

  redo 'git-trigger' change.
- Git. [Noud de Brouwer]

  pardon i seem to have had a:
- Unused & coding standard. [Noud de Brouwer]

  Removed some total unused code and corrected some toward the CakePHP coding standard.
- Signature Blacklist. [Noud de Brouwer]

  removed unused view.
- Import Regexp. [Noud de Brouwer]

  removed unused code.
- Import Regexp. [Noud de Brouwer]

  Renamed Import Whitelist to Import Regexp.
- Validation field. [Andras Iklody]

  A field in the event index showing it clearly whether the event has been
  published or not - shows a small image (placeholder atm)
- Fixed deprecated errors. [Andras Iklody]

  Removed cause of deprecated errors (Pass by reference)
- Log & code duplication. [Noud de Brouwer]

  $this->Html->image($nonExistingImage)
  showed up in tmp/logs/error.log and
  the origin this is in 2 Views, so a View Element was created.
- Doc & build. [Noud de Brouwer]

  move technical_design into app/build/.
- Log. [Noud de Brouwer]

  do not logs/error.log if an img does not exist.
- Sanitize. [Noud de Brouwer]

  Sanitize countermeasures.
- Log & coding standards. [Noud de Brouwer]

  do not logs/error.log if an img does not exist.
  and overcome the,
  Each PHP statement must be on a line by itself.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- DB. [Noud de Brouwer]

  give MYSQL.txt the correct .sql extension.
- Sanitize. [Noud de Brouwer]

  Sanitize countermeasures.
- Sanitize. [Noud de Brouwer]

  Sanitize countermeasures.
- Added validation field to the event index. [Andras Iklody]

  A small image at the front of each line showing whether the event has been
  validated (published) or not. The images are placeholders for now.
- Sanitize. [Noud de Brouwer]

  Sanitize countermeasures.
- DB. [Noud de Brouwer]

  clean up conversion.
- HTML. [Noud de Brouwer]

  make Pages/using_the_system.ctp valid HTML.
- HTML. [Noud de Brouwer]

  make Events/view.ctp valid HTML.
- Merge branch 'develop' of ssh://misp.ncirc.nato.int/home/git/cydefsig
  into develop. [Noud de Brouwer]
- Removed option "Sandbox" from analysis. [Andras Iklody]
- GenerateAllFor<FieldName> [Charlie Root]

  conflicts with CAKE/Model/Model::_call() so no findBy<FieldName>.
  (and various very minor other things.)
- JQuery. [Noud de Brouwer]

  deactivateButtons.js was bad and is not used anymore, so removed.
- JQuery. [Noud de Brouwer]

  version was bumped but actual file not removed.
- Static program analysis. [Noud de Brouwer]

  New Static program analysis Makefile for f.i. Coding Standards with reports in app/build.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards typo.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards work file.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- Coding standards. [Noud de Brouwer]

  Coding Standards.
- PHP. [Noud de Brouwer]

  lcfirst (PHP 5 >= 5.3.0).
- GenerateAllFor<FieldName> [Noud de Brouwer]

  missed adding app/Lib/CamelCase.php and app/Config/routes.php.
- Event.analysis. [Noud de Brouwer]

  set analysis* in view().
- Paging. [Noud de Brouwer]

  6 (used during test) -> 60 again.
- GenerateAllFor<FieldName> [Noud de Brouwer]

  so we can use an URL like:
  http://localhost/<TableName>/generateAllFor<FieldName>/newValue/oldValue
  for example:
  http://localhost/events/generateAllForAnalysis/0/null
  http://localhost/users/generateAllForInvitedBy/1/0
  http://localhost/users/generateAllForRoleId/1/0
- Sanitize. [Noud de Brouwer]

  Sanitize::clean() but redo the info and value fields.
- Search. [Noud de Brouwer]

  After added feedback on entered search terms for search attributes
  and search logs, this now also works for LogsController::index()
  and next and previous page.
- Merge branch 'develop' of ssh://misp.ncirc.nato.int/home/git/cydefsig
  into develop. [Noud de Brouwer]
- Added missing 4th option to analysis levels. [Andras Iklody]
- Added a missing view for password changes. [Andras Iklody]
- Sanitize. [Noud de Brouwer]

  do not Sanitize::clean() $this->request->data.
- Fixed an issue with the events. [Andras Iklody]
- Fix for the Attributes. [Andras Iklody]
- Sanitize. [Noud de Brouwer]

  small correction on a "\n" in info.
- 2 SQL files missing. [Andras Iklody]

  - added them now
- Added features from branch analysis_levels. [Andras Iklody]

  -Analaysis levels setable for events as per milestone item 94
  -Password change forced as per milestone item 109
  -Added feedback on entered search terms for search attributes
  -fixed the authentication issue
  -some minor fixes
- Merge branch 'master' into develop. [noud]
- Oeps. [noud]

  leftover debug() removed.
- Merge branch 'master' into develop. [noud]

  Conflicts:
  	app/Controller/AttributesController.php
  	app/Controller/EventsController.php
- RESTfull sync. [noud]

  this is in responce to the email
  From: <User1088@QET.BE>
  To: <ndebrouwer@hotmail.com>, <andrzej.dereszowski@ncirc.nato.int>
  Subject: Re: sync/REST
  Date: Fri, 7 Dec 2012 13:30:10 +0000
  in this there is a complaint about the RESTfull sync workings.
  the email hints about 2 possible options:
  i) RESTfull add event without attributes (conform the web interface)
  ii) RESTfull add event with attributes (more conform the code)

  both are implemented and can be choisen in bootstrap.php by
  Configure::write('CyDefSIG.rest', 'ii') or 'i'.
- Merge branch 'master' into develop. [noud]

  Conflicts:
  	app/Controller/AttributesController.php
  	app/Controller/EventsController.php
  	app/Controller/ServersController.php
  	app/Model/Event.php
- CakePHP. [noud]

  CakePHP update from 2.2.3 to 2.2.4
- JQuery. [noud]

  bump JQuery from 1.8.2(.min) to 1.8.3(.min).
- RESTfull sync. [noud]

  Let RESTfull only work conform the web pages (to Christophes wish),
  so add/edit event apart from add/edit attribute.
  (there is annotation in the code to revert back to full RESTfull and
  add/edit the attribute(s) alongside add/edit the event.)
- RESTfull sync. [noud]

  redone delete attribute and add that to the sync.
- RESTfull. [noud]

  make RESTfull event add and edit work again.
- RESTfull sync. [noud]

  RESTfull attribute add, edit and view, to be usefull in sync.
- RESTfull/sync. [noud]

  redid the sync, so if add and exist, send HTTP 302 and different
  Location, and do edit there.
  Still, the final result has to compare the attributes and if needed
  RESTfull delete.
- Fix bug when published event that is added using REST is not pushed to
  remote servers. [Christophe Vandeplas]
- Removing update functionality for REST. [Christophe Vandeplas]
- Merge branch 'master' of code.lab.modiss.be:cydefsig. [Christophe
  Vandeplas]
- Fix bug of sync. [Christophe Vandeplas]
- ExtJs. [noud]

  reverted, cause no need.
  was:
  does not show on production.
  this is the ExtJs not being there?
  or php (>5.2.8) not build without --disable-json.
- Role. [noud]

  renamed everything group to role (i.s.o. renaming just the visable).
- Role. [noud]

  renamed everything group to role (i.s.o. renaming just the visable).
- Source Code Review. [noud]

  sanitize everything displayed from the db.
  (and some small coding standard whitespaces)
- Roles. [noud]

  only be able to tick actions when manage (& publish) org events.
- RBAC and Roles. [noud]

  did add Acl Admin and Audit.
- Sync. [noud]

  have sync option in role.
  and only display the Sync Actions when sync option or admin.
  (still has to be disabled if role is below manage org events.
- Attributes. [noud]

  display "#Attr.".
- Distribution. [noud]

  show "All" if distribution is All communities in Events/index.ctp and
  Events/view.ctp.
- Changes to the related events mouseover bubble. [Andras Iklody]

  Removed unneeded headers and changed the address to relative to avoid the
  sending of an OPTIONS REST request.
- Db. [noud]

  clean up temp db .sql files.
- Db. [noud]

  clean up temp db .sql files.
- Db. [noud]

  besides regex data in MYSQL.txt for a clean install
  have MYSQL.regex.sql for a Cydefsig update.
- Db. [noud]

  make top db conversion script path relative.
- Db. [noud]

  conversion needs a Organization name,
  so name that in the README.txt as well.
- Db. [noud]

  add the regex table to db conversion.
- Typo. [noud]

  typo
- Coding standards. [noud]

  coding standards tells us "space"."space"
- Menu. [noud]

  correct menu on add/edit Import Whitelist.
- Correlation. [noud]

  corrected very old error if one event got 3 attributes having the
  same value1 but variation in value2.
  (in the past the correlation got signed to the 1st attribute, not to the
  respective attributes.)
- Updated some images. [Andras Iklody]

  Update to some images to reflect the changes to the whitelists.
- Minor update to some linking to the documentation. [Andras Iklody]

  Updated a few links to link to specific portions of certain pages in the
  documentation instead of just the page itself.
- Coding standards. [noud]

  whitespace police.
- Added bubble when hovering over related events. [noud]

  suppres already named caregorie again.
- Merge branch 'develop' of ssh://172.29.79.164/home/git/cydefsig into
  develop. [Andras Iklody]
- User Guide. [noud]

  corrected conform the app for attributes as well.
- User Guide. [noud]

  corrected conform the app.
- Update to the hover effect on related items. [Andras Iklody]

  Several occurances of links to the same event in the attribute list
  caused all instances except the first one to not display any event info
  when hovered over. Fixed.
- Coding standards. [noud]

  coding standards tells us "space"."space"
- Whitelists. [noud]

  better naming and regex block named in administration.ctp
- Added bubble when hovering over related events. [noud]

  suppres already named caregorie again.
- Import Whitelist. [noud]

  more replacements to uniform the data, so more correlation.
- Import Whitelist. [noud]

  if not regex and only replacement, consider that as a comment.
- Readme.txt. [noud]

  readme.txt update
- Added bubble when hovering over related events. [noud]

  no need to re-include jquery given it's included in
  View/Layouts/default.ctp.
- Added bubble when hovering over related events. [noud]

  make baseurl variable conform bootstrap.
- Added bubble when hovering over related events. [noud]

  make authkey variable conform the authenticated user.
- Added bubble when hovering over related events. [Andras Iklody]

  Hovering over related events will reveal the "info" field of the event
  without clicking on it.
- Coding standards. [noud]

  correction conform conding standards.
- Import Whitelist. [noud]

  if Import Whitelist item has regex and no replacement, then do not allow
  an attribute having value the regex and do not allow events having info
  conform that regex.
- Code. [noud]

  a "1" gremlin removed.
- Regex white/blacklist. [noud]

  correct nameing of the buttons.
- Merge branch 'develop' of
  ssh://misp.ncirc.nato.int/home/git/cydefsig.git into develop. [noud]
- Changes to the manual. [Andras Iklody]

  Added information about Regex, changed some minor things.
- Regex and blacklist. [noud]

  blacklist, as in, do not input attributes, is working now,
  for manual, batch and GFI Sandbox import.
- Merge branch 'regex' into develop. [Noud de Brouwer]
- Input regex. [noud]

  use RegexBehavior on Event.info and Attribute.value.
- Tiny histogram change. [Andras Iklody]

  Changed the height of the list of types to fit the amount of data
- Slight change to the histogram. [Andras Iklody]

  Data for types that had "|" or "-" in the name (such as ip-src)
  were omitted - should be fixed now
- Db. [noud]

  spit generatePrivate into attr and event part (given long runtime).
- Correlation. [noud]

  do not show the same event id multiple times for one attribute shown.
- User. [noud]

  no possibility to delete oneself.
- Trim. [noud]

  use the TrimBehavior on all inputable models.
- Terms. [noud]

  removed termsaccepted and newsread from user add,
  so the user herself has to accept the terms.
- Distibution. [noud]

  generatePrivate conform new distribution.
- Distibution. [noud]

  add generateHop to migratemisp11to2.
  (generatePrivate should still be looked at.)
- Distribution. [noud]

  generate hop count.
- Distribution. [noud]

  do not do anything upon delete in regard to distribution.
- Distribution. [noud]

  if distribute upstream, do not alter org, user_id nor distribution
  settings.
- Correlation. [noud]

  altered so an event distribution preveals over it's attributes
  distribution.
- Even slighter modification to the manual (a typo and a few white
  spaces) [Andras Iklody]
- Slight modification to the manual (removing some whitespace errors)
  [Andras Iklody]
- Updated the manual to conform with coding standards. [Andras Iklody]
- Coding standards. [noud]

  correct conform coding standards.
- Coding standards. [noud]

  whitespace police
- Updated the manual with the REST API portion. [Andras Iklody]
- Event/attribute delete. [noud]

  In version 1 and 2 of misp/cydefsig there's a delete button upper left
  in the menu that a) does not delete or b) does not return to a visable
  url after deletion.
  As a 'fix' those delete buttons are now removed, given there does still
  exist delete in the index view.
- Os. [noud]

  various test dirs added just for conveniance.
- Db. [noud]

  up-to-date db.
- Sync. [noud]

  lastpushedid reminder.
- Trim. [noud]

  add TrimBehavior to use in Servers and lateron in Attributes.
- Attributes delete. [noud]

  oeps, attribute delete inadvertably deleted from view.
- Validation. [noud]

  trim all string fields in server.
  (later bring this to AppModel or behavior level)
- Audit log & terms. [noud]

  do not handle a timed out user log.
  and
  better check on login and termsaccepted.
- Attributes. [noud]

  hide attributeDistribution tooltip on open.
- Delete event. [noud]

  in edit event screen now give correct id in delete alert box.
- Correlation. [noud]

  repair correlation after introduction of 'This server-only'.
- Correlation. [noud]

  sort Related Events decending on date and second on id.
- Coding standards. [noud]

  better parameters on callback routines.
- Correlation. [noud]

  some correction so no missing correlation.
- Correlation. [noud]

  respect the latest added 'This server-only'.
- RBAC. [noud]

  respect setting for edit attribute.
- RBAC. [noud]

  respect setting for edit event.
- Terms. [noud]

  activate a route for routeafterlogin on timeout.
- Private. [noud]

  show 'This server-only' events to all on the server.
- Terms. [noud]

  deactivate a route.
- Users. [noud]

  show the correct Org during edit.
- Terms. [noud]

  better routes to support termaccepted.
- RBAC. [noud]

  name what to do during install for RBAC tables and content.
- Terms. [noud]

  route to terms even if an 'admin' option is chosen.
- Correlation. [noud]

  CyDefSIG.correlation being 'default' and 'sql' are depreciated.
- Code standards. [noud]

  we emit XHTML 1.0 Transitional.
  so to check, encapsulate using:

  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml">
  <body>

  <<actual_page>>

  </body></html>

  and use http://sourceforge.net/projects/eclipsetidy/ to validate.
- Sync. [noud]

  validation on server.authkey having minlenght of 40 like user.authkey.
- Code standards. [noud]

  html cleanup.
- Html. [noud]

  removed some html giving warnings.
- Sync. [noud]

  corrected pull for events having no distributable attributes.
- Sync & code. [noud]

  a new NameController() needs $Name->constructClasses().
  odd this ever did work before (CakePHP 2.2.2 versus 2.2.3 diff?).
- Sync & merge. [noud]

  merged develop with master and have to alter ServersController a little.
- Merge branch 'master' into develop. [noud]

  Conflicts:
  	app/Controller/ServersController.php
- Merge branch 'master' of /home/git/cydefsig. [Andrzej Dereszowski]

  Conflicts:
  	app/Controller/AppController.php
- Fixes bug where no email alert is sent when event is added using API
  (and published) [Christophe Vandeplas]
- Fixes bug when alerting and a single gpg key is giving problems.
  [Christophe Vandeplas]
- Revert "blackhole" [Christophe Vandeplas]

  This reverts commit 899ef6300b554d77aa842e0e987973d6980e2898.
- Bugfix issue where delete event will also be triggered on servers with
  no push active. [Christophe Vandeplas]
- Merge branch 'master' of code.lab.modiss.be:cydefsig. [Christophe
  Vandeplas]
- Fixes download-sync-bug when only one event is present on the remote
  instance. [Christophe Vandeplas]
- Fixes bug 87 - on import of existing event: event info changed, tagged
  private. Also fixes events tagged private when added using REST api.
  [Christophe Vandeplas]
- Sync. [noud]

  push from v2 to v1.
- Correlation. [noud]

  just for intermediate db-update.
  (all MYSQL.*.sql should be removed lateron)
- Code standards. [noud]

  whitespace police.
- Terms. [noud]

  slight better formulated AppController::beforeFilter()
- Code standards. [noud]

  conform code standards.
- Version. [noud]

  removed a "-" copied in from a patch file.
- Terms. [noud]

  slight better formulated AppController::beforeFilter()
- Code standards. [noud]

  respect code standards.
- Sync. [noud]

  array correction done so no 2 kinda the same tests during pull.
- Sync. [noud]

  pull goes okay with just one event.
  pull with multiple events was already okay.
- PHP. [noud]

  CakePHP php minimum_version="5.2.8" but lcfirst was introduced in PHP
  5.3, so i reverted to 'strtolower(substr('.
- Users views. [noud]

  whole menu in admin_view.
  active delete button in edit.
- Sync. [noud]

  sync attributes on pull.
- Sync. [noud]

  conform the new distribution.
  pull on events works too.
- Distribution. [noud]

  conform latest, having:
  - Your organization only
  - This server-only
  - This Community-only
  - Connected communities
  - All communities

  Push is tested, pull not yet.
- Code. [noud]

  have the distribution description in one place, just the model.
- Dns. [noud]

  config if there is a name server available and do not use if not there.
- Db. [noud]

  db conversion using whitelist, not whitelists.
- Index. [noud]

  some line disapeared, in view as well on attribute level.
  Andras Iklody suggested a html non breaking space, that worked.
- Code. [noud]

  removed small double code.
- Sync (publish) [noud]

  Event publish button in events index and event view does
  report push failure(s) if any remote server is down.
- Correlation. [noud]

  fixed correlations being double accounted.
- Db. [noud]

  extra name migratemisp11to2 to run on server.
- Db. [noud]

  updated the db conversion from master->develop.
- Terms. [noud]

  take 2, for a user must accept terms.
- Sync. [noud]

  admin must be able to delete servers, Andras corrected.
- Terms. [noud]

  reverted just done commit
  (Can't use method return value in write context ).
- Terms. [noud]

  check for user logged in (if not a server looks total stalled).
- Sync. [noud]

  admins must be able to delete a server.
- Logout. [noud]

  keep the logout in footer as well (besides the logout in menu).
- RBAC. [noud]

  use $isAclAdd for New Server.
- Whitelist. [noud]

  cleanup whitelist.
- Hostname & port. [noud]

  if no baseurl given in bootstrap.php use the server configuration.
- Merge branch 'develop' of ssh://172.29.79.164/home/git/cydefsig into
  develop. [Andras Iklody]
- Code standards. [noud]

  slight updated code standards test script.
- Cleaning up and changing the user guide. [Andras Iklody]

  - user guide: information about the new number of attributes field in the list of events added
  - updated the event showing a list of events
  - removed obsolete images
- Code standards. [noud]

  corrections toward code standards.
- Index. [noud]

  some line disapeared.
  Andras Iklody suggested a html non breaking space, that worked.
- Count. [noud]

  result view for AttributesController::checkComposites()
- Count & GFI Sandbox. [noud]

  count # attributes in events index.
  plus various fixes for distribution in correlation of a GFI Sandbox
  upload.
- Merge branch 'develop' of
  ssh://misp.ncirc.nato.int/home/git/cydefsig.git into develop. [noud]
- Small change to the user guide. [Andras Iklody]

  Fixed the table of contents misalignment and added a line about IE9/10 compatibility mode causing issues
- GFI Sandbox. [noud]

  files having size 0 are not md5 summed in CakePHP.
- Correlation. [noud]

  if second attribute, create the reverse correlation as well.
- Terms. [noud]

  user must accept terms.
- Correlation. [noud]

  resolved comment typo.
- RBAC. [noud]

  corrected mayModify in Attribute/edit.ctp.
- Correlation. [noud]

  respect distribution Org in correlations.
  (for this
  add correlations.1_private conform MYSQL.correlaton.sql
  and
  AppController::generateCorrelation() must be run)
- Merge branch 'develop' of
  ssh://misp.ncirc.nato.int/home/git/cydefsig.git into develop. [noud]
- Change to the user manual. [Andras Iklody]

  Again a slight change, removed a script that numbered the <h2> headers for the ToC creation. Also fixed a few images.
- Update to the new user guide. [Andras Iklody]

  The old script to create an automatic table of contents was accidentally left in in the previous version, it is removed now.
- New user guide. [Andras Iklody]

  User guide for cydefsig v2
- Merge. [noud]

  botched merge..so commit..but empty.
- RBAC. [noud]

  AttributesController::edit() know's it's own attribute now for RBAC
  check.
- Correlation. [noud]

  respect distribution Org only.
- Sync. [noud]

  make pull work on an event with just one attribute.
- RBAC. [noud]

  admin can always publish.
- RBAC. [noud]

  slight better left menu if no <ul><li>items.
- RBAC. [noud]

  better users views.
- RBAC. [noud]

  servers, but add only when Manage Organization Events.
- RBAC. [noud]

  do not show New Event if no right.
- RBAC. [noud]

  just edit your own did still give edit org as well.
  can be tested if now correct.
- RBAC. [noud]

  now should be okay on the checkGroup.
  (mind, we have a PHP 5.3.10 (dev) and 5.2.10 (f.a.) difference.
  for CakePHP should be php > 5.2.8, pear > 1.9.0 and phpunit 3.5.0)
- RBAC. [noud]

  check if $user exists, if no, not logged in.
- RBAC. [noud]

  //$user =
  ClassRegistry::init('User')->findById($this->Auth->user('id'));
  $this->loadModel('User');
  $user = $this->User->findById($this->Auth->user('id'));
- RBAC. [noud]

  should now respect Manage, so also edit, own and org events
  in the db-update procedure as well.
  ‏
- RBAC. [noud]

  should now respect Manage, so also edit, own and org events.‏
- RBAC. [noud]

  change the “Requested Level of User Access” items
  conform "draft of Terms-ofUse and Joining Instruction".‏
- SQL. [noud]

  add Servers.organization.
- RBAC. [noud]

  role only add could still publish her own events,
  this should be not possible anymore.
- Distribution. [noud]

  removed No push leftovers as a distribution.
- SQL. [noud]

  pull-up all changes to the db model,
  so MYSQL.txt has all needed for a clean start db.
- Contact reporter. [noud]

  Submit to org button in the contact reporter view – changed it
  to just submit, having the tickbox to contact a person only + the submit
  to org button seems a bit confusing.
- Distribution. [noud]

  removed No push as a distribution.
- Logout. [noud]

  moved logout from footer right to Global Actions.
- Distribution. [noud]

  now attributes do work same for pull like push.
- Distribution. [noud]

  let pull behave same way as a push in regard to distribution.
- Distribution. [noud]

  do not push Community nor No push conform private.
- Search attributes. [noud]

  disallow invalid combinations of types and
  categories which would always throw 0 results.
- RBAC. [noud]

  name all Role i.s.o. Group.
- Version. [noud]

  show version in footer and only when logged in.
- Flags. [noud]

  correct from 50*50 to 48*48, so it's an icon size.
- Audit log. [noud]

  Following events are now being logged:
  1. Adding a new user.
  2. Deleting a user.
- Users. [noud]

  invited by filled.
- Audit log. [noud]

  Search logs allows for searching for “publish” as Action. Publish is
  saved in the logs as an edit with the change being publish () => (1).
  Now, edit (so unpublish) is still edit and publish is action.
- Audit log. [noud]

  Search logs and paging now works as expected (conform search
  attributes).
- NIDS. [noud]

  Unpublished events with an attribute flagged for IDS signature will
  create an IDS signature (should be published only).
- Whitelist. [noud]

  menu in views.
- Users. [noud]

  name Delete User on button i.s.o. Delete.
- Users. [noud]

  inactive Delete during edit of My Profile.
- Users. [noud]

  inactive Delete User in My Profile.
- Audit log. [noud]

  paging now works.
- Minor. [noud]

  cleanup of groups, logs and whitelists views.
- ExtJs. [noud]

  does not show on production.
  this is the ExtJs not being there?
  or php (>5.2.8) not build without --disable-json.
- Distribution. [noud]

  border="1"-testleftover removed.
- Distribution. [noud]

  if distribution is All, so not displayed in an index nor in attributes
  per event, there is missing a line-part in IE.
  Did add 1 space for All, this will maybe display the line-part again.
- Dropdowns. [noud]

  let the risk dropdown in event add and edit behave like the other
  dropdowns.
- Dropdowns. [noud]

  no space in edit Attribute categories dropdown.
- Internationalisation. [noud]

  just small __() for translation lateron.
- (internationalization) [noud]

  setFlash using __(), so transletable lateron.
- SQL. [noud]

  update of MYSQL.servers.sql,
  not using organization field.
- Install. [noud]

  variable cydefsig home dir.
- Distribution. [noud]

  distribution changes conform func.spec.
- RBAC. [noud]

  We have a rule(?), if so:
  $isAclAdd || $event['Event']['user_id'] == $me['id'].
  This rule, i "have add right OR the event was and is already mine".
  if that's correct, that was forgotten in the actions_menu.ctp.
- Merge branch 'master' into develop. [noud]
- Blackhole. [noud]

  full out-commented.
- Blackhole. [noud]

  revert the commit, this screws CSRF
  (thanks to Christophe for noticing)
- JQuery. [noud]

  bump JQuery from 1.7.2(.min) to 1.8.2(.min).
- CakePHP. [noud]

  CakePHP update from 2.2.2 to 2.2.3
- IDS Signature. [noud]

  corrected wrong description for IDS Signature.
- Correlation. [noud]

  to overcome a possible error on empty correlations.
- Crypt_GPG. [noud]

  small comment about debug and
  small note in readme about file rights.
- RBAC. [noud]

  real inactive buttons.
- Fixed lost JS helper in EventsController. [Andrzej Dereszowski]
- GFI Sandbox. [noud]

  Replace Windows specific info in a $string with environment variables en
  registry keys.
- Dropdowns. [noud]

  undo better optgroup support in dropdown in Attribute::add()
  and just remove the not usable empty category.
- Dropdowns. [noud]

  better optgroup support in dropdown in Attribute::add().
- Distribution. [noud]

  better descriptive tooltip text.
- Dropdowns. [noud]

  better optgroup support in dropdowns where 'ALL' or '' is used
  in Search Attributes and Search Logs.
- Distribution. [noud]

  do not display distribution 'All' in Events index or Event view.
- Outcommented a debug (PGP related). [noud]
- Blackhole. [noud]

  add component security to GroupsController.
- Pulldowns. [noud]

  removed the select optgroup.
- Distribution. [noud]

  distribution on add is default "All".
- GFI Sandbox. [noud]

  regexp replacement of usernames.
- Distribution. [noud]

  changes and cleanup.
- Wording change. [noud]

  so this works.
- Wording change. [Andrzej Dereszowski]

  Changed Private column to Distribution + some minor vocabulary changes.
- Merge branch 'master' into develop. [noud]
- Merge branch 'master' of
  ssh://misp.ncirc.nato.int/home/git/cydefsig.git. [noud]
- JQuery. [noud]

  bump JQuery from 1.7.2(.min) to 1.8.2(.min).
- CakePHP. [noud]

  CakePHP update from 2.2.2 to 2.2.3
- IDS Signature. [noud]

  corrected wrong description for IDS Signature.
- Correlation. [noud]

  to overcome a possible error on empty correlations.
- IDS Signature description. [noud]

  wrong description for signature.
  (possible commited 2 times)
- Private. [noud]

  description in event::view().
- Merge branch 'master' into develop. [noud]
- Crypt_GPG. [noud]

  small comment about debug and
  small note in readme about file rights.
- New attribute type - yara sig. [Andrzej Dereszowski]
- GFI sandbox. [noud]

  better representation of a downloadable attribute
  in a link (just href the file name, not including the path).
- Private. [noud]

  Add "Pull only" as a sharing state where,
  everybody does see an event, is pullable,
  but will never be pushed.

  Has a generatePrivate for db conversion now.
- Private. [noud]

  Private events are true private and
  running a server in 2 modes (private and sync),
  so real private (red) or private to server (amber)
  or full distributable (green).

  Mind this needs a change to tables events, attributes and correlation.
  These are in MYSQL.private.sql.
- Merge branch 'master' into develop. [noud]
- Blackhole. [noud]

  i have an idea this blackholeCallback seems to overcome a lot of
  blackhole situations we got.
  Notably during deleting multiple events from the index,
  this improved not getting a blackhole a lot.
- GFI Sandbox. [noud]
- Routes (logs pagination) [noud]

  recommitted to be sure it's in repo.
- RBAC. [noud]

  Group in user profile is no link.
- Merge branch 'master' into develop. [noud]
- Code Standards. [noud]

  Given xxx.default.php, do not check database.php anymore.
- RBAC. [noud]

  more correct deactivated buttons being gray but as well having no
  effect.
- RBAC. [noud]

  removed a leftover on in-activating buttons that did show on IE.
- Merge branch 'master' into develop. [noud]
- NCIRC PHP security settings compatibility patch. [Andrzej Dereszowski]

  This patch corrects a small thing in Cake code that makes it compatible with open_basedir restriction NCIRC uses in /etc/php.ini

  	new file:   build/patches/lib_Cake_View_MediaView.php.diff
- Xxx.default.php. [noud]

  put plugins loading into bootstrap.default.php
- Groups. [noud]

  Do not delete group if there is still Users as children.
- Merge branch 'master' into develop. [noud]

  Conflicts:
  	app/Config/bootstrap.php
- Cosmetic changes. [Andrzej Dereszowski]

  Descriptions in the export functionality polished.
- Merge branch 'master' of
  ssh://misp.ncirc.nato.int:55555/home/git/cydefsig. [Andrzej
  Dereszowski]
- Configuration files renamed to better handle git merges on production
  systems. [Andrzej Dereszowski]

  Please add new features with their default values. Their should contain only example values.

  	renamed:    app/Config/bootstrap.php -> app/Config/bootstrap.default.php
  	renamed:    app/Config/core.php -> app/Config/core.default.php
  	renamed:    app/Config/database.php -> app/Config/database.default.php
- Merge branch 'master' into develop. [noud]
- Comment. [noud]

  The actual view to be able to send comment to Org or Owner/user_id.
- Export. [noud]

  Use config CyDefSIG.name in NIDS export.
- Comment. [noud]

  Be able to send comment to Org or Owner/user_id.
- Version. [noud]

  Display a version in header.
- Export. [noud]

  /CyDefSig/MISP/ in NIDS export.
- Validation. [noud]

  corrected again..filename was wrong,
  filename|md5 was correct.
  so reverted the filename|md5 change.
- Code Standards. [noud]

  Somehow 2 "!"s got lost in Attribute.php.
  Somehow one change from type_definitions to typeDefinitons sliped
  through.
- Audit log. [noud]

  Edit user (now?) needs an extra check on the second password.
- Merge branch 'master' into develop. [noud]
- Code Standards. [noud]

  Cleanup (again) the AppHelper.
- Merge branch 'master' into develop. [noud]

  Conflicts:
  	app/Config/bootstrap.php
- CakePHP. [noud]

  Removed diffs that already are placed in build/patches.
- CakePHP. [noud]

  Update from CakePHP to version 2.2.2
  as well as needed patch files.
- Db. [noud]

  small notes about database.
- Continious Integration. [noud]

  Jenkins makefile.
- Audit log. [noud]

  System operators readme message.
- Merge branch 'master' into develop. [noud]
- CakePHP. [noud]

  To be able to update CakePHP (regularly),
  we found the current differences and now
  put these diffs to build/patches.

  Patches are now relative to $CakePHP_HOME.
- Code Standards. [noud]

  For the moment we use this given we do have Jenkins,
  but not the ssh keys in place for Jenkins to connect to Git.
- Audit log. [noud]

  After change plugins, forgot to skip revision in SysLogLogableBehavior.
- Merge branch 'master' into develop. [noud]

  Conflicts:
  	app/Controller/AppController.php
  	app/Controller/AttributesController.php
  	app/Controller/EventsController.php
  	app/Controller/ServersController.php
  	app/Controller/UsersController.php
  	app/Model/Attribute.php
  	app/Model/Event.php
  	app/Model/Server.php
  	app/Model/User.php
  	app/View/Attributes/edit.ctp
  	app/View/Attributes/index.ctp
  	app/View/Elements/actions_menu.ctp
  	app/View/Events/add.ctp
  	app/View/Events/index.ctp
  	app/View/Events/view.ctp
  	app/View/Events/xml/view.ctp
  	app/View/Servers/index.ctp
  	app/View/Users/admin_index.ctp
- Merge and code standards. [noud]

  Forgot to clean View/Helper/AppHelper.php.
  Changed underscore method names to private and protected where
  appropriate given phpcs code standards errors.
- Merge. [noud]

  validateAttributeValue always has to return true.
- Merge (code_standards into master) [noud]

  Small correction to git manual merge where i did forgot 2 lines in
  NidsExportComponent.php so NIDS export did not work anymore. (is okay
  again now.)
- Merge branch 'coding_standards' [noud]

  Conflicts:
  	app/Controller/Component/NidsExportComponent.php
- Pagination. [noud]

  Same pagination in Events as in Attributes.
- CakePHP. [noud]

  Located the patches done to CakePHP to be able to upgrade CakePHP.
- CakePHP Coding Standards. [noud]

  Not return in a switch but after that switch statement.
- CakePHP Coding Standards. [noud]

  changed to camel caps format where needed.
- CakePHP Coding Standards. [noud]

  http://book.cakephp.org/2.0/en/contributing/cakephp-coding-conventions.html

  Eclipse:
  Window->Preferences
  	General->Editors->Text Editors
  		Displayed tab width:	4
  		Insert spaces for tabs	NOT
  	PHP->Code Style->Formatter
  		Tab policy:	Tabs
  File->Convert Line Delimeters To->Unix [default]

  http://mark-story.com/posts/view/static-analysis-tools-for-php
  for instance:
  phpcs --standard=CakePHP app/Model/

  Not yet done is all camel caps format.
- IE. [noud]

  no scrollbars during print fixed wrong,
  now overflow visable i.s.o. hidden.
- IE. [noud]

  no scrollbars during print.
- Merge branch 'master' of
  ssh://misp.ncirc.nato.int/home/git/cydefsig.git. [noud]

  Conflicts:
  	app/Controller/Component/NidsExportComponent.php
- Merge branch 'master' of code.lab.modiss.be:cydefsig. [Andrzej
  Dereszowski]
- Merge branch 'master' of git@code.lab.modiss.be:cydefsig.git.
  [Christophe Vandeplas]
- Temporary workaround for bug in slow NIDS export. [Christophe
  Vandeplas]
- Whitelist. [noud]

  Seemingly we can not do name resolving(?),
  function nametoipl containing gethostbynamel removed.
- GFI sandbox import. [noud]

  Replace Windows environment variables
  %UserProfile% and %AllUsersProfile%.
- GFI sandbox import. [noud]

  do not load non existing stored_created_file.
- Better placement of plugins (touching RBAC & Audit log) [noud]

  If it's just an existing behavior or lib,
  place it in a plugin directory structure in <cydefsig>/plugins.

  If there is a need to change an extern existing plugin,
  extend the existing plugin by a new plugin in <cydefsig>/app/Plugin.

  This way there is a very clean devision between own and external code.
  The external code can be updated without touching own nor changed code.
- RBAC. [noud]

  Forgot to call saveAcl in Groups::add().
  (to correct wrong behavior, edit group,
  do not change any and button submit.)
- RBAC. [noud]

  Terms page missed button deactivation.
- XML related. [noud]

  Made tools/curl/input/event.xml more anonymous.
  Events/xml/view.ctp wrongly showed category_order.
  REST Event add did not work anymore given GFI sandbox import.
- Merge branch 'master' into develop. [noud]

  Conflicts:
  	app/Controller/EventsController.php
  	app/Model/Attribute.php
  	app/View/Events/view.ctp
- Sync & Correlation. [noud]

  During sync and correlation = db,
  an attachment or malware did not get processed into
  Attribute.data, so will not be synced.
  Now, conform other correlation methods being 'default' or 'sql'
  the attachment or malware is synced as well.
  (master has been synced with mil.be not using db correlation,
  so should have the data.)
- NIAS. [noud]

  CyDefSIG.showowner=false, to not show email.
  CyDefSIG.sync=false, to not show the text 'private'.*)

  *) note, this does remove List Servers and no sync from NATO
  to MIL.be in functionality besides missing the account so credentials
  there.
- Merge branch 'master' of
  ssh://misp.ncirc.nato.int/home/git/cydefsig.git. [noud]
- Merge branch 'master' of code.lab.modiss.be:cydefsig. [Andrzej
  Dereszowski]
- Removed published from. [Christophe Vandeplas]
- REST. [noud]

  Small correction to delete attribute after uuid change.
- Login. [noud]

  small shell script to reset password. Used like:
  ./Console/cake password <email> <passwd>
- Sync. [noud]

  On publish and no configured GnuPG, do tell
  event is published but no email sent.
- Sync and REST. [noud]

  REST delete event working again after uuid change.
- Merge branch 'master' of code.lab.modiss.be:cydefsig. [Andrzej
  Dereszowski]
- Fixes inconsistent relatedAttributes and relatedEvents arrays with
  different correlation implementations. [Christophe Vandeplas]
- Removes 'Published from' reference. [Christophe Vandeplas]
- Sync and gpg. [noud]

  If no gnupg installed.. do not tell, for NIAS demo.
- Validation. [noud]

  add event and empty info now does not MethodNotAllowedException
  but Flash and show the invalid.
- Sync. [noud]

  small correction after uuid correction,
  so delete attribute works again.
- Merge branch 'master' of code.lab.modiss.be:cydefsig. [Andrzej
  Dereszowski]
- Merge branch 'master' of git@code.lab.modiss.be:cydefsig.git.
  [Christophe Vandeplas]
- Refactored uuid integration (moved to beforeFilter) [Christophe
  Vandeplas]
- REST. [noud]

  cURL scripts, used besides example-rest.py to do REST testing.
- REST (and Sync) [noud]

  Make REST edit work.
- Sync. [noud]

  get the user and org correct,
  given authkey them are known to the system.
- Further cleanup of logo improvement. [Christophe Vandeplas]
- Fixes bug of bad implementation of header logo. [Christophe Vandeplas]
- Cleaned up artifacts from refactored logo display. [Christophe
  Vandeplas]
- Python REST example script. [Christophe Vandeplas]
- Improve logo and email display features. [Christophe Vandeplas]
- Fix document-root location (security) [Christophe Vandeplas]
- Database schema. [noud]

  MYSQL.txt is initial schema, so whitelist table must be inhere as well.
- Merge branch 'master' of code.lab.modiss.be:cydefsig. [Andrzej
  Dereszowski]

  Conflicts:
  	app/Controller/Component/NidsExportComponent.php
- Fixes bug where expired GPG keys break the email-alert system.
  [Christophe Vandeplas]
- Bugfix snort rule-rewriting where some required variables were not
  given to the snortRule() function. [Christophe Vandeplas]
- Minor layout improvement on the export info page. [Christophe
  Vandeplas]
- Improve accuracy of http hostname detection. [Christophe Vandeplas]
- Sync. [noud]

  Database schema updated for sync and re-added event.user_id.
- Sync. [noud]

  Better square and croped images.
- Sync. [noud]

  To test it's handy to run a virtual hosted CyDefSIG having it's own
  database besides an already existing CyDefSIG.
  This is the Apache virtual host setup.
- Sync. [noud]

  Example data describing the NATO CyDefSIG server.
- Sync. [noud]

  The actual logos used for visable flags in Events::index.
- Sync. [noud]

  Sync worked, but we did not know what to do with user_id and org.
  Now, on sync, anonymize the user_id, get the Server.organization and put
  that into Event.org.
  And, display owning flag if Event.user_id or get the Server.logo
  belonging to Event.org (=Server.organization) when Event.user_id is
  empty (=0).

  To this there is organization name and logo in bootstrap and
  other organizations names and logos in Servers.
- Extra bug. [noud]

  Add attribute, do not fill in any, and hit Submit, gives error messages.
- Add attribute. [noud]

  Add attribute, do not fill in any, and hit Submit, did give error
  messages.
- Correlation. [noud]

  do not use the AttributesController::event now,
  just use the old EventsController::view.
- Use DS in stead of '/'. [noud]
- Delete (published) event or attribute. [noud]

  Previous, upon delete only on the local server the event or attribute
  was deleted.
  Now, if delete, look for same event or attribute (using it's uuid)
  and delete on remote servers as well.
  Also look and delete if not published, so no dangling/zombie copies
  remain on remote servers.
- Authkey validation bug and cleanup of fixed bugs list. [noud]
- Authkey validation. [noud]

  An authkey with any length, so less then 40, could be entered.
  Now authkey has to have a length of 40 (or higher).
- HIDS exports sorted (and small indention correction). [noud]
- Whitelist not on NidsExportComponent::urlRule. [noud]

  In hindsight, an url should not be excluded given a host or domain name.
- Correlation speedup using AttributesController i.s.o.
  EventsController. [noud]

  We forgot to change some view things using the right controller.
- REST edit Event implementation. [noud]

  Now after publish, edit and (re)publish an event,
  that event will be updated on the other servers.
- Event.user_id. [noud]

  Event.user_id was re-added but we still missed some,
  so an added event would get user_id set to zero.
  Now Event gets the correct user_id again from
  the person logged in and adding.
  (lateron this must not be used during sync.)
- Whitelist. [noud]

  Mention the whitelist for NDIS export on Export page.
- Whitelist. [noud]

  An admin can maintain a whitelist of host, domain name and ip numbers.
  In the NIDS export lines containing whitelist items are commented out.
- Correlation performance gain. [noud]

  in Config/bootstrap.php add
  Configure::write('CyDefSIG.correlation', 'sql');

  possible values:
  - default, like it was
  - db, correlation in database
  - sql, selection on attributes i.s.o. per attribute
    (sql improvement possible if result conform db above)

  Network activity, ip-src
  30 class-C network ip addresses
  (7650 tupels) (time in ms)

            default     db    sql
  all         25366  16601  15941
              24839  16604  15611
  paginated   16759   8447   6615
              17734   8639   8846

  this is used in both:
  - events/view/<id>
  - attributes/event/<id>
- Bug, unknown server internet name and pull. [noud]
- Fix to pulling from an unknown server. [noud]

  - a server having a non-existing internet name gives
    "php_network_getaddresses:
    getaddrinfo failed: Name or service not known"
    on pull.
- Sync Servers, error if server no MISP or non-existing hostname. [noud]
- Sync Servers, fix if server no MISP or non-existing hostname. [noud]

  - a server containing no MISP gives "XML cannot be read." on publish.
  - a server having a non-existing internet name gives
    "php_network_getaddresses: getaddrinfo failed: Name or service not
  known" on publish.
- Export HIDS files with MD5 and SHA-1. [noud]
- (Audit) logs. [noud]

  The writing of the log in User was done by me using calls to the PHP db
  driver (during my second or third day). Very wrong given that is driver
  and db dependant. Now use CakePHPs calls to have abstraction.
- GFI Sandbox upload. [noud]

  If add event, give a GFI Sandbox export file upload field option.
  Unzip, read .xml, add attachment malware, created files and ip-dst.
- LogableBehavior. [noud]

  removed some debug() and fixed writing to syslog when deleting event
  with attributes.
- Event.user_id rollback(-part). [noud]
- Loggable behaviour. [noud]

  some merge correction for events and servers, so we log again.
- SysLog.SysLog lib import. [noud]
- Merge branch 'develop_0.2.2-0.2.3' into develop. [Andrzej Dereszowski]

  Conflicts:
  	app/Config/Schema/schema_0.2.2.php
  	app/Config/routes.php
  	app/Controller/AppController.php
  	app/Controller/UsersController.php
  	app/Model/User.php
  	app/README.txt
- Shit. [Andrzej Dereszowski]
- Forgot LogableBehavior in the first commit. [noud]
- Audit and Access Control granulation in News page. [noud]
- Admin Paginator fix. [noud]
- DataBase migrate, Audit and Access Control granulation. [noud]
- Rollback of pagination on event view. [git]

  Comeback to previous event layout. This does not change the preformance issue so it is not worth to put in stable.
  We will move it to the devel branch
- Fix, paging on event with lots of attributes. [noud]
- 2 new bugs: - event with lots of attributes has no paging. - non-
  composite attribute and non-printable. [noud]
- Fixed non-printable in no-composite attribute. [noud]
- Show events with user.email if admin. [noud]
- Redo Event.user_id. [noud]
- Search Attributes fixed. [noud]
- Fixes the Search Attributes. [noud]
- Remove extra dot between filename and ext when downloading attachment.
  [noud]
- News: removed some old stuff EventsController: contact mail display
  name from the config file. [deresz]
- Merge branch 'develop_0.2.2_fixes' into develop. [Andrzej Dereszowski]

  Conflicts:
  	app/Model/Attribute.php
- New bug.. type filename|md5, conform type md5 strtolower. [noud]
- Fix, do strtolower on types filename|md5 and filename|sha1 conform
  types md5 and sha1. [noud]
- New bug, authError gets displayed before login. [noud]
- Fix to authError getting displayed before login. [noud]
- Upload always ticked if malware-sample, always unticked if attachment.
  [noud]
- Corrects the download in IE fix, to filename.ext.zip or filename.ext.
  (Got filename.ext.zip.zip for attachment and filename.ext.ext for
  malware given the previous fix) [noud]
- New bug, Add User and validation error gives extra authkey not
  defined. [noud]
- Fix to New User, some validation error then authkey not defined.
  [noud]
- Download attachment does not work on MS Internet Explorer. This _can_
  be a fix, not sure. If not, CakePHP bug #2554 or others. [noud]
- One extra bug (IE download). [noud]
- Correction to upload so zip only ticked when malware and not when
  attachement. [noud]
- Do validation after edit attribute. [noud]
- Bug found. [noud]
- Fix to: Add attribute, non-valid, correct, ´black-holed´. [noud]
- Only show categories with type attachment or malware-sample in Add
  Attachement view. (this was..No possibility to upload if type
  attachement or malware-sample is not in category.) [noud]
- 2 extra bugs found. [noud]
- No possibility to upload if type attachement or malware-sample is not
  in category. [noud]
- List of outstanding and fixed bugs. [noud]
- Edit composite attribute to non-composite attribute fix. [noud]
- Make the documentation "brand-neutral" to be able to develop it in a
  community. [deresz]
- Use CyDefSIG.name from Config in alert e-mail subjects. [deresz]
- Correction to "link" attribute type - links were not actually created.
  Also changed it to proper "cake" way. [deresz]
- Some modifications to category/attribute matrix. MISP database is now
  compatible for sync with CyDefSIG. [deresz]
- Merge branch 'develop' of code.lab.modiss.be:cydefsig into
  develop_0.2.2_fixes. [Andrzej Dereszowski]
- Forgot debug comment. [Christophe Vandeplas]
- Improved NIDS output. [Christophe Vandeplas]
- Fixed silly bug in priority assignment of nids export. [Christophe
  Vandeplas]
- Fixed nids snort rule conversion because of greedy * and + [Christophe
  Vandeplas]
- Minor improvement in usability on index pages. [Christophe Vandeplas]
- Improvement of nids - level and message. [Christophe Vandeplas]
- Micro fix in nids export. [Christophe Vandeplas]
- Changed classtype. [Christophe Vandeplas]
- First migration script for misp0.2 to misp1.0 (not finished)
  [Christophe Vandeplas]
- Some improvement on database level. [Christophe Vandeplas]
- Fix an php error when importing attributes with incorrect type -
  category validation. [Christophe Vandeplas]
- Updated DB structure. [Christophe Vandeplas]
- Fixing bug created in commit 957e4f232bbfc58ff6630c7da8353d57316e4973.
  [Christophe Vandeplas]
- Minor memory usage improvements by referencing in foreach ($array as
  &$value) loop. [Christophe Vandeplas]
- Cleanup of comments and todos minor memory performance improvement.
  [Christophe Vandeplas]
- Fixed bug in termsaccepted. [Christophe Vandeplas]
- Info on how to use a same CakePHP lib directory for multiple
  instances. [Christophe Vandeplas]
- Merge branch 'develop' of code.lab.modiss.be:cydefsig into develop.
  [Christophe Vandeplas]
- Cleanup of directory. [Christophe Vandeplas]
- Updated console version from newer cakephp. [Christophe Vandeplas]
- Removed reference to useless user_id. fixed bug where Contact reporter
  doesn't work when user does not exist (contact reporter now sends
  mails to all the org) [Christophe Vandeplas]
- Servers.lastpushedid and Servers.lastpulledid. [noud]
- Admin Paginator fix. [noud]
- Revert "Audit and ACL first cut." [root]

  This reverts commit 5818231f4841bc862f2ad5bdaf70648a811250e9.
- Audit and ACL first cut. [noud]
- Revert "Audit database table." [noud]

  This reverts commit f5bf89e62408c29a02b27e5e0be5d2356412fa27.
- Audit database table. [noud]
- I think comment should not be correlated neither but correct me if I'm
  wrong. [Andrzej Dereszowski]
- Fixed huge SQL injection vulnerability created in bruteforce
  protection. Shame on me !!! [Christophe Vandeplas]
- Minor change. [Christophe Vandeplas]
- Implementation of a anti-brute-force password guessing mechanism.
  [Christophe Vandeplas]
- Sanitize::html() to h() for views is the way to go. [Christophe
  Vandeplas]
- Unique attribute for nids export. [Christophe Vandeplas]
- Removed description field ( should be replaced by comment )
  [Christophe Vandeplas]
- Better error outputting. [Christophe Vandeplas]
- Attribute types validation is now a separate function that uses the
  Attribute->type_definitions variable. [Christophe Vandeplas]
- Forgot to add js to previous commits. [Christophe Vandeplas]
- Minor fixes. [Christophe Vandeplas]
- Fixes security issue (overwrite existing event) [Christophe Vandeplas]
- Select boxes with filtering now. [Christophe Vandeplas]
- Improved documentation. [Christophe Vandeplas]
- Minor fix in Attribute tooltip more documentation (autogenerated)
  [Christophe Vandeplas]
- Fixed merge conflicts with HEAD at belmod Merge branch 'develop' of
  code.lab.modiss.be:cydefsig into develop. [Andrzej Dereszowski]

  Conflicts:
  	app/Controller/EventsController.php
  	app/Model/Attribute.php
- Part of the documentation added - docu written by Miguel Soria Machado
  (CERT-EU) [Christophe Vandeplas]
- Fixed error when type was not set. [Christophe Vandeplas]
- Fixed logic bug. [Christophe Vandeplas]
- Only sync event on publish when sync feature is on. [Christophe
  Vandeplas]
- Auto-upload when publish event. [Christophe Vandeplas]
- Moved some functions around. [Christophe Vandeplas]
- Push / pull seems to work with attachment support. Lots of testing
  required. [Christophe Vandeplas]
- Limit saveAssociated using fieldList. [Christophe Vandeplas]
- Attachment support in REST API. [Christophe Vandeplas]
- REST XML request also received base64 encoded file content.
  [Christophe Vandeplas]
- Minor layout improvement. [Christophe Vandeplas]
- Fixes previous commit. [Christophe Vandeplas]
- Layout improvement in attribute display. [Christophe Vandeplas]
- Workaround for bug where uuid is not set when empty. See bug
  http://cakephp.lighthouseapp.com/projects/42648-cakephp/tickets/2893.
  [Christophe Vandeplas]
- Fix bug when editing attributes. [Christophe Vandeplas]
- Fixes typo in alert message. [Christophe Vandeplas]
- Help messages implementation (forms and list views). [Andrzej
  Dereszowski]
- Explanation messages implemenented for forms and for list views (using
  "title" html element) [Andrzej Dereszowski]
- Fix recommendation of pentest for autocomplete. [Christophe Vandeplas]
- Fixes bug where event is not unpublished when attribute is edited.
  [Christophe Vandeplas]
- Fixes bugs in NIDS export with duplicate SIDs. [Christophe Vandeplas]
- . [Christophe Vandeplas]
- Fixes event with no attributes in REST request. [Christophe Vandeplas]
- Fixes problem of not being able to import events with single
  attribute. [Christophe Vandeplas]
- Added CyDefSIG.name to allow changing the title of the site.
  [Christophe Vandeplas]
- Fixes issue 67. [Christophe Vandeplas]
- More fixes for the sync. [Christophe Vandeplas]
- Basic sync push seems to work. [Christophe Vandeplas]
- Fixes security bug in XML REST request. [Christophe Vandeplas]
- Do not show related events if the variable was not set. [Christophe
  Vandeplas]
- Fixes lowercase attribute bug in xml output of Events/view and hide
  value1 and value2 from the output. [Christophe Vandeplas]
- Fixes issue 64. [Christophe Vandeplas]
- Moved alert email functionality to separate function _sendAlertEmail()
  REST event add requests also send out mails where necessary.
  [Christophe Vandeplas]
- Fixes issue 66 - https://code.lab.modiss.be/p/cydefsig/issues/66/
  [Christophe Vandeplas]
- Fixes bug in discovered while running migrate02to021 script.
  [Christophe Vandeplas]
- Split value to value1 and value2. You need to update the DB schema and
  run /events/migrate02to021 to migrate the data. [Christophe Vandeplas]
- Bugfix in Attribute validation Do not search for related attributes
  for specific types. [Christophe Vandeplas]
- Fixed typo. [Christophe Vandeplas]
- Merge commit '280baac98902789ee69186539474a2e82156659e' into develop.
  [Christophe Vandeplas]

  Resolved Conflicts in:
  	app/View/Events/view.ctp
- Patched deleting of attributes. [Andrzej Dereszowski]
- Minor cosmetic changes. [Andrzej Dereszowski]
- REST POST of event and signatures works (basics, no error-handling)
  [Christophe Vandeplas]
- Start of documentation concerning REST. [Christophe Vandeplas]
- Allow saving of data using REST API. [Christophe Vandeplas]
- Logging in for REST using Authorized HTTP header field. [Christophe
  Vandeplas]
- Fix db engine. [Christophe Vandeplas]
- Db structure for sync functionality. [Christophe Vandeplas]
- Add, edit, delete and (basic) Manual Sync server functionality added.
  [Christophe Vandeplas]
- Micro usability improvement. [Christophe Vandeplas]
- Moved security to see profile to isAuthorized to keep consistency.
  [Christophe Vandeplas]
- XML format for attributes index. [Christophe Vandeplas]
- Merge commit '9e043116228c4866b18e92acb076462845bcf22a' into develop
  Fixed conflicts in: app/View/Events/view.ctp. [Christophe Vandeplas]
- Minor changes: - when admin adds a user, auth key is automatically
  suggested - auth refresh is performed after user edition. [Andrzej
  Dereszowski]
- Fix for the routing problem on admin-privileged users. All links that
  need to be routed to admin-prefixed method have to have 'admin' =>
  true in the parameters. [Andrzej Dereszowski]
- - some bugfixes in validation corrected - new attribute type - link to
  external site. [Andrzej Dereszowski]
- Bug fixes in the admin view - password changing for other users -
  corrected admin_view. [Andrzej Dereszowski]
- - small bug with "No GPG key" message marked in the code - path to
  homedir for GPG added in User.php. [Andrzej Dereszowski]
- - Attributes index view fixed (attachments) [Andrzej Dereszowski]
- - signatures are displayed by category always in the same order
  defined in model. [Andrzej Dereszowski]
- Minor correction: - login page does not display "invalid user" when
  first time presented to the user - "Log Off" button removed from the
  print view. [Andrzej Dereszowski]
- Logo position corrected. [Andrzej Dereszowski]
- Merge commit 'dee8a866e691fde2eedbd9a2418a6027f88d07cf' into develop.
  [Christophe Vandeplas]
- Fixed bug where GPG homedir was not set in a few places. [Christophe
  Vandeplas]
- Implemented basics for private, nonsyncable, Events or Attributes.
  [Christophe Vandeplas]
- First version or REST API to export data. [Christophe Vandeplas]
- Minor changes. [Christophe Vandeplas]
- Forgot updated default layout for info bloxes. [Christophe Vandeplas]
- Added some infoboxes when adding Attributes. [Christophe Vandeplas]
- Allow publishing of events without sending email. [Christophe
  Vandeplas]
- Fixed minor CSRF vulnerability + added google link on vulnerability
  type. [Christophe Vandeplas]
- First experimental test of importing events from a remote server. Only
  new events are imported. [Christophe Vandeplas]
- Fixed minor bugs. [Christophe Vandeplas]
- Changed alerted -> published other minor fixes. [Christophe Vandeplas]
- Minor change in getRelatedAttributes function. [Christophe Vandeplas]
- Filename|sha1 data validation. [Christophe Vandeplas]
- Filename|sha1. [Christophe Vandeplas]
- Fix admin routing. [Christophe Vandeplas]
- Added a migrate() function to generate uuid for events and attributes
  that didn't have an uuid. [Christophe Vandeplas]
- Renamed Signature to Attribute. [Christophe Vandeplas]
- XML export ... woohoo !!! [Christophe Vandeplas]
- Number of entries in the index lists. [Christophe Vandeplas]
- Fix error when there are no related events/signatures, or simply
  signatures. [Christophe Vandeplas]
- Forgot to update DB structure after category support. [Christophe
  Vandeplas]
- Micro HTML bugfixes in views. [Christophe Vandeplas]
- Preformance improvement when searching for related events (by reusing
  results from related signatures search) [Christophe Vandeplas]
- Md5 and sha1 hashes now automatically lowercase cleaned up some code
  and fixed some vulnerabilities. [Christophe Vandeplas]
- Print Cascading Stylesheets and minor layout fixes. [Christophe
  Vandeplas]
- Extra vulnerability type. [Christophe Vandeplas]
- Implemented file-upload of attachment or password protected malware-
  samples. Base code contributed by Andrzej Dereszowski. [Christophe
  Vandeplas]
- Confirm password functionality (thanks to Andrzej) [Christophe
  Vandeplas]
- Updated DB structure. [Christophe Vandeplas]
- Minor micro changes. [Christophe Vandeplas]
- Signature is now known as Attribute. [Christophe Vandeplas]
- Not finished editing -> not published. [Christophe Vandeplas]
- Whatever. [Christophe Vandeplas]
- Graph for Signatures Type per organisation. [Christophe Vandeplas]
- Fix bug of login/authinfo not refreshed when reseting authkey.
  [Christophe Vandeplas]
- Layout improvements. [Christophe Vandeplas]
- IsAuthorized now handles permissions on admin,delete,edit,... actions.
  [Christophe Vandeplas]
- UUID support for syncing. [Christophe Vandeplas]
- Rename Finish Edit to Publish Event. [Christophe Vandeplas]
- Fixes bug: to_ids should be there otherwise you cannot edit the
  signature to change the "to_ids" checkbox. By Andrzej Dereszowski.
  [Christophe Vandeplas]
- Cleanup old __('Actions') and non echo __() [Christophe Vandeplas]
- Updated DB structure and content. [Christophe Vandeplas]
- Migration to CakePHP 2.1. Most of the functionality migrated, Q&A
  review required. [Christophe Vandeplas]
- Terms and Conditions and News splashpage Updated DB structure: ALTER
  TABLE `users` ADD `termsaccepted` TINYINT( 1 ) NOT NULL , ADD
  `newsread` DATE NOT NULL. [Christophe Vandeplas]
- Micro change in export text. [Christophe Vandeplas]
- Temporary workaround for problem to edit profile. [Christophe
  Vandeplas]
- Implement batch import of signatures. [Christophe Vandeplas]
- Powered by. [Christophe Vandeplas]
- Export to text formats. [Christophe Vandeplas]
- Fixed information disclosure vulnerability on groups pages.
  [Christophe Vandeplas]
- Updated README based on feedback from Jeroen Vanderauwera and some
  corrections. [Christophe Vandeplas]
- Show org for admin. [Christophe Vandeplas]
- Show link between events on the signature level. [Christophe
  Vandeplas]
- Reverted sort order of Signature Types Histogram. [Christophe
  Vandeplas]
- Changed sort-order of Signature Types Histogram. [Christophe
  Vandeplas]
- Snort signature type is now exported to NIDS and cleaned up.
  [Christophe Vandeplas]
- Updated table structure. [Christophe Vandeplas]
- Allows the user to choose a custom NIDS start SID. [Christophe
  Vandeplas]
- Added more clear Edit Profile button -
  https://code.lab.modiss.be/p/cydefsig/issues/29/ [Christophe
  Vandeplas]
- Miror layout improvements in emails. [Christophe Vandeplas]
- Fixes HTML entities in email. [Christophe Vandeplas]
- Data validation - duplicate signatures for same event. [Christophe
  Vandeplas]
- Bugfix userslist and types_histogram. [Christophe Vandeplas]
- List number of events shared by Org list type of signatures shared by
  Org. [Christophe Vandeplas]
- Allow string-in-file. [Christophe Vandeplas]
- Snort signature type has no datavalidation. [Christophe Vandeplas]
- Added 'snort' signature type. [Christophe Vandeplas]
- Database structure and rough license. [Christophe Vandeplas]
- List members (orgs) of the platform. [Christophe Vandeplas]
- Allow to hide (default) the name of the Organisation that posted the
  event. [Christophe Vandeplas]
- Fixed filesystem permissions. [Christophe Vandeplas]
- Default To IDS checkbox is checked. [Christophe Vandeplas]
- To_nids renamed to to_ids and implemented. [Christophe Vandeplas]
- Stylesheet improvements. [Christophe Vandeplas]
- Shows ID in event list and detail. [Christophe Vandeplas]
- Micro fix. [Christophe Vandeplas]
- Contact reporter now lets a user add a custom message. [Christophe
  Vandeplas]
- Cleaned workaround for empty password behavior of Auth component.
  [Christophe Vandeplas]
- Add basic XSRF protection for add, edit actions. [Christophe
  Vandeplas]
- Minor fixes in git repo. [Christophe Vandeplas]
- Authkey reset functionality and fixed bugs in users_controller.
  [Christophe Vandeplas]
- Events/snort is now refactored to events/nids Backwards compatibility
  with the url is still kept. [Christophe Vandeplas]
- Implemented relations dynamically. [Christophe Vandeplas]
- Removed forgotten comment. [Christophe Vandeplas]
- Fixes authkey generation. [Christophe Vandeplas]
- Added missing files. [Christophe Vandeplas]
- Fixed Snort export - DNS format. [Christophe Vandeplas]
- Xml export now done properly fixed bug in xml export. [Christophe
  Vandeplas]
- Changed snort rule message. [Christophe Vandeplas]
- Minor fixes. [Christophe Vandeplas]
- Fixed email + gpg alert bugs. [Christophe Vandeplas]
- Color improvement in notification message. [Christophe Vandeplas]
- Better color-based error messages. [Christophe Vandeplas]
- Moved getRelatedEvents() to Event model. [Christophe Vandeplas]
- Micro improvement. [Christophe Vandeplas]
- Related info also in alert email. [Christophe Vandeplas]
- Added relation between events (implementation not yet ideal)
  [Christophe Vandeplas]
- Added AS a signature type. [Christophe Vandeplas]
- Only send out encrypted alerts if set in bootstrap config file.
  [Christophe Vandeplas]
- Export info in separate page. [Christophe Vandeplas]
- Minor layout improvements. [Christophe Vandeplas]
- Minor change. [Christophe Vandeplas]
- Initial import. [Christophe Vandeplas]

