#include <stdio.h>
#include "logagent_rpc_test.h"
#include "logagent_rpc_cli.h"

namespace logagent {

	TestTool :: TestTool() {
	}

	TestTool :: ~TestTool() {
	}

	int TestTool :: critical( OptMap & ) {
		return -1;
	}

	int TestTool :: error( OptMap & ) {
		return -1;
	}

	int TestTool :: warning( OptMap & ) {
		return -1;
	}

	int TestTool :: info( OptMap & ) {
		return -1;
	}

	int TestTool :: debug( OptMap & ) {
		return -1;
	}

	int TestTool :: opreport( OptMap & ) {
		return -1;
	}

	int TestTool :: opquery( OptMap & ) {
		return -1;
	}

	int TestTool :: webreport( OptMap & ) {
		return -1;
	}

	int TestTool :: busireport( OptMap & ) {
		return -1;
	}


	TestToolImpl:: TestToolImpl() {
	}

	TestToolImpl:: ~TestToolImpl() {
	}

	int TestToolImpl :: critical( OptMap & opt_map ) {
		debugmsg req;

		Client cli;
		int ret = cli.critical( req );
		printf( "%s return %d\n", __func__, ret );

		return 0;
	}

	int TestToolImpl :: error( OptMap & opt_map ) {
		debugmsg req;

		Client cli;
		int ret = cli.error( req );
		printf( "%s return %d\n", __func__, ret );

		return 0;
	}

	int TestToolImpl :: warning( OptMap & opt_map ) {
		debugmsg req;

		Client cli;
		int ret = cli.warning( req );
		printf( "%s return %d\n", __func__, ret );

		return 0;
	}

	int TestToolImpl :: info( OptMap & opt_map ) {
		debugmsg req;

		Client cli;
		int ret = cli.info( req );
		printf( "%s return %d\n", __func__, ret );

		return 0;
	}

	int TestToolImpl :: debug( OptMap & opt_map ) {
		debugmsg req;

		Client cli;
		int ret = cli.debug( req );
		printf( "%s return %d\n", __func__, ret );

		return 0;
	}

	int TestToolImpl :: opreport( OptMap & opt_map ) {
		opmsg req;

		req.time = 1476678433;
		req.user = "david";
		req.action = "Logout";

		Client cli;
		int ret = cli.opreport( req );
		printf( "%s return %d\n", __func__, ret );

		return 0;
	}

	int TestToolImpl :: opquery( OptMap & opt_map ) {
		opqueryreq req;
		opqueryres res;

		req.user = "david";
		req.begintime = 1476678433;
		req.endtime = 1476678493;

		Client cli;
		int ret = cli.opquery( req, res );
		printf( "%s return %d\n", __func__, ret );
		for(std::list<opmsg>::iterator it = res.oplogs.begin();
				it != res.oplogs.end();
				++it) {
			printf( "\t%d %s %s %s %s\n", 
					it->time, 
					it->user.c_str(), 
					it->action.c_str(),
					it->args.c_str(),
					it->others.c_str() );
		}

		return 0;
	}

	int TestToolImpl :: webreport( OptMap & opt_map ) {
		webmsg req;

		Client cli;
		int ret = cli.webreport( req );
		printf( "%s return %d\n", __func__, ret );

		return 0;
	}

	int TestToolImpl :: busireport( OptMap & opt_map ) {
		busimsg req;

		Client cli;
		int ret = cli.busireport( req );
		printf( "%s return %d\n", __func__, ret );

		return 0;
	}


}

using namespace logagent;

void showUsage( const char * program )
{
	printf( "Usage:\n" );
	printf( "          %s [-c <config>] [-f <func>] [-h]\n", program );
	printf( "Options:\n" );
	printf( "          -c\tconfigure file of client\n" );
	printf( "          -f\trpc method or function\n" );
	printf( "          -h\tshow help\n" );
	printf( "Examples:\n");

	TestTool::Name2Func_t * name2func = TestTool::GetName2Func();

	for( int i = 0; ; i++ ) {
		TestTool::Name2Func_t * iter = &( name2func[i] );

		if( NULL == iter->name ) break;

		printf( "          %s -c logagent_rpc_cli.conf -f %s %s\n", program, iter->name, iter->usage );
	}

	exit( 0 );
}

int main( int argc, char * argv[] )
{
	const char * func = NULL;
	const char * config = NULL;

	for( int i = 1; i < argc - 1; i++ ) {
		if( 0 == strcmp( argv[i], "-c" ) ) {
			config = argv[ ++i ];
		}
		if( 0 == strcmp( argv[i], "-f" ) ) {
			func = argv[ ++i ];
		}
		if( 0 == strcmp( argv[i], "-h" ) ) {
			showUsage( argv[0] );
		}
	}

	if( NULL == func ) showUsage( argv[0] );

	if( NULL != config ) Client::Init( config );

	TestTool::Name2Func_t * target = NULL;

	TestTool::Name2Func_t * name2func = TestTool::GetName2Func();

	for( int i = 0; i < 100; i++ ) {
		TestTool::Name2Func_t * iter = &( name2func[i] );

		if( NULL == iter->name ) break;

		if( 0 == strcasecmp( func, iter->name ) ) {
			target = iter;
			break;
		}
	}

	if( NULL == target ) showUsage( argv[0] );

	OptMap opt_map( target->opt_string );

	if( ! opt_map.Parse( argc, argv ) ) showUsage( argv[0] );

	TestTool::ToolFunc_t targefunc = target->func;

	TestToolImpl tool;

	if( 0 != ( tool.*targefunc ) ( opt_map ) ) showUsage( argv[0] );

	return 0;
}
