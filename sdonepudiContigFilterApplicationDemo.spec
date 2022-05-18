/*
A KBase module: sdonepudiContigFilterApplicationDemo
This sample module contains one small method that filters contigs.
*/

module sdonepudiContigFilterApplicationDemo {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_sdonepudiContigFilterApplicationDemo(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
