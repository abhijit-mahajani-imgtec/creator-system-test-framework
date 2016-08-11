#/************************************************************************************************************************
# Copyright (c) 2016, Imagination Technologies Limited and/or its affiliated group companies.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#     1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
#        following disclaimer.
#     2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#        following disclaimer in the documentation and/or other materials provided with the distribution.
#     3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
#        products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#************************************************************************************************************************/

from framework.awa_enums import AwaError
from framework.awa_enums import AwaLWM2MError

def _CheckExceptionHasError(testCase, exceptionContext, error, pathResultError, pathResultLWM2MError):
    testCase.assertGreater(len(exceptionContext.args), 3)
    testCase.assertEqual(error, exceptionContext.args[1], str(AwaError(exceptionContext.args[1])) + " != " + str(error) +" " + str(exceptionContext.args))

    assertionMessage = str(AwaError(exceptionContext.args[2])) + " != " + str(pathResultError) +" " + str(exceptionContext.args)
    testCase.assertEqual(pathResultError, exceptionContext.args[2], assertionMessage)

    assertionMessage = str(AwaLWM2MError(exceptionContext.args[3])) + " != " + str(pathResultLWM2MError) +" " + str(exceptionContext.args)
    testCase.assertEqual(pathResultLWM2MError, exceptionContext.args[3], assertionMessage)

def CheckForException(testCase, successFunction, assertion, exception, awaError, pathResultError=AwaError.Unspecified, pathResultLWM2MError=AwaLWM2MError.Unspecified):
    try:
        successFunction(testCase, assertion)
    except exception as exceptionContext:
        if awaError != None:
            _CheckExceptionHasError(testCase, exceptionContext, awaError, pathResultError, pathResultLWM2MError)
    else:
        testCase.fail("Exception " + str(exception) +" was not thrown")