import FWCore.ParameterSet.Config as cms

from RecoBTag.SecondaryVertex.candidateCombinedSecondaryVertexV2Computer_cfi import *

candidateNegativeCombinedSecondaryVertexV2Computer = candidateCombinedSecondaryVertexV2Computer.clone()
candidateNegativeCombinedSecondaryVertexV2Computer.vertexFlip = True
candidateNegativeCombinedSecondaryVertexV2Computer.trackFlip = True
candidateNegativeCombinedSecondaryVertexV2Computer.trackSelection.sip3dSigMax = 0
candidateNegativeCombinedSecondaryVertexV2Computer.trackPseudoSelection.sip3dSigMax = 0
candidateNegativeCombinedSecondaryVertexV2Computer.trackPseudoSelection.sip2dSigMin = -99999.9
candidateNegativeCombinedSecondaryVertexV2Computer.trackPseudoSelection.sip2dSigMax = -2.0
